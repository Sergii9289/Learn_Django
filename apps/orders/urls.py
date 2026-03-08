from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_item, name='add_item'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),
]