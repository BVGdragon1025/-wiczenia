a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")

while True:
    k = float(a) + float(b)
    j = (float(a) * float(b)) / 2
    if k != 100 and j != 66:
        print("Wynik dodawania: ", k)
        print("Średnia: ", j)
        a = input("Podaj kolejną liczbę a: ")
        b = input("Podaj kolejną liczbę b: ")
    else:
        print("Dodawania jest równe zeru lub średnia jest równa 66")
        break
