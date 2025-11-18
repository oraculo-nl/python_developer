# Doel: verschil laten zien; staticmethod heeft geen cls/self, classmethod krijgt cls.

class Rekentool:
    factor = 10

    @staticmethod
    def vermenigvuldig(a, b):
        return a * b

    @classmethod
    def maal_factor(cls, x):
        return x * cls.factor

print(Rekentool.vermenigvuldig(3, 4))  # 12
print(Rekentool.maal_factor(7))        # 70
