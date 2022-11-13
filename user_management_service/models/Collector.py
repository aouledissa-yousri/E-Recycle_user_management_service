from user_management_service.models import Citizen

class Collector(Citizen):

    def __init__(self, *args):
        super().__init__(*args)
    