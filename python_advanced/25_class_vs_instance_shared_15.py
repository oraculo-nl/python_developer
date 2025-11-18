# Doel: class attribuut is gedeeld; instance attribuut is uniek.

class Teller:
    aantal = 0  # class attribuut
    def __init__(self):
        Teller.aantal += 1
        self.id = Teller.aantal  # instance attribuut

a = Teller(); b = Teller()
print("klassikaal:", Teller.aantal)  # 2
print("instanties:", a.id, b.id)     # 1 2
