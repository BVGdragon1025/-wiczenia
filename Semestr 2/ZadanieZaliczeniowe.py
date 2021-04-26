class Osoba:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def print_name(self):
        return repr(self.__name + self.__surname)


class Dane(Osoba):
    def __init__(self, pesel, street, street_num):
        super(Dane, self).__init__(self,self.__name, self.__surname)
        self.pesel = pesel
        self.street = street
        self.street_num = street_num

    def print_id_card(self):
        print("------------------------")
        print(f"{self.__name} {self.__surname}")
        print(f"{self.street} {self.street_num}")
        print(f"{self.pesel}")
        print("------------------------")

class Druzyna:
    def __init__(self, sport_type, coach):
        self.sport_type = sport_type
        self.coach = coach

    def show_all(self):
        return repr(self.coach + self.sport_type)


class Zawodnicy(Druzyna):
    def __init__(self, how_many_players):
        super(Zawodnicy, self).__init__(self.sport_type, self.coach)
        self.how_many_players = how_many_players

    def show_all(self):
        return repr(self.coach + self.sport_type + self.how_many_players)


class Hotel:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        return "Obiekty usunięte"


class Inside(Hotel):
    def __init__(self, rooms, floors):
        super(Inside, self).__init__("hotel")
        self.rooms = rooms
        self.floors = floors


hotel1 = Inside(2, 1)
hotel2 = Inside(5, 2)


def show_inside():
    for hotels in (hotel1, hotel2):
        print("Piętra: ",hotels.floors, "Pokoje: ",hotels.rooms)


show_inside()