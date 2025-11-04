# CSV-bestand schrijven
import csv

with open("data.csv", "w", newline="") as f:
    schrijver = csv.writer(f)
    schrijver.writerow(["naam", "leeftijd"])
    schrijver.writerow(["Lisa", 21])
    schrijver.writerow(["Tom", 23])
print("CSV-bestand geschreven.")
