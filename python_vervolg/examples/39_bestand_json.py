# JSON-bestand lezen en schrijven
import json

data = {"naam": "Sara", "leeftijd": 25}

# Schrijven
with open("data.json", "w") as f:
    json.dump(data, f)

# Lezen
with open("data.json", "r") as f:
    geladen = json.load(f)

print(type(geladen))
print(geladen)
