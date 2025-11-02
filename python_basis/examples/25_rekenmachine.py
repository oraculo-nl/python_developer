# Eenvoudige rekenmachine voor twee getallen
print("Kies een bewerking: +, -, *, /")
op = input("Bewerking: ")
x = float(input("Eerste getal: "))
y = float(input("Tweede getal: "))

if op == "+":
    uit = x + y
elif op == "-":
    uit = x - y
elif op == "*":
    uit = x * y
elif op == "/":
    uit = x / y
else:
    print("Onbekende bewerking.")
    exit()

print(f"{x} {op} {y} = {uit}")
