import random
tab = []
print("1 - Lotto")
print("2 - Multi Multi")
print("3 - Mini Lotto")
w = int(input("Wybierz które losowanie chcesz przeprowadzić: "))


if w == 1:
    for j in range(0, 6):
        i = random.randint(1, 49)
        if i in tab:
            i = random.randint(1, 49)
            tab.append(i)
        if i not in tab:
            tab.append(i)
    print("Wylosowane liczby to:", tab)

elif w == 2:
    for j in range(0, 20):
        i = random.randint(1, 80)
        if i in tab:
            i = random.randint(1, 80)
            tab.append(i)
        if i not in tab:
            tab.append(i)
    print("Wylosowane liczby to:", tab)

elif w == 3:
    for j in range(0, 5):
        i = random.randint(1, 42)
        if i in tab:
            i = random.randint(1, 42)
            tab.append(i)
        if i not in tab:
            tab.append(i)
    print("Wylosowane liczby to:", tab)
else:
    print("Błąd.")
