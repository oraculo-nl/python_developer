import csv
from collections import Counter

counts = Counter()

with open("Smartphone_Usage_Productivity_Dataset_50000.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        counts[row["Gender"].strip()] += 1

print(f"Unique count: {len(counts)}")
for gender, n in counts.items():
    print(f"{gender}: {n}")