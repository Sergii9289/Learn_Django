from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Головна сторінка нашого блогу
    path('posts/', views.blog_posts, name='blog_posts'),
    path('avatar/', views.upload_avatar, name="upload_avatar"),
]