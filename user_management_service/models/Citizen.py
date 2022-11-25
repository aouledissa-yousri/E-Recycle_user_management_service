class Citizen():

    def __init__(self,*args):

        self.name = None
        self.lastname = None
        self.user_profile= None
        self.recycleCoins = 0
        
       


    def getData(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "user_profile": self.user_profile,
            "recycleCoins": self.recycleCoins
        }
    
    def setData(self, data):
        self.name = data["name"]
        self.lastname = data["lastname"]
        self.user_profile = data["user_profile"]
        self.recycleCoins = data["recycleCoins"]
       