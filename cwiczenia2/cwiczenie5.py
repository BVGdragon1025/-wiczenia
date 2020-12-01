a = float(input("Podaj ilość promili we krwi: "))

if 0 <= a < 0.2:
    print("Może pan jechać")
elif 0.2 <= a < 0.5:
    print("Stan po spożyciu alkoholu, wykroczenie i mandacik :)")
elif 0.5 <= a:
    print("Stan nietrzeźwości, pańskie prawo jazdy poproszę :)")
else:
    print("Detektor wywaliło po za skalę")
