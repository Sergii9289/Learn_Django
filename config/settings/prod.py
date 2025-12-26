"""
Налаштування для продакшена
"""

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Продакшен база (наприклад PostgreSQL)
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

# Безпека
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # 1 рік
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Застосовувати до всіх піддоменів
SECURE_HSTS_PRELOAD = True  # Рекомендується для попереднього завантаження HSTS