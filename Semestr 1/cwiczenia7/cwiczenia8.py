import random

x = int(input("Podaj zakres początkowy: "))
y = int(input("Podaj zakres końcowy: "))
z = int(input("Ile liczb wylosować: "))
tab_r = []

for i in range(0, z):
    a = random.randint(x, y)
    tab_r.append(a)
    i += 1

print("Twoje liczby: ", tab_r)
print("A teraz je pomieszam :)")

random.shuffle(tab_r)

print("Po pomieszaniu: ", tab_r)

r = str(input("Jak chcesz je posortować? Rosnąco, czy malejąco?: "))

if r == str("rosnąco"):
    tab_r.sort()
    print("Rosnąco: ", tab_r )
else:
    tab_r.sort(reverse=bool(1))
    print("Malejąco: ", tab_r)
