# Doel: __len__, __iter__, __call__ hooks laten zien.

class Agenda:
    def __init__(self, items=None):
        self._items = [] if items is None else list(items)
    def __len__(self):
        return len(self._items)
    def __iter__(self):
        return iter(self._items)
    def __call__(self, item):
        self._items.append(item)

a = Agenda(["meetup", "les"])
print(len(a))         # 2
for it in a:
    print("->", it)
a("code review")      # object is "callable"
print(len(a))         # 3
