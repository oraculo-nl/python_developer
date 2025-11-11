import matplotlib.pyplot as plt

data = {"Jan": 5, "Feb": 8, "Mrt": 6, "Apr": 9}

# Gesorteerd op maandnaam (alfabetisch als voorbeeld)
maanden = sorted(data.keys())
waarden = [data[m] for m in maanden]

plt.bar(maanden, waarden)
plt.title("Waarden per maand")
plt.xlabel("Maand")
plt.ylabel("Waarde")
plt.xticks(rotation=30)
plt.show()