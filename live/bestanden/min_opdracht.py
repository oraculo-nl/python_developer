'''
Schrijf een programma dat:
Een lijst met namen en cijfers bevat, bijv. [("Anna", 7.5), ("Rik", 8.2),
("Mila", 6.9)]
De gegevens in een CSV-bestand opslaat met de kolommen naam en cijfer
Het CSV-bestand opnieuw opent en de gemiddelde score berekent
Het gemiddelde op het scherm print met een f-string
'''
import csv

gegevens = [("Anna", 7.5), ("Rik", 8.2), ("Mila", 6.9)]
bestandsnaam = "scores.csv"

# 1) Opslaan naar CSV (kolommen: naam, cijfer)
with open(bestandsnaam, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["naam", "cijfer"])
    writer.writeheader()
    for naam, cijfer in gegevens:
        writer.writerow({"naam": naam, "cijfer": cijfer})

# 2) CSV opnieuw openen en gemiddelde berekenen
cijfers = []
with open(bestandsnaam, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cijfers.append(float(row["cijfer"]))

gemiddelde = sum(cijfers) / len(cijfers) if cijfers else 0

# 3) Print met f-string
print(f"Het gemiddelde cijfer is: {gemiddelde:.2f}")