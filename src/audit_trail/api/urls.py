from django.urls import path
from .views import AuditTrailList

urlpatterns = [
    path(
        "<slug:organisation>/<slug:category>/<slug:document_key>/",
        AuditTrailList.as_view(),
        name="document_audit_trail",
    ),
]
