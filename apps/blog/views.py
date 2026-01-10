from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Profile
from .forms import AvatarUploadForm
from django.http import JsonResponse
from django.views.generic import ListView, FormView, CreateView
from django.urls import reverse_lazy


class PostsListView(ListView):
    model = BlogPost
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return BlogPost.objects.order_by('-created_at')


class PostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'author']  # поля для заповнення
    success_url = reverse_lazy('blog:blog_posts')  # після створення перенаправляє на список постів

    def form_valid(self, form):
        # Можна додати додаткову логіку перед збереженням
        response = super().form_valid(form)
        return response


class AvatarUploadView(FormView):
    template_name = 'blog/upload_avatar.html'
    form_class = AvatarUploadForm

    def dispatch(self, request, *args, **kwargs):
        print(f"Request method: {request.method}, Request path: {request.path}")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        profile = form.cleaned_data['author']
        profile.avatar = form.cleaned_data['avatar']
        profile.save()
        return redirect('blog:profile')


def home(request):
    return render(request, 'blog/home.html', {'greeting': 'Вітаю у Django проекті Сергія Цеміка!'})


def view_avatar(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'blog/view_avatar.html', {'profile': profile})


def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
