import logging

from django.core.management.base import BaseCommand, CommandError

from elasticsearch.exceptions import ConnectionError

from categories.models import Category
from search.utils import put_category_mapping


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = Category.objects.select_related(
            "organisation",
            "category_template"
        )
        for category in categories:
            index_name = category.get_index_name()
            logger.info(f"Creating mapping for index {index_name}")

            try:
                put_category_mapping(category.id)
            except ConnectionError:
                raise CommandError("Elasticsearch cannot be found")
