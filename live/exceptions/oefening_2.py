import csv

# csv.DictReader()

def lees_config(pad):
    try:
        with open (pad, newline='') as csvfile:
            r = csv.DictReader(csvfile)
            for row in r:
                if len(row) != 3:
                    raise ValueError()
                print(row)
    except FileNotFoundError:
        print("file niet gevonden")
    except OSError:
        print("OS error opgetreden")


lees_config("bestand.csv")