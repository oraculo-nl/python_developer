# Doel: __add__, __repr__, __eq__ voor een simpele Vector.

class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

v = Vector2D(1,2) + Vector2D(3,4)
print(v)                # Vector2D(4, 6)
print(v == Vector2D(4,6))
