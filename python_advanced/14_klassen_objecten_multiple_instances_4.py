# Doel: elke instantie heeft zijn eigen staat.

class Rekening:
    def __init__(self, houder, saldo=0):
        self.houder = houder
        self.saldo = saldo
    def stort(self, bedrag):
        self.saldo += bedrag

r1 = Rekening("Ali", 100)
r2 = Rekening("Bo", 50)
r1.stort(20)
print(r1.houder, r1.saldo)  # Ali 120
print(r2.houder, r2.saldo)  # Bo 50
