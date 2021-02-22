import math

print("Równanie kwadratowe to: y=ax^2*bx*c")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = (b**2) - (4 * a * c)
print(delta)
if delta > 0:
    x1 = -b - math.sqrt(delta) / 2*a
    x2 = +b - math.sqrt(delta) / 2*a
    print("Miejsca zerowe to: " + str(x1) + " i " + str(x2))
elif delta == 0:
    x1 = -b - math.sqrt(delta) / 2 * a
    print("Miejsce zerowe to: " + str(x1))
else:
    print("Brak rozwiązań")
