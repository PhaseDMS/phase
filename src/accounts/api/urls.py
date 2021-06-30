
from django.urls import path

from accounts.api.views import UserViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/$', user_list, name='user-list'),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<pk>\d+)/$',
        user_detail, name='user-detail'),
]
