from .base import *

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = config("AWS_S3_ENDPOINT_URL")
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = "static"
AWS_DEFAULT_ACL = "public-read"

STATIC_URL = "{}/{}/{}/".format(
    AWS_S3_ENDPOINT_URL, AWS_STORAGE_BUCKET_NAME, AWS_LOCATION
)

# django security configurations
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "error_5xx": {
            "()": "django.utils.log.ServerFormatter",
            "format": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "error_5xx_handler": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{BASE_DIR}/log/error_5xx.log",
            "formatter": "error_5xx",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 50,  # 50MB
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["error_5xx_handler"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
