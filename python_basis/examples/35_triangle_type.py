# Drie zijden -> type driehoek (geldig, gelijkzijdig, gelijkbenig, ongelijkzijdig)
a = float(input("Zijde a: "))
b = float(input("Zijde b: "))
c = float(input("Zijde c: "))

# Driehoeksongelijkheid
geldig = (a + b > c) and (a + c > b) and (b + c > a)
if not geldig:
    print("Geen geldige driehoek")
else:
    if a == b == c:
        print("Gelijkzijdig")
    elif a == b or a == c or b == c:
        print("Gelijkbenig")
    else:
        print("Ongelijkzijdig")
