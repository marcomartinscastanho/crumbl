import uuid
from django.db import models


class Tag(models.Model):
    name = models.CharField(primary_key=True, default=uuid.uuid4, max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def num_posts(self):
        return len(self.posts.all())
