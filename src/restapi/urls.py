from django.urls import path, include
from rest_framework import routers

from notifications.api import views as notifications_views
from favorites.api import views as favorites_views
from bookmarks.api import views as bookmarks_views
from restapi.views import TaskPollView


router = routers.DefaultRouter()
router.register(
    "notifications", notifications_views.NotificationViewSet, basename="notification"
)
router.register("favorites", favorites_views.FavoriteViewSet, basename="favorite")
router.register("bookmarks", bookmarks_views.BookmarkViewSet, basename="bookmark")


urlpatterns = [
    path("", include(router.urls)),
    path("discussion/", include("discussion.api.urls")),
    path("accounts/", include("accounts.api.urls")),
    path("distribution-lists/", include("distriblists.api.distribution_list_urls")),
    path("audit-trail/", include("audit_trail.api.urls")),
    # Task progress polling url
    path("poll/<slug:job_id>/", TaskPollView.as_view(), name="task_poll"),
]
