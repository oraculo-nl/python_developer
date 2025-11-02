# Door een dictionary itereren
prijzen = {"appel": 0.8, "banaan": 1.0, "kers": 2.5}
for fruit, prijs in prijzen.items():
    print(f"Een {fruit} kost {prijs:.2f} euro")
