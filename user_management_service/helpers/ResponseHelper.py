class ResponseHelper:
    @staticmethod
    def responseResult(response):
        if response.status_code == 200 :

            return response.text
        else:
            return "Error has occured"