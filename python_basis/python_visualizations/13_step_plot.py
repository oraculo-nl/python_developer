"""
Step plot vs line plot — useful for piecewise-constant data.
Run: python 13_step_plot.py
"""
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [2, 2, 3, 3, 5, 5]

plt.step(x, y, where="post", label="Step (post)")
plt.plot(x, y, label="Line")
plt.title("Step vs Line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.tight_layout()
# plt.savefig("03_step_plot.png", dpi=150, bbox_inches="tight")
plt.show()
