from django.contrib.auth.models import User
from django.http import HttpResponse

from classes.threatApi import ThreatApi


def getAll(request):
    threats = ThreatApi()
    threats.populate()

    return HttpResponse(threats.json, content_type="application/json")
