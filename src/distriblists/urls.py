from django.urls import path

from distriblists.views import DistributionListImport

urlpatterns = [

    path('import/',
        DistributionListImport.as_view(),
        name='distrib_list_import'),
]
