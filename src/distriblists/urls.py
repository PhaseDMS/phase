# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from distriblists.views import DistributionListImport

urlpatterns = [

    url(r'^import/$',
        DistributionListImport.as_view(),
        name='distrib_list_import'),
]
