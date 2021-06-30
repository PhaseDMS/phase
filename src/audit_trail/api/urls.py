from django.urls import path
from .views import AuditTrailList

urlpatterns = [
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/$',
        AuditTrailList.as_view(),
        name='document_audit_trail'),
]
