while True:
    a = int(input("Podaj liczbę a: "))
    b = int(input("podaj liczbę b: "))
    if a == 0 or b == 0:
        print("Jedna z wartości to zero")
        break
    else:
        print("Wynik: ", float(a+b/2))
