post_code = input("Podaj kod pocztowy (bez myślników): ")
try:
    if len(post_code) != 5:
        print("Kod jest zbyt długi lub zbyt krótki")
    elif post_code is not int:
        print("Brak cyfr, lub dałeś myślnik")
    else:
        with open("kodypocztowe.txt", "a") as write_postal:
            write_postal.write(post_code + "\n")
            print("Kod pocztowy dodany!")
except FileNotFoundError:
    with open("kodypocztowe.txt", "x") as create_file:
        create_file.write(post_code + "\n")
        print("Kod pocztowy dodany!")
