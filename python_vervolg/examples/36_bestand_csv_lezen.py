# CSV-bestand lezen
import csv

with open("data.csv", "r") as f:
    lezer = csv.reader(f)
    for rij in lezer:
        print(rij)
