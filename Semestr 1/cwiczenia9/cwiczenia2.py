import statistics
tel = {
    "Jan": "123456789",
    "Robert": "123456789",
    "Andrzej": "123456789",
    "Karol": "123456789",
    "Romek": "123456789",
    "Szymon": "123456789",
    "Grzegorz": "123456789",
    "Karolina": "123456789",
    "Anna": "123456789",
    "Maja": "123456789"
}

"""for i in range(10):
    nazwisko = str(input("Podaj nazwisko: "))
    numer = str(input("Podaj numer: "))
    tel[nazwisko] = numer
"""
print(tel)

telf = list(tel.keys())[0]
tell = list(tel.keys())[len(tel)-1]

print(telf, tell)

tel[telf] = "b"
tel[tell] = "c"

print(tel)


telm1 = statistics.median_low(tel)
telm2 = statistics.median_high(tel)

print(telm1, telm2)

del tel[telm1]
del tel[telm2]

print(tel)
tel.clear()


tel[input("Podaj nazwisko: ")] = input("Podaj numer tel.: ")
tel[input("Podaj nazwisko: ")] = input("Podaj numer tel.: ")
print(tel)

