# Doel: object-binnen-object (has-a).

class Motor:
    def __init__(self, vermogen):
        self.vermogen = vermogen

class Auto:
    def __init__(self, merk, motor):
        self.merk = merk
        self.motor = motor

a = Auto("Volvo", Motor(110))
print(a.merk, a.motor.vermogen)
