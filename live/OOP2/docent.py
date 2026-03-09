from live.OOP2.persoon import Persoon

class Docent(Persoon):
    def __init__(self, naam, leeftijd, vak):
        super().__init__(naam, leeftijd)
        self.vak = vak
    def __repr__(self):
        return f"Docent({self.naam}, {self.leeftijd}, {self.vak})"
    def __str__(self):
        return f"{self.naam} {self.leeftijd} {self.vak}"