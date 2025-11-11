import csv

with open("sample_data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)   # gebruikt de eerste rij als header
    rows = [row for row in reader]

# Voorbeeld: eerste record
# print(len(rows))
# print(rows[0]['city'])
# print(rows[1])
print(type(rows))
print(rows[0])

for row in rows:
    if row['city'] == 'Amsterdam':
        print(row['name'],'woont in', row['city'])

# {'name': 'Alice', 'age': '30', 'city': 'Amsterdam'}