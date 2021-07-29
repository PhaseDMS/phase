"""Development settings and globals."""
from unipath import Path  # Avoid pyflakes complains

import warnings

from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE  # Avoid pyflake complains

# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# ######### END DEBUG CONFIGURATION

# Third party templates are cached.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "OPTIONS": {
            "debug": True,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.static",
                "accounts.context_processors.navigation",
                "accounts.context_processors.branding_on_login",
                "notifications.context_processors.notifications",
                "reviews.context_processors.reviews",
                "dashboards.context_processors.dashboards",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.app_directories.Loader",
                    ],
                ),
                "django.template.loaders.filesystem.Loader",
            ],
        },
    },
]


# ######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SEND_EMAIL_REMINDERS = True
SEND_NEW_ACCOUNTS_EMAILS = True
# ######### END EMAIL CONFIGURATION


# ######### DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "phase",
        "USER": "phase",
        "PASSWORD": "phase",
        "HOST": "localhost",
        "PORT": "",
    }
}
# ######### END DATABASE CONFIGURATION


# ######### CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
# ######### END CACHE CONFIGURATION


# ######### TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += ("debug_toolbar",)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ("127.0.0.1",)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

DEBUG_TOOLBAR_PATCH_SETTINGS = False
# Disable template panel because of this bug:
# https://github.com/jazzband/django-debug-toolbar/issues/910


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": {
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
    },
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
# ######### END TOOLBAR CONFIGURATION

warnings.filterwarnings(
    "error",
    r"DateTimeField .* received a naive datetime",
    RuntimeWarning,
    r"django\.db\.models\.fields",
)

# ######### TRANSMITTALS IMPORT CONFIGURATION

TRS_IMPORTS_ROOT = Path("/tmp/dummy_ctr")

TRS_IMPORTS_CONFIG = {
    "dummy_ctr": {
        "INCOMING_DIR": TRS_IMPORTS_ROOT.child("incoming"),
        "REJECTED_DIR": TRS_IMPORTS_ROOT.child("rejected"),
        "TO_BE_CHECKED_DIR": TRS_IMPORTS_ROOT.child("tobechecked"),
        "ACCEPTED_DIR": TRS_IMPORTS_ROOT.child("accepted"),
        "EMAIL_LIST": ["test@localhost"],
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ALLOWED_HOSTS = ["phase", "phasectr", "phase.local"]


try:
    from .local_private import *  # noqa
except ImportError:
    pass
