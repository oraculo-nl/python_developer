# Doel: verschil tussen __repr__ (debug) en __str__ (gebruiker).

class Boek:
    def __init__(self, titel, auteur):
        self.titel = titel
        self.auteur = auteur
    def __repr__(self):
        return f"Boek(titel={self.titel!r}, auteur={self.auteur!r})"
    def __str__(self):
        return f"{self.titel} - {self.auteur}"

b = Boek("Python 101", "Anna")
print(repr(b))  # Debug
print(b)        # Voor gebruiker
