class Cat:
    def __init__(self, nazwa, wiek, rasa, plec, waga, glod, ):
        self.nazwa = nazwa
        self.wiek = wiek
        self.rasa = rasa
        self.plec = plec
        self.waga = waga
        self.glod = glod

    def cat_name(self):
        print("Jestem " + self.nazwa)

    def cat_age(self):
        print("Mam", self.wiek, "lat.")

    def what_cat(self):
        print("Moja rasa to " + self.rasa)

    def cat_gender(self):
        if self.plec == "M":
            print("Jestem kotem")
        else:
            print("Jestem kotką")

    def cat_weight(self):
        print("Ważę " + self.waga + "kg")

    def is_hungry(self):
        if self.glod == "Głodny":
            print("Chcę jeść!")
        else:
            print("Nie chcę jeść (kłamstwo, bo koty są wiecznie głodne)")


mruczek = Cat("Mruczek",5,"dachowiec","M","4","Głodny")

print(mruczek.cat_name(), mruczek.cat_age(), mruczek.what_cat(), mruczek.cat_gender(), mruczek.cat_weight(),
      mruczek.is_hungry())