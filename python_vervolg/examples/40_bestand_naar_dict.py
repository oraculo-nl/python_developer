import csv

with open("sample_data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)   # gebruikt de eerste rij als header
    rows = [row for row in reader]

# Voorbeeld: eerste record
print(rows[0])
# {'name': 'Alice', 'age': '30', 'city': 'Amsterdam'}