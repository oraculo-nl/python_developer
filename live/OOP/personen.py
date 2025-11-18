# class Persoon():
#     def __init__(self, naam, leeftijd):
#         self.naam = naam
#         self.leeftijd = leeftijd
#         self.__aanwezig = False
#     def is_aanwezig(self):
#         return self.__aanwezig
#     def checkt_in(self):
#         self.__aanwezig = True
#     def checkt_out(self):
#         self.__aanwezig = False
#
# class Docent(Persoon):
#     aantal_docenten = 0
#     def __init__(self, naam, leeftijd, vak):
#         super().__init__(naam, leeftijd)
#         self.vak = vak
#         Docent.aantal_docenten+=1
#
# class Student(Persoon):
#     def __init__(self, naam, leeftijd, studentennummer):
#         super().__init__(naam, leeftijd)
#         self.studentennummer = studentennummer
#
#
# lijst = [Docent("Jan", 50, "geschiedenis"),
#          Docent("Piet", 30, "Aardrijkskunde"),
#         Docent("Arnold", 40, "Gym"),
#          Student("Klaas", 20, 827348972)]
#
# for persoon in lijst:
#     print(persoon.naam)
#     persoon.checkt_in()
#     if persoon.leeftijd == 20:
#         persoon.checkt_out()
#
#
# print("het aantal docenten is momenteel:", Docent.aantal_docenten)
#
# for persoon in lijst:
#     print(persoon.is_aanwezig())
#
# class Verkooporder():
#     def __init__(self):
#         self.orderregels = []
#
# class Verkooporderregel():
#     def __init__(self):
#         pass
#

class Klas():
    totaal = 0
    def __init__(self, lijst):
        self.studenten = list(lijst)
        Klas.totaal+=1
    def __add__(self, other):
        self.studenten.append(other.studenten)
    @staticmethod
    def plustotaal():
        Klas.totaal+=1

leerlingen = ["jan","piet"]

k = Klas(leerlingen)
k2 = Klas(leerlingen)
print(k.studenten)

leerlingen.append("arendjan")

print(k.studenten)

print(1+1)

14:30