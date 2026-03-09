class Auto:
    def __init__(self, merk):
        self.__merk = merk
        self.snelheid = 0
    def versnellen(self, snelheid):
        self.snelheid += snelheid
    def remmen(self,snelheid):
        if self.snelheid - snelheid < 0:
            self.snelheid = 0
        else:
            self.snelheid -= snelheid
    def get_merk(self):
        return self.__merk
    def __repr__(self):
        return f"Auto({self.__merk}, {self.snelheid})"
    def __str__(self):
        return f"{self.__merk} {self.snelheid}"