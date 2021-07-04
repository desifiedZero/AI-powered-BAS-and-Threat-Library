import json
import os

from djangoProject import settings


class ThreatApi:
    def __init__(self):
        self.threatList = []

    def add(self, threat):
        if not isinstance(threat, Threat):
            return None
        self.threatList.append(threat)

    @property
    def dict(self):
        ret = {
            "success": True,
            "threats": []
        }
        for threat in self.threatList:
            ret['threats'].append(threat.dict)
        return ret

    @property
    def json(self):
        return json.dumps(self.dict)

    def populate(self):
        path = os.path.join(settings.BASE_DIR, 'tl.json')
        file = open(path, 'r')
        threats = json.load(file)

        for threat in threats['threats']:
            self.add(Threat(threat))


class Threat:
    def __init__(self, id, cve, name, description, impact):
        self.id = id
        self.cve = cve
        self.name = name
        self.description = description
        self.impact = impact

    def __init__(self, threat):
        self.id = threat['id']
        self.cve = threat['cve']
        self.name = threat['name']
        self.description = threat['description']
        self.impact = threat['impact']

    @property
    def dict(self):
        return {
            "id": self.id,
            "cve": self.cve,
            "name": self.name,
            "description": self.description,
            "impact": self.impact,
        }

    @property
    def json(self):
        return json.dumps(self.dict)
