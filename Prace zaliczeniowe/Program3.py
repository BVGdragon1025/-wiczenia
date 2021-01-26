# Na ten moment popsute jest sprawdzanie czy pytanie już było. Właściwie działa, ale resetuje licznik.
# Do poprawki

import random

# Krotka z pytaniami
qstns = ("Rozwiń skrót HTML",
         "Rozwiń skrót CSS",
         "Rozwiń skrót JS",
         "W jaki sposób zapiszesz szesnastkowo kolor czarny",
         "W jaki sposób zapiszesz szesnastkowo kolor biały",
         "Językiem czego jest HTML?",
         "Jaką komendą można sprawdzić zawartość pliku w Linuxie?",
         "Jakim typem języka jest Python?",
         "Czy C++ jest językiem kompilowanym?",
         "Jakie słowo definiuje funkcję w Pythonie?",
         "Jakie rozszerzenie ma plik JavaScript? (bez kropki)",
         "Jakie rozszerzenie ma plik C++? (bez kropki)",
         "Czy C++ to język interpretowany?",
         "Jak nazywa się język ezoteryczny zainspirowany memiczną "
         "mową kotów?",
         "Czy Python to język interpretowany?",
         "Czy Python to język kompilowany?",
         "28"
         )

# Krotka z odpowiedziami
answrs = ("Hypertext Markup Language",
          "Cascade Style Sheet",
          "JavaScript",
          "000000",
          "FFFFFF",
          "Znaczników",
          "cat",
          "Interpretowanym",
          "Tak",
          "def",
          "js",
          "cpp",
          "Nie",
          "LOLCAT",
          "Tak",
          "Nie",
          "28"
          )

# Tablica z wartościami, które już były
repeat = []


def main():
    print("Witaj w quizie!")
    print("Pamiętaj, aby odpowiedzi na pytania były napisane poprawnie")
    choice = input("Czy jesteś gotów? Tak lub Nie: ")
    if choice == "Tak" or choice.capitalize() == "Tak" or choice.lower() == "tak":
        quiz()
        grade(quiz())
    else:
        print("Widzimy się więc wkrótce!")


def quiz():
    # Licznik punktów
    points = 0
    for i in range(10):
        quest = random.randint(0, len(qstns)-1)
        # Sprawdzenie czy pytanie już było (obecnie zepsute)
        if quest in repeat:
            quest = random.randint(0, len(qstns) - 1)
        else:
            repeat.append(quest)
            # Wyświetlenie pytania i zapytanie usera
            print(qstns[quest])
            answer = input("Podaj odpowiedź: ")
            # Sprawdzenie poprawności odpowiedzi
            if answer.capitalize() == answrs[quest]\
                    or answer == answrs[quest]\
                    or answer.upper() == answrs[quest]:
                # Dodanie punktu
                print("Dobra odpowiedź!, +1")
                points += 1
                print(points)
                print(repeat)
            else:
                print(points)
                print(repeat)
                print("Zła odpowiedź, lecimy dalej")
    return points


# Podliczenie punktów i wystawienie oceny
def grade(points):
    print(points)
    if points <= 3:
        print("Ocena niedostateczna. Powodzenia następnym razem")
    elif 3 < points <= 5:
        print("Ocena dostateczna. Mogło być lepiej, ale zaliczyłeś!")
    elif 5 < points <= 7:
        print("Ocena dostateczna. Może być!")
    elif 7 < points <= 8:
        print("Ocena dobra. Nieźle się spisałeś!")
    elif 8 < points <= 9:
        print("Ocena bardzo dobra. Świetna robota!")
    else:
        print("Ocena celująca. Rozwaliłeś ten test, gratulacje!")


main()
