from django.urls import path

from exports.views import ExportCreate, ExportList, DownloadView


urlpatterns = [

    path('$',
        ExportList.as_view(),
        name="export_list"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/$',
        ExportCreate.as_view(),
        name="export_create"),
    path('(?P<uid>[-\w]+)/$',
        DownloadView.as_view(),
        name='export_download')
]
