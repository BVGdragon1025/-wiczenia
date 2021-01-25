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

def menu():
    print("Wybierz sposób przeliczania: ")
    print("[1] Dolary na inną walutę: ")
    print("[2] Inna waluta na dolary: ")
    choice = str(input("Wybierz: "))
    return choice


def wybor(choice):
    menu()
    if choice == "1":
        print("Na jaką walutę: ")
        choice2 = str(input("Wybierz: "))
    else:
        print("Jaka waluta")
        choice2 = str(input("Wybierz: "))


wybor(menu)
