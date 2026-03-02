def hello(naam='onbekend'):
    print(naam)
    return

def vermenigvuldig(x, y):
    return x * y

lijst = [(1,2),(3,4),(5,6),(7,8)]

for x, y in lijst:
    print(vermenigvuldig(x, y))

def is_even(x):
    return x % 2 == 0

def is_even2(x):
    if x % 2 == 0:
        return True
    else:
        return False

def gemiddelde(getallen):
    return sum(getallen) / len(getallen)


def herhaal(tekst, aantal_keren):
    return (tekst * aantal_keren)

print(herhaal("hallo \n", 3))

print(herhaal("andere tekst \n", 2))