from user_management_service.models import Citizen
from user_management_service.helpers.ResponseHelper import ResponseHelper
from Global.settings import CORE_URL
import requests, json


class CitizenService:
    

    @staticmethod 
    def signUp(request):
        requestData = json.loads(request.body)["data"]
        citizen =  Citizen()
        citizen.setData(requestData)
        response=requests.post(CORE_URL+'signUp/',json=citizen.getData())
        return ResponseHelper.responseResult(response)



    @staticmethod
    def login(request):
        requestData = json.loads(request.body)["data"]
        response=requests.post(CORE_URL+'login/', json = requestData)
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def logout(request):
        token = request.headers['token']
        response=requests.delete(CORE_URL+'logout/',headers={'token': token})
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def logoutAllSessions(request):
        token = request.headers['token']
        response=requests.delete(CORE_URL+'logoutAllSessions/',headers={'token': token})
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def logoutAllOtherSessions(request):
        token = request.headers['token']
        response=requests.delete(CORE_URL+'logoutAllOtherSessions/',headers={'token': token})
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def confirmAccount(request):
        requestData = json.loads(request.body)["data"]
        response=requests.patch(CORE_URL+'confirmAccount/',json = requestData)
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def enableTwoFactorAuth(request):
        token = request.headers['token']
        response=requests.patch(CORE_URL+'enableTwoFactorAuth/',headers={'token': token})
        return ResponseHelper.responseResult(response)



    @staticmethod
    def disableTwoFactorAuth(request):
        token = request.headers['token']
        response=requests.patch(CORE_URL+'disableTwoFactorAuth/',headers={'token': token})
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def twoFactorAuth(request):
        requestData = json.loads(request.body)["data"]
        response=requests.patch(CORE_URL+'twoFactorAuth/',json = requestData)
        return ResponseHelper.responseResult(response)

    


    @staticmethod
    def requestPasswordReset(request):
        requestData = json.loads(request.body)["data"]
        response=requests.post(CORE_URL+'requestPasswordReset/',json = requestData)
        return ResponseHelper.responseResult(response)


        
    


    @staticmethod
    def checkPasswordResetCode(request):
        requestData = json.loads(request.body)["data"]
        response=requests.delete(CORE_URL+'checkPasswordResetCode/',json = requestData)
        return ResponseHelper.responseResult(response)

    

    @staticmethod
    def resetPassword(request):
        requestData = json.loads(request.body)["data"]
        response=requests.patch(CORE_URL+'resetPassword/',json = requestData)
        return ResponseHelper.responseResult(response)

        
    

    @staticmethod
    def changePassword(request):
        requestData = json.loads(request.body)["data"]
        response=requests.patch(CORE_URL+'changePassword/',json = requestData)
        return ResponseHelper.responseResult(response)

    


    #redirect to google login page
    def googleLoginGateway():
        response=requests.get(CORE_URL+'googleLoginGateway')
        return ResponseHelper.responseResult(response)



    #redirect to facebook login page
    def facebookLoginGateway():
        response=requests.get(CORE_URL+'facebookLoginGateway')
        return ResponseHelper.responseResult(response)


    

    

    

        






    






    

        
