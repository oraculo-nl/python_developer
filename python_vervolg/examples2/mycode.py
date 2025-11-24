

def do_something(a,b):
    return a+b

class Auto():
    MAX_SPEED = 180
    def __init__(self, speed, saldo=0):
        self.speed = speed
    def geefGas(self, snelheid):
        if self.speed+snelheid <= self.MAX_SPEED:
            self.speed+=snelheid
        return self.speed



a = Auto(100)
print(a.geefGas(40))
