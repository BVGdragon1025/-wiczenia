from statistics import median
tab = []

n = int(input("Podaj początek zakresu: "))
x = int(input("Podaj koniec zakresu zakresu: "))

while True:
    if n == 0 or x == 0:
        print("Podałeś gdzieś zero")
        break
    else:
        for i in range(n, x):
            i += 1
            tab.append(i)


tab_2 = tab[0:6]
print("Twoja tablica liczb: ", tab_2)
print("Wartość maksymaalna: ", max(tab_2))
print("Wartość minimalna: ", min(tab_2))
print("Średnia: ", len(tab_2))
print("Mediana: ", median(tab_2))
