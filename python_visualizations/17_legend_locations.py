"""
Legend placement options.
Run: python 17_legend_locations.py
"""
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 2, 3, 4]

plt.plot(x, y1, label="Quadratic")
plt.plot(x, y2, label="Linear")
plt.title("Legend locations")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")  # try: "upper left", "lower right", etc.
plt.grid(True)
plt.tight_layout()
# plt.savefig("07_legend_locations.png", dpi=150, bbox_inches="tight")
plt.show()
