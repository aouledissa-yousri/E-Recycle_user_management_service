import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from user_management_service.decorators import checkAccessToken



from user_management_service.services.CitizenService import CitizenService

class CitizenController:
     
    @api_view(["POST"])
    @staticmethod
    def signUp(request):
        return JsonResponse({"result": CitizenService.signUp(request)})
    
    @api_view(["POST"])
    @staticmethod
    def login(request):
        return JsonResponse({"result": CitizenService.login(request)})

# class CitizenController:s
#     @staticmethod
#     def addCitizen(request):
#         request = json.loads(request.body)


    @api_view(["DELETE"])
    @staticmethod
    @checkAccessToken
    def logout(request):
        return JsonResponse({"result": CitizenService.logout(request)})

    
    @api_view(["DELETE"])
    @staticmethod
    @checkAccessToken
    def logoutAllSessions(request):
        return JsonResponse({"result": CitizenService.logoutAllSessions(request)})

    
    @api_view(["DELETE"])
    @staticmethod
    @checkAccessToken
    def logoutAllOtherSessions(request):
        return JsonResponse({"result": CitizenService.logoutAllOtherSessions(request)})
    

    @api_view(["PATCH"])
    @staticmethod
    def confirmAccount(request):
        return JsonResponse({"result": CitizenService.confirmAccount(request)})
    

    @api_view(["PATCH"])
    @staticmethod
    @checkAccessToken
    def enableTwoFactorAuth(request):
        return JsonResponse({"result": CitizenService.enableTwoFactorAuth(request)})
    

    @api_view(["PATCH"])
    @staticmethod
    @checkAccessToken
    def disableTwoFactorAuth(request):
        return JsonResponse({"result": CitizenService.disableTwoFactorAuth(request)})

    @api_view(["PATCH"])
    @staticmethod
    def twoFactorAuth(request):
        return JsonResponse({"result": CitizenService.twoFactorAuth(request)})
    

    @api_view(["POST"])
    @staticmethod
    def requestPasswordReset(request):
        return JsonResponse({"result": CitizenService.requestPasswordReset(request)})
    

    @api_view(["DELETE"])
    def checkPasswordResetCode(request):
        return JsonResponse({"result": CitizenService.checkPasswordResetCode(request)})
    
    @api_view(["PATCH"])
    def resetPassword(request):
        return JsonResponse({"result": CitizenService.resetPassword(request)})
    

    @api_view(["PATCH"])
    @checkAccessToken
    def changePassword(request):  
        return JsonResponse({"result": CitizenService.changePassword(request)})


    @api_view(["GET"])
    def googleLoginGateway(request):
        return JsonResponse({"result": CitizenService.googleLoginGateway()}) 
    

    @api_view(["GET"])
    def googleLogin(request):
        return JsonResponse({"result": CitizenService.googleLogin(request)})
    

    @api_view(["GET"])
    def facebookLoginGateway(request):
        return JsonResponse({"result": CitizenService.facebookLoginGateway()})
    

    @api_view(["GET"])
    def facebookLogin(request):
        return JsonResponse({"result": CitizenService.facebookLogin(request)})
    
        

