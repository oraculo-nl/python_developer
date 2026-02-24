import statistics

personen  = {
    "Jim":24,
    "Sjon":30,
    "Kees":64
}

print (round(statistics.mean(personen.values()),1))

print(sum(personen.values())//len(personen))

print(sum((personen["Jim"], personen["Sjon"], personen["Kees"]))//3)

totaal=0
for leeftijd in personen.values():
    totaal +=leeftijd
gem_leeftijd=totaal/len(personen)
print(round(gem_leeftijd,1))

