class Smartphone:

    def __init__(self, name, model, price, bateria, nr_telefonu, memory, os, os_ver, charged):
        self.name = name
        self.model = model
        self.price = price
        self.bateria = bateria
        self.nr_telefonu = nr_telefonu
        self.memory = memory
        self.os = os
        self.os_ver = os_ver
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

    def SystemUpdate(self):
        if self.os == "Android" and self.os_ver < 6:
            print("Twój system jest nieaktualny. Zaktualizuj swój system!")
        elif self.os == "Android" and self.os_ver >= 6:
            print("Twój telefon jest w miarę aktualny.")
        elif self.os == "Symbian":
            print("Twój telefon jest przestarzały. Kup nowy!")
        else:
            print("Twój telefon jest zaktualizowany.")

    def RunningApps(self, apps):
        print("Obecnie uruchomione aplikacje", "(", self.name, self.model, "):", apps)

    def __del__(self):
        if self.model == "Galaxy Note 7":
            print("Wyrzuciłeś", self.name, self.model, ". Boom!")
        else:
            print("Wyrzuciłeś", self.name, self.model)


smartfon1 = Smartphone("Nokia", "3310", 0, 1600, "997998999", "32", "Symbian","3", 100)
smartfon2 = Smartphone("Samsung", "Galaxy Note 7", 500, 3500, "999899799", "64", "Android", 5, 50)
smartfon3 = Smartphone("Xiaomi", "Redmi Note 8t", 800, 4000, "080979898", "64", "Android", 10, 0)

smartfon3.IsCharged()
smartfon2.BasicStuff()
smartfon3.Charge(80)
smartfon2.SystemUpdate()
smartfon1.SystemUpdate()
smartfon3.SystemUpdate()
smartfon3.RunningApps(apps=("Kalkulator", "Fruit Ninja"))


