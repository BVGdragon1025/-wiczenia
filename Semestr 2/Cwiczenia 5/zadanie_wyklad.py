import sqlite3
import os
conn = sqlite3.connect('music.db')


class MusicDB:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

        if not os.path.exists('music.db'):
            conn.execute("CREATE TABLE songs("
                         "ID INT NOT NULL AUTO INCREMENT,"
                         "ARTIST TEXT NOT NULL,"
                         "TITLE TEXT NOT NULL),"
                         "PRIMARY KEY (ID);")
            conn.close()

    def music_add(self):
        self.artist = input("Podaj nazwę wykonawcy: ")
        self.title = input("Podaj jego utwór: ")

        conn.execute(f"INSERT INTO songs (ARTIST, TITLE) VALUES ('{self.artist}','{self.title}');")
        print("Piosenka dodana!")
        conn.close()

    def music_del(self):
        pass