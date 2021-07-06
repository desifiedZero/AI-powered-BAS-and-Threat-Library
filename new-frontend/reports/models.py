from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from rest_framework import serializers


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    output = models.CharField(max_length=3000, null=True)
    threat = models.IntegerField(max_length=30, null=True)
    success = models.BooleanField(default=0)

    def __str__(self):
        return self.id
