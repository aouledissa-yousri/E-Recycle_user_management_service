from django.urls import path

from user_management_service.controllers.CitizenController import CitizenController
from user_management_service.controllers.MaterialController import MaterialController
from user_management_service.controllers.RecycleRequestController import RecycleRequestController


urlpatterns = [

    #citizen paths
    path("signUp/", CitizenController.signUp),
    path("login/", CitizenController.login),
    path("confirmAccount/", CitizenController.confirmAccount),
    path("logout/", CitizenController.logout),
    path("logoutAllSessions/", CitizenController.logoutAllSessions),
    path("logoutAllOtherSessions/", CitizenController.logoutAllOtherSessions),
    path("enableTwoFactorAuth/", CitizenController.enableTwoFactorAuth),
    path("disableTwoFactorAuth/", CitizenController.disableTwoFactorAuth),
    path("twoFactorAuth/", CitizenController.twoFactorAuth),


    path("requestPasswordReset/", CitizenController.requestPasswordReset),
    path("checkPasswordResetCode/", CitizenController.checkPasswordResetCode),
    path("resetPassword/", CitizenController.resetPassword),
    path("changePassword/", CitizenController.changePassword),


    path("googleLoginGateway/", CitizenController.googleLoginGateway),
    path("googleLogin/", CitizenController.googleLogin),

    path("facebookLoginGateway/", CitizenController.facebookLoginGateway),
    path("facebookLogin/", CitizenController.facebookLogin),

     #material paths
    path("addMaterial/", MaterialController.addMaterial),



    #recycle request paths
    path("makeRecycleRequest", RecycleRequestController.makeRecycleRequest),
    path("withdrawRecycleRequest", RecycleRequestController.withdrawRecycleRequest)





   
]