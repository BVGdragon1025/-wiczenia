import dateutil.easter
import datetime


def menu():
    print("Witaj w programie!")
    print("Co chcesz zrobić? ")
    print("[1] Dowiedzieć się co było wczoraj i jutro ")
    print("[2] Odkryć w jaki dzień się urodziłeś ")
    print("[3] Dowiedzieć się kiedy Wielkanoc")
    choice = input("Wybierz funkcję: ")
    if choice == "1":
        days()
    elif choice == "2":
        birthday()
    elif choice == "3":
        easter_day()
    else:
        print("Zły wybór!")


def days():
    # Timedelta ustawiona jest, aby pokazywać dzień do przodu
    # (lub dzienń do tyłu, zależnie od działania)
    # Dzisiejsza data
    today = datetime.date.today()
    print("Dzisiaj mamy: ", today.strftime("%d-%m-%Y"))
    # Wyświetlenie wczorajszej daty
    yesterday = today - datetime.timedelta(days=1)
    print("Wczoraj mieliśmy: ", yesterday.strftime("%d-%m-%Y"))
    # Wyświetlenie dzisiejszej daty
    tommorrow = today + datetime.timedelta(days=1)
    print("Jutro będzie: ", tommorrow.strftime("%d-%m-%Y"))


def birthday():
    # Słownik użyty do tłumaczenia nazw angielskich (raczej logiczne)
    day_dict = {"Monday": "Poniedziałek",
                "Tuesday": "Wtorek",
                "Wednesday": "Środa",
                "Thursday": "Czwartek",
                "Friday": "Piątek",
                "Saturday": "Sobota",
                "Sunday": "Niedziela"}
    day = int(input("Podaj dzień (liczbowo): "))
    month = int(input("Podaj miesiąc (liczbowo): "))
    year = int(input("Podaj rok (liczbowo, pełny): "))
    full_date = datetime.date(year, month, day)
    dom = full_date.strftime("%A")
    print("Urodziłeś się w: ",day_dict[dom])


def easter_day():
    # Tak, skorzystałem z gotowej funkcji z biblioteki dateutil
    # Wiem, powinienem napisać to sam
    # Ale to było za dużo dla mnie, aby wykalkulować jeden dzień
    # I to jeszcze taki losowy, zależny od pełni, innego święta i przesilenia
    # Kto na to wpadł, ja sie pytam
    # A na rozwiązanie wpadłem kiedy przeszukując Internety i widząc ten sam algorytm wszędzie
    # w końcu ktoś na StackOverflow podał tę bibliotękę i stweirdziłem że to jest lepsze rozwiązanie
    # Wartość 3 oznacza współczesną metodę, używaną w Polsce
    year = int(input("Podaj rok: "))
    print("Wielkanoc wypada w: ", dateutil.easter.easter(year, 3))


menu()
