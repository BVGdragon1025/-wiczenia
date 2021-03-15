import random

class Pojazd:
    def __init__(self, ile_kol, ile_ludzi, poj_silnika, max_speed, przebieg, paliwo, tablica, kolor):
        self.ile_kol = ile_kol
        self.ile_ludzi = ile_ludzi
        self.poj_silnik = poj_silnika
        self.max_speed = max_speed
        self.przebieg = przebieg
        self.paliwo = paliwo
        self.tablica = tablica
        self.kolor = kolor

    def JedzProsto(self):
        print("Jadę prosto")

    def PodajTablice(self):
        return self.tablica

    def __del__(self):
        return True


class Samochod(Pojazd):
    def __init__(self, ile_drzwi, bagaznik, ile_kol,ile_ludzi,poj_silnika,max_speed,przebieg,paliwo,tablica,kolor):
        super().__init__(ile_kol,ile_ludzi,poj_silnika,max_speed,przebieg,paliwo,tablica,kolor)
        self.ile_drzwi = ile_drzwi
        self.bagaznik = bagaznik

    def WrzucDoBagaznika(self):
        tab_rzeczy = []
        ile_rzeczy = int(input("Ile chcesz włożyć?"))
        for i in range(ile_rzeczy):
            rzeczy = input("Co chcesz wrzucić do bagażnika?: ")
            tab_rzeczy.append(rzeczy)
        print("Wrzuciłeś: ", tab_rzeczy)
        if len(tab_rzeczy) >= 20:
            print("Zapchałeś bagażnik")
        else:
            print("Jeszcze coś sie zmieści")

    def WyrzucPasazerow(self):
        ilu = input("Ilu chcesz wyrzucić (nie pytam czemu): ")
        if ilu >= self.ile_ludzi:
            print("Wyrzuciłeś wszystkich. Czemu?")
        else:
            print(f"Wyrzuciłeś {ilu} z {self.ile_ludzi} pasażerów. Czemu?")

    def __del__(self):
        return True


class Motocykl(Pojazd):
    def __init__(self, typ, schowek,wys_siodla,rama,ile_kol,ile_ludzi,poj_silnika,max_speed,przebieg,paliwo,tablica,kolor):
        super().__init__(ile_kol,ile_ludzi,poj_silnika,max_speed,przebieg,paliwo,tablica,kolor)
        self.typ = typ
        self.schowek = schowek
        self.wys_siodla = wys_siodla
        self.rama = rama

    def Stojka(self):
        ktore_kolo = input("Na którym kole chcesz stać?: ")
        szansa = random.randrange(0,9)
        print(f"Próbujesz zrobić stójkę na {ktore_kolo} kole...")
        if szansa >= 5:
            print("... i udało ci się!")
        else:
            print("... i coś poszło nie tak. Jedzesz dalej normalnie.")

    def __del__(self):
        return True


opel = Samochod(5,True, 4, "5", 1.9, 200, 400000, "Diesel", "DW997", "Czarny Metalic")
kawasaki = Motocykl("Ścigacz",True,"60cm",True,2,2,600,"Duża",50000,"Benzin","DWR42069","Zielony")
opel.WyrzucPasazerow()
kawasaki.Stojka()

