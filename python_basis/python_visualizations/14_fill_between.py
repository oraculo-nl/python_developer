"""
Fill the area under a curve (or between two curves).
Run: python 14_fill_between.py
"""
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y, label="y = x^2")
plt.fill_between(x, y, 0, alpha=0.3)  # shade between y and baseline 0
plt.title("Fill Between (area under curve)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.tight_layout()
# plt.savefig("04_fill_between.png", dpi=150, bbox_inches="tight")
plt.show()
