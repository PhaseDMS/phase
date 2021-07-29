from django.urls import include, path
from django.http import HttpResponse
from django.contrib import admin
from django.conf import settings

from privatemedia.views import ProtectedDownload


admin.autodiscover()

admin.site.login_template = "registration/login.html"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("restapi.urls")),
    path("accounts/", include("accounts.urls")),
    path("favorites/", include("favorites.urls")),
    path("reviews/", include("reviews.urls")),
    path("distriblists/", include("distriblists.urls")),
    path("imports/", include("imports.urls")),
    path("transmittals/", include("transmittals.urls")),
    path("search/", include("search.urls")),
    path("exports/", include("exports.urls")),
    path("feeds/", include("feeds.urls")),
    path(
        "protected/<file_path>", ProtectedDownload.as_view(), name="protected_download"
    ),
    path("reporting/", include("reporting.urls")),
    path("", include("categories.urls")),
    path("", include("dashboards.urls")),
    path("", include("documents.urls")),
    path(
        "robots\.txt",
        lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain"),
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
