"""
Log scale on y-axis (semilogy) — useful for multiplicative growth.
Run: python 15_log_scale_basics.py
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 10, 100, 1000, 10000]

plt.plot(x, y, marker="o")
plt.yscale("log")  # or: plt.xscale("log") / both: "log"
plt.title("Log scale (y-axis)")
plt.xlabel("x")
plt.ylabel("y (log scale)")
plt.grid(True)
plt.tight_layout()
# plt.savefig("05_log_scale_basics.png", dpi=150, bbox_inches="tight")
plt.show()
