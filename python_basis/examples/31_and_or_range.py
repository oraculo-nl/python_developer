# Controleer leeftijd met vergelijkingen en logische operators
age = int(input("Leeftijd: "))
if 18 <= age <= 65:
    print("Werkende leeftijd (18 t/m 65)")
elif age < 18:
    print("Jonger dan 18")
else:
    print("Ouder dan 65")

# Korting: student of 65+ krijgt korting
is_student = input("Ben je student? (j/n): ").strip().lower() == "j"
has_discount = is_student or age >= 65
print(f"Korting van toepassing: {has_discount}")
