import webbrowser

lp = {
    "darek": "supersilne1",
    "user666": "szatandobryjest",
    "uberhaxxor": "133780085",
    "marek": "lowca",
    "admin": "Zx34bb12!",
    "krzak": "niewiemcowpisac"
}

l1 = str(input("Podaj login: "))
h1 = str(input("Podaj hasło: "))
url1 = "https://youtu.be/dQw4w9WgXcQ"
url2 = "https://youtu.be/AcmaNJfRQf0"

for kl, w in lp.items():
    if h1 == lp.get(kl):
        if l1 == "admin":
            print("Witaj, Administratorze(tm)")
            webbrowser.open(url2)
            break
        elif l1 != "admin":
            print("Witaj, Użytkowniku")
            webbrowser.open(url1)
            break
        else:
            print("Próbuj dalej!")
            break
