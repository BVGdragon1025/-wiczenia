class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hejka to ja {self.name} twoj kotelek. Mam {self.age} lat")

    def make_sound(self):
        print("Miau")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hejka wabię się {self.name}. I mam {self.age} lat")

    def make_sound(self):
        print("Hau")


cat1 = Cat("Mruczuś", 2.5)
dog1 = Dog("Rex", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
