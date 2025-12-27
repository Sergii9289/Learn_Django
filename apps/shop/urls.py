# apps/shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),  # головна сторінка
    path('<int:category_id>/', views.category_detail, name='category_detail'),
    path('<int:category_id>/<slug:product_name>/', views.product_detail, name='product_detail'),
]