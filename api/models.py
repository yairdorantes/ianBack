from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    # image = models.ImageField(upload_to='products')
    
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = JSONField(blank=True)
    def __str__(self):
        return f"{self.user.username}'s cart"


class UserProfile(AbstractUser):
    avatar = models.TextField(default="",blank=True)
