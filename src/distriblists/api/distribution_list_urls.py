
from django.urls import path

from distriblists.api.views import DistributionListList  # Yes, a list of lists


urlpatterns = [
    path('<slug:organisation>/<slug:category>/',
        DistributionListList.as_view(),
        name='distributionlist-list'),
]
