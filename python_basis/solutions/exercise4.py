n = int(input("n: "))
if n <= 0:
    print("Voer een positief getal in.")
else:
    som = 0
    for i in range(1, n + 1):
        som += i
    print("Som van 1 t/m", n, "=", som)