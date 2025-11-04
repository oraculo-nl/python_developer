# Regels één voor één lezen
with open("voorbeeld.txt", "r") as f:
    for regel in f:
        print("Regel:", regel.strip())
