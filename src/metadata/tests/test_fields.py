from django.test import TestCase

from metadata.factories import ValuesListFactory
from metadata.fields import get_choices_from_list
from metadata.handlers import populate_values_list_cache


class ConfigurableChoiceFieldTest(TestCase):
    def setUp(self):
        self.values_list = ValuesListFactory(
            values={
                "test1": "Test 1",
                "test2": "Test 2",
                "test3": "Test 3",
            }
        )
        populate_values_list_cache()

    def test_choices_from_list(self):
        choices = get_choices_from_list(self.values_list.index)
        self.assertCountEqual(
            choices,
            [
                ("test1", "test1 - Test 1"),
                ("test2", "test2 - Test 2"),
                ("test3", "test3 - Test 3"),
            ],
        )
