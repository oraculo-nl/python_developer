klas = {
    "studenten": [
        {"naam": "Vera", "leeftijd": 28},
        {"naam": "Kevin", "leeftijd": 24},
        {"naam": "Eva", "leeftijd": 30}
    ]
}
leeftijden = [student["leeftijd"] for student in klas["studenten"]]
gemiddelde = sum(leeftijden)/len(leeftijden)
print(f"Gemiddelde leeftijd = {gemiddelde:.2f}")