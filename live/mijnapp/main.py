from lees_csv import lees_csv
from analyse_csv import analyseer_csv

def main():
    rijen = lees_csv()
    analyseer_csv(rijen)

if __name__ == "__main__":
    main()