from django.urls import path

from .views import Report

urlpatterns = [
    # Reports page
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/$',
        Report.as_view(),
        name='category_report'),
]
