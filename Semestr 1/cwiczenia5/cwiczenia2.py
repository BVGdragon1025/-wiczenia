a = int(input("Podaj zakres końcowy: "))

for i in range(a, 0, -1):
    if i % 6 == 0 and i % 9 == 0:
        print(i)
