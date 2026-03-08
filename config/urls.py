# D:\Python\LearnDjango\mysite\config\urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from apps.blog.views import post_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.index, name='index'),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('shop/', include('apps.shop.urls', namespace='shop')),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

    # 👇 авторизація
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', TemplateView.as_view(template_name='logout.html'), name='logout'),
    path('register/', post_views.register, name='register'),
    path('logout/confirm/', auth_views.LogoutView.as_view(), name='logout-confirm'),

    # 👇 accounts
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
]

if settings.DEBUG:  # Тільки для режиму розробки
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns