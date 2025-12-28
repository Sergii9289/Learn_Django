from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Profile
from .forms import AvatarUploadForm
from django.http import JsonResponse
from django.views.generic import ListView, FormView


class PostsListView(ListView):
    model = BlogPost
    template_name = 'blog_posts.html'
    context_object_name = 'posts'


class AvatarUploadView(FormView):
    template_name = 'upload_avatar.html'
    form_class = AvatarUploadForm

    # def dispatch(self, request, *args, **kwargs):
    #     # Перевірка авторизації
    #     if not request.user.is_authenticated:
    #         return JsonResponse({"error": "Futenthication needed"}, status=401)
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        profile = form.cleaned_data['author']
        profile.avatar = form.cleaned_data['avatar']
        profile.save()
        return redirect('blog:profile')


def home(request):
    return render(request, 'home.html', {'greeting': 'HELLO!'})


def view_avatar(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'view_avatar.html', {'profile': profile})


def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
