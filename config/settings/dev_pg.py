"""
Налаштування для розробки
"""

from .base import *

DEBUG = env("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "prod_db",
        "USER": "prod_user",
        "PASSWORD": "12345",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}