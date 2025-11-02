# Werken met floats
a = 0.1 + 0.2
print(a)  # kleine afrondingsfout mogelijk

# Afronden
print(round(a, 2))

# Optellen en vermenigvuldigen
prijs = 19.99
aantal = 3
totaal = prijs * aantal
print("Totaalprijs:", round(totaal, 2), "euro")
