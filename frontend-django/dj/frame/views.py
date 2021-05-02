from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registeration(request):
    return render(request, 'registeration.html')

def navbar(request):
    return render(request, 'navbar.html')

def login(request):
    return render(request, 'login.html')
  