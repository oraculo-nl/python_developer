# Doel: filteren en sorteren van objecten met list comprehensions en sorted().

class Student:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten
    def uitschrijven(self):
        print("schrijft uit")

klas = [Student("Ali", 78), Student("Bo", 92), Student("Chen", 85)]
geslaagd = [s for s in klas if s.punten >= 80]
gesorteerd = sorted(klas, key=lambda s: s.punten, reverse=True)

print([s.naam for s in geslaagd])         # ['Bo', 'Chen']
print([(s.naam, s.punten) for s in gesorteerd])

for s in geslaagd:
    print(s.naam)
    s.uitschrijven()

11:25