import math

tempc = float(input("Podaj temperaturę w stopniach Celsjusza: "))
tempf = (tempc*1.8)+32
tempk = tempc+273

print("W przeliczeniu na stopnie Fahrenheit'a: ", tempf)
print("W przeliczeniu na Kelwiny: ", tempk)

if tempf <= 32:
    print("Woda zamarza")
elif tempf >= 212:
    print("Woda wrze")
else:
    print("Z wodą nic się nie dzieje")

print("A teraz przelicznik temperatur.")
print("Wybierz z czego na co chcesz przeliczać: 1. K na F, 2. F na K, 3. K na C, 4. C na K ")
w = int(input("Podaj cyfrę: "))
a = float(input("Podaj temperaturę: "))


def knaf():
    convkf = ((a*1.8)-459.67)
    print("Po konwersji: ", convkf)


def fnak():
    convfk = ((a*+459.67)/(5/9))
    print("Po konwersji: ", convfk)


def knac():
    convkc = a-273
    print("Po konwersji: ", convkc)


def cnak():
    convck = a+273
    print("Po konwersji: ", convck)


if w == 1:
    knaf()
elif w == 2:
    fnak()
elif w == 3:
    knac()
elif w == 4:
    cnak()
else:
    print("Zły wybór")
