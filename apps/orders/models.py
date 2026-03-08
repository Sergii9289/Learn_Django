# apps/orders/models.py
from django.db import models
from django.contrib.auth.models import User
from apps.shop.models import Product
from django.db.models import Sum, F


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cart"
    )

    def __str__(self):
        return f"Cart of {self.user.username}"

    def total_price(self):
        return self.items.aggregate(
            total=Sum(F("quantity") * F("product__price"))
        )["total"] or 0



class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.brand} {self.product.model} x{self.quantity}"

    def total_price(self):
        return self.product.price * self.quantity