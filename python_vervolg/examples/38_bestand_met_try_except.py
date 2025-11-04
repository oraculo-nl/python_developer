# Bestanden met foutafhandeling
try:
    with open("niet_bestaand.txt", "r") as f:
        inhoud = f.read()
except FileNotFoundError:
    print("Bestand niet gevonden!")
