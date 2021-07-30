import logging

from django.core.exceptions import FieldDoesNotExist
from django.db import models

from elasticsearch.helpers import bulk
from elasticsearch.exceptions import ConnectionError

from core.celery import app
from categories.models import Category
from search import elastic, INDEX_SETTINGS
from documents.models import Document
from django.conf import settings


logger = logging.getLogger(__name__)


def refresh_index(index):
    """Make latest data available."""
    elastic.indices.refresh(index=index)


def create_index(index):
    """Create all needed indexes."""
    elastic.indices.create(index=index, ignore=400, body=INDEX_SETTINGS)


def delete_index(index):
    """Delete existing ES indexes."""
    elastic.indices.delete(index=index, ignore=404)


def index_revision(revision):
    """Saves a document's revision into ES's index."""
    document = revision.document
    es_key = "{}_{}".format(document.document_key, revision.revision)
    index_name = revision.document.category.get_index_name()
    try:
        elastic.index(
            index=index_name,
            id=es_key,
            body=revision.to_json(),
        )
    except ConnectionError:
        logger.error("Error connecting to ES. The doc %d will no be indexed" % es_key)


@app.task
def index_document(document_id):
    """Index all revisions for a document"""
    document = Document.objects.select_related().get(pk=document_id)
    revisions = document.get_all_revisions()
    actions = list(map(build_index_data, revisions))

    bulk(elastic, actions, chunk_size=settings.ELASTIC_BULK_SIZE, request_timeout=60)


def index_revisions(revisions):
    """Index a bunch of revisions."""
    actions = list(map(build_index_data, revisions))
    bulk(elastic, actions, chunk_size=settings.ELASTIC_BULK_SIZE, request_timeout=60)

    indices = set([a['_index'] for a in actions])
    for index in indices:
        refresh_index(index)


def bulk_actions(actions):
    bulk(elastic, actions, chunk_size=settings.ELASTIC_BULK_SIZE, request_timeout=60)


def build_index_data(revision):
    index_name = revision.document.category.get_index_name()
    return {
        "_index": index_name,
        "_id": revision.unique_id,
        "_source": revision.to_json(),
    }


@app.task
def unindex_document(document_id):
    """Removes all revisions of a document from the index."""
    document = Document.objects.select_related().get(pk=document_id)
    revisions = document.get_all_revisions()
    actions = [
        {
            "_op_type": "delete",
            "_index": document.category.get_index_name(),
            "_id": revision.unique_id,
        }
        for revision in revisions
    ]

    bulk(
        elastic,
        actions,
        raise_on_error=False,
        chunk_size=settings.ELASTIC_BULK_SIZE,
        request_timeout=60,
    )


TYPE_MAPPING = [
    ((models.CharField, models.TextField), "text"),
    ((models.IntegerField,), "long"),
    (
        (
            models.DecimalField,
            models.FloatField,
        ),
        "double",
    ),
    (
        (
            models.DateField,
            models.TimeField,
        ),
        "date",
    ),
    (
        (
            models.BooleanField,
            models.BooleanField,
        ),
        "boolean",
    ),
]


@app.task
def put_category_mapping(category_id):
    category = Category.objects.select_related(
        "organisation", "category_template__metadata_model"
    ).get(pk=category_id)

    index_name = category.get_index_name()
    doc_class = category.document_class()
    mapping = get_mapping(doc_class)
    elastic.indices.put_mapping(
        index=index_name,
        body=mapping,
    )


def get_mapping(doc_class):
    """Creates an elasticsearch mapping for a given document class.

    See: http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/mapping.html

    Note: with elasticsearch, sorting cannot be done on "analyzed" values. We
    use multifields so fields can be indexed twice, one analyzed version, and
    one not_analyzed. Thus, we can search, filter, sort or query any field.

    See: http://www.elasticsearch.org/guide/en/elasticsearch/guide/current/multi-fields.html

    """
    revision_class = doc_class.get_revision_class()

    # Since ES 7.0, you have to manually define an "_all" field
    mapping = {
        "properties": {
            "_all": {
                "type": "text",
                "analyzer": "nGram_analyzer",
                "search_analyzer": "whitespace_analyzer",
                # "index": "not_analyzed",
            }
        }
    }

    config = doc_class.PhaseConfig
    field_types = getattr(config, "es_field_types", {})
    filter_fields = list(config.filter_fields)
    column_fields = list(dict(config.column_fields).values())
    additional_fields = getattr(config, "indexable_fields", [])
    fields = set(filter_fields + column_fields + additional_fields)

    for field_name in fields:
        try:
            field = doc_class._meta.get_field(field_name)
        except FieldDoesNotExist:
            try:
                field = revision_class._meta.get_field(field_name)
            except FieldDoesNotExist:
                field = getattr(doc_class, field_name, None)
                if field is None:
                    field = getattr(revision_class, field_name, None)
                    if field is None:
                        warning = (
                            "Field {} cannot be found and will not be indexed".format(
                                field_name
                            )
                        )
                        logger.warning(warning)

        es_type = (
            get_mapping_type(field_name, field, field_types) if field else "string"
        )

        field_dict = {
            "type": es_type,
            "fields": {
                "raw": {
                    "type": "keyword",
                }
            }
        }

        if field_name in column_fields:
            field_dict.update({
                "copy_to": "_all"
            })

        mapping["properties"].update({
            field_name: field_dict
        })

    return mapping


def get_mapping_type(name, field, field_types):
    """Get the elasticsearch mapping type from a django field."""
    if name in field_types:
        return field_types[name]

    for typeinfo, typename in TYPE_MAPPING:
        if isinstance(field, typeinfo):
            return typename
    return "text"
