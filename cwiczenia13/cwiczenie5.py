#zadanie 5, zrobione przez Danilla
def BMI(weight, height):
    BMI = (weight) / (height * height)
    print(BMI)
    if BMI <= 18.5:
        print("Masz niedowagę")
    elif BMI > 18.5 and BMI <= 24.99:
        print("Twoja waga jest prawidłowa")
    elif BMI > 25.00:
        print("Masz nadwagę!!!")
    print("Teraz wiesz co musisz robić.")

weight = float(input("Podaj wagę w kilogramach: "))
height = float(input("Podaj wzrost w metrach: "))
print(BMI(weight, height))