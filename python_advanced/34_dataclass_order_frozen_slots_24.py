# Doel: extra opties: order=True, frozen=True, slots=True (Python 3.10+).

from dataclasses import dataclass

@dataclass(order=True, frozen=True, slots=True)
class Student:
    naam: str
    score: int

s1 = Student("Ali", 8)
s2 = Student("Bo", 9)
print(s1 < s2)     # True door order=True
# s1.score = 10    # zou een fout geven door frozen=True
