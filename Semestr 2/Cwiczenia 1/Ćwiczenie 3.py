class Smartphone:

    def __init__(self, name, model, price, bateria, nr_telefonu, memory, os, charged):
        self.name = name
        self.model = model
        self.price = price
        self.bateria = bateria
        self.nr_telefonu = nr_telefonu
        self.memory = memory
        self.os = os
        self.charged = charged

    def IsCharged(self):
        print(self.name, self.model, "jest ")
        if self.charged > 80:
            print("Naładowany")
        elif 80 > self.charged >= 50:
            print("Niezbyt naładowany")
        else:
            print("Rozładowany")

    def BasicStuff(self):
        print(self.name, self.model)

    def Charge(self, charged):
        how_much = 0
        while how_much != charged:
            how_much += 5
            print("Naładowano ", how_much, "procent")

    def __del__(self):
        print("Wyrzuciłeś", self.name, self.model)


smartfon1 = Smartphone("Nokia", "3310", 0, 1600, "997998999", "32", "Symbian", 100)
smartfon2 = Smartphone("Samsung", "Galaxy Note 7", 500, 3500, "999899799", "64", "Android", 50)
smartfon3 = Smartphone("Xiaomi", "Redmi Note 8t", 800, 4000, "080979898", "64", "Android", 0)

smartfon3.IsCharged()
smartfon2.BasicStuff()
smartfon3.Charge(80)


