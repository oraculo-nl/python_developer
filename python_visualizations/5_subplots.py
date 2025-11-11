import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y1 = [n*n for n in x]
y2 = [n*2 for n in x]

# Twee subplots naast elkaar
fig, axes = plt.subplots(1, 2, figsize=(8, 3))

axes[0].plot(x, y1)
axes[0].set_title("Kwadratisch")

axes[1].plot(x, y2, "g--")
axes[1].set_title("Lineair")

fig.suptitle("Meerdere grafieken")
plt.tight_layout()
plt.show()
