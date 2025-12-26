from django.urls import path
from . import views

app_name = 'blog'  # Вказуємо namespace для додатку

urlpatterns = [
    path('', views.home, name='home'),  # Головна сторінка нашого блогу
    path('posts/', views.blog_posts, name='blog_posts'),
    path('avatar/', views.upload_avatar, name="upload_avatar"),
    path('avatar/<int:pk>/', views.view_avatar, name="view_avatar"),  # динамічний url
]