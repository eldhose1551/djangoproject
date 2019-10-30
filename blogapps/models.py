from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from tinymce.models import HTMLField
from datetime import datetime
from tinymce import models as tinymce_models

user = get_user_model()


class Author(models.Model):
    author = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    author_image = models.ImageField(upload_to='pics', blank=True, null=True, default='author.jpg')
    description = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.author.username


class Blogs(models.Model):
    title = models.CharField(max_length=200, unique=True, default="")
    # content = models.TextField(max_length=500, default="")
    content = tinymce_models.HTMLField('Content')
    image = models.ImageField(upload_to='pics', blank=True, default='author.jpg')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default="")
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)


class Comment(models.Model):
    # blog=models.ForeignKey(Blogs,)
    name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200, default="")
    website = models.CharField(max_length=200, default="")
    message = tinymce_models.HTMLField('Message')
    date = models.DateTimeField(default=datetime.now, blank=True)
