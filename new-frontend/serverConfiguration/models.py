from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ServerConfiguration(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=150)

    def __str__(self):
        return self.user_id
