# 06_reduce_sum.py
# Onderwerp: reduce() voor aggregatie (samenvatten tot 1 waarde)

from functools import reduce

getallen = [1, 2, 3, 4]

som = reduce(lambda a, b: a + b, getallen)
product = reduce(lambda a, b: a * b, getallen)

if __name__ == "__main__":
    print("som:", som)
    print("product:", product)
