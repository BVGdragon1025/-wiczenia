class Parking:
    def __init__(self, places, registered):
        self.places = places
        self.registered = registered


class Pojazd(Parking):
    def __init__(self,places,registered, reg_num,):
        super().__init__(places, registered)
        self.reg_num = reg_num

    def pojazd_add(self):
        pojazd_tab = []


