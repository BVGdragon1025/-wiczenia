class YellowPages:
    contact_dict = {}

    def __init__(self, number, name, surname):
        self.number = number
        self.name = name
        self.surname = surname

    def return_dict(self):
        return YellowPages.contact_dict

    def add_contact(self):
        name_list = []
        self.name = input("Podaj imię: ")
        self.surname = input("Podaj nazwisko: ")
        self.number = input("Podaj numer telefonu: ")
        name_list.append(self.name)
        name_list.append(self.surname)
        YellowPages.contact_dict[self.number]: name_list
        print("Kontakt dodany!")

    def delete_contact(self):
        number = input("Podaj numer telefonu do usunięcia: ")
        YellowPages.contact_dict.pop(number)

    def update_contact(self):
        YellowPages.return_dict(self)
        number = input("Wpisz numer telefonu do edycji: ")
        YellowPages.contact_dict.update(number)

    def export_to_file(self):
        with open("contact.txt", "x") as export_contact:
            for key, value in YellowPages.contact_dict:
                export_contact.write(key + " " + value)

    def sort_contacts(self):

