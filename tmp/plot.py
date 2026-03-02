import matplotlib.pyplot as plt



dagen = [1, 2, 3, 4, 5]

temp = [7, 9, 11, 10, 12]


plt.plot(dagen, temp, label="Temperatuur")

plt.title("Temperatuur over dagen")

plt.xlabel("Dag")

plt.ylabel("Graden (C)")

plt.legend(); plt.grid(True)

plt.show()