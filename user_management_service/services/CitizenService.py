import json
from os import stat
import requests
from django import http
import requests
from user_management_service.models import Citizen
from Global.settings import CORE_URL
from user_management_service.helpers.ResponseHelper import ResponseHelper

class CitizenService:
    

    @staticmethod 
    def signUp(request):
        request = json.loads(request.body)
        citizen =  Citizen()
        citizen.setData(request)
        response=requests.post(CORE_URL+'signUp/',json=citizen.getData())
        return ResponseHelper.responseResult(response)

    @staticmethod
    def login(request):
        request = json.loads(request.body)
        response=requests.post(CORE_URL+'login/',json =request)
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def logout(request):
        request = request.headers['token']
        response=requests.delete(CORE_URL+'logout/',headers={'token': request})
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def logoutAllSessions(request):
        request = request.headers['token']
        response=requests.delete(CORE_URL+'logoutAllSessions/',headers={'token': request})
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def logoutAllOtherSessions(request):
        request = request.headers['token']
        response=requests.delete(CORE_URL+'logoutAllOtherSessions/',headers={'token': request})
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def confirmAccount(request):
        request = json.loads(request.body)
        response=requests.patch(CORE_URL+'confirmAccount/',json = request)
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def enableTwoFactorAuth(request):
        request = request.headers['token']
        response=requests.patch(CORE_URL+'enableTwoFactorAuth/',headers={'token': request})
        return ResponseHelper.responseResult(response)



    @staticmethod
    def disableTwoFactorAuth(request):
        request = request.headers['token']
        response=requests.patch(CORE_URL+'disableTwoFactorAuth/',headers={'token': request})
        return ResponseHelper.responseResult(response)


    
    @staticmethod
    def twoFactorAuth(request):
        request = json.loads(request.body)
        response=requests.patch(CORE_URL+'twoFactorAuth/',json = request)
        return ResponseHelper.responseResult(response)

    


    @staticmethod
    def requestPasswordReset(request):
        request = json.loads(request.body)
        response=requests.post(CORE_URL+'requestPasswordReset/',json = request)
        return ResponseHelper.responseResult(response)


        
    


    @staticmethod
    def checkPasswordResetCode(request):
        request = json.loads(request.body)
        response=requests.delete(CORE_URL+'checkPasswordResetCode/',json = request)
        return ResponseHelper.responseResult(response)

    

    @staticmethod
    def resetPassword(request):
        request = json.loads(request.body)
        response=requests.patch(CORE_URL+'resetPassword/',json = request)
        return ResponseHelper.responseResult(response)

        
    

    @staticmethod
    def changePassword(request):
        request = json.loads(request.body)
        response=requests.patch(CORE_URL+'changePassword/',json = request)
        return ResponseHelper.responseResult(response)

    


    #redirect to google login page
    def googleLoginGateway():
        response=requests.get(CORE_URL+'googleLoginGateway')
        return ResponseHelper.responseResult(response)


    

    #google login 
    def googleLogin(request):
        request = json.loads(request.body)
        response=requests.get(CORE_URL+'googleLogin/',json = request)
        return ResponseHelper.responseResult(response)

        
    

    #redirect to facebook login page
    def facebookLoginGateway():
        response=requests.get(CORE_URL+'facebookLoginGateway')
        return ResponseHelper.responseResult(response)


    #facebook login
    def facebookLogin(request):
        request = json.loads(request.body)
        response=requests.get(CORE_URL+'facebookLogin/',json = request)
        return ResponseHelper.responseResult(response)

    

    

        






    






    

        
