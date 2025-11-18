# Doel: intuïtieve analogie van objecten met eigenschappen en gedrag.

class Lamp:
    def __init__(self, kleur):
        self.kleur = kleur
        self.aan = False
    def schakel(self):
        self.aan = not self.aan

l = Lamp("wit")
print("Lamp aan?", l.aan)
l.schakel()
print("Lamp aan?", l.aan)
