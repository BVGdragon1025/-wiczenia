# Zadanie 2, zrobione przez Kubę

import math as m


def Main():
    figure = input("Wybierz swoją figurę: K - Kula, S - Stożek, P - prostopadłościan")
    if figure == "K":
        Kula()
    elif figure == "S":
        Stozek()
    else:
        Prostopadloscian()


def Kula():
    r = float(input("Podaj promien kuli: "))
    if r <= 0:
        print("Promień nie może być ujemny lub równy zero")
        return
    p = 4 * m.pi * r ** 2
    print("Pole kuli wynosi:", p)
    v = 4 / 3 * m.pi * r ** 3
    print("Objęctość kuli wynosi: ", v)


def Stozek():
    r = float(input("Podaj wartość promienia podstawy"))
    l = float(input("Podaj wartość tworzącej stożka"))
    h = float(input("Podaj wartość wysokości stożka"))
    if r and l and h <= 0:
        print("Podane wartości nie mogą być mniejsze lub równe zero")
        return
    p = m.pi * r * (r + l)
    v = 1 / 3 * m.pi * r ** 2 * h
    print("Powierzchnia stożka wynosi: ", p)
    print("Objętość stożka wynosi: ", v)


def Prostopadloscian():
    if input("Czy ten prostopadłościan jest sześcianem?: TAK/NIE") == "TAK":
        a = float(input("Podaj wartość krawędzi: "))
        p = 6 * a ** 2
        v = a ** 3
        print("Pole sześcianu wynosi: ", p)
        print("Objętość sześcianu wynosi: ", v)
    else:
        a = float(input("Podaj wartość pierwszej krawędzi: "))
        b = float(input("Podaj wartość drugiej krawędzi: "))
        c = float(input("Podaj wartość trzeciej krawędzi: "))
        if a and b and c <= 0:
            print("Podane wartości nie mogą być mniejsze lub równe zero")
            return
        p = 2 * a * b + 2 * a * c + 2 * b * c
        v = a * b * c
        print("Pole prostopadlościanu wynosi: ", p)
        print("Objętość prostopadlościanu wynosi: ", v)


Main()