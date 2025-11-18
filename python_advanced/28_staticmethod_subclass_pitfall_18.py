# Doel: laten zien dat staticmethod class data niet dynamisch ziet (hardcoded classnaam).
# Tip: gebruik classmethod voor dynamische resolutie.

class Auto:
    wielen = 4
    @staticmethod
    def toon_wielen_hardcoded():
        print(Auto.wielen)  # vast naar Auto

class Truck(Auto):
    wielen = 6

Auto.toon_wielen_hardcoded()   # 4
Truck.toon_wielen_hardcoded()  # 4 (niet 6)
print(Auto.wielen)
print(Truck.wielen)