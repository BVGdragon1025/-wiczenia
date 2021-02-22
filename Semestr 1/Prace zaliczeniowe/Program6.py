# Krotka z literkami, by ładnie wyświetlało użytkownikowi znaki temperatur
# Wartości bo backslashu to znak stopni w Unicode. Kelwin nie ma, bo kelwiny to kelwiny
# Do sprawdzenia - czemu kiedy przeliczam z Newtonów na Celsjusze, to przy 100 Celsjuszach mówi, że woda jest ciekła
conv_names = ("\u00b0C", "\u00b0F", "K", "\u00b0N")


# Menu wyboru pierwszej temperatury
def conv1_menu():
    print("Wybierz z czego chcesz konwertować: ")
    print("[1] Celsjusze ")
    print("[2] Fahrenheity ")
    print("[3] Kelwiny ")
    print("[4] Skala Newtona ")
    choice1 = input("Wybierz: ")
    return choice1


# Menu wyboru drugiej temperatury
def conv2_menu():
    print("Wybierz na co chcesz konwertować: ")
    print("[1] Celsjusze ")
    print("[2] Fahrenheity ")
    print("[3] Kelwiny ")
    print("[4] Skala Newtona ")
    choice2 = input("Wybierz: ")
    return choice2


# Konwersja z stopni Celsjusza.
def conv_c(choice2, temp):
    if choice2 == "2":
        conv_temp = (temp * 1.8)+32
    elif choice2 == "3":
        conv_temp = temp + 273.15
    else:
        conv_temp = temp * (33/100)
    return conv_temp


# Konwersja z stopni Fahrenheita.
def conv_f(choice2, temp):
    if choice2 == "1":
        conv_temp = (temp - 32)/1.8
    elif choice2 == "3":
        conv_temp = (temp + 459.67)*(5/9)
    else:
        conv_temp = (temp-32)*(11/60)
    return conv_temp


# Konwersja z Kelwinów.
def conv_k(choice2, temp):
    if choice2 == "1":
        conv_temp = temp - 273.15
    elif choice2 == "2":
        conv_temp = (temp*(9/5)) - 459.67
    else:
        conv_temp = (temp-273.15)*(33/100)
    return conv_temp


# Konwersja z skali Newtona.
def conv_n(choice2, temp):
    if choice2 == "1":
        conv_temp = (temp*100)/33
    elif choice2 == "2":
        conv_temp = (temp*(60/11)) + 32
    else:
        conv_temp = (temp*(100/33))+273.15
    return conv_temp


# Wyświetlenie, czy woda zamarza, czy wrze lub czy nic się z nią nie dzieje
# Wiem, pewnie da się to zapisać lepiej. Na ten moment jednak nie wiem jak.
def high_low_temp(choice2, conv_temp):
    if choice2 == "1":
        if conv_temp <= 0:
            print("Woda zamarza")
        elif conv_temp >= 100:
            print("Woda wrze")
        else:
            print("Woda jest w stanie ciekłym")
    elif choice2 == "2":
        if conv_temp <= 32:
            print("Woda zamarza")
        elif conv_temp >= 212:
            print("Woda wrze")
        else:
            print("Woda jest w stanie ciekłym")
    elif choice2 == "3":
        if conv_temp <= 273.15:
            print("Woda zamarza")
        elif conv_temp >= 373.15:
            print("Woda wrze")
        else:
            print("Woda jest w stanie ciekłym")
    elif choice2 == "4":
        if conv_temp <= 0:
            print("Woda zamarza")
        elif conv_temp >= 33:
            print("Woda wrze")
        else:
            print("Woda jest w stanie ciekłym")
    else:
        print("Błąd!")


# Serce programu, sprawdzenie czy user nie wybrał tej samej temperatury i wywołanie odpowiednich funkcji.
# Plus jeszcze wypisanie skonwertowanej temperatury
# Pewnie da się to zrobić lepiej, ale hej, działa :)
def conv(choice1, choice2):
    if choice1 == choice2:
        print("Nie możesz konwertować tej samej jednostki na nią samą!")
    else:
        if choice1 == "1":
            temp = float(input("Podaj temperaturę w %s: " % conv_names[int(choice1)-1]))
            conv_c(choice2, temp)
            print("Temperatura po konwersji wynosi: ", conv_c(choice2, temp), conv_names[int(choice2)-1])
            high_low_temp(choice2, conv_c(choice2, temp))
        elif choice1 == "2":
            temp = float(input("Podaj temperaturę w %s: " % conv_names[int(choice1)-1]))
            conv_f(choice2, temp)
            print("Temperatura po konwersji wynosi: ", conv_f(choice2, temp), conv_names[int(choice2)-1])
            high_low_temp(choice2, conv_c(choice2, temp))
        elif choice1 == "3":
            temp = float(input("Podaj temperaturę w %s: " % conv_names[int(choice1)-1]))
            conv_k(choice2, temp)
            print("Temperatura po konwersji wynosi: ", conv_k(choice2, temp), conv_names[int(choice2)-1])
            high_low_temp(choice2, conv_c(choice2, temp))
        elif choice1 == "4":
            temp = float(input("Podaj temperaturę w %s: " % conv_names[int(choice1)-1]))
            conv_n(choice2, temp)
            print("Temperatura po konwersji wynosi: ", conv_n(choice2, temp), conv_names[int(choice2)-1])
            high_low_temp(choice2, conv_c(choice2, temp))
        else:
            print("Brak takiej jednostki. Jeszcze.")


# Main, bym nie musiał wypisywać wszystkiego osobno
def main():
    conv(conv1_menu(), conv2_menu())


# Wywołanie maina. Tyle.
main()
