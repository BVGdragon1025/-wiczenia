a = float(input("Podaj liczbę: "))

if a == 0:
    print("Podałeś 0")
elif a < 0:
    if a % 2 != 0:
        print("Liczba ujemna, nieparzysta")
    else:
        print("Liczba ujemna, parzysta")
elif a > 0:
    if a % 2 != 0:
        print("Liczba dodatnia, nieparzysta")
    else:
        print("Liczba dodatnia, parzysta")
else:
    print("Wyjątek")
