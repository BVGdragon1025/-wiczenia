import random

x = int(input("Podaj zakres początkowy: "))
y = int(input("Podaj zakres końcowy: "))
z = int(input("Ile liczb wylosować: "))
tab_r = []

for i in range(0, z):
    a = random.randint(x, y)
    tab_r.append(a)
    i += 1

print(tab_r)
m = max(tab_r)

print("Maksymalna wartość: ", m)
print("Wystąpiła: ", tab_r.count(m), "razy")
