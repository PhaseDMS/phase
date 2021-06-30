
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
    path('<slug:organisation>/<slug:category>/', user_list, name='user-list'),
    path('<slug:organisation>/<slug:category>/<int:pk>/',
        user_detail, name='user-detail'),
]
