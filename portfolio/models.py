from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    habilidades = models.TextField(max_length=350)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title
