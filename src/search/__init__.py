from django.conf import settings

from elasticsearch import Elasticsearch, RequestsHttpConnection


elastic = Elasticsearch(settings.ELASTIC_HOSTS, connection_class=RequestsHttpConnection)


# Here, we define some the analyzers used to index the `_all` field
#
# Since the _all field is used in autocomplete queries, we use two different
# analyzers.
#
# The first analyzer tokenizes the data then run edge_ngrams on each token.
# The search analyzer tokenizes the query but don't generate ngrams of it.
# It ensures that partial words are matched by the index.
#
# See https://www.elastic.co/guide/en/elasticsearch/reference/7.14/analysis-edgengram-tokenizer.html

INDEX_SETTINGS = {
    "settings": {
        "index": {
            "max_ngram_diff": 128,
        },
        "analysis": {
            "analyzer": {
                "ngram_analyzer": {
                    "tokenizer": "keyword",
                    "filter": ["lowercase", "asciifolding", "ngram_filter"],
                },
                "whitespace_analyzer": {
                    "tokenizer": "whitespace",
                    "filter": ["lowercase", "asciifolding"],
                },
            },
            "filter": {
                "ngram_filter": {
                    "type": "ngram",
                    "min_gram": 3,
                    "max_gram": 128
                }
            },
        }
    }
}
