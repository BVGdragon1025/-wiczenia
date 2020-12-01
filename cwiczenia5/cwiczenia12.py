import random
import time
tab = []

print("Symulacja opiera się o 50 rzutów")
time.sleep(3)

print("Rzucam monetami...")

for i in range(0, 50):
    j = random.randint(0, 1)
    if j == 0:
        tab.append("orzeł")
    if j == 1:
        tab.append("reszka")
time.sleep(5)

print("Przeliczam ile jest orłów...")
tc1 = tab.count("orzeł")
time.sleep(3)

print("Przeliczam ile jest reszek...")
tc2 = tab.count("reszka")
time.sleep(3)

print("Składam wyniki w całość...")
time.sleep(5)

print("Gotowe!")
time.sleep(1)

print("Jakie były rzuty: ", tab)
print("Ile było orłów: ", tc1)
print("Ile było reszek: ", tc2)
