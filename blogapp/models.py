from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

user = get_user_model()


class Author(models.Model):
    author = models.OneToOneField(user, on_delete=models.CASCADE)
    author_image = models.ImageField(upload_to='pics', blank=True, default='author.jpg')


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True, default="")
    content = models.TextField(max_length=500, default="")
    image = models.ImageField(upload_to='pics', blank=True, default='author.jpg')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
