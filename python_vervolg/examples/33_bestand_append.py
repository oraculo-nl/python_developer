# Tekst toevoegen aan een bestaand bestand
with open("voorbeeld.txt", "a") as f:
    f.write("\nNog een extra regel toegevoegd.")
print("Regel toegevoegd.")
