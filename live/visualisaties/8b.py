
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]

y1 = [3, 4, 2, 7, 8]


y2 = [2, 2, 3, 3, 4]

plt.style.use("seaborn-v0_8")

plt.plot(x, y1, label="Reeks 1")

plt.plot(x, y2, label="Reeks 2", alpha=0.5)

plt.title("Transparantie en stijl")

plt.grid(True); plt.legend()

plt.savefig("plot_example.png", dpi=150, bbox_inches="tight")
plt.savefig("plot_example.svg")
plt.show()