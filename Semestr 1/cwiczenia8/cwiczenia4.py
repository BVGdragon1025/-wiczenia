tup1 = ("pies", "kot", "foka", "lew", "wąż", "słoń")
c = int(0)

for i in tup1:
    s = str(input("Podaj słowo: "))
    if s in tup1:
        print("Szukane słowo jest w krotce")
        print("Jego indeks: ", tup1.index(s))
        break
    else:
        print("Nie ma takiego słowa.")
        break

tup2 = tup1 + ("koń", "ryba", "tygrys", "koala", "axolotl", "nosacz sundajski")

for i in tup2:
    s = str(input("Podaj kolejne słowo: "))
    if s in tup2:
        print("Szukane słowo jest w krotce")
        print("Jego indeks: ", tup2.index(s))
        break
    else:
        print("Nie ma takiego słowa.")
        break

s = str(input("Podaj jakieś zdanie: "))
tabs = list(s.split())
print(tabs)

for i in tabs:
    if tabs[c] in tup2:
        print("Słowo", tabs[c], "jest w krotce.", "To słowo pojawiło się: ", tabs.count(tabs[c]), "razy")
        c += 1
    else:
        print("Słowo", tabs[c], "nie jest w krotce. Idę dalej.")
        c += 1
