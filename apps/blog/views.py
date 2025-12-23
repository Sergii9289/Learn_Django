from django.shortcuts import render, redirect
from .models import BlogPost
from .models import Profile
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
            return redirect('upload_avatar')
    else:
        form = AvatarUploadForm()
    return render(request, 'upload.html', {'form': form})

