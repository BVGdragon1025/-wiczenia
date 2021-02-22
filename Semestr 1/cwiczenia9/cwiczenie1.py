menu = {
    "Margherita": "18.20",
    "Tradycyjna": "22.90",
    "Farmera": "27.20",
    "Bolognese": "22.90",
    "Tonno": "27.20",
    "Romana": "27.20",
    "Bruno": "22.90",
    "Vesuvio": "28.00",
    "Gyros": "32.00",
    "Oregano": "27.20",
}

maxk = max(menu, key=menu.get)
mink = min(menu, key=menu.get)

for k, v in menu.items():
    print(k)
    print(v)
    print(k, v)

print(maxk)
print(mink)

del menu[maxk]
del menu[mink]

print(menu)


nazwa = str(input("Podaj nazwę pizzy: "))
cena = str(input("Podaj jej cenę: "))
menu[nazwa] = cena

print(menu)
