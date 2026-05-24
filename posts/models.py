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


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "comments"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "likes"
        unique_together = ['post', 'user']  # Prevents a user from liking the same post twice
    
    def __str__(self):
        return f"{self.user.username} liked post {self.post.id}"
