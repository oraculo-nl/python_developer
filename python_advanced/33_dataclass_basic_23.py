# Doel: dataclass basis met automatische __init__, __repr__, __eq__.

from dataclasses import dataclass

@dataclass
class Punt:
    x: int
    y: int

p1 = Punt(2,5)
p2 = Punt(2,5)
print(p1)           # Punt(x=2, y=5)
print(p1 == p2)     # True
