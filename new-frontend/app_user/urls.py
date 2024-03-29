from django.urls import path

from . import views

urlpatterns = [
    path('', views.redir, name='redir'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('settings/', views.user_settings, name='user.settings'),
]
