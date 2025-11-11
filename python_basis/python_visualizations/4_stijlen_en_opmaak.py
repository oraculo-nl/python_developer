import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 2, 3, 4]

plt.style.use("ggplot")     # voorbeeldstijl
plt.plot(x, y1, "r--o", label="kwadratisch")
plt.plot(x, y2, "b-^", label="lineair")
plt.xlim(0, 4)
plt.ylim(0, 16)
plt.xticks([0, 1, 2, 3, 4])
plt.title("Stijlen en opmaak")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
