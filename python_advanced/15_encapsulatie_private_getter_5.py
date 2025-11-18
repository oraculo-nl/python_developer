# Doel: name mangling __saldo en een getter laten zien.

class Bankrekening:
    def __init__(self, saldo=0):
        self.__saldo = saldo
    def stort(self, bedrag):
        self.__saldo += bedrag
    def get_saldo(self):
        return self.__saldo

r = Bankrekening(100)
r.stort(25)
print(r.get_saldo())           # 125
print(r._Bankrekening__saldo)  # technisch bereikbaar (name mangling)
