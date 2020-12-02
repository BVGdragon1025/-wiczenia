tup_a = tuple(input("Podaj pierwszy wyraz: "))
tup_b = tuple(input("Podaj drugi wyraz: "))

list_a = list(tup_a)
list_b = list(tup_b)

list_a.sort()
list_b.sort()

print(list_a, list_b)

if list_a == list_b:
    print("Anagram")
else:
    print("Nie anagram")
