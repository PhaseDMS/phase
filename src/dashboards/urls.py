from django.urls import path

from dashboards.views import DashboardView

urlpatterns = [
    path('<slug:organisation>/dashboards/<slug:dashboard>/',
        DashboardView.as_view(),
        name='dashboard_detail'),
]
