from live.OOP2.auto import Auto

class RaceAuto(Auto):
     def versnellen(self, delta):
         self.snelheid += 50 * delta