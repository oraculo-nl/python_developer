import matplotlib.pyplot as plt

data = {"Apples": 10, "Bananas": 15,"Cherries": 7}
plt.bar(data.keys(), data.values())
plt.title("Fruit per soort")
plt.xlabel("Soort")
plt.ylabel("Aantal")
plt.show()