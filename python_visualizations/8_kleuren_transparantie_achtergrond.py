import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [3, 4, 6, 7, 8]
y2 = [2, 2, 3, 3, 4]

plt.style.use("seaborn-v0_8")   # voorbeeldstijl
plt.plot(x, y1, label="Reeks 1", alpha=0.7)
plt.plot(x, y2, label="Reeks 2", alpha=0.7)
plt.grid(True)
plt.legend()
plt.title("Transparantie en stijl")
plt.show()