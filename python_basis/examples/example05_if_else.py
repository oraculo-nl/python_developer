# eerste_stappen_4.py
# -------------------
# If, elif en else — thema: filmavond

print("Welkom bij de bioscoop!")

# Vraag basisinformatie
naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))

print(f"Leuk dat je er bent, {naam}!")

# Bepaal ticketprijs op basis van leeftijd
if leeftijd < 12:
    prijs = 6.0
    categorie = "kind"
elif leeftijd < 18:
    prijs = 8.5
    categorie = "tiener"
elif leeftijd >= 65:
    prijs = 7.0
    categorie = "senior"
else:
    prijs = 10.0
    categorie = "volwassene"

# let op, je kunt speciale karakters toevoegen \n betekent een nieuwe regel
print(f"\nJe valt in de categorie: {categorie}")
print(f"Ticketprijs: €{prijs:.2f}")

# Extra: korting met kortingscode
print()
korting = input("Heb je een kortingscode? (ja/nee) ").lower()
if korting == "ja":
    prijs = prijs * 0.9
    print("Korting toegepast! (10%)")

print(f"Te betalen bedrag: €{round(prijs, 2)}")

print("\nVeel plezier met de film!")
