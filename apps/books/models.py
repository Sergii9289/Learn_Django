from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)   # Назва книги
    author = models.CharField(max_length=100)  # Автор
    genre = models.CharField(max_length=50)    # Жанр
    year = models.PositiveIntegerField()       # Рік видання

    def __str__(self):
        return f"{self.title} — {self.author} ({self.year})"