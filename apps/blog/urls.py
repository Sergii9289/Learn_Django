from django.urls import path
from . import views
from .views import PostsListView, AvatarUploadView, PostCreateView

app_name = 'blog'  # Вказуємо namespace для додатку

urlpatterns = [
    path('', views.home, name='home'),  # Головна сторінка нашого блогу
    path('posts/', PostsListView.as_view(), name='blog_posts'),
    path('avatar/', AvatarUploadView.as_view(), name="upload_avatar"),
    path('avatar/<int:pk>/', views.view_avatar, name="view_avatar"),  # динамічний url
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
]