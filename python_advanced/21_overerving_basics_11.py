# Doel: simpele subklasse die methode overschrijft.

class Dier:
    def __init__(self, naam):
        self.naam = naam
    def geluid(self):
        return "..."
    def lopen(self):
        print("loopt")

class Hond(Dier):
    def geluid(self):
        return "woef"

class Kat(Dier):
    def geluid(self):
        return "miauw"
    def lopen(self):
        print("loopt als een kat")
        super().lopen()

print(Hond("Rex").geluid())

k = Kat("Tommy")

k.lopen()

