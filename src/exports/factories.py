import factory
from factory.django import DjangoModelFactory

from exports.models import Export


class ExportFactory(DjangoModelFactory):
    class Meta:
        model = Export

    querystring = ""
