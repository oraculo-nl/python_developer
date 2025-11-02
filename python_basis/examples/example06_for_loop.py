# eerste_stappen_5a.py
# -------------------
# For-loop voorbeeld — stemmen tellen voor favoriete films

print("Stem op je favoriete film!")
print("Opties: 1 = Actie, 2 = Komedie, 3 = Drama")

stemmen_actie = 0
stemmen_komedie = 0
stemmen_drama = 0

# Vraag 5 keer om een stem
for i in range(1, 6):
    stem = int(input(f"Stem {i}/5: "))
    if stem == 1:
        stemmen_actie += 1
    elif stem == 2:
        stemmen_komedie += 1
    elif stem == 3:
        stemmen_drama += 1
    else:
        print("Ongeldige keuze! Stem niet geteld.")

print("\nUitslag:")
print("Actie:", stemmen_actie)
print("Komedie:", stemmen_komedie)
print("Drama:", stemmen_drama)
print("Bedankt voor het stemmen!")
