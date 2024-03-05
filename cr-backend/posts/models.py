from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    text = models.TextField(max_length=1000, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    position = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=100)
    thumb = models.URLField()
    large = models.URLField()

    class Meta:
        ordering = ["post", "position"]
