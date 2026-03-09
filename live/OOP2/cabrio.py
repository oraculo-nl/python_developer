from live.OOP2.auto import Auto


class Cabrio(Auto):
    def versnellen(self, delta):
        self.snelheid += 2 * delta