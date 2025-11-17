lijst = list(range(1,11))
#
#
# lijst2 = []
# for getal in lijst:
#     if getal % 2 == 0:
#         lijst2.append(getal * getal)
# # print(lijst2)

# lijst3 = [getal * getal for getal in lijst if getal % 2 == 0]
#
# print(lijst3)

# def som_even_kwadraten():
#     lijst3 = [getal * getal for getal in lijst if getal % 2 == 0]
#     return lijst3
#
# print(som_even_kwadraten())
#


def kwadrateren(x):
    return x * x

lijst5 = []

# for getal in lijst:
#     print(kwadrateren(getal))
#     lijst5.append(kwadrateren(getal))
#
# print(lijst5)

# f = lambda x: x * x
# print(list(map(f, lijst)))
# f2 = lambda x: x % 2 == 0
# print(list(filter(f2, lijst)))
from functools import reduce
def functie_kwadrateren(lijst):
    f = lambda x: x * x
    # print(list(map(f, lijst)))
    f2 = lambda x: x % 2 == 0
    f3 = lambda x,y: x+y
    l = list(filter(f2, lijst))
    l2 = list(map(f, l))
    print(reduce(f3,l2))

functie_kwadrateren([1,2,3,4])
functie_kwadrateren([3,4,5,6])

13:15
