from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Profile
from .forms import AvatarUploadForm


def home(request):
    return render(request, 'home.html', {'greeting': 'HELLO!'})


def blog_posts(request):
    posts = BlogPost.objects.all()  # Отримуємо всі пости
    return render(request, 'blog_posts.html', {'posts': posts})


def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.cleaned_data['author']
            profile.avatar = form.cleaned_data['avatar']
            profile.save()
            return redirect('blog:upload_avatar')
    else:
        form = AvatarUploadForm()
    return render(request, 'upload.html', {'form': form})


def view_avatar(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'view_avatar.html', {'profile': profile})