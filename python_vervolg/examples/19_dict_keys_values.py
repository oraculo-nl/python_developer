# Sleutels en waarden ophalen
boek = {"titel": "1984", "auteur": "George Orwell", "jaar": 1949}
# print(boek.keys())
# print(boek.values())
# values = boek.values()

for k, v in boek.items():
    print("type sleutel:",type(k), "type waarde:", type(v))
