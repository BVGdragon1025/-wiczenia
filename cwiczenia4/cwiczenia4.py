a = input("Podaj liczbę: ")

while float(a) != 0:
    b = input("Podaj drugą liczbę: ")
    if float(b) != 0:
        a = (float(a)*float(b)) / 2
        print(a)
    else:
        print("Wpisałeś zero")
else:
    print("Wpisałeś zero")
