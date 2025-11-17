import csv

def lees_config(pad):
    try:
        with open (pad, newline='') as csvfile:
            r = csv.DictReader(csvfile)
            for row in r:
                if len(row) != 2:
                    raise ValueError("deze regel heeft niet het vereiste aantal kolommen: "+str(r.line_num))
                print(row['a'])
    except FileNotFoundError:
        print("file niet gevonden")
    except OSError:
        print("OS error opgetreden")


lees_config("bestand.csv")