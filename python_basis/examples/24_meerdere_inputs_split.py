# Meerdere inputs op één regel, gescheiden door spaties
regel = input("Voer drie gehele getallen in, gescheiden door spaties: ")
a_str, b_str, c_str = regel.split()
a, b, c = int(a_str), int(b_str), int(c_str)
print(f"Invoer: {a}, {b}, {c}")
print(f"Som = {a + b + c}, Product = {a * b * c}")
