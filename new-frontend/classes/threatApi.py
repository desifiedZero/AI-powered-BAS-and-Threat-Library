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
    def __init__(self, id, cve, name, description, impact, image, file, call, params, success_keywords):
        self.id = id
        self.cve = cve
        self.name = name
        self.description = description
        self.impact = impact
        self.image = image
        self.file = file
        self.call = call
        self.params = params
        self.success_keywords = success_keywords

    def __init__(self, threat):
        self.id = threat['id']
        self.cve = threat['cve']
        self.name = threat['name']
        self.description = threat['description']
        self.impact = threat['impact']
        self.image = threat['image']
        self.file = threat['file']
        self.call = threat['call']
        self.params = threat['params']
        self.success_keywords = threat['success_keywords']

    @property
    def dict(self):
        return {
            "id": self.id,
            "cve": self.cve,
            "name": self.name,
            "description": self.description,
            "impact": self.impact,
            "image": self.image,
            "file": self.file,
            "call": self.call,
            "params": self.params,
            "success_keywords": self.success_keywords
        }

    @property
    def json(self):
        return json.dumps(self.dict)
