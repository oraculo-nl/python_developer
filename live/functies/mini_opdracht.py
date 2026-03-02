"""
Schrijf een programma dat:
- een lijst met cijfers bevat (bijv. [6.5, 8.0, 7.3, 9.1])
- een functie gemiddelde(lijst) heeft die het gemiddelde teruggeeft
- een functie beoordeling(gem) heeft die:
  ▶ “Onvoldoende” print bij < 5.5
  ▶ “Voldoende” bij 5.5-7.9
  ▶ “Goed” bij >= 8
Gebruik f-strings om de resultaten netjes te tonen.
"""

def gemiddelde(getallen: list[float]) -> float:
    if not getallen:
        return 0
    return sum(getallen) / len(getallen)

def beoordeling(gem: float) -> str:
    if gem < 5.5:
        return "Onvoldoende"
    elif gem < 8:
        return "Voldoende"
    else:
        return "Goed"

cijfers = [6.5, 8.0, 7.3, 9.1]
gem = gemiddelde(cijfers)

print(f"Cijfers: {cijfers}")
print(f"Gemiddelde: {gem:.1f}")
print(f"Beoordeling: {beoordeling(gem)}")


