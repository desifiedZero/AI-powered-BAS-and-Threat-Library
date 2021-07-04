from django.urls import path
from . import views

urlpatterns = [
    path('threats', views.getAll, name='json.threats.all'),
]