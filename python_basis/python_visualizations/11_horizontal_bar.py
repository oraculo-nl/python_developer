"""
Horizontal bar chart from a dictionary.
Run: python 11_horizontal_bar.py
"""
import matplotlib.pyplot as plt

data = {"Apples": 10, "Bananas": 15, "Cherries": 7, "Dates": 5}
labels = list(data.keys())
values = list(data.values())

plt.barh(labels, values)
plt.title("Horizontal bar chart")
plt.xlabel("Quantity")
plt.ylabel("Fruit")
plt.tight_layout()
# plt.savefig("01_horizontal_bar.png", dpi=150, bbox_inches="tight")
plt.show()
