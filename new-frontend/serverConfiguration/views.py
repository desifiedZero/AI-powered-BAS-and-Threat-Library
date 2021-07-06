from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from serverConfiguration.models import ServerConfiguration


@login_required
def get(request):
    if request.method == 'POST':
        return set_conf(request)
    try:
        conf = ServerConfiguration.objects.get(user=request.user)
    except ServerConfiguration.DoesNotExist:
        conf = ServerConfiguration.objects.create(user_id=request.user.id)
    data = {
        'conf': conf
    }
    return render(request, "user/server/configuration.dj.html", data)


@login_required
def set_conf(request):
    post = request.POST
    hostname = post['hostname']
    try:
        server_configuration = ServerConfiguration.objects.get(user=request.user)
        server_configuration.hostname = hostname
        server_configuration.save()
    except ServerConfiguration.DoesNotExist:
        server_configuration = ServerConfiguration.objects.create(user=request.user, hostname=hostname)
        server_configuration.save()
    return redirect('server.configure')