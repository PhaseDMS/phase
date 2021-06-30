import factory
from factory import fuzzy

from accounts.factories import UserFactory
from .models import Activity


class ActivityFactory(factory.DjangoModelFactory):
    class Meta:
        model = Activity

    actor = factory.SubFactory(UserFactory)
    verb = fuzzy.FuzzyChoice(Activity.VERB_CHOICES)
