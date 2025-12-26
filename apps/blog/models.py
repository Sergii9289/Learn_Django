from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')  # Завантаження в папку avatars/

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)  # Текстове поле з обмеженням довжини
    content = models.TextField()  # Велике текстове поле
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення

    def __str__(self):
        return self.title
