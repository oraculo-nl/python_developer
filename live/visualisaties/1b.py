
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]


plt.plot(x, y, label="Reeks 1")
plt.title("Eenvoudige lijnplot")
plt.xlabel("x-waarden")
plt.ylabel("y-waarden")
plt.grid(True)
plt.legend()
plt.show()