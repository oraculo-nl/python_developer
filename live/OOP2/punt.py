from dataclasses import dataclass

@dataclass
class Punt:
    x: int
    y: int

p1 = Punt(2,5)
print(p1)
print(p1.x)