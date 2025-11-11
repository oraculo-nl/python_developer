# Gebruik functies uit utils.py (zelfde map)
import utils

print(utils.groet("Sanne"))
for n in range(5):
    print(n, "even?" , utils.is_even(n))
