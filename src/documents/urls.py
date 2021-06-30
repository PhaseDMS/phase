from django.urls import path

from documents.views import (
    DocumentList, DocumentCreate, DocumentDetail, DocumentEdit,
    DocumentDownload, DocumentRedirect, DocumentRevise, DocumentDelete,
    DocumentRevisionDelete, RevisionFileDownload, DocumentFileDownload
)

urlpatterns = [

    # Document short url
    path('documents/(?P<document_key>[\w-]+)/$',
        DocumentRedirect.as_view(),
        name='document_short_url'),

    # Downloads
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/download/$',
        DocumentDownload.as_view(),
        name="document_download"),

    # Documents
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/$',
        DocumentList.as_view(),
        name="category_document_list"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/create/$',
        DocumentCreate.as_view(),
        name="document_create"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/$',
        DocumentDetail.as_view(),
        name="document_detail"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/edit/$',
        DocumentEdit.as_view(),
        name="document_edit"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/edit/(?P<revision>\d+)/$',
        DocumentEdit.as_view(),
        name="document_edit"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/revise/$',
        DocumentRevise.as_view(),
        name="document_revise"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/delete/$',
        DocumentDelete.as_view(),
        name="document_delete"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/revision_delete/$',
        DocumentRevisionDelete.as_view(),
        name="document_revision_delete"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/(?P<revision>\d+)/(?P<field_name>\w+)/$',
        RevisionFileDownload.as_view(),
        name="revision_file_download"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/(?P<field_name>\w+)/$',
        DocumentFileDownload.as_view(),
        name="document_file_download"),
]
