# Vergelijk twee getallen en toon de grootste (of gelijk)
a = float(input("Eerste getal: "))
b = float(input("Tweede getal: "))
if a > b:
    print(f"{a} is groter dan {b}")


elif a < b:
    print(f"{a} is kleiner dan {b}")
else:
    print(f"{a} is gelijk aan {b}")
