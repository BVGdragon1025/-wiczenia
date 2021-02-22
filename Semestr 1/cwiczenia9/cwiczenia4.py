import webbrowser
lista = {}
j = 0
for i in range(5):
    mail2 = str(input("Podaj maila do wysyłania spamu: "))
    lista[i] = mail2

mail = str(input("Podaj swojego maila, aby wygrać iPhone'a 1000000!: "))
i = str(input("Wpisz który jesteś w kolejce! "))
lista[i] = mail

print("Haha, nie dostaniesz iPhona 1000000!")
while j != 10:
    # webbrowser.open("https://www.domowe-wypieki.pl/przepisy/ciasta/953-puszysty-sernik-bez-spodu")

    print("SERNICZKOWY SPAM")
    j += 1
webbrowser.open("mailto:", new=1)
print(lista)
