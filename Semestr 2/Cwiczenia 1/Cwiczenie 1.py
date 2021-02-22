class Car:

    def __init__(self, marka, typ, przebieg, kolor, wartosc):
        self.marka = marka
        self.typ = typ
        self.przebieg = przebieg
        self.kolor = kolor
        self.wartosc = wartosc

    def how_far(self):
        return "Przejechał {} km.".format(self.przebieg)

    def what_car(self):
        return "Samochód jest marki {}".format(self.marka)

    def what_type(self):
        return "{} jest {}".format(self.marka, self.typ)

    def what_color(self):
        return "Ma kolor {}".format(self.kolor)

    def how_much(self):
        return "Jest warty {} zł".format(self.wartosc)

    def skrec_w_lewo(self):
        return "(pisk opon, {} skręca w lewo)".format(self.marka)


ferrari = Car("Ferrari", "kabriolet", "6500", "czerwony", "250000")

print(ferrari.what_car())
print(ferrari.what_type())
print(ferrari.what_color())
print(ferrari.how_much())
print(ferrari.how_far())
print(ferrari.skrec_w_lewo())
