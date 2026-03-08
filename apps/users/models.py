# D:\Python\LearnDjango\mysite\apps\users\models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Додаємо свої поля
    registration_date = models.DateTimeField(auto_now_add=True)