while True:
    n = input("Podaj liczbę: ")
    if float(n) % 69 != 0:
        print(n)
    else:
        print("Podałeś  podzielną prze 69, wiec kończę działanie pętli")
        break
