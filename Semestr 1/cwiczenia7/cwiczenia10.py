n = int(input("Podaj ile liczb Fibonacciego chcesz: "))
tab_p = [1, 1]

for i in range(n - 2):
    tab_p.append(tab_p[i] + tab_p[(i+1)])

print("Liczby: ", tab_p)
