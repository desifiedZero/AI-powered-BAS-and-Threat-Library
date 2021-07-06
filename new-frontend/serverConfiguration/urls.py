from django.urls import path
from . import views

urlpatterns = [
    path('configure/', views.get, name='server.configure'),
]