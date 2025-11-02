# Max van drie getallen met geneste if's en vergelijkingen
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

# Geneste aanpak
if x >= y:
    if x >= z:
        m = x
    else:
        m = z
else:
    if y >= z:
        m = y
    else:
        m = z
print(f"Maximaal: {m}")
