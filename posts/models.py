from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField(upload_to="posts")
    description = models.CharField(max_length=500, blank=True, default="")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)

    class Meta:
        db_table = "posts"
