import sqlite3
import os


class YellowBook:
    def __init__(self, name, surname, number, dbname):
        self.name = name
        self.surname = surname
        self.number = number
        self.dbname = dbname

    def create_db(self):
        self.dbname = input("Podaj nazwę nowej bazy: ")
        if not os.path.exists(f"{self.dbname}.db"):
            conn = sqlite3.connect(f"{self.dbname}.db")
            with conn:
                conn.execute("CREATE TABLE KONTAKTY("
                             "id INTEGER NOT NULL,"
                             "name TEXT NOT NULL,"
                             "surname TEXT NOT NULL,"
                             "number INTEGER NOT NULL,"
                             "PRIMARY KEY('id' AUTOINCREMENT));")
                conn.commit()
        else:
            print("Podana baza już istnieje. Spróbuj inną nazwę.")

    def check_db(self):
        if not self.dbname:
            for file in os.listdir():
                print(file.endswith(".db"))
            choice = input("Wybierz z której bazy danych chcesz korszystać: ")
            self.dbname = choice

    def add_number(self):
        YellowBook.check_db(self)
        conn = sqlite3.connect(f"{self.dbname}.db")
        i = input("Ile chcesz dodać kontaktów?: ")
        self.name = input("Wpisz imię osoby: ")
        self.surname = input("Wpisz nazwisko osoby: ")
        self.number = input("Wpisz numer osoby: ")
        if i == "1":
            conn.execute(
                f"INSERT INTO KONTAKTY (name,surname,number) "
                f"VALUES('{self.name}','{self.surname}',{self.number});"
            )
            conn.execute("SELECT * FROM KONTAKTY;")
            conn.commit()
            print("Kontakt dodany!")

        else:
            for j in range(int(i)):
                conn.execute(
                    f"INSERT INTO KONTAKTY (name,surname,number) "
                    f"VALUES('{self.name}','{self.surname}',{self.number});"
                )
                conn.execute("SELECT * FROM KONTAKTY;")
                conn.commit()
            print("Kontakty dodane!")

    def read_number(self):
        YellowBook.check_db(self)
        conn = sqlite3.connect(f"{self.dbname}.db")
        cursor = conn.execute("SELECT * FROM KONTAKTY;")
        for row in cursor:
            print(row)

    def delete_number(self):
        YellowBook.check_db(self)
        conn = sqlite3.connect(f"{self.dbname}.db")
        YellowBook.read_number(self)
        choice = input("Wpisz numer ID osoby do usunięcia: ")
        confirm = input("Czy chcesz usunąć ten kontakt? Operacji nie można cofnąć! [y]Tak, [n]Nie: ")
        if confirm == "y" or confirm.lower == "y":
            conn.execute(f"DELETE FROM KONTAKTY WHERE id='{choice}';")
            conn.commit()
        else:
            print("Usunięcie cofnięte!")

    def update_number(self):
        YellowBook.check_db(self)
        conn = sqlite3.connect(f"{self.dbname}.db")
        YellowBook.read_number(self)
        choice = input("Wpisz numer ID osoby do aktualizacji: ")
        self.number = input("Podaj nowy numer tej osoby: ")
        conn.execute(f"UPDATE KONTAKTY SET number='{self.number}' WHERE id='{choice}'")
        print("Kontakt zaktualizowany!")
        conn.commit()

    def menu(self):
        while True:
            choice = input("Witaj! Wybierz co chcesz zrobić: \n"
                           "[1]Stworzyć bazę,\n"
                           "[2]Dodać kontakt,\n"
                           "[3]Wypisać kontakty,\n"
                           "[4]Usunąć kontakt,\n"
                           "[5]Zaktualizować kontakt,\n"
                           "[q]Wyjść: ")
            if choice == "1":
                YellowBook.create_db(self)
            elif choice == "2":
                YellowBook.add_number(self)
            elif choice == "3":
                YellowBook.read_number(self)
            elif choice == "4":
                YellowBook.delete_number(self)
            elif choice == "5":
                YellowBook.update_number(self)
            elif choice == "q" or choice.lower() == "q":

                break
            else:
                print("Brak takiego wyboru.")


YellowBook.menu(YellowBook)