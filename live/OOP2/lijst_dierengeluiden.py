from dier import Dier
from hond import Hond
from vogel import Vogel

dieren = [Hond(), Vogel()]

for d in dieren:
    print(d.geluid())