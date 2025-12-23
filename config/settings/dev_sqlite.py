"""
Налаштування для розробки
"""

from .base import *

DEBUG = env("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = []

# Локальна база (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
