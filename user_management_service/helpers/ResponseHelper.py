class ResponseHelper:
    
    @staticmethod
    def responseResult(response):
        if response.status_code == 200 :
            return response.json()
        
        return {"message": "Error has occured"}