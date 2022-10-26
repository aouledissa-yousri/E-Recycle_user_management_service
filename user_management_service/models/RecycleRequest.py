class RecycleRequest():
    def __init__(self,quantity,location,unit,dateSubmitted,status,citizen,material) -> None:
        self.quantity = quantity
        self.location = location
        self.unit = unit
        self.dateSubmitted = dateSubmitted
        self.status = status
        self.citizen = citizen
        self.material = material