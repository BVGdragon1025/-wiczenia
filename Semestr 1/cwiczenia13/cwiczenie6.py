def dec_to_bin(decimal):
    binary = bin(decimal)
    return binary


def dec_to_hex(decimal):
    hexdec = hex(decimal)
    return hexdec


def bin_to_hex(binary):
    binhex = hex(binary)
    return binhex


def hex_to_bin(hexa):
    hexbin = bin(hexa)
    return hexbin


def dec_to_oct(decimal):
    decoct = oct(decimal)
    return decoct


a = int(input("Podaj liczbę: "))
print("Postać binarna: ", dec_to_bin(a))
print("Postać szesnastkowa: ", dec_to_hex(a))
print("Postać ósemkowa: ", dec_to_oct(a))
b = int(input("Wpisz liczbę w formie binarnej (01): "), 2)
print("Postać z binarnej na szesnastkową: ", bin_to_hex(b))
c = int(input("Wpisz liczbę w formie szesnastkowej (0-9 oraz a-f): "), 16)
print("Postać z szesnastkowej na binarną: ", hex_to_bin(c))
