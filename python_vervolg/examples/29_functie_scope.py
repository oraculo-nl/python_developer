# Variabele scope
x = 10

def toon_getal():
    x = 5  # lokale variabele
    print("Binnen functie:", x)

toon_getal()
print("Buiten functie:", x)
