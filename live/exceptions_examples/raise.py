def verdubbel(x):
    if not isinstance(x, (int, float)):
        raise TypeError("verdubbel verwacht een getal")
    return 2 * x


try:
    print(verdubbel("abc"))
except TypeError as e:
    print("Fout:", e)

# programmeer een try-except-else-finally
