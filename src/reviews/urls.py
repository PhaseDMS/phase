from django.urls import path

from reviews.views import (
    ReviewersDocumentList,
    LeaderDocumentList,
    ApproverDocumentList,
    ReviewFormView,
    StartReview,
    CancelReview,
    BatchStartReviews,
    BatchCancelReviews,
    PrioritiesDocumentList,
    ReviewHome,
    CommentsDownload,
    CommentsArchiveDownload,
)
from reviews.feeds import (
    FeedReviewersDocumentList,
    FeedLeaderDocumentList,
    FeedApproverDocumentList,
)

urlpatterns = [
    # Review home page
    path("", ReviewHome.as_view(), name="review_home"),
    # Cancel review
    path(
        "<slug:document_key>/cancel/",
        CancelReview.as_view(),
        name="document_cancel_review",
    ),
    path(
        "<slug:organisation>/<slug:category>/batchcancel/",
        BatchCancelReviews.as_view(),
        name="batch_cancel_reviews",
    ),
    # Start review
    path(
        "<slug:organisation>/<slug:category>/batchstart/",
        BatchStartReviews.as_view(),
        name="batch_start_reviews",
    ),
    path(
        "<slug:organisation>/<slug:category>/<slug:document_key>/",
        StartReview.as_view(),
        name="document_start_review",
    ),
    # Review steps
    path(
        "priorities/",
        PrioritiesDocumentList.as_view(),
        name="priorities_review_document_list",
    ),
    path(
        "reviewers/",
        ReviewersDocumentList.as_view(),
        name="reviewers_review_document_list",
    ),
    path("leader/", LeaderDocumentList.as_view(), name="leader_review_document_list"),
    path(
        "approver/",
        ApproverDocumentList.as_view(),
        name="approver_review_document_list",
    ),
    # Review steps feeds
    path(
        "reviewers.rss",
        FeedReviewersDocumentList.as_view(),
        name="feed_reviewers_review_document_list",
    ),
    path(
        "leader.rss",
        FeedLeaderDocumentList.as_view(),
        name="feed_leader_review_document_list",
    ),
    path(
        "approver.rss",
        FeedApproverDocumentList.as_view(),
        name="feed_approver_review_document_list",
    ),
    # Review form
    path("<slug:document_key>/", ReviewFormView.as_view(), name="review_document"),
    # Comments download
    path(
        "<slug:document_key>/<int:revision>/comments/<int:review_id>/",
        CommentsDownload.as_view(),
        name="download_review_comments",
    ),
    path(
        "<slug:document_key>/<int:revision>/comments/all.zip",
        CommentsArchiveDownload.as_view(),
        name="download_review_comments_archive",
    ),
]
