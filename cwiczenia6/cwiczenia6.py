n = int(input("Podaj przedział do ilu liczb chcesz wprowadzać: "))

for i in range(0, n):
    a = int(input("Podaj liczbę: "))
    if -6 <= a <= 6:
        print("Liczba należy do przedziału od -6 do 6")
    else:
        print("Liczba nie jest w przedziale od -6 do 6")
