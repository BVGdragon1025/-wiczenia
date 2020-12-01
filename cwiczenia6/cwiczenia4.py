import random
import time

print("Losuję liczbę...")
r = random.randint(0, 100)
time.sleep(3)
print("Ok, zgadnij jaka to liczba :)")
time.sleep(2)

c = 0


while c != 3:
    a = float(input("Podaj swoją propozycję: "))
    if a > r:
        c += 1
        time.sleep(1)
        print("Podałeś za dużą, próbuj dalej :)")
        # continue
    elif a < r:
        c += 1
        time.sleep(1)
        print("Podałeś za małą, próbuj dalej :)")
        # continue
    else:
        time.sleep(1)
        print("Gratuluję, wygrałeś!")
        time.sleep(1)
        print("Wylosowaną liczbą było: ", r)
        break
else:
    # time.sleep(1)
    print("Koniec żyć :). Haha, przegrałeś!")
    time.sleep(2)
    print("Wylosowaną liczbą było: ", r)
