from django.urls import path

from .views import FavoriteList

urlpatterns = [
    # Favorites
    path("", FavoriteList.as_view(), name="favorite_list"),
]
