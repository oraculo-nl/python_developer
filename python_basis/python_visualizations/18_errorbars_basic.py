"""
Basic error bars with plain lists.
Run: python 18_errorbars_basic.py
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2.0, 2.5, 3.0, 3.5]
yerr = [0.2, 0.1, 0.3, 0.2]  # symmetric errors

plt.errorbar(x, y, yerr=yerr, fmt="o-", capsize=4, label="Measurements")
plt.title("Error bars (basic)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.tight_layout()
# plt.savefig("08_errorbars_basic.png", dpi=150, bbox_inches="tight")
plt.show()
