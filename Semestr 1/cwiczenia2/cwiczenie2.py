a = input("Podaj wartość liczbową: ")

if int(a) <= 10:
    print("Wartość jest mniejsza bądź równa 10")
elif 10 < int(a) <= 25:
    print("Wartość jest większa od 10, lecz mniejsza bądź równa 25")
elif int(a) > 25:
    print("Wartość jest większa od 25")
else:
    print("wtf?")
