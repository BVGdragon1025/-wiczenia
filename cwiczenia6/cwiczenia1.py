i = int(input("Ile wartości chcesz wprowadzić?: "))
tab = []
j = 0

while j < i:
    a = float(input("Podaj liczby: "))
    j += 1
    if a < 0:
        continue
    else:
        tab.append(a)
        print(tab)
print("Średnia to: ", sum(tab)/i)
