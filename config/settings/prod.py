"""
Налаштування для продакшена
"""

from .base import *

DEBUG = False
ALLOWED_HOSTS = ["mydomain.com", "www.mydomain.com"]

# Продакшен база (наприклад PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "prod_db",
        "USER": "prod_user",
        "PASSWORD": "секретний_пароль",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Безпека
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True