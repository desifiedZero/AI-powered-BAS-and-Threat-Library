from django.db import models

# Create your models here.


class AppUser(models.Model):
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=16)

    def __str__(self):
        return self.email