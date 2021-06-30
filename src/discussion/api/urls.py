
from django.urls import path

from discussion.api.views import DiscussionViewSet

note_list = DiscussionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
note_detail = DiscussionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('(?P<document_key>[\w-]+)/(?P<revision>\d+)/$', note_list, name='note-list'),
    path('(?P<document_key>[\w-]+)/(?P<revision>\d+)/(?P<pk>\d+)/$', note_detail, name='note-detail'),
]
