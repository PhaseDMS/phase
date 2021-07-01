import factory
from factory.django import DjangoModelFactory
from factory import fuzzy

from discussion.models import Note


class NoteFactory(DjangoModelFactory):
    class Meta:
        model = Note

    body = fuzzy.FuzzyText()
