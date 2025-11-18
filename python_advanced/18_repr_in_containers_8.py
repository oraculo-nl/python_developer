# Doel: laten zien dat containers __repr__ gebruiken van hun elementen.

class Film:
    def __init__(self, titel, score):
        self.titel = titel
        self.score = score
    def __repr__(self):
        return f"Film(titel={self.titel!r}, score={self.score})"

films = [Film("A", 8.0), Film("B", 7.2)]
print(films)  # gebruikt __repr__ van Film voor elk element
