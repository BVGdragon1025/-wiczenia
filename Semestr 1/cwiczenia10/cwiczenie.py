import random

lista = ["Real Madryt", "Bayern Monachium", "Manchester City", "Manchester United", "Borussia Dortmund",
         "Legia Warszawa", "Chealsea Londyn", "Juventus Turyn", "Athetico Madryt", "F.C. Liverpool",
         "Inter Mediolan", "Szachtar Donieck", "Ajax Amsterdam", "FC Porto", "Red Bull Salzburg",
         "Dynamo Kijów", "F.C. Tottenham", "Olympique Lion", "Celtic Glasgow", "F.C. Monaco"]

LigaA = set()
LigaB = set()
LigaC = set()
LigaD = set()

while len(LigaA) < 10:
    r = random.choice(lista)
    LigaA.add(r)

while len(LigaB) < 10:
    r = random.choice(lista)
    LigaB.add(r)

while len(LigaC) < 10:
    r = random.choice(lista)
    LigaC.add(r)

while len(LigaD) < 10:
    r = random.choice(lista)
    LigaD.add(r)

print()
print("Zestaw A: ", LigaA)
print()
print("Zestaw B: ", LigaB)
print()
print("Zestaw C: ", LigaC)
print()
print("Zestaw D: ", LigaD)
print()
print("Wspólne A i B: ", LigaA.intersection(LigaB))
print("Wspólne B i C: ", LigaB.intersection(LigaC))
print("Wspólne C i D: ", LigaC.intersection(LigaD))
print("Wspólne D i A: ", LigaD.intersection(LigaA))
print()
print("Różnica A i B: ", LigaA.difference(LigaB))
print("Różnica B i C: ", LigaB.difference(LigaC))
print("Różnica C i D: ", LigaC.difference(LigaD))
print("Różnica D i A: ", LigaD.difference(LigaA))
print()
print("Suma A i B: ", LigaA.union(LigaB))
print("Suma B i C: ", LigaB.union(LigaC))
print("Suma C i D: ", LigaC.union(LigaD))
print("Suma D i A: ", LigaD.union(LigaA))
print()
print("Czy A jest podzbiorem B: ", LigaA.issubset(LigaB))
print("Czy B jest podzbiorem C: ", LigaB.issubset(LigaC))
print("Czy C jest podzbiorem D: ", LigaC.issubset(LigaD))
print("Czy D jest podzbiorem A: ", LigaD.issubset(LigaA))
print()
print("Czy B jest podzbiorem A: ", LigaA.issuperset(LigaB))
print("Czy C jest podzbiorem B: ", LigaB.issuperset(LigaC))
print("Czy D jest podzbiorem C: ", LigaC.issuperset(LigaD))
print("Czy A jest podzbiorem D: ", LigaD.issuperset(LigaA))
print()
print("Ilość wspólnych elementów A i B: ", len(LigaA.intersection(LigaB)))
print("Ilość wspólnych elementów B i C: ", len(LigaB.intersection(LigaC)))
print("Ilość wspólnych elementów C i D: ", len(LigaC.intersection(LigaD)))
print("Ilość wspólnych elementów D i A: ", len(LigaD.intersection(LigaA)))
LigaAodB = LigaA - LigaB
LigaBodC = LigaB - LigaC
LigaCodD = LigaC - LigaD
LigaDodA = LigaD - LigaA
print()
print("Elementy nie powtarzające się w A i B: ", LigaAodB)
print("Elementy nie powtarzające się w B i C: ", LigaBodC)
print("Elementy nie powtarzające się w C i D: ", LigaCodD)
print("Elementy nie powtarzające się w D i A: ", LigaDodA)
listaAodB = list(LigaAodB)
listaBodC = list(LigaBodC)
listaCodD = list(LigaCodD)
listaDodA = list(LigaDodA)
print()
print("Konwersja na listę A od B", listaAodB)
print("Konwersja na listę B od C", listaBodC)
print("Konwersja na listę C od D", listaCodD)
print("Konwersja na listę D od A", listaDodA)
# Dzięki temu możemy edytować nieedytowalne dane, bądź sortować te nie sortowalne.
# Dodatkowo w listach możemy dodać wartości powtarzające się.
