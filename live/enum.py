prijzen = [4.5, 9.9, 2.5, 3.0]
totaal = 0
for i, p in enumerate(prijzen):
    print(f"Prijs {i}: €{p}")
    totaal += p
print(f"Totaal = €{totaal}")
