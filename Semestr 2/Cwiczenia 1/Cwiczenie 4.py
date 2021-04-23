class Student:
    def __init__(self, name, surname, age, mood, hunger, will, which_semester):
        self.name = name
        self.surname = surname
        self.age = age
        self.mood = mood
        self.hunger = hunger
        self.will = will
        self.which_semester = which_semester

    def id(self):
        print(self.name, self.surname, self.age)

    def is_hungry(self):
        if self.hunger > 80:
            print("Jesteś głodny. Zjedz coś!")
        elif 80 >= self.hunger > 50:
            print("Burczy ci w brzuchu. Zjedzenie czegoś może być dobrym pomysłem.")
        elif 50 >= self.hunger > 20:
            print("Czujesz lekki niedosyt. Możesz coś wrzucić na ząb.")
        else:
            print("Jesteś w miarę najedzony. Przeżyjesz ten dzień.")

    def dec_hunger(self):
        food = {
            "Pizza": -50,
            "Jabłko": -10,
            "Snickers": -30,
            "Kanapka": -45,
            "Rogal": -25,
            "Bułka": -45,
        }

        print(food.keys())
        food_type = input("Wpisz co chcesz zjeść: ")

        for key, value in food.items():
            final_hunger = self.hunger + value
            if food_type == key:
                print("Zjadłeś:", key, ". Twój poziom głodu wynosi: ", final_hunger)
                self.hunger = final_hunger
                Student.is_hungry(self)

    def your_mood(self):
        print("Twój nastrój: ", self.mood)
        change = input("Czy chcesz go zmienić? [y]Tak, [n]Nie: ")
        if change == "y" or change.lower() == "y":
            mood = input("W jakim jesteś teraz nastroju?: ")
            print("Twój natrój: ", mood)
        else:
            print("Twój natrój to wciąż: ", self.mood)

    def your_will(self):
        if self.will == "Niska":
            print("Nie chce ci się nic robić. Chyba musisz się odprężyć.")
        elif self.will == "Średnia":
            print("Czujesz że chcesz coś zrobić, ale za chwilę. Chyba potrzebujesz motywacji.")
        elif self.will == "Wysoka":
            print("Czujesz motywację i chęci do pracy. Ciekawe na ile wystarczą...")
        else:
            print("Twoja wola jest określona jako: ",self.will)

    def how_long(self):
        remaining = 7 - self.which_semester
        print("Jesteś na ", self.which_semester, "semestrze.")
        print("Jeszcze ", remaining, "semestrów")
        if remaining >= 5:
            print("To dopiero początek...")
        elif 5 > remaining >= 3:
            print("Już połowa za tobą...")
        elif 3 > remaining >= 1:
            print("Już prawie koniec...")
        elif remaining == 0:
            print("Koniec koszmaru.")


student1 = Student("Dominik", "Nawrot", 22, "Ok", 60, "Wysoka", 2)
student1.id()
student1.is_hungry()
student1.dec_hunger()
student1.your_mood()
student1.your_will()
student1.how_long()

