class Ja:
    def __init__(self, age=18):
        self.__age = age

    # getter
    def get_age(self):
        return self.__age

    # setter
    def set_age(self, x):
        self.__age = x


dominik = Ja()

dominik.set_age(22)
print(dominik.get_age())
print(dominik.__age)
