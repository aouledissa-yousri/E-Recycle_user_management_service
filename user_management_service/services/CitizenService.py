import json
from os import stat
import requests
from django import http
import requests
from user_management_service.classes.Citizen import Citizen
coreURL='http://127.0.0.1:7000/core/'
def responseResult(response):
        if response.status_code == 200 :

            return response.text
        else:
            return "Error has occured"

class CitizenService:
    

    @staticmethod 
    def signUp(request):
        request = json.loads(request.body)
        citizen =  Citizen()
        citizen.setData(request)
        response=requests.post(coreURL+'signUp/',json=citizen.getData())
        return responseResult(response)

    @staticmethod
    def login(request):
        request = json.loads(request.body)
        response=requests.post(coreURL+'login/',json =request)
        return responseResult(response)


    
    @staticmethod
    def logout(request):
        request = request.headers['token']
        response=requests.delete(coreURL+'logout/',headers={'token': request})
        return responseResult(response)


    
    @staticmethod
    def logoutAllSessions(request):
        request = request.headers['token']
        response=requests.delete(coreURL+'logoutAllSessions/',headers={'token': request})
        return responseResult(response)


    
    @staticmethod
    def logoutAllOtherSessions(request):
        request = request.headers['token']
        response=requests.delete(coreURL+'logoutAllOtherSessions/',headers={'token': request})
        return responseResult(response)


    
    @staticmethod
    def confirmAccount(request):
        request = json.loads(request.body)
        response=requests.patch(coreURL+'confirmAccount/',json = request)
        return responseResult(response)


    
    @staticmethod
    def enableTwoFactorAuth(request):
        request = request.headers['token']
        response=requests.patch(coreURL+'enableTwoFactorAuth/',headers={'token': request})
        return responseResult(response)



    @staticmethod
    def disableTwoFactorAuth(request):
        request = request.headers['token']
        response=requests.patch(coreURL+'disableTwoFactorAuth/',headers={'token': request})
        return responseResult(response)


    
    @staticmethod
    def twoFactorAuth(request):
        request = json.loads(request.body)
        response=requests.patch(coreURL+'twoFactorAuth/',json = request)
        return responseResult(response)

    


    @staticmethod
    def requestPasswordReset(request):
        request = json.loads(request.body)
        response=requests.post(coreURL+'requestPasswordReset/',json = request)
        return responseResult(response)


        
    


    @staticmethod
    def checkPasswordResetCode(request):
        request = json.loads(request.body)
        response=requests.delete(coreURL+'checkPasswordResetCode/',json = request)
        return responseResult(response)

    

    @staticmethod
    def resetPassword(request):
        request = json.loads(request.body)
        response=requests.patch(coreURL+'resetPassword/',json = request)
        return responseResult(response)

        
    

    @staticmethod
    def changePassword(request):
        request = json.loads(request.body)
        response=requests.patch(coreURL+'changePassword/',json = request)
        return responseResult(response)

    


    #redirect to google login page
    def googleLoginGateway():
        response=requests.get(coreURL+'googleLoginGateway')
        return responseResult(response)


    

    #google login 
    def googleLogin(request):
        request = json.loads(request.body)
        response=requests.get(coreURL+'googleLogin/',json = request)
        return responseResult(response)

        
    

    #redirect to facebook login page
    def facebookLoginGateway():
        response=requests.get(coreURL+'facebookLoginGateway')
        return responseResult(response)


    #facebook login
    def facebookLogin(request):
        request = json.loads(request.body)
        response=requests.get(coreURL+'facebookLogin/',json = request)
        return responseResult(response)

    

    

        






    






    

        
