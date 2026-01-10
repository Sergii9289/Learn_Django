from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.blog.urls', namespace='blog')),  # підключаємо з namespace
    path('shop/', include('apps.shop.urls', namespace='shop')),  # підключаємо з namespace
    path('books/', include('apps.books.urls', namespace='books')),  # підключаємо з namespace
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
]

if settings.DEBUG:  # Тільки для режиму розробки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
