
a = input("Podaj wartość a: ")
b = input("Podaj wartość b: ")

# modulo - dzielenie z resztą

if int(a) == 0 or int(b) == 0:  # sprawdzenie, czy mamy jakieś zero tutaj
    print("Jedna z wartości jest zerem")
elif int(a) % int(b) == 0:  # liczba nie zwraca reszty, więc jest podzielna
    print("Wartość " + str(a) + " jest podzielna przez " + str(b))
else:  # liczba zwraca resztę, więc nie jest podzielna
    print("Wartość " + str(a) + " nie jest podzielna przez " + str(b))
