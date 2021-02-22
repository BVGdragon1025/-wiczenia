months = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik",
          "listopad", "grudzień"]
while True:
    i = int(input("Podaj liczbę miesiąca: "))
    if i == 0:
        print("Podaj wartość od 1 do 12")
        continue
    try:
        print(months[i - 1])
        break
    except i != 0 or i < 0:
        print("Podaj wartość od 1 do 12")
