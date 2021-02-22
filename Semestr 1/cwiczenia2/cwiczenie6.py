a = float(input("Wprowadź pierwszą liczbę: "))
b = float(input("Wprowadź drugą liczbę: "))
c = float(input("Wprowadź trzecią liczbę: "))
d = float(input("Wprowadź czwartą liczbę: "))

if a > b:                                                                      # sprawdzenie pierwszej i drugiej liczby
    if a > c:                                                                  # Sprawdzenie pierwszej i trzeciej liczby
        if a > d:                                                              # Sprawdzenie pierwszej i czwartej liczby
            print("Liczba " + str(a) + " jest największa")
    elif a < c:                                                 # Jeśli liczba pierwsza jednak jest mniejsza od trzeciej
        print("Liczba " + str(c) + " jest największa")
    elif a < d:                                                 # Jeśli liczba pierwsza jednak jest mniejsza od czwartej
        print("Liczba " + str(d) + " jest największa")
elif a < b:                                                                     # sprawdzenie pierwszej i drugiej liczby
    if b > c:                                                                   # sprawdzenie drugiej i trzeciej liczby
        if b > d:                                                               # sprawdzenie drugiej i czwartej liczby
            print("Liczba " + str(b) + " jest największa")
    elif b < c:                                                    # Jeśli liczba druga jest jednak mniejsza od trzeciej
        print("Liczba " + str(c) + " jest największa")
    elif b < d:                                                    # Jeśli liczba druga jest jednak mniejsza od czwartej
        print("Liczba " + str(d) + " jest największa")
elif a == b == c == d:                                                                      # Jeśli liczby są identyczne
    print("Liczby są identyczne")
else:                                                                                         # Jeśli czegoś przeoczyłem
    print("Wyjątek!")