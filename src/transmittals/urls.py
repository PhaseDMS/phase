from django.urls import path

from transmittals.views import (
    TransmittalList, TransmittalDiff, TransmittalRevisionDiff,
    TransmittalDownload, PrepareTransmittal, CreateTransmittal,
    AckOfTransmittalReceipt, BatchAckOfTransmittalReceipt,
    FileTransmittedDownload)

urlpatterns = [
    path('<slug:organisation>/<slug:category>/prepare/',
        PrepareTransmittal.as_view(),
        name="transmittal_prepare"),
    path('<slug:organisation>/<slug:category>/create/',
        CreateTransmittal.as_view(),
        name="transmittal_create"),
    path('<slug:organisation>/<slug:category>/ack/',
        BatchAckOfTransmittalReceipt.as_view(),
        name="transmittal_batch_ack_of_receipt"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/ack/',
        AckOfTransmittalReceipt.as_view(),
        name="transmittal_ack_of_receipt"),
    path('<slug:organisation>/<slug:category>/<slug:document_key>/file_transmitted/<slug:related_document_key>/<int:related_revision>/',
        FileTransmittedDownload.as_view(),
        name='file_transmitted_download'),

    # Incoming transmittal urls
    path('incoming/',
        TransmittalList.as_view(),
        name="transmittal_list"),
    path('incoming/<int:transmittal_pk>/<slug:document_key>/',
        TransmittalDiff.as_view(),
        name='transmittal_diff'),
    path('incoming/<int:transmittal_pk>/<slug:document_key>/download/',
        TransmittalDownload.as_view(),
        name='transmittal_download'),
    path('incoming/<int:transmittal_pk>/<slug:document_key>/<slug:revision_document_key>/<int:revision>/',
        TransmittalRevisionDiff.as_view(),
        name='transmittal_revision_diff'),
]
