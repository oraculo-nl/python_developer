# Oppervlakte en omtrek van een cirkel
import math
r = float(input("Straal (in meters): "))
opp = math.pi * r ** 2
omt = 2 * math.pi * r
print(f"Voor r = {r} m: oppervlakte = {opp:.3f} m², omtrek = {omt:.3f} m")
