class Bankrekening():
    aantal_bankrekeningen = 0
    def __init__(self):
        Bankrekening.aantal_bankrekeningen+=1
        self.__saldo=0
    def stort(self, bedrag):
        self.__saldo += bedrag
        print(f"gestort:{bedrag} nieuw saldo: {self.__saldo}")
    def opname(self, bedrag):
        if self.__saldo - bedrag < 0:
            print("niet genoeg saldo op de rekening")
        else:
            self.__saldo -= bedrag
            print(f"opgenomen: {bedrag} nieuwe saldo: {self.__saldo}")
    def saldo_opvragen(self):
        print (f"je saldo is:{self.__saldo}")
    def __repr__(self):
        return f"Bankrekening(saldo={self.__saldo})"
    def __str__(self):
        return f"saldo={self.__saldo}"

b = Bankrekening()

print(repr(b))
print(b)

# b.stort(100)
# b.saldo_opvragen()
# b.stort(200)
# b.opname(10)
# b.opname(1000)
# b.saldo_opvragen()

bankrekening2 = Bankrekening()

print(Bankrekening.aantal_bankrekeningen)