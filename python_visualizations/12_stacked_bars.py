"""
Stacked bar chart with plain Python lists.
Run: python 12_stacked_bars.py
"""
import matplotlib.pyplot as plt

categories = ["Q1", "Q2", "Q3", "Q4"]
product_a = [5, 7, 3, 4]
product_b = [2, 4, 5, 3]

# Bottom is the cumulative height of previous stacks
plt.bar(categories, product_a, label="Product A")
plt.bar(categories, product_b, bottom=product_a, label="Product B")
plt.title("Stacked bars (A + B)")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
# plt.savefig("02_stacked_bars.png", dpi=150, bbox_inches="tight")
plt.show()
