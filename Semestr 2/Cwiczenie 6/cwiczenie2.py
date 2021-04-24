import sqlite3
import os

conn = sqlite3.connect("workers.db")

if not os.path.exists("workers.db"):
    with conn:
        conn.execute("CREATE TABLE workers("
                     "id INTEGER NOT NULL,"
                     "name TEXT NOT NULL,"
                     "surname TEXT NOT NULL,"
                     "city TEXT NOT NULL,"
                     "earnings INTEGER NOT NULL,"
                     "PRIMARY KEY('id' AUTOINCREMENT));")
        conn.commit()
else:
    with conn:
        conn.execute("CREATE TABLE IF NOT EXISTS workers("
                     "id INTEGER NOT NULL,"
                     "name TEXT NOT NULL,"
                     "surname TEXT NOT NULL,"
                     "city TEXT NOT NULL,"
                     "earnings INTEGER NOT NULL,"
                     "PRIMARY KEY('id' AUTOINCREMENT));")
        conn.commit()


class WorkersList:
    def __init__(self, name, surname, city, earnings):
        self.name = name
        self.surname = surname
        self.city = city
        self.earnings = earnings

    def sort_by_name(self):
        cursor = conn.execute("SELECT * FROM workers ORDER BY name;")
        print("Lista pracowników (uporządkowana wg. imienia:\n")
        for row in cursor:
            print(row)
        print()

    def show_workers(self):
        cursor = conn.execute("SELECT * FROM workers;")
        for row in cursor:
            print(row)
        print()

    def add_worker(self):
        how_much = int(input("Ile osób chcesz dodać? (numerycznie): "))
        for i in range(how_much):
            self.name = input("Wpisz nazwę osoby: ")
            self.surname = input("Wpisz nazwisko osoby: ")
            self.city = input("Wpisz jej miasto: ")
            self.earnings = int(input("Wpisz jej zarobki: "))
            conn.execute(f"INSERT INTO workers (name, surname, city, earnings)"
                         f"VALUES('{self.name}','{self.surname}','{self.city}',{self.earnings});")
            conn.commit()
            print("Pracownik dodany!\n")

    def delete_worker(self):
        WorkersList.show_workers(self)
        choice = int(input("Wpisz ID pracownika do usunięcia: "))
        conn.execute(f"DELETE FROM workers WHERE id='{choice}';")
        conn.commit()
        print("Pracownik usunięty.\n")

    def update_worker(self):
        WorkersList.show_workers(self)
        choice = int(input("Wpisz ID pracownika do edycji: "))
        self.city = input("Podaj nowe miasto dla pracownika: (naciśnij ENTER aby pominąć): ")
        if self.city:
            conn.execute(f"UPDATE workers SET city='{self.city}' WHERE id='{choice}';")
        self.earnings = int(input("Podaj nowe zarobki pracownika: (naciśnij ENTER aby pominąć): "))
        if self.earnings:
            conn.execute(f"UPDATE workers SET earnings='{self.earnings}' WHERE id='{choice}';")
        conn.commit()
        conn.execute(f"SELECT * FROM workers WHERE id='{choice}';")
        print("Pracownik zaktualizowany!\n")

    def min_max_earnings(self):
        choice = input("Wybierz co chcesz wyświetlić: [1]Osoby z zarobkami wyższymi niż...,"
                       " [2]Osoby z zarobkami niższymi niż...: ")
        how_much = int(input("Podaj kwotę graniczną: "))
        if choice == "1":
            print(f"Osoby z zarobkami wyższymi niż {how_much}:")
            cursor = conn.execute(f"SELECT * FROM workers WHERE earnings>'{how_much}';")
            for row in cursor:
                print(row)
            print()
        elif choice == "2":
            print(f"Osoby z zarobkami niższymi niż {how_much}:")
            cursor = conn.execute(f"SELECT * FROM workers WHERE earnings<'{how_much}';")
            for row in cursor:
                print(row)
            print()

    def menu(self):
        while True:
            print("Witaj! Wybierz co chcesz zrobić: \n"
                  "[1]Wyświetlić pracowników (alfabetycznie wg. imienia), \n"
                  "[2]Dodać pracownika, \n"
                  "[3]Usunąć pracownika, \n"
                  "[4]Zaktualizować dane o pracowniku, \n"
                  "[5]Sprawdzić maks. i min. zarobki pracowników, \n"
                  "[q] Wyjść")
            choice = input("Wybierz: ")
            if choice == "1":
                WorkersList.sort_by_name(self)
            elif choice == "2":
                WorkersList.add_worker(self)
            elif choice == "3":
                WorkersList.delete_worker(self)
            elif choice == "4":
                WorkersList.update_worker(self)
            elif choice == "5":
                WorkersList.min_max_earnings(self)
            elif choice == "q" or choice.lower() == "q":
                conn.close()
                break
            else:
                print("Zły wybór!")


WorkersList.menu(WorkersList)
