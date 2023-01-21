from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    # owner = models.CharField(max_length=200)


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporte_pledges'
    )
    # supporter = models.CharField(max_length=200)