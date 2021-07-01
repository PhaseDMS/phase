import factory
from factory.django import DjangoModelFactory

from bookmarks.models import Bookmark


class BookmarkFactory(DjangoModelFactory):
    class Meta:
        model = Bookmark

    name = factory.Sequence(lambda n: "Bookmark {0}".format(n))
