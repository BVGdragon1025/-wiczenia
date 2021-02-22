x = float(input("Podaj liczbę: "))

while x % 12 != 0:
    x = float(input("Podaj następną liczbę: "))
    if x % 12 == 0:
        print("Podałeś liczbę podzielną przez 12")
    else:
        continue
