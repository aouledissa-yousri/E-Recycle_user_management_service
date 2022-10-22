from rest_framework.decorators import api_view

from django.http import JsonResponse

from user_management_service.services.RecycleRequestService import RecycleRequestService

class RecycleRequestController: 



    @api_view(["POST"])
    @staticmethod
    def makeRecycleRequest(request):
        return JsonResponse(RecycleRequestService.makeRecycleRequest(request))
    

    @api_view(["POST"])
    @staticmethod
    def withdrawRecycleRequest(request):
        return JsonResponse(RecycleRequestService.withdrawRecycleRequest(request))