# 1 GB = 0.91313 GB
# Chyba go rozwinę aby wykrywał jednostkę podaną przez użytkownika

# Main, z inputem i z wyświetleniem wyniku, a także z wyjaśnieniem.
def main():
    capacity = int(input("Podaj jakiej wielkości kupiłeś dysk (w GB): "))
    cap_calc(capacity)
    print("Rzeczywista pojemność to ", cap_calc(capacity), "GB")
    print("To o ", (capacity - cap_calc(capacity)), "mniej!")
    print("Powodem jest to, jak producenci zapisują pojemność dysków.")
    print("Zapisują oni ją na bazie dziesiętnej (1GB = 1000MB)")
    print("A Windows wyświetla ją na bazie binarnej (1GB = 1024MB)")
    print("Stąd ta różnica.")


# Proste równanko
def cap_calc(capacity):
    real_cap = capacity * 0.91313
    return real_cap


#Wywołanie maina
main()
