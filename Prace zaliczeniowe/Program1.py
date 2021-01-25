# Ubezpieczenie emerytalne - 9.76%
# ubezpieczenie rentowe - 1.5%
# ubezpieczenie chorobowe - 2.45%
# ubezpieczenie zdrowotne - 9%
# zaliczka na pit - (17 lub 32 przy skali podatkowej)

def brutto():
    money = float(input("Podaj ile zarobiłeś brutto: "))
    ue = money*0.0976  # ubezpieczenie emerytalne
    ur = money*0.0015  # ubezpieczenie rentowe
    uc = money*0.0245  # ubezpieczenie chorobowe
    uspol = ue + ur + uc  # ubezpieczenia społeczne
    puz = money - uspol  # podstawa do ubezpieczenia zdrowotnego
    uz = puz * 0.09  # ubezpieczenie zdrowotne
    tax = uspol + uz
    odliczenie = puz * 0.0775  # Odliczona składka zdrowotna

    if money < 85528:
        money_brutto = round(money - (tax + (money * 0.17 - 43.76-odliczenie)), 2)
        print("Dostaniesz netto: ", money_brutto)
    else:
        money_brutto = round(money - (tax + (money * 0.32 - 43.76-odliczenie)), 2)
        print("Dostaniesz netto: ", money_brutto)


brutto()
