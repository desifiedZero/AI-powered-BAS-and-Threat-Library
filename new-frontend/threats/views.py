import io
import os
from contextlib import redirect_stdout

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from classes.threatApi import ThreatApi
from reports.models import Report
from serverConfiguration.models import ServerConfiguration
from threats.models import Threat, ThreatSerializer


@login_required
def getAll(request):
    all_threats = Threat.objects.all()
    data = {
        #'threats': all_threats
        'threats': threats_get()['threats']
    }
    return render(request, 'user/threats/main.dj.html', data)


@login_required
def threat(request, id):
    threats = threats_get()
    pass_threat = None
    for threat in threats['threats']:
        if threat['id'] == id:
            pass_threat = threat
            break

    data = {
        'threat': pass_threat
    }
    return render(request, 'user/threats/threat.dj.html', data)
#    try:
#        th = Threat.objects.get(id=id)
#    except Threat.DoesNotExist:
#        raise Http404("CVE does not exist on this system")
#    data = {
#        'threat': th
#    }
#    return render(request, 'user/threats/threat.dj.html', data)

def threats_get():
    threats = ThreatApi()
    threats.populate()

    return threats.dict


@login_required
def launch_attack(request, id):
    threats = threats_get()
    threat = None
    for th in threats['threats']:
        if th['id'] == id:
            threat = th
            break
    f = io.StringIO()
    with redirect_stdout(f):
        import importlib
        call = threat['call']
        file = threat['file']
        mod = importlib.import_module("attacks." + file.split(".py")[0])
        method = getattr(mod, call)
        if len(threat['params']) == 1 and threat['params'][0] == 'hostname':
            try:
                method(ServerConfiguration.objects.get(user_id=request.user.id).hostname)
            except BadRequest:
                return BadRequest()
    out = f.getvalue()
    out = out.replace('', '\n')
    success = 0
    for keyword in threat['success_keywords']:
        if out.find(keyword) >= 0:
            success = 1
            break
    report = Report.objects.create(user_id=request.user.id, output=out, threat=threat['id'], success=success)
    report.save()
    data = {
        "threat": threat,
        "success": success,
        "report": report,
    }
    return render(request, 'user/threats/launch.dj.html', data)
