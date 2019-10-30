from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from tinymce.models import HTMLField
from datetime import datetime
from django.contrib.auth import get_user_model
from django.conf import settings

user = get_user_model()


class Textile(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=None)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics', blank=True, default='author.jpg')


class Cart(models.Model):
    title = models.ForeignKey(Textile, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    size = models.IntegerField(default=None)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    totalprice=models.IntegerField(default=None)

class Buynow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    title = models.ForeignKey(Textile, on_delete=models.CASCADE, blank=True, null=True)
    state = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    apartment = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    postcode= models.IntegerField(default=None)
    phone = models.IntegerField(default=None)
    firstname = models.CharField(max_length=100, default=None)
    lastname = models.CharField(max_length=100, default=None)
    email = models.EmailField(default=None)


class Coupon(models.Model):
    code = models.CharField(max_length=50)
    cprice = models.IntegerField(default=0)
