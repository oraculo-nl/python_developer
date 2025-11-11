import matplotlib.pyplot as plt

# Staafdiagram
fruit = ["Appel", "Banaan", "Kers"]
aantal = [10, 15, 7]
plt.bar(fruit, aantal)
plt.title("Fruit per soort")
plt.show()

# Scatterplot
x = [1, 2, 3, 4, 5]
y = [5, 3, 6, 2, 7]
plt.scatter(x, y)
plt.title("Scattervoorbeeld")
plt.show()

# Histogram
metingen = [1,1,2,2,2,3,3,4,5,5,5,5]
plt.hist(metingen, bins=5)
plt.title("Histogram metingen")
plt.show()

# (Optioneel) Cirkeldiagram
labels = ["A", "B", "C"]
waarden = [40, 35, 25]
plt.pie(waarden, labels=labels, autopct="%1.0f%%")
plt.title("Verdeling categorieën")
plt.show()
