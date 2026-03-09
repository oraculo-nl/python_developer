class Rekening:
    def __init__(self, saldo=0):
        self.__saldo = saldo
    def stort(self, bedrag):
        self.__saldo += bedrag
    def opname(self, bedrag, user):
        if user == "admin":
            self.__saldo -= bedrag
            print(f"opname van {bedrag} gelukt")
            print(f"nieuw saldo: {self.__saldo}")
        else:
            print("niet toegestaan")
    def saldo_opvragen(self):
        return self.__saldo

r = Rekening(100)
print(r.saldo_opvragen())
r.stort(25)
print(r.saldo_opvragen())
r.opname(10, "bill")
r.opname(1000, "admin")


print(r.saldo_opvragen())