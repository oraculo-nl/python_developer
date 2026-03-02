# create a function that simulates a die roll
import math
import random

print(math.sqrt(25))

for i in range(10):
    print(random.randint(1,10))

def roll_die(sides: int = 6) -> int:
    """Simuleert een dobbelsteenworp (standaard 6 zijden)."""
    if sides < 2:
        raise ValueError("A die must have at least 2 sides.")
    return random.randint(1, sides)

# voorbeeld
print(f"You rolled: {roll_die()}")
print(f"You rolled a 20-sided die: {roll_die(20)}")



