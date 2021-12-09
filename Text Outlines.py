# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Stroke, Normal

fig = plt.figure(figsize=(8, 3)) #figsize 是一个属性，因此不用去管他，只需要知道它能起到什么作用就好，它就是用来定义你的图像的大小。这句话的意思就是作为plt的一个方法的figure。
ax = fig.add_axes([0, 0, 1, 1], frameon=False)

gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
# spans two rows:
ax3 = fig.add_subplot(gs[:, 1])

family = "Pacifico"
size = 100
cmap = plt.cm.magma
text = "Matplotlib"

for x in np.linspace(0, 1, 20):
    lw, color = x * 225, cmap(1 - x)
    t = ax.text(
        0.5,
        0.45,
        text,
        size=size,
        color="none",
        weight="bold",
        va="center",
        ha="center",
        family=family,
        zorder=-lw,
    )
    t.set_path_effects([Stroke(linewidth=lw + 1, foreground="black")])
    t = ax.text(
        0.5,
        0.45,
        text,
        size=size,
        color="black", # Word Color
        weight="bold",
        va="center",
        ha="center",
        family=family,
        zorder=-lw + 1,
    )
    t.set_path_effects([Stroke(linewidth=lw, foreground=color)])
t = ax.text(
    1.0,
    0.01,
    "https://matplotlib.org ",
    va="bottom",
    ha="right",
    size=10,
    color="white",
    family="Roboto",
    alpha=0.50,
)
plt.show()
