from django.urls import path

from dashboards.views import DashboardView

urlpatterns = [
    path('(?P<organisation>[\w-]+)/dashboards/(?P<dashboard>[\w-]+)/$',
        DashboardView.as_view(),
        name='dashboard_detail'),
]
