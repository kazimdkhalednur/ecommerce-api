from datetime import timedelta

from .base import *

AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS = [
    *INSTALLED_APPS,
    "drf_spectacular_sidecar",  # required for Django collectstatic discovery
]

INTERNAL_IPS = [
    "127.0.0.1",
]

REST_FRAMEWORK.update(
    {
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    }
)

SPECTACULAR_SETTINGS.update(
    {
        "SWAGGER_UI_DIST": "SIDECAR",
        "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
        "REDOC_DIST": "SIDECAR",
    }
)

DEBUG_TOOLBAR_CONFIG = {"IS_RUNNING_TESTS": False}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=365),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
}


if not TESTING:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "debug_toolbar",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]
