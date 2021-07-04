from django.db import models

# Create your models here.
from rest_framework import serializers


class Report(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    image = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.id


class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"

