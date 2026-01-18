from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')  # Завантаження в папку avatars/

    def __str__(self):
        return self.name