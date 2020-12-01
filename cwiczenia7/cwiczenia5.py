import random
from collections import Counter

x = int(input("Podaj początek zakresu: "))
z = int(input("Podaj koniec zakresu: "))
n = int(input("Ile chcesz liczb?: "))
tab = []
tab2 = []
tab3 = []

for i in range(n):
    a = random.randint(x, z)
    tab.append(a)
    i += 1

print(tab)
print("Trzeci element od końca: ", tab[-3])

print("Który element od końca chcesz usunąć? (zakres od 0 do ", n, ")")
k = int(input("Podaj teraz: "))

tab.pop(-k)
print(tab)

print("Wygeneruję drugi ciąg na podstawie twoich ustawień")
for i in range(n):
    a = random.randint(x, z)
    tab2.append(a)
    i += 1

print(tab2)
print("Teraz scalę nową listę z twoją listą")
tab3 = tab + tab2
print(tab3)

print("Jej długość: ", len(tab3))

print("Ilość powtórzeń: ", Counter(tab3))