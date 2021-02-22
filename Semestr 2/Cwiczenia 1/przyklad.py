class Parrot:
    species = "ptak"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} śpiewa {}".format(self.name, song)

    def dance(self):
        return "{} tańczy".format(self.name)


blu = Parrot("Blu", 10)
ara = Parrot("Ara", 15)
red = Parrot("Red", 8)
winston = Parrot("Winston", 12)

print("Blu jest {}".format(blu.__class__.species))
print("Ara jest {}".format(ara.__class__.species))
print("Red jest {}".format(red.__class__.species))
print("Winston jest {}".format(winston.__class__.species))

print("{} ma {} lat".format(blu.name, blu.age))
print("{} ma {} lat".format(ara.name, ara.age))
print("{} ma {} lat".format(red.name, red.age))
print("{} ma {} lat".format(winston.name, winston.age))

print(blu.sing("Happy"))
print(blu.dance())
print(blu.dance())
