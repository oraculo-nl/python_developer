with open("test.txt") as f:
    inhoud = f.readlines()

# loop door de inhoud en printen
for regel in inhoud:
    print(regel, end="")