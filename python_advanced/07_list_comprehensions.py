# 07_list_comprehensions.py
# Onderwerp: List comprehensions (transformeren + filteren)

getallen = [1, 2, 3, 4, 5, 6]

kwadraten = [x * x for x in getallen]
even_kwadraten = [x * x for x in getallen if x % 2 == 0]

if __name__ == "__main__":
    print("kwadraten:", kwadraten)
    print("even_kwadraten:", even_kwadraten)
