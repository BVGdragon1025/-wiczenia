imie = str(input("Podaj swoje imię "))
nazw = str(input("Podaj swoje nazwisko: "))
nrtel = str(input("Podaj swój numer telefonu: "))
but = str(input("Podaj rozmiar swojego buta: "))

print("Czy w imieniu są liczby?", imie.isalpha())
print("Czy w nazwisku są liczby?", nazw.isalpha())
print("Czy w numerze telefonu są same cyfry?", nazw.isnumeric())
print("Czy w numerze buta są same cyfry?", nazw.isnumeric())

if imie.islower():
    imiep = imie.capitalize()
    print("Imię w poprawnym formacie: ", imiep)
else:
    print("Imię zapisane poprawnie: ", imie)

if nazw.islower():
    nazwp = nazw.capitalize()
    print("Nazwisko w poprawnym formacie: ", nazwp)
else:
    print("Nazwisko zapisane poprawnie: ", nazw)

if not nrtel.isnumeric():
    nrtelp = nrtel.replace(nrtel[3], " ") and nrtel.replace(nrtel[7], " ")
    print("Numer telefonu po poprawie: ", nrtelp)
else:
    print("Telefon zapisany poprawnie: ", nrtel)

if not but.isnumeric():
    butp = str(input("Podaj numer buta (tylko liczby)"))
    print("Poprawiony numer buta: ", butp)
else:
    print("Numer buta zapisany poprawnie: ", but)

if imie.endswith("a") or imie == "Nel":
    print("Przypuszczam że jesteś kobietą")
else:
    print("Przypuszczam, że jesteś facetem")
