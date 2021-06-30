from django.urls import path

from feeds.views import (
    AlertHome,
    AlertNewDocuments,
    AlertClosedReviews,
    AlertStartedReviews,
    AlertOverdueDocuments,
)
from feeds.feeds import (
    FeedNewDocuments,
    FeedClosedReviews,
    FeedStartedReviews,
    FeedOverdueDocuments,
)


urlpatterns = [
    path(
        "<slug:organisation>/<slug:category>/",
        AlertHome.as_view(),
        name="category_feeds",
    ),
    path(
        "<slug:organisation>/<slug:category>/new_documents/",
        AlertNewDocuments.as_view(),
        name="alert_new_documents",
    ),
    path(
        "<slug:organisation>/<slug:category>/new_documents.rss",
        FeedNewDocuments.as_view(),
        name="feed_new_documents",
    ),
    path(
        "<slug:organisation>/<slug:category>/closed_reviews/",
        AlertClosedReviews.as_view(),
        name="alert_closed_reviews",
    ),
    path(
        "<slug:organisation>/<slug:category>/closed_reviews.rss",
        FeedClosedReviews.as_view(),
        name="feed_closed_reviews",
    ),
    path(
        "<slug:organisation>/<slug:category>/under_review/",
        AlertStartedReviews.as_view(),
        name="alert_started_reviews",
    ),
    path(
        "<slug:organisation>/<slug:category>/under_review.rss",
        FeedStartedReviews.as_view(),
        name="feed_started_reviews",
    ),
    path(
        "<slug:organisation>/<slug:category>/overdue_documents/",
        AlertOverdueDocuments.as_view(),
        name="alert_overdue_documents",
    ),
    path(
        "<slug:organisation>/<slug:category>/overdue_documents.rss",
        FeedOverdueDocuments.as_view(),
        name="feed_overdue_documents",
    ),
]
