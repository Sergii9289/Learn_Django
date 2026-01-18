# apps/blog/models/post.py
from django.db import models
from django.urls import reverse
from .author import Profile
from .category import Category   # 👈 імпорт категорії

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    categories = models.ManyToManyField(Category, related_name="posts")  # 👈 зв’язок багато‑до‑багатьох
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})