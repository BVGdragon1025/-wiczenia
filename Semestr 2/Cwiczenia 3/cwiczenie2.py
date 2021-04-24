beer_list = []


class Beer:
    def __init__(self, name, price, alc_percentage, beer_type, grade):
        self.name = name
        self.price = price
        self.alc_percentage = alc_percentage
        self.beer_type = beer_type
        self.grade = grade

    def add_beer(self):
        help_list = []
        how_much = int(input("Ile piw chcesz dodać? (numerycznie): "))
        for i in range(how_much):
            self.name = input("Podaj nazwę piwa: ")
            self.price = float(input("Podaj cenę piwa: "))
            self.alc_percentage = float(input("Podaj ile procent ma piwo: "))
            self.beer_type = input("Podaj jakiego typu to piwo: ")
            self.grade = int(input("Jak oceniasz to piwo (0-5): "))
            help_list.append(self.name)
            help_list.append(self.price)
            help_list.append(self.alc_percentage)
            help_list.append(self.beer_type)
            help_list.append(self.grade)
            beer_list.append(help_list)

    def order_by_grade(self):
        print(beer_list.sort())


heineken = Beer("Heineken", 5.30, 5, "Lager", 4)

print(beer_list)

