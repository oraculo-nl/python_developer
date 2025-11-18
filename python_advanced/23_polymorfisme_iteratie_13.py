# Doel: zelfde methode-naam, ander gedrag; lijst met gemengde objecten.

class Dier:
    def geluid(self):
        return "..."

class Hond(Dier):
    def geluid(self):
        return "woef"

class Kat(Dier):
    def geluid(self):
        return "miauw"

dieren = [Hond(), Kat(), Hond()]
print([d.geluid() for d in dieren])
