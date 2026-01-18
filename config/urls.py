from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from apps.blog.views import post_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.index, name='index'),  # Головна сторінка нашого сайту
    # path('', include('apps.blog.urls', namespace='blog')),  # підключаємо з namespace
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('shop/', include('apps.shop.urls', namespace='shop')),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
]
if settings.DEBUG:  # Тільки для режиму розробки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
