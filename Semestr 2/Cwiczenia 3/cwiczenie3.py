import os


class Obywatel:
    def __init__(self, name, surname, street, street_num, postal_code, city):
        self.name = name
        self.surname = surname
        self.street = street
        self.street_num = street_num
        self.postal_code = postal_code
        self.city = city

    def add_person(self):
        self.name = input("Podaj imię: ")
        self.surname = input("Podaj imię: ")
        self.street = input("Podaj ulicę: ")
        self.street_num = int(input("Podaj numer mieszkania: "))
        self.postal_code = input("Podaj kod pocztowy: ")
        self.city = input("Podaj miasto: ")
        print("Osoba dodana!")

    def card(self):
        Obywatel.add_person(self)
        print("-------------------------------------------")
        print(f"{self.name} {self.surname}")
        print(f"ul. {self.street} {self.street_num}")
        print(f"{self.postal_code} {self.city}")
        print("-------------------------------------------")
        if not os.path.exists("card.txt"):
            with open("card.txt", "x") as writefile:
                writefile.write(
                    f"-------------------------------------------\n"
                    f"{self.name} {self.surname}\n"
                    f"ul. {self.street} {self.street_num}\n"
                    f"{self.postal_code} {self.city}\n"
                    f"-------------------------------------------\n"
                )
        else:
            with open("card.txt", "a") as writefile:
                writefile.write(
                    f"-------------------------------------------\n"
                    f"{self.name} {self.surname}\n"
                    f"ul. {self.street} {self.street_num}\n"
                    f"{self.postal_code} {self.city}\n"
                    f"-------------------------------------------\n"
                )
        print("Wizytówka wygenerowana w pliku 'card.txt'.")


person1 = Obywatel("Dominik", "Nawrot", "Zmyślona", 28, "56-400", "Oleśnica")
person1.card()
Obywatel.card(Obywatel)

