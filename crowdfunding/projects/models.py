from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg, Count, Min, Sum
from django.utils import timezone

User = get_user_model()

now = timezone.now()
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.PositiveIntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    # owner = models.CharField(max_length=200)
    # liked_by = models.ManyToManyField(
    #     User,
    #     related_name='liked_projects'
    # )

    @property
    def total(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']



class Pledge(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField()
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    date_created = models.DateTimeField(auto_now_add=True)


class ProjectUpdates(models.Model):
    content = models.TextField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='project_udpates'
    )
    date_created = models.DateTimeField(auto_now_add=True)


class LikedBy(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='likedby_project'
    )
    liked_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liked_by_user'
    )
    date_created = models.DateTimeField(auto_now_add=True)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
