from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)  # Текстове поле з обмеженням довжини
    content = models.TextField()             # Велике текстове поле
    author = models.CharField(max_length=50) # Автор поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення

    def __str__(self):
        return self.title  # Для зручного відображення в адмінці