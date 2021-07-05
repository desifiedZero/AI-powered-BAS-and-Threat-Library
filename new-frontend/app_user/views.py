from django.contrib import messages
from django.contrib.auth import authenticate, logout as logout_user, login as login_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect

# Create your views here.
from app_user.models import AppUser


def login(request):
    if request.method == 'POST':
        return login_submit(request)
    return render(request, 'login/login.dj.html')


def login_submit(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    print(user)
    if user is not None:
        login_user(request, user)
        next = request.GET.get('next')
        if (next is not None) and ('logout' not in next):
            return redirect(next)
        return redirect('dashboard')
    messages.add_message(request, messages.ERROR, "Username/Password Incorrect")
    return render(request, 'login/login.dj.html')


def register(request):
    if request.method == 'POST':
        return register_submit(request)
    return render(request, 'login/register.dj.html')


def register_submit(request):
    if request.method == 'POST':
        userdata = request.POST
        if userdata['password'] == userdata['confirm_password']:
            User.objects.create_user(userdata['username'], userdata['email'], userdata['password'],
                                     first_name=userdata['fname'], last_name=userdata['lname'], is_staff=False)
            return HttpResponse("<h1>User has been registered.</h1>")
        return HttpResponse("<h1>Error: Could not create user.</h1>"
                            "<a href=\"/register\">Get back to register page</a>")
    return HttpResponseBadRequest('Invalid request type')


@login_required
def logout(request):
    logout_user(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.dj.html')


@login_required
def user_settings(request):
    if request.method == 'POST':
        return set_user_settings(request)
    return render(request, 'user/settings/index.dj.html')


@login_required
def set_user_settings(request):
    user = User.objects.get(username=request.user.username)
    post = request.POST
    if user.check_password(post['old_password']):
        if post['new_password'] == post['repeat_new_password']:
            user.set_password(post['new_password'])
            user.save()
            messages.success(request, "Please log in again")
            return redir(request)
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'user/settings/index.dj.html')
    else:
        messages.error(request, 'Incorrect Password')
        return redirect('user.settings')


def redir(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')
