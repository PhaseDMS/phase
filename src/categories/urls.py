from django.urls import path

from categories.views import CategoryList


urlpatterns = [
    path('',
        CategoryList.as_view(),
        name="category_list"),
]
