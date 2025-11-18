class Fiets():
    def __init__(self, merk, soort='Herenfiets'):
        self.__merk=merk
        self.__snelheid=0
        self.__soort=soort
    def trap_sneller(self, delta):
        self.__snelheid+=delta
    def rem(self, delta):
        self.__snelheid-=delta
    def get_merk(self):
        return self.__merk
    def get_snelheid(self):
        if user == 'Ali':
            return self.__snelheid



f = Fiets(merk="Batavus", soort="Damesfiets")

f.get_snelheid()

f.





print(f.snelheid)


