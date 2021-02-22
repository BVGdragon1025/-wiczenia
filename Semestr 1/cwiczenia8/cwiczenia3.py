import random

tab1 = []
tab2 = []

for i in range(0,101):
    tab1.append(random.randrange(0, 100, 2))

for i in range(0,100):
    j = random.randrange(0, 100)
    if j % 2 == 0:
        j += 1
        tab2.append(j)
    else:
        tab2.append(j)


print(tab1)
print(tab2)

tup1 = tuple(tab1)
tup2 = tuple(tab2)

tup3 = tup1 + tup2
print("0 jest: ", tup3.count(0))
print("100 jest: ", tup3.count(100))
print("Miejsce w pamięci: ", id(tup3))
