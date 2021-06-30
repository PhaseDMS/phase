from django.urls import path


from search.views import SearchDocuments


urlpatterns = [
    path('(?P<organisation>[\w-]+)/(?P<category>[\w-]+)/$',
        SearchDocuments.as_view(),
        name='search_documents'),
]
