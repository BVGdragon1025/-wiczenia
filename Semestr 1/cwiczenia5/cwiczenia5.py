import math

# pierwszy sposób
n = int(input("Podaj liczbę do obliczenia silni: "))
i = 1

for a in range(1, n+1):
    i = i * a

print("Silnia z liczby", n, "to", i)

# drugi sposób
h = math.factorial(n)
print(h)

