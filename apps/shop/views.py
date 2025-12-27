from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    return render(request, 'shop/home.html', {
        'title': 'Головна сторінка магазину',
        'greeting': 'Ласкаво просимо до нашого магазину!',
        'categories': categories,  # передаємо список категорій у шаблон
    })

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()  # завдяки related_name="products"
    return render(request, 'shop/category_detail.html', {
        'category': category,
        'products': products,
    })

def product_detail(request, category_id, product_name):
    product = get_object_or_404(Product, category_id=category_id, slug=product_name)
    return render(request, 'shop/product_detail.html', {
        'product': product,
    })