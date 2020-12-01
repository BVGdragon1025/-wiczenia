import random

tab_r = []
tab_u = []
tab_w = []


print("Zaczynamy losowanie liczb...")
for i in range(0, 6):
    a = random.randint(1, 49)
    if a in tab_r:
        a = random.randint(1, 49)
        tab_r.append(a)
    if a not in tab_r:
        tab_r.append(a)


print("Teraz wprowadź swoje liczby")
for i in range(6):
    a = int(input("Wprowadź liczby (1-49): "))
    if 1 <= a <= 49:
        tab_u.append(a)
    else:
        a = int(input("Wprowadź jeszcze raz (1-49)"))
        tab_u.append(a)

print("Wylosowane liczby to: ", tab_r)
print("Twoje liczby: ", tab_u)

print("Sprawdźmy ile trafiłeś...")

tab_u.sort()
tab_r.sort()

#  print(tab_u)
#  print(tab_r)

for i in range(0, 6):
    if tab_r[i] in tab_u:
        tab_w.append(tab_r[i])
        i += 1
    else:
        continue

print("O to co trafiłeś: ", tab_w, ". Trafiłeś więc ", len(tab_w))

if len(tab_w) == 0:
    print("Nic nie wygrałeś :(")
elif len(tab_w) == 1:
    print("Wygrałeś 2 zł")
elif len(tab_w) == 2:
    print("Wygrałeś 5 zł")
elif len(tab_w) == 3:
    print("Wygrałeś 1000 zł")
elif len(tab_w) == 4:
    print("Wygrałeś 20 000 zł")
elif len(tab_w) == 5:
    print("Wygrałeś 500 000 zł")
elif len(tab_w) == 6:
    print("Wygrałeś 1 000 000 zł!")