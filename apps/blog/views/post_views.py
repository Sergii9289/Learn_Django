from django.shortcuts import render, redirect, get_object_or_404
from ..models import BlogPost, Profile, Category
from ..forms import AvatarUploadForm
from django.views.generic import (ListView, FormView,
                                  CreateView, DetailView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class PostsListView(ListView):
    model = BlogPost
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'created_at')  # значення за замовчуванням
        order = self.request.GET.get('order', 'desc')  # напрямок сортування

        # Мапа дозволених полів
        allowed_sorts = {
            'created_at': 'created_at',
            'title': 'title',
            'author': 'author__name',
        }

        sort_field = allowed_sorts.get(sort, 'created_at')

        if order == 'asc':
            return BlogPost.objects.order_by(sort_field)
        return BlogPost.objects.order_by(f'-{sort_field}')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Profile.objects.all()
        context['categories'] = Category.objects.annotate(post_count=Count('posts'))
        # Передаємо вибрані параметри для шаблону
        context['current_sort'] = self.request.GET.get('sort', 'created_at')
        context['current_order'] = self.request.GET.get('order', 'desc')
        return context


class PostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'author', 'categories']  # 👈 додали categories
    success_url = reverse_lazy('blog:blog_posts')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/post_form.html'  # можна використати той самий шаблон, що й для створення
    fields = ['title', 'content', 'author', 'categories']  # поля для редагування
    context_object_name = 'post'

    def get_success_url(self):
        # після редагування перенаправляє на сторінку перегляду цього поста
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'  # шаблон підтвердження видалення
    context_object_name = 'post'
    success_url = reverse_lazy('blog:blog_posts')  # після видалення перенаправляє на список постів


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


def index(request):
    return render(request, 'blog/home.html', {'greeting': 'Вітаю у Django проекті Сергія Цеміка!'})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматично залогінити після реєстрації
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
