class Citizen():

    def __init__(self,*args):

        if len(args)>0:
            self.name = args[0]
            self.lastname = args[1]
            self.user_profile= args[2]
        
        else:
            pass


    def getData(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "user_profile": self.user_profile,
        }
    
    def setData(self, data):
        self.name = data["name"]
        self.lastname = data["lastname"]
        self.user_profile = data["user_profile"]
       