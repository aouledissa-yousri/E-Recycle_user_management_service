from user_management_service.models import Collector
from user_management_service.helpers import ResponseHelper
from Global.settings import CORE_URL
import requests, json

class CollectorService: 
    
    @staticmethod 
    def signUp(request):
        requestData = json.loads(request.body)["data"]
        collector =  Collector()
        collector.setData(requestData)
        response=requests.post(CORE_URL+'signUp/',json=collector.getData())
        return ResponseHelper.responseResult(response)
    

    #redirect to google login page
    @staticmethod 
    def googleLoginGateway(request):
        response=requests.get(CORE_URL+'collector/googleLoginGateway')
        return ResponseHelper.responseResult(response)


    #redirect to facebook login page
    def facebookLoginGateway(request):
        response=requests.get(CORE_URL+'collector/facebookLoginGateway')
        return ResponseHelper.responseResult(response)
    
    
