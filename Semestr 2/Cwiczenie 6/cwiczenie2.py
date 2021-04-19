import sqlite3
import os

conn = sqlite3.connect("workers.db")


class WorkersList:
    def __init__(self, name, surname, city, earnings):
        self.name = name
        self.surname = surname
        self.city = city
        self.earnings = earnings
