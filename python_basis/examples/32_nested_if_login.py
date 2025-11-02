# Geneste if's voor een simpele login-check
user = input("Gebruikersnaam: ").strip()
pwd = input("Wachtwoord: ").strip()

if user == "admin":
    if pwd == "geheim":
        print("Welkom, admin!")
    else:
        print("Fout wachtwoord voor admin.")
else:
    if user != "":
        print("Welkom, gewone gebruiker.")
    else:
        print("Gebruikersnaam mag niet leeg zijn.")
