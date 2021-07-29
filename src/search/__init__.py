from django.conf import settings

from elasticsearch import Elasticsearch, RequestsHttpConnection


elastic = Elasticsearch(settings.ELASTIC_HOSTS, connection_class=RequestsHttpConnection)


INDEX_SETTINGS = {
    "settings": {
        "analysis": {
            "filter": {
                "nGram_filter": {
                    "type": "ngram",
                }
            },
            "analyzer": {
                "nGram_analyzer": {
                    "type": "custom",
                    "tokenizer": "keyword",
                    "filter": ["lowercase", "asciifolding", "nGram_filter"],
                },
                "whitespace_analyzer": {
                    "type": "custom",
                    "tokenizer": "keyword",
                    "filter": ["lowercase", "asciifolding"],
                },
            },
        }
    }
}
