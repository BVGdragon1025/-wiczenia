import random
tab = []

for j in range(0, 6):
    i = random.randint(1, 49)
    if i in tab:
        i = random.randint(1, 49)
        tab.append(i)
    if i not in tab:
        tab.append(i)

print(tab)
print(len(tab))
