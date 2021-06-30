from django.urls import path

from documents.views import (
    DocumentList, DocumentCreate, DocumentDetail, DocumentEdit,
    DocumentDownload, DocumentRedirect, DocumentRevise, DocumentDelete,
    DocumentRevisionDelete, RevisionFileDownload, DocumentFileDownload
)

urlpatterns = [

    # Document short url
    path('documents/<slug:document_key>/',
        DocumentRedirect.as_view(),
        name='document_short_url'),

    # Downloads
    path('<slug:organisation>/<slug:category>/download/',
        DocumentDownload.as_view(),
        name="document_download"),

    # Documents
    path('<slug:organisation>/<slug:category>/',
        DocumentList.as_view(),
        name="category_document_list"),
    path('<slug:organisation>/<slug:category>/create/',
        DocumentCreate.as_view(),
        name="document_create"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/',
        DocumentDetail.as_view(),
        name="document_detail"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/edit/',
        DocumentEdit.as_view(),
        name="document_edit"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/edit/<int:revision>/',
        DocumentEdit.as_view(),
        name="document_edit"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/revise/',
        DocumentRevise.as_view(),
        name="document_revise"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/delete/',
        DocumentDelete.as_view(),
        name="document_delete"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/revision_delete/',
        DocumentRevisionDelete.as_view(),
        name="document_revision_delete"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/<int:revision>/<slug:field_name>/',
        RevisionFileDownload.as_view(),
        name="revision_file_download"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/<slug:field_name>/',
        DocumentFileDownload.as_view(),
        name="document_file_download"),
]
