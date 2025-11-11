import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 5]

plt.plot(x, y, marker="o")
plt.title("Annotaties voorbeeld")

# Annotatie naar hoogste punt
max_y = max(y)
max_i = y.index(max_y)
plt.annotate(
    "Max",
    xy=(x[max_i], max_y),
    xytext=(x[max_i]+0.5, max_y+0.5),
    arrowprops={"arrowstyle": "->"}
)

# Losse tekst
plt.text(1, 7.5, "Noot: data is fictief")

plt.show()