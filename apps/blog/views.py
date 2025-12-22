from django.shortcuts import render
from .models import BlogPost

def home(request):
    return render(request, 'home.html', {'greeting': 'HELLO!'})

def blog_posts(request):
    posts = BlogPost.objects.all()  # Отримуємо всі пости
    return render(request, 'blog_posts.html', {'posts': posts})