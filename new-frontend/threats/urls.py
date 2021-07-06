from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAll, name='threats.all'),
    path('<str:id>', views.threat, name='threats.threat'),
    path('launch/<str:id>', views.launch_attack, name='threats.launch'),
]