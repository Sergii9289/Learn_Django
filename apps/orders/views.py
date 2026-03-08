# orders\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.shop.models import Product
from .models import Cart, CartItem

@login_required
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('orders:cart')

@login_required
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('orders:cart')

@login_required
def cart_view(request):
    cart = getattr(request.user, "cart", None)
    return render(request, "orders/cart.html", {"cart": cart})