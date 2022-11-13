from rest_framework.decorators import api_view 
from django.http import JsonResponse
from user_management_service.services import CollectorService, CitizenService



class CollectorController: 
    
    @api_view(["POST"])
    @staticmethod
    def signUp(request):
        return JsonResponse(CollectorService.signUp(request))
    

    @api_view(["GET"])
    @staticmethod 
    def googleLoginGateway(request):
        return JsonResponse(CollectorService.googleLoginGateway(request))
    
    @api_view(["GET"])
    @staticmethod 
    def facebookLoginGateway(request):
        return JsonResponse(CollectorService.facebookLoginGateway(request))
    
    