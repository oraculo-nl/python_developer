"""
Set equal aspect ratio — useful when x and y units should be equal.
Run: python 16_aspect_equal.py
"""
import math
import matplotlib.pyplot as plt

# Plot a unit circle using plain lists
xs = []
ys = []
for t in range(0, 361, 10):
    rad = t * math.pi / 180.0
    xs.append(math.cos(rad))
    ys.append(math.sin(rad))

fig, ax = plt.subplots()
ax.plot(xs, ys)
ax.set_aspect("equal", adjustable="box")  # circle looks like a circle
ax.set_title("Equal aspect ratio (unit circle)")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.tight_layout()
# fig.savefig("06_aspect_equal.png", dpi=150, bbox_inches="tight")
plt.show()
