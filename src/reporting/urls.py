from django.urls import path

from .views import Report

urlpatterns = [
    # Reports page
    path('<slug:organisation>/<slug:category>/',
        Report.as_view(),
        name='category_report'),
]
