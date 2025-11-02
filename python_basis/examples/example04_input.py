# eerste_stappen_3.py
# -------------------
# Werken met input() en typecasting — thema: reizen

print("Welkom bij: je eerste reisberekening!")

# Vraag de gebruiker om wat gegevens
naam = input("Wat is je naam? ")
print(f"Hallo, {naam}!") # let op hier wordt een variabele in een string gestopt, zgn f-string


print()
# Vraag afstand en tijd (strings → floats)
afstand = float(input("Hoeveel kilometer moet je reizen? "))
tijd = float(input("Hoeveel uur duurt dat ongeveer? "))

# Bereken gemiddelde snelheid
snelheid = afstand / tijd

print(f"Je reist met een gemiddelde snelheid van {round(snelheid, 1)} km/u.")

print()
# Vraag brandstofverbruik
verbruik = float(input("Hoeveel liter brandstof verbruik je per 100 km? "))

# Bereken totale verbruikte brandstof
totaal_verbruik = (afstand / 100) * verbruik

print(f"Je verbruikt ongeveer {round(totaal_verbruik, 2)} liter brandstof.")

print()
print("Goed gedaan! Je hebt input, typecasting en berekeningen gebruikt.")
