import sqlite3
import os
conn = sqlite3.connect('music.db')

if not os.path.exists('music.db'):
    conn.execute("CREATE TABLE songs "
                 "('id'	INTEGER NOT NULL,'artist'	"
                 "TEXT NOT NULL,'title'	TEXT NOT NULL,"
                 "PRIMARY KEY('id' AUTOINCREMENT));")
    conn.commit()
else:
    conn.execute("CREATE TABLE IF NOT EXISTS songs"
                 "(id INTEGER NOT NULL,"
                 "artist TEXT NOT NULL,"
                 "title	TEXT NOT NULL,"
                 "PRIMARY KEY('id' AUTOINCREMENT));")
    conn.commit()


class MusicDB:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def music_add(self):
        self.artist = input("Podaj nazwę wykonawcy: ")
        self.title = input("Podaj jego utwór: ")

        conn.execute(f"INSERT INTO songs (ARTIST, TITLE) VALUES ('{self.artist}','{self.title}');")
        conn.commit()
        print("Piosenka dodana!")

    def music_del(self):
        self.artist = input("Podaj nazwę wykonawcy: ")
        self.title = input("Podaj tytuł utworu: ")
        print(f"Czy chcesz usunąć {self.title} zespołu {self.artist}?")
        confirm = input("Operacji tej nie można cofnąć! [y]Tak, [n]Nie: ")
        if confirm == "y" or confirm.lower() == "y":
            conn.execute(f"DELETE FROM songs WHERE artist='{self.artist}' AND title='{self.title}';")
            print("Piosenka usunięta!")
            conn.commit()

    def music_write(self):
        cursor = conn.execute("SELECT * FROM songs;")
        for row in cursor:
            print("ID: ", row[0], " | ", row[1], " - ", row[2])

    def music_update(self):
        MusicDB.music_write(self)
        choice = input("Wpisz ID utworu, który chcesz zaktualizować: ")
        self.artist = input("Wpisz nową nazwę zespołu (jeśli nie chcesz zmieniać, naciśnij ENTER): ")
        self.title = input("Wpisz nową nazwę utworu (jeśli nie chcesz zmieniać, naciśnij ENTER): ")
        if not self.artist:
            conn.execute(f"UPDATE songs SET title = '{self.title}' WHERE id={choice};")
        elif not self.title:
            conn.execute(f"UPDATE songs SET artist = '{self.artist}' WHERE id={choice};")
        else:
            conn.execute(f"UPDATE songs SET artist = '{self.artist}' AND title = '{self.title}' WHERE id={choice};")
        print("Utwór zaktualizowany!")
        conn.commit()

    def menu(self):
        while True:
            choice = input("Witaj! Wybierz co chcesz zrobić: \n"
                           "[1]Dodać utwór,\n"
                           "[2]Usunąć utwór,\n"
                           "[3]Zobaczyć wszystkie utwory,\n"
                           "[4]Zaktualizować utwór,\n"
                           "[q]Wyjść: ")
            if choice == "1":
                MusicDB.music_add(self)
            elif choice == "2":
                MusicDB.music_del(self)
            elif choice == "3":
                MusicDB.music_write(self)
            elif choice == "4":
                MusicDB.music_update(self)
            elif choice == "q" or choice.lower() == "q":
                conn.close()
                break
            else:
                print("Brak takiego wyboru.")


MusicDB.menu(MusicDB)