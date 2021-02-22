import random
tab = []

for j in range(0, 5):
    i = random.randint(1, 42)
    if i in tab:
        i = random.randint(1, 42)
        tab.append(i)
    if i not in tab:
        tab.append(i)

print(tab)
print(len(tab))
