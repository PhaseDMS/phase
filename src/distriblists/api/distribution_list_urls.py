
from django.urls import path

from distriblists.api.views import DistributionListList  # Yes, a list of lists


urlpatterns = [
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/$',
        DistributionListList.as_view(),
        name='distributionlist-list'),
]
