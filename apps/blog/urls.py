from django.urls import path
from . import views
from .views.post_views import *

app_name = 'blog'  # Вказуємо namespace для додатку

urlpatterns = [
    # path('', views.home, name='home'),  # Головна сторінка нашого сайту
    path('posts/', PostsListView.as_view(), name='blog_posts'),
    path('avatar/', AvatarUploadView.as_view(), name="upload_avatar"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
