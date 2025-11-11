# Een bestand lezen
with open("data/voorbeeld.txt", "r") as f:
    inhoud = f.read()
print("Inhoud van het bestand:")
print(inhoud)
