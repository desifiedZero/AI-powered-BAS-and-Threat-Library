from django.shortcuts import render

# Create your views here.
from classes.threatApi import ThreatApi
from reports.models import Report


def getAll(request):
    reports = Report.objects.filter(user_id=request.user.id)
    data = {
        'reports': reports
    }

    return render(request, "user/reports/reports.dj.html", data)


def get(request, id):
    report = Report.objects.get(id=id)
    print(report.date_added)
    threats = ThreatApi()
    threats.populate()
    ths = threats.dict
    threat = None
    for th in ths['threats']:
        if int(th['id']) == int(report.threat):
            threat = th
            break
    data = {
        "report": report,
        "threat": threat
    }
    return render(request, "user/reports/report.dj.html", data)


