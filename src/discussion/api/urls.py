from django.urls import path

from discussion.api.views import DiscussionViewSet

note_list = DiscussionViewSet.as_view({"get": "list", "post": "create"})
note_detail = DiscussionViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)


urlpatterns = [
    path("<slug:document_key>/<int:revision>/", note_list, name="note-list"),
    path(
        "<slug:document_key>/<int:revision>/<int:pk>/", note_detail, name="note-detail"
    ),
]
