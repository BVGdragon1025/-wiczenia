x = float(254)

while x <= 320:
    while x % 2 != 0 and x % 5 == 0:
        print(x)
        x += 1
    else:
        x += 1
        pass

