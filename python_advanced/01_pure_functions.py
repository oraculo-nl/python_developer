# 01_pure_functions.py
# Onderwerp: Pure functies (geen globals, geen side effects)

def optel(a, b):
    # Pure functie: alleen afhankelijk van input, geen bijwerkingen
    return a + b

def som_van_kwadraten(getallen):
    # Nog een pure functie
    totaal = 0
    for x in getallen:
        totaal += x * x
    return totaal

if __name__ == "__main__":
    print("optel(2, 3) ->", optel(2, 3))
    print("som_van_kwadraten([1, 2, 3]) ->", som_van_kwadraten([1, 2, 3]))
