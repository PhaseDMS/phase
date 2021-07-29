from django.urls import path


from search.views import SearchDocuments


urlpatterns = [
    path(
        "<slug:organisation>/<slug:category>/",
        SearchDocuments.as_view(),
        name="search_documents",
    ),
]
