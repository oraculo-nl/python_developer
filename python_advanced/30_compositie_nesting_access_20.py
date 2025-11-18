# Doel: dieper geneste toegang en doorgeven van gedrag.

class Adres:
    def __init__(self, straat, stad):
        self.straat = straat
        self.stad = stad

class Persoon:
    def __init__(self, naam, adres):
        self.naam = naam
        self.adres = adres
    def verhuis(self, nieuwe_stad):
        self.adres.stad = nieuwe_stad

p = Persoon("Bo", Adres("Kerkstraat", "Zwolle"))
print(p.adres.straat, p.adres.stad)
p.verhuis("Lelystad")
print(p.adres.straat, p.adres.stad)
