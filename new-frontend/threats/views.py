from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from threats.models import Threat, ThreatSerializer


@login_required
def getAll(request):
    all_threats = Threat.objects.all()
    data = {
        'threats': all_threats
    }
    return render(request, 'user/threats/main.dj.html', data)


@login_required
def threat(request, id):
    try:
        th = Threat.objects.get(id=id)
    except Threat.DoesNotExist:
        raise Http404("CVE does not exist on this system")
    data = {
        'threat': th
    }
    return render(request, 'user/threats/threat.dj.html', data)
