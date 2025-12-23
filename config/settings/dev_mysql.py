"""
Налаштування для розробки
"""

from .base import *

DEBUG = env("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = []

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'my_db',
    'USER': 'my_db_user',
    'PASSWORD': '12345',
    'HOST': 'localhost',
    'PORT': '3306',
}
}