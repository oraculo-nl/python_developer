import csv

# Methode 1
with open("movies.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    total = sum(1 for _ in reader)
print('Methode 1:')
print("Totaal (incl. header):", total)
print("Aantal data-rijen:", total - 1)

# Methode 2
with open("movies.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    count = sum(1 for _ in reader)
print('Methode 2:')
print("Aantal data-rijen:", count)