import math


def suma(a, b):
    c = a + b
    return c


def roznica(a, b):
    c = a - b
    return c


def mnozenie(a, b):
    c = a * b
    return c


def dzielenie(a, b):
    c = a / b
    return c


def pierwiastek(a):
    c = math.sqrt(a)
    return c


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print("Suma: ", suma(a, b))
print("Różnica: ", roznica(a, b))
print("Mnożenie: ", mnozenie(a, b))
print("Dzielenie: ", dzielenie(a, b))
print("Pierwiastek pierwszej liczby: ", pierwiastek(a))
print("Pierwiastek drugiej liczby: ", pierwiastek(b))
