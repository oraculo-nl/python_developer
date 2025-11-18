# Doel: skelet voor Bibliotheekbeheer met een kleine bug om te spotten.

class Boek:
    def __init__(self, titel, auteur):
        self.titel = titel
        self.auteur = auteur
        self.uitgeleend = False
    def __repr__(self):
        status = "uit" if self.uitgeleend else "aanwezig"
        return f"Boek({self.titel!r}, {self.auteur!r}, {status})"

class Bibliotheek:
    def __init__(self):
        self.boeken = []
    def voeg_toe(self, boek):
        self.boeken.addend(boek)  # BUG: methode bestaat niet

bib = Bibliotheek()
# Laat studenten de bug fixen naar: self.boeken.append(boek)
