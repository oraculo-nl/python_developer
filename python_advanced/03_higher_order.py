# 03_higher_order.py
# Onderwerp: Higher-order functies (functie als argument/returnwaarde)

def maak_vermenigvuldiger(factor):
    def inner(x):
        return x * factor
    return inner

def toepassen(func, waarde):
    return func(waarde)

if __name__ == "__main__":
    keer3 = maak_vermenigvuldiger(3)
    print("keer3(10) ->", keer3(10))
    print("toepassen(keer3, 7) ->", toepassen(keer3, 7))
