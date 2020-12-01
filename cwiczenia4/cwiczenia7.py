a = int(input("Podaj liczbę: "))

while a != 0:
    if a == 2 or a == 3:
        print("Liczba jest pierwsza")
        break
    elif a % 2 == 0 or a % 3 == 0:
        print("Liczba nie jest pierwsza")
        break
    elif a % 1 == 0 and a % a == 0:
        print("Liczba jest pierwsza")
        break
    else:
        print("Liczba nie jest pierwsza")
        break
else:
    print("Liczba równa 0")
