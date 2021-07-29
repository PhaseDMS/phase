from django.urls import path

from exports.views import ExportCreate, ExportList, DownloadView


urlpatterns = [
    path("", ExportList.as_view(), name="export_list"),
    path(
        "<slug:organisation>/<slug:category>/",
        ExportCreate.as_view(),
        name="export_create",
    ),
    path("<slug:uid>/", DownloadView.as_view(), name="export_download"),
]
