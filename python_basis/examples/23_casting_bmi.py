# BMI = gewicht(kg) / lengte(m)^2
gewicht = float(input("Gewicht in kg: "))
lengte = float(input("Lengte in meters (bijv. 1.75): "))
bmi = gewicht / (lengte ** 2)
print(f"Je BMI is {bmi:.1f}")
