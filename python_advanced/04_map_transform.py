# 04_map_transform.py
# Onderwerp: map() voor transformatie

getallen = [1, 2, 3, 4]
kwadraten = list(map(lambda x: x * x, getallen))
verdubbeld = list(map(lambda x: x * 2, getallen))

if __name__ == "__main__":
    print("kwadraten:", kwadraten)
    print("verdubbeld:", verdubbeld)
