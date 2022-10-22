import json
from django.http import JsonResponse
import jwt

from Global.settings import SECRET_KEY


#check if access token is valid or not when making a post request to the server
def checkAccessToken(func, algorithm="HS512"):
    
    def wrapper(request, *args, **kwargs):
        try: 
            _token = request.headers["Token"]
            try:
                jwt.decode(_token, SECRET_KEY, algorithms = [algorithm])

                return func(request, *args, **kwargs)
                

            except jwt.exceptions.DecodeError:
                return JsonResponse({"response": "invalid token"})

        except KeyError: 
            return JsonResponse({"response": "invalid token"})

    return wrapper

# def checkValidParameters(func):
#     def wrapper(request, *args, **kwargs):
#         request = json.loads(request.body)
#         d=[]
#         for k in request:
#             d.append(k)
        



