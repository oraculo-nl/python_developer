# Doel: simpele subklasse die methode overschrijft.

class Dier:
    def __init__(self, naam):
        self.naam = naam
    def geluid(self):
        return "..."

class Hond(Dier):
    def geluid(self):
        return "woef"

print(Hond("Rex").geluid())
