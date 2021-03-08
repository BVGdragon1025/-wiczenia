class Book:

    def __init__(self, author, title, year, publishing, genre):
        self.author = str(author)
        self.title = str(title)
        self.year = int(year)
        self.publishing = str(publishing)
        self.genre = str(genre)


book_list = []
example = Book("Dmitry Glukhovsky", "Metro 2033", 2015, "Insignis", "Science Fiction")
book_list.append(example)


def menu():
    while True:
        choice = input("Podaj co chesz zrobić?\n"
                       "[1] Dodaj książkę/książki\n"
                       "[2] Oznacz jako czytaną: ")

        if choice == "1":
            add_to_list()
        elif choice == "2":
            pass
        elif choice == "4":
            pass
        elif choice == "4":
            book_sort()
        else:
            print("Zły wybór")


def add_to_list():
    how_much = int(input("Podaj ile książek chcesz dodać (liczbowo): "))
    for i in range(how_much):
        author = input("Podaj autora: ")
        title = input("Podaj tytuł: ")
        year = int(input("Podaj rok wydania: "))
        publishing = input("Podaj wydawnictwo: ")
        genre = input("Podaj gatunek: ")
        book = Book(author, title, year, publishing, genre)
        book_list.append(book)
        print("Książka dodana!")


def book_sort():
    for i, Book in range(len(book_list)):
        print(book_list[i])


menu()
