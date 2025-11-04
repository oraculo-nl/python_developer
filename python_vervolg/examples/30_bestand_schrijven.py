# Een bestand openen om te schrijven
with open("voorbeeld.txt", "w") as f:
    f.write("Dit is een testbestand.\n")
    f.write("Bestanden werken eenvoudig in Python!")
print("Bestand geschreven.")
