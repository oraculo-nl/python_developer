# eerste_stappen_5c.py
# -------------------
# While-loop met break — snacks bestellen tot de gebruiker 'stop' typt

print("Welkom bij de bioscoop-snackbar!")
print("Typ de naam van een snack om deze toe te voegen.")
print("Typ 'stop' als je klaar bent.\n")

bestellingen = []

while True:
    snack = input("Voeg een snack toe: ").lower()
    if snack == "stop":
        break
    elif snack == "":
        print("Geen invoer gedetecteerd, probeer opnieuw.")
    else:
        bestellingen.append(snack)
        print(f"'{snack}' toegevoegd aan je bestelling.")

print("\nJe hebt de volgende snacks besteld:")
for snack in bestellingen:
    print("-", snack.capitalize())

print("\nVeel plezier met de film!")
