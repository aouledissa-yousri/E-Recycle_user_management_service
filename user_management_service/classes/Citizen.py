class Citizen():

    def __init__(self,*args):

        if len(args)>0:
            self.name = args[0]
            self.lastname = args[1]
            self.user_profile= args[2]
            self.recycleRequests = args[3]
        
        else:
            pass


    # def __init__(self,name,lastname,user_profile,recycleRequests):
    #     self.name = name
    #     self.lastname = lastname
    #     self.user_profile= user_profile
    #     self.recycleRequests = recycleRequests

    def getData(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "user_profile": self.user_profile,
            "recycleRequests": self.recycleRequests,
        }
    
    def setData(self, request):
        self.name = request.get("name")
        self.lastname = request.get("lastname")
        self.user_profile = request.get("user_profile")
        self.recycleRequests = request.get("recycleRequests")
       