import random
tab = []

for j in range(0, 20):
    i = random.randint(1, 80)
    if i in tab:
        i = random.randint(1, 80)
        tab.append(i)
    if i not in tab:
        tab.append(i)

print(tab)
print(len(tab))
