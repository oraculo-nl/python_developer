# 05_filter_select.py
# Onderwerp: filter() voor selectie

getallen = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, getallen))
groter_dan_3 = list(filter(lambda x: x > 3, getallen))

if __name__ == "__main__":
    print("even:", even)
    print("groter_dan_3:", groter_dan_3)
