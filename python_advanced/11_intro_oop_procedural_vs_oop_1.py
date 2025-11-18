# Doel: laat het verschil zien tussen losse functies (procedureel) en OOP.

# Procedureel
merk = "Volvo"
snelheid = 0

def versnellen(delta):
    global snelheid
    snelheid += delta

versnellen(20)
print("Procedureel:", merk, snelheid)  # Volvo 20

# OOP
class Auto:
    def __init__(self, merk):
        self.merk = merk
        self.snelheid = 0
    def versnellen(self, delta):
        self.snelheid += delta

a = Auto("Volvo")
a.versnellen(20)
print("OOP:", a.merk, a.snelheid)      # Volvo 20
