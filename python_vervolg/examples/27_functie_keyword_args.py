# Keyword arguments gebruiken
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(naam="Lisa", leeftijd=22, stad="Zwolle")
