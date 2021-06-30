from django.urls import path

from imports.views import ImportList, FileUpload, ImportStatus, ImportTemplate


urlpatterns = [
    path("", ImportList.as_view(), name="import_list"),
    path("template/", ImportTemplate.as_view(), name="import_template"),
    path("import/", FileUpload.as_view(), name="import_file"),
    path("<slug:uid>/", ImportStatus.as_view(), name="import_status"),
]
