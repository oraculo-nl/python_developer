import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.title("Opslaan van figuren")
plt.xlabel("x")
plt.ylabel("y")

# Opslaan vóór plt.show()
plt.savefig("plot_example.png", dpi=150, bbox_inches="tight")
plt.savefig("plot_example.pdf")   # vectorformaat
plt.show()