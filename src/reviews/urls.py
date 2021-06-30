from django.urls import path

from reviews.views import (
    ReviewersDocumentList, LeaderDocumentList, ApproverDocumentList,
    ReviewFormView, StartReview, CancelReview, BatchStartReviews,
    BatchCancelReviews, PrioritiesDocumentList, ReviewHome, CommentsDownload,
    CommentsArchiveDownload,
)
from reviews.feeds import (
    FeedReviewersDocumentList, FeedLeaderDocumentList, FeedApproverDocumentList)

urlpatterns = [

    # Review home page
    path('$',
        ReviewHome.as_view(),
        name='review_home'),

    # Cancel review
    path('(?P<document_key>[\w-]+)/cancel/$',
        CancelReview.as_view(),
        name="document_cancel_review"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/batchcancel/$',
        BatchCancelReviews.as_view(),
        name="batch_cancel_reviews"),

    # Start review
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/batchstart/$',
        BatchStartReviews.as_view(),
        name="batch_start_reviews"),
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/(?P<document_key>[\w-]+)/$',
        StartReview.as_view(),
        name="document_start_review"),

    # Review steps
    path('priorities/$',
        PrioritiesDocumentList.as_view(),
        name="priorities_review_document_list"),
    path('reviewers/$',
        ReviewersDocumentList.as_view(),
        name="reviewers_review_document_list"),
    path('leader/$',
        LeaderDocumentList.as_view(),
        name="leader_review_document_list"),
    path('approver/$',
        ApproverDocumentList.as_view(),
        name="approver_review_document_list"),

    # Review steps feeds
    path('reviewers.rss$',
        FeedReviewersDocumentList.as_view(),
        name="feed_reviewers_review_document_list"),
    path('leader.rss$',
        FeedLeaderDocumentList.as_view(),
        name="feed_leader_review_document_list"),
    path('approver.rss$',
        FeedApproverDocumentList.as_view(),
        name="feed_approver_review_document_list"),

    # Review form
    path('(?P<document_key>[\w-]+)/$',
        ReviewFormView.as_view(),
        name="review_document"),

    # Comments download
    path('(?P<document_key>[\w-]+)/(?P<revision>\d+)/comments/(?P<review_id>\d+)/$',
        CommentsDownload.as_view(),
        name="download_review_comments"),
    path('(?P<document_key>[\w-]+)/(?P<revision>\d+)/comments/all.zip$',
        CommentsArchiveDownload.as_view(),
        name="download_review_comments_archive"),
]
