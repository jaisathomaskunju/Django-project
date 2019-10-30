from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Textile(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=None)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics', blank=True, default='author.jpg')


users = get_user_model()


class Cart(models.Model):
    title = models.ForeignKey(Textile, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    # user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default="")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    # user = models.ForeignKey(users, on_delete=models.CASCADE, default="")
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(default=None)
    date = models.DateTimeField(default=datetime.now, blank=True)
    # color = models.CharField(max_length=200, default="")
    size = models.IntegerField(default=None)


class Checkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    title = models.ForeignKey(Textile, on_delete=models.CASCADE, default="")
    state = models.CharField(max_length=100, default=None)
    street = models.CharField(max_length=100, default=None)
    apartment = models.CharField(max_length=100, default=None)
    town = models.CharField(max_length=100, default=None)
    postcode = models.IntegerField(max_length=6, default=None)
    phone = models.IntegerField(max_length=10, default=None)
    firstname = models.CharField(max_length=20, default=None)
    lastname = models.CharField(max_length=20, default=None)
    email = models.EmailField(default=None)


class Coupon(models.Model):
    code = models.CharField(max_length=10, default=None)
    cprice = models.IntegerField(default=0)
