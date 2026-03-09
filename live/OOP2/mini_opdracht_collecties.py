from film import Film

# films = [Film("Deer Hunter", 8.0), Film("Rocky", 7.2)]
import csv

films = []

with open("films.csv", newline="") as f:
    reader = csv.reader(f)
    for rij in reader:
        film = Film(rij[0], float(rij[1]))
        film.inkomsten(10)
        films.append(film)

for film in films:
    print(film)

leukste_films = [s for s in films if s.score >= 7]
gesorteerd = sorted(leukste_films, key=lambda s: s.score)

for film in gesorteerd:
    print(film.titel, film.score, film.get_inkomsten())