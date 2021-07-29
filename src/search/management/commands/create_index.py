import logging

from django.core.management.base import BaseCommand, CommandError

from elasticsearch.exceptions import ConnectionError

from categories.models import Category
from search.utils import create_index


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = Category.objects.select_related(
            "organisation",
            "category_template"
        )
        for category in categories:
            index_name = category.get_index_name()
            logger.info(f"Creating index {index_name}")

            try:
                create_index(index_name)
            except ConnectionError:
                raise CommandError("Elasticsearch cannot be found")
