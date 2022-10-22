
import json
from django.views import View
import requests


class MaterialService(object): 

    @staticmethod
    def addMaterial(request):
        request = json.loads(request.body)
        r=requests.post('http://127.0.0.1:7000/core/logoutAllSessions/',json = request)
        if r.status_code == 200 :

            return r.text
        else:
            return "Error has occured"

        

        