n = int(input("Podaj dowolną liczbę: "))
tab = []

for i in range(1, n+1):
    if n % i == 0:
        tab.append(i)
        i += 1
    else:
        i +=1

print("Naturalne dzielniki liczby", n, ": ", tab)