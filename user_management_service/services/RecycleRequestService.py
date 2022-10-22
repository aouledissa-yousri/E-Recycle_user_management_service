


import json
import requests

class RecycleRequestService: 
    

    @staticmethod
    def makeRecycleRequest(request):
        request = json.loads(request.body)
        r=requests.post('http://127.0.0.1:7000/core/makeRecycleRequest/',json = request)
        if r.status_code == 200 :

            return r.text
        else:
            return "Error has occured"
    

    def withdrawRecycleRequest(request):

        request = json.loads(request.body)
        r=requests.post('http://127.0.0.1:7000/core/withdrawRecycleRequest/',json = request)
        if r.status_code == 200 :

            return r.text
        else:
            return "Error has occured"
