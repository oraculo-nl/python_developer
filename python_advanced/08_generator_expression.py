# 08_generator_expression.py
# Onderwerp: Generator expression (lazy evaluatie)

kwadraten_gen = (x * x for x in range(5))

if __name__ == "__main__":
    print("next(kwadraten_gen) ->", next(kwadraten_gen))
    print("rest ->", list(kwadraten_gen))
