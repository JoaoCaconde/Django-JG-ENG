from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)

    def __str__(self):
        return self.title
