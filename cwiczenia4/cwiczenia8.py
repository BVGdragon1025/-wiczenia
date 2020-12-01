wplata = 333
kwota = 0
miesiac = 1

while miesiac <= 12:
    odsetki = (wplata * miesiac) * 0.08
    suma = odsetki + (wplata * miesiac)
    print("Ma odłożone w ", miesiac, "miesiąc(u) ", suma, " zł.")
    print("Odestki: ", odsetki, " zł.")

    miesiac += 1

