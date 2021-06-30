from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from categories.factories import CategoryFactory
from accounts.factories import UserFactory
from exports.factories import ExportFactory
from exports.models import Export
from search.utils import delete_index, create_index


class ExportCreateTests(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.user = UserFactory(
            email="testadmin@phase.fr",
            password="pass",
            is_superuser=True,
            category=self.category,
        )
        self.client.login(email=self.user.email, password="pass")
        self.url = reverse(
            "export_create", args=[self.category.organisation.slug, self.category.slug]
        )

    def test_export_create_cleanup_old_exports(self):
        delete_index()
        create_index()
        now = timezone.now()
        for delta in range(0, 25):
            ExportFactory(
                owner=self.user,
                category=self.category,
                created_on=now + timedelta(days=-delta),
            )

        self.assertEqual(Export.objects.all().count(), 25)

        self.client.post(self.url)

        self.assertEqual(Export.objects.all().count(), 20)
