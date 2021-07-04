from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    token = models.CharField(max_length=150, default=None)

    def __str__(self):
        return self.email