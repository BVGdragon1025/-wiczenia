a = list(input("Podaj ciąg liczb: "))

tab_r = a[::-1]
# print(a)
# print(tab_r)
if tab_r == a:
    print("Palindrom, ale i tak wydrukuję rezultat: ", tab_r)
else:
    print("Odwrócony będzie wygladać tak: ", tab_r)
