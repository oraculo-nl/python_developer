# Doel: basis class, __init__, methoden, instanties.

class Fiets:
    def __init__(self, merk, snelheid=0):
        self.merk = merk
        self.snelheid = snelheid
    def trap_sneller(self, delta):
        self.snelheid += delta
    def rem(self, delta):
        self.snelheid = max(0, self.snelheid - delta)

f = Fiets("Gazelle")
f.trap_sneller(15)
f.rem(5)
print(f.merk, f.snelheid)  # Gazelle 10
