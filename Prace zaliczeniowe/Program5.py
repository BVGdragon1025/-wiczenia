# Stan przelicznika na dzień 23.01.2020:
# 1 Baht Tajski to 0.033 Dolara
# 1 Bitcoin to 32368,60 Dolarów
# 1 Ngultrum to 0.014 dolara
# 1 Ugija to 0.028 dolara
# 1 Ether to 1256,48 dolara
# --------Dodane przeze mnie--------
# 1 Dogecoin to 0.00856 dolara
# 1 boliwar wenezuelski (Dong) to 0.000043 dolara
# 1 panamski balboa to 1 dolar
# 1 korona czeska to 0.047 dolara
# 1 monero to 139.44 dolarów


# Krotka z wartościami poszczegolnych walut
tuple_conv = (0.033, 32368.00, 0.014, 0.028, 1256.48,
              0.00856, 0.00043, 1, 0.047, 139.44)

# Krotka z nazwami walut
tuple_names = ("Baht", "Bitcoin", "Ngultrum", "Ugija",
               "Etherum", "Dogecoin", "boliwar wenezuelski (Dong)",
               "panamski balboa", "koron czeskich",
               "monero")


def menu():  # Menu dla użytkownika
    print("Wybierz sposób przeliczania: ")
    print("[1] Dolary na inną walutę: ")
    print("[2] Inna waluta na dolary: ")
    choice = str(input("Wybierz: "))
    return choice


def wybor(choice):  # Wybor typu przeliczenia

    if choice == "1":
        print("Na jaką walutę: ")
        print_choices()
        choice2 = str(input("Wybierz: "))
        conversion(choice, choice2)
    else:
        print("Jaka waluta")
        print_choices()
        choice2 = str(input("Wybierz: "))
        conversion(choice, choice2)


def print_choices():  # Wydruk wyborów, aby oszczędzić linijki
    print("[1] Baht Tajski ")
    print("[2] Bitcoin ")
    print("[3] Ngultrum ")
    print("[4] Ugija ")
    print("[5] Etherum ")
    print("[6] Dogecoin ")
    print("[7] Boliwar Wenezuelski (Dong) ")
    print("[8] Panamski Balboa ")
    print("[9] Korona czeska ")
    print("[10] Monero ")


def conversion(choice, choice2):  # Konwersja walut na podstawie wyboru sposobu konwersji
    if choice == "1":
        dolar = int(input("Podaj ile dolarów: "))
        conv = dolar / tuple_conv[int(choice2)-1]
        print(dolar, "$ to", round(conv, 2), tuple_names[int(choice2)-1])
    elif choice == "2":
        other = int(input("Podaj ile: "))
        conv = other * tuple_conv[int(choice2) - 1]
        print(other, tuple_names[int(choice2) - 1], "to", round(conv, 2), "$")


wybor(menu())
