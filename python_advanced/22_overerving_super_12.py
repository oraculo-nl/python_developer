# Doel: super() gebruiken om init van basisklasse aan te roepen.

class Dier:
    def __init__(self, naam):
        self.naam = naam

class Hond(Dier):
    def __init__(self, naam, ras):
        super().__init__(naam)
        self.ras = ras

h = Hond("Rex", "Labrador")
print(h.naam, h.ras)
