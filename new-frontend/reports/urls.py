from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAll, name='reports.all'),
    path('<int:id>', views.get, name='reports.get'),
]
