import csv


def lees_csv():
    rijen = []
    with open("bestand.csv") as csvfile:
        r = csv.DictReader(csvfile)
        for row in r:
            rijen.append(row)
    return rijen