a = float(input("Wprowadź pierwszą liczbę: "))
b = float(input("Wprowadź drugą liczbę: "))
c = float(input("Wprowadź trzecią liczbę: "))

if a > b:  # sprawdzenie pierwszej i drugiej liczby
    if a > c:  # Sprawdzenie piewszej i trzeciej liczby
        print("Liczba " + str(a) + " jest największa")
    elif a < c:  # Jeśli liczba pierwsza jednak jest mniejsza od trzeciej
        print("Liczba " + str(c) + " jest największa")
elif a < b:  # sprawdzenie pierwszej i drugiej liczby
    if b > c:  # sprawdzenie drugiej i trzeciej liczby
        print("Liczba " + str(b) + " jest największa")
    elif b < c:  # Jeśli liczba druga jest jednak mniejsza od trzeciej
        print("Liczba " + str(c) + " jest największa")
elif a == b == c:  # Jeśli liczby są identyczne
    print("Liczby są identyczne")
else:  # Jeśli czegoś przeoczyłem
    print("Wyjątek!")
