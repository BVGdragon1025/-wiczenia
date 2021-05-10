import random


def part1():
    stos = []
    kolejka = []

    for i in range(50):
        stos.append(random.randint(0,100))

    print("Stos: ", stos)

    for elements in stos:
        kolejka.insert(0, elements)

    print("Kolejka: ", kolejka)


part1()


def part2():
    kolejka2 = []
    with open("losowe_liczby.txt", "w+") as writenumbers:
        for i in range(50):
            writenumbers.write(str(random.randrange(0, 100)) + "\n")

    with open("losowe_liczby.txt", "r") as readnumbers:
        print("Liczby w pliku: ", readnumbers.read().rsplit("\n"))
        for numbers in readnumbers:
            kolejka2.append(numbers.rsplit("\n"))
        print("Kolejka: ", kolejka2)


part2()
