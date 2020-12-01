import random
"""""
x = int(input("Podaj początek zakresu: "))
z = int(input("Podaj koniec zakresu: "))
n = int(input("Ile chcesz liczb: "))
"""""
tab = []


x = random.randint(1, 101)
z = random.randint(102, 202)
n = random.randint(1, 50)

for i in range(0, n):
    a = random.randint(x, z)
    tab.append(a)
    i += 1

print("Twoja lista liczb: ", tab)
print("Jej długość: ", len(tab))
print("Usuwam duplikaty...")
tab2 = list(dict.fromkeys(tab))
print("Lista bez duplikatów: ", tab2)
print("Jej długość", len(tab2))
print("Różnica długości: ", len(tab)-len(tab2))
