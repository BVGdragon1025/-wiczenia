import math


class Figury:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def menu(self):
        while True:
            print("Witaj w kalkulatorze. Wybierz figurę:\n"
                  "[1]Kolo, "
                  "[2]Kwadrat, "
                  "[3]Prostokąt, "
                  "[4]Trapez, "
                  "[5]Romb, "
                  "[6]Trójkąt, "
                  "[q]Wyjście")
            choice = input("Wybierz: ")
            if choice == "1":
                Kolo.pokola(Kolo)
            elif choice == "2":
                Kwadrat.pokwadratu(Kwadrat)
            elif choice == "3":
                Prostokat.poprostokata(Prostokat)
            elif choice == "4":
                Trapez.potrapezu(Trapez)
            elif choice == "5":
                Romb.porombu(Romb)
            elif choice == "6":
                Trojkat.potrojkota(Trojkat)
            elif choice == "q" or choice.lower() == "q":
                break
            else:
                print("Zła opcja")


class Kolo(Figury):
    def __init__(self, r, d):
        super(Kolo, self).__init__(r, d, self.h)
        self.r = r
        self.d = d

    def pokola(self):
        self.r = float(input("Podaj promień koła: "))
        pole = round(self.r*(math.pi**2), 2)
        obw = round(2*math.pi*self.r,2)
        print("Pole koła wynosi: ", pole)
        print("Obwód koła wynosi: ", obw)


class Kwadrat(Figury):
    def __init__(self, a):
        super(Kwadrat, self).__init__(a, self.b, self.h)
        self.a = a

    def pokwadratu(self):
        self.a = float(input("Podaj długość boku: "))
        pole = round(self.a**2, 2)
        obw = round(self.a*4, 2)
        print("Pole kwadratu to: ", pole)
        print("Obwód kwadratu to: ", obw)


class Prostokat(Figury):
    def __init__(self, a, b):
        super(Prostokat, self).__init__(a, b, self.h)
        self.a = a
        self.b = b

    def poprostokata(self):
        self.a = float(input("Podaj długość pierwszego boku: "))
        self.b = float(input("Podaj długość drugiego boku: "))
        pole = round(self.a*self.b, 2)
        obw = round((2*self.a)+(2*self.b), 2)
        print("Pole prostokąta to: ", pole)
        print("Obwód prostokąta to: ", obw)


class Trapez(Figury):
    def __init__(self, a, b, h, b1, b2):
        super(Trapez, self).__init__(a, b, h)
        self.a = a
        self.b = b
        self.h = h
        self.b1 = b1
        self.b2 = b2

    def potrapezu(self):
        self.a = float(input("Podaj długość dolnej podstawy: "))
        self.b = float(input("Podaj długość górnej podstawy: "))
        self.h = float(input("Podaj wysokość: "))
        pole = round((((self.a+self.b)*self.h)/2), 2)
        choice = input("Czy twój trapez jest prostokątny? [y]Tak, [n]Nie: ")
        if choice == "y" or choice.lower() == "y":
            self.b1 = float(input("Podaj długość boku: "))
            obw = round(self.a+self.b+self.h+self.b1, 2)
            print("Pole trapezu to: ", pole)
            print("Obwód trapezu to: ", obw)
        elif choice == "n" or choice.lower() == "n":
            self.b1 = float(input("Podaj długość pierwszego boku: "))
            obw = round(self.a+self.b+(self.b1*2), 2)
            print("Pole trapezu to: ", pole)
            print("Obwód trapezu to: ", obw)
        else:
            print("Zła opcja")


class Romb(Figury):
    def __init__(self, a, b, b1, b2, b3, b4):
        super(Romb, self).__init__(a, b, self.h)
        self.a = a
        self.b = b
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4

    def porombu(self):
        self.a = float(input("Podaj długość pionowej przekątnej: "))
        self.b = float(input("Podaj długośc poziomej przekątnej: "))
        pole = round((self.a*self.b)/2, 2)
        bok = round(math.sqrt(((self.a/2)**2)+((self.b/2)**2)), 2)
        obw = round((4*bok), 2)
        print("Pole rombu to: ", pole)
        print("Obwod rombu to: ", obw, ", bok =", bok)


class Trojkat(Figury):
    def __init__(self, a, h, b1, b2):
        super(Trojkat, self).__init__(a, self.b, h)
        self.a = a
        self.h = h
        self.b1 = b1
        self.b2 = b2

    def potrojkota(self):
        self.a = float(input("Podaj długość podstawy: "))
        self.h = float(input("Podaj wysokość trójkąta: "))
        pole = round(((self.a*self.h)/2), 2)
        choice = input("Jaki jest twój trójkąt? [1]Równoboczny, [2]Równoramienny, [3]Prostokątny: ")
        if choice == "1":
            obw = round(3*self.a, 2)
            print("Pole trójkąta to: ", pole)
            print("Obwód trójkąta to: ", obw)
        elif choice == "2":
            bok = round((math.sqrt((self.a/2)**2)+(self.h**2)),2)
            obw = round(self.a+(bok*2), 2)
            print("Pole trójkąta to: ", pole)
            print("Obwód trójkąta to: ", obw)
        else:
            bok = round((math.sqrt((self.a / 2) ** 2) + (self.h ** 2)), 2)
            obw = round(bok+self.a+self.h)
            print("Pole trójkąta to: ", pole)
            print("Obwód trójkąta to: ", obw)


Figury.menu(Figury)
