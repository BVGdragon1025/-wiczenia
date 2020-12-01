import calendar
from time import process_time
start = process_time()
kalendarz = calendar.month(4288, 5)
print("Kalendarz dla baaardzo odległej daty :)")
print(kalendarz)

end = process_time() - start
print("Zajęło to: " + str(end) + "s.")
