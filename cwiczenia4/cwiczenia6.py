a = int(input("Podaj liczbę: "))
b = 0
c = 0

while a % 2 == 0 or a % 3 == 0:
    b += 1
    if a % b == 0:
        if a == b:
            break
        c = a + b
        print(b)
    else:
        if b == a:
            break
        continue
