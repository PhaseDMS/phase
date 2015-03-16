# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse

from categories.factories import CategoryFactory
from accounts.factories import UserFactory


class TransmittalListTests(TestCase):

    def setUp(self):
        self.category = CategoryFactory()
        user = UserFactory(
            email='testadmin@phase.fr',
            password='pass',
            is_superuser=True,
            category=self.category)
        self.client.login(email=user.email, password='pass')
        self.url = reverse('transmittal_list')

    def test_empty_transmittal_list(self):
        res = self.client.get(self.url)
        self.assertContains(res, 'There are no transmittals here')
