paswoord = input("Voer het paswoord in: ")
geheim = "python"
aantal_keer = 3

while paswoord != geheim and aantal_keer > 1:
    aantal_keer -= 1
    if aantal_keer >0:
        print("je account is gelockt")
        break
    print("verkeerd paswoord! je hebt nog ", aantal_keer,"kansen")
    paswoord = input("Voer het paswoord in: ")

if paswoord == geheim:
    print("je bent ingelogd")


