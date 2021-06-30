from django.urls import reverse

from categories.factories import CategoryFactory
from accounts.factories import UserFactory
from documents.factories import DocumentFactory
from documents.tests.test_views import GenericViewTest
from favorites.models import Favorite


class FavoriteTest(GenericViewTest):
    url = reverse("favorite_list")

    def setUp(self):
        self.category = CategoryFactory()
        self.user = UserFactory(
            email="test@phase.fr", password="pass", category=self.category
        )
        self.client.login(email=self.user.email, password="pass")

        self.user2 = UserFactory(
            email="test2@phase.fr", password="pass", category=self.category
        )

    def test_favorite_list(self):
        """Tests that a favorite list is accessible if logged in."""
        res = self.client.get(self.url)
        self.assertContains(
            res, "<p>You do not have any document marked as favorite.</p>"
        )

    def test_favorite_privacy(self):
        """Tests that a favorite is not shared accross users."""
        document = DocumentFactory(
            document_key="gloubigoulba",
            category=self.category,
        )
        Favorite.objects.create(document=document, user=self.user2)

        res = self.client.get(self.url)
        self.assertContains(
            res, "<p>You do not have any document marked as favorite.</p>"
        )
        self.assertNotContains(res, "gloubigoulba")

        self.client.login(email=self.user2.email, password="pass")
        res = self.client.get(self.url)
        self.assertContains(res, "gloubigoulba")
