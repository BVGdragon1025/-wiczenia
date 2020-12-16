import math
a = float(input("Podaj kąt: "))

sina = math.sin(a)
cosa = math.cos(a)
tga = math.tan(a)

print("Sinus: ", sina)
print("Cosinus: ", cosa)
print("Tangens: ", tga)

try:
    ctga = 1/tga
except ZeroDivisionError:
    print("Brak ctg")
else:
    print("Cotangens: ", ctga)