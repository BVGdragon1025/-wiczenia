import time

class Zwierze:
    def __init__(self,ile_nog,kolor,wiek,czy_grozne,zyje_w_polsce,czy_udomowione,czy_glodny):
        self.ile_nog = ile_nog
        self.kolor = kolor
        self.wiek = wiek
        self.czy_grozne = czy_grozne
        self.zyje_w_polsce = zyje_w_polsce
        self.czy_udomowione = czy_udomowione
        self.czy_glodny = czy_glodny

class Kot(Zwierze):
    def __init__(self,rasa,nazwa,ile_zyc):
        super().__init__()
        self.rasa = rasa
        self.nazwa = nazwa
        self.ile_zyc = ile_zyc

    def zamrucz(self):
        for i in range(5):
            print("Mrau")
            time.sleep(2)

    def czy_spi(self):
        print("Kot jeszcze śpi.")
        time.sleep(5)
        print("Już nie.")

    def spadnij_na_4_lapy(self):
        pass

    def ile_zyc(self):
        return "Twój kot ma "+self.ile_zyc+"żyć."
