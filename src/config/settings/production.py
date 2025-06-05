import os

from .base import *

# django security configurations
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

os.makedirs("logs", exist_ok=True)
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
            "filename": f"{BASE_DIR}/logs/error_5xx.log",
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
