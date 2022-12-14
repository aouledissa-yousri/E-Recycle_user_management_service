from django.urls import path

from user_management_service.controllers import *


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
    path("collector/googleLoginGateway/", CitizenController.googleLoginGateway),

    path("facebookLoginGateway/", CitizenController.facebookLoginGateway),
    path("collector/facebookLoginGateway/", CitizenController.facebookLoginGateway),


    #collector paths
    path("collector/signUp/", CollectorController.signUp),

   
]