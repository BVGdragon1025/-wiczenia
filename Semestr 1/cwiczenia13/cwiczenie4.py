#zadanie 4, zrobione przez Danilla
wysok_m = int(input("Na jakiej wysokośći lecimy w metrach: "))
wysok_km = float(wysok_m / 1000)
if wysok_km < 5:
    print(f"{wysok_km}km to za nisko!")
else:
    print("Na tej wysokości jesteź już bezpieczny.")