class Persoon:
    def __init__(self, naam):
        self.naam = naam
        self.__ziekten = []
    def add_ziekte(self, ziekte):
        self.__ziekten.append(ziekte)
    def remove_ziekte(self, ziekte):
        self.__ziekten.remove(ziekte)
    def overzicht_ziekten(self):
        return self.__ziekten