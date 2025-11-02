# While-loop met break
geheim = 7
while True:
    gok = int(input("Raad het getal (1-10): "))
    if gok == geheim:
        print("Goed geraden!")
        break
    else:
        print("Fout, probeer opnieuw.")
