# Ubezpieczenie emerytalne - 9.76%
# ubezpieczenie rentowe - 1.5%
# ubezpieczenie chorobowe - 2.45%
# ubezpieczenie zdrowotne - 9%
# koszty uzyskania przychodu - 250 zł
# kwota wolna od podatku - 43,76 zł
# zaliczka na pit - (17 lub 32 przy skali podatkowej)

# Napisanie tego to była droga przez mękę
# Za duzo matmy i ogarniania co gdzie ma być dodane/odjęte
# Jak myślę sobie, że drugie zadanie opiera się o to, to tracę chęć do życia
# A na pomysł wpadłem szukając aplikacji do wyliczania tego na internecie.
# https://poradnikprzedsiebiorcy.pl/kalkulator-wynagrodzen

def netto():
    money_brutto = float(input("Podaj twoją kwotę brutto: "))
    sk_em = money_brutto * 0.0976  # Składka emerytalna
    sk_rent = money_brutto * 0.015  # Składka rentowa
    sk_ch = money_brutto * 0.0245  # składka chorobowa
    sk_spol = sk_em + sk_rent + sk_ch  # składki społeczne
    # print("Składki społeczne: ",round(sk_spol,2))
    pod_uz = money_brutto - sk_spol  # Podstawa do ubezpieczenia zdrowotnego
    zal_pd = int(pod_uz - 250)  # Zaliczka na pod. dochodowy
    # print("Zaliczka na podatek dochodowy: ",zal_pd)

    if (money_brutto * 12) < 85258:  # Podatek jest różny w zależności od zarobków w roku
        pod_tax = zal_pd * 0.17  # Podstawa do obliczenia podatku dochodowego
        # print("Podstawa do obliczenia podatku dochodowego: ", round(pod_tax,2))
        tax = pod_tax - 43.76  # Podstawa minus kwota wolna od podatku
        # print("Podstawa po odjęciu kwoty wolnej od podatku: ", round(tax,2))
    else:
        pod_tax = zal_pd * 0.32
        tax = pod_tax - 43.76

    zal_uz = pod_uz * 0.09  # Zaliczka na ubezpieczenia społeczne
    # print("Ubezpieczenie zdrowotne: ",round(zal_uz,2))
    odl_sk_zdr = pod_uz * 0.0775  # Zaliczka na ubezpieczenie po odliczeniu
    # print("Ubezpieczenie zdrowotne po odliczeniu: ",round(odl_sk_zdr,2))
    zal_pd_dz = int(tax - odl_sk_zdr)  # Podatek dochodowy do zapłaty
    # print("Zaliczka na podatek dochodowy do zapłaty: ",zal_pd_dz)
    money_netto = money_brutto - (sk_spol + zal_uz + zal_pd_dz)
    print("Twoja kwota netto to: ",round(money_netto,2), " zł")


netto()
