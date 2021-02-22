# 1 GB = 0.91313 GB
# Chyba go rozwinę aby wykrywał jednostkę podaną przez użytkownika

# Przeliczniki dla odpowiednich wartości
cap_dict = {"MB": 1048576,
            "GB": 1073741824,
            "TB": 1099511627776}


# Proste równanko
def cap_calc(capacity, measure):
    if measure.upper() == "GB":
        real_cap = (capacity * (10**9))/1073741824
        return real_cap
    elif measure.upper() == "MB":
        real_cap = (capacity * (10**6))/1048576
        return real_cap
    elif measure.upper() == "TB":
        real_cap = (capacity * (10**12))/1099511627776
        return real_cap
    else:
        print("Bład")


# Main, z inputem i z wyświetleniem wyniku, a także z wyjaśnieniem.
def main():
    capacity = int(input("Podaj jakiej wielkości kupiłeś dysk (te cyferki): "))
    measure = input("Podaj w jakich jednostkach (MB, GB, TB): ")
    cap_calc(capacity, measure)
    print("Twój dysk ma rzeczywistą pojemność: ", round(cap_calc(capacity, measure), 2), measure)
    print("Powodem jest inny zapis producentów dysku i inne wyświetlanie pojemności przez system Windows")
    print("Producenci zapisują pojemność dziesiętnie, a Windows pokazuje ją binarnie")
    print("No chyba, że masz Mac'a, to wtedy widzisz pojemność taką jaką zapisuje producent dysku.")
    print("Nie oznacza to, że masz mniej miejsca. Masz go tyle samo. To jak z milami i metrami - taka sam odległość, "
          "ale zapisana inaczej.")


# Wywołanie maina
main()
