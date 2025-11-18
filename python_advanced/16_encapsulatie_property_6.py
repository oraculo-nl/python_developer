# Doel: property als moderne vervanger van getter/setter.

class Temperatuur:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, waarde):
        if waarde < -273.15:
            raise ValueError("Te koud")
        self._celsius = waarde

t = Temperatuur(20)
t.celsius = 22
print(t.celsius)

t.celsius=30
print(t.celsius)