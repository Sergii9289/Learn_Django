from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.blog.urls', namespace='blog')),  # підключаємо з namespace
    path('shop/', include('apps.shop.urls', namespace='shop')),  # підключаємо з namespace
]

if settings.DEBUG:  # Тільки для режиму розробки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)