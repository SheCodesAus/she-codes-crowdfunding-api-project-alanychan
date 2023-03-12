from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True)
    location  = models.CharField(max_length=150, null=True)
    photo_meme = models.URLField(null=True)

    def __str__(self):
        return self.username
