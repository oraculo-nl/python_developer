# Doel: zelfde methode-naam, ander gedrag; lijst met gemengde objecten.

class Dier:
    def geluid(self):
        return "..."

class Hond(Dier):
    def geluid(self):
        return "woef"
    def kwispelen(self):
        print("Kwispelen")

class Kat(Dier):
    def geluid(self):
        return "miauw"

class Schildpad(Dier):
    def geluid(self):
        return "zucht"
#
dieren = [Hond(), Kat(), Hond(), Schildpad()]
#
#
#
# print([d.geluid() for d in dieren])
#
# for d in dieren:
#     print(d.geluid())
#     if isinstance(d, Hond):
#         d.kwispelen()


from gebruik_dieren import test_dieren

test_dieren(dieren)
