"""
Figure: Privacy-utility tradeoff curve (replaces previous dual-axis chart).
- x-axis: epsilon (privacy budget consumed; left = stronger privacy, right = weaker)
- y-axis: Final score (monocular)
- each point = one epoch checkpoint, colored by epoch (training-time progress)
- e74 highlighted as the Pareto knee (best privacy ckpt)

This is the standard "privacy-utility tradeoff" plot used in DP papers, where
the optimal operating point is naturally a knee on the curve, not a contrived
crossing of two axes.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

from _style import use_style, save, PALETTE

use_style()

# ---- Data from Table 4 ----
epoch = np.array([0, 10, 22, 31, 40, 49, 52, 64, 68, 74, 79])
eps   = np.array([0.94, 3.28, 4.91, 5.91, 6.81, 7.65, 7.92, 8.94, 9.27, 9.76, 10.15])
final = np.array([64.26, 67.09, 68.36, 69.85, 70.28, 70.94, 71.54, 71.91, 72.51, 73.15, 72.38])
peak_idx = int(np.argmax(final))
C_HIGH = PALETTE["vermillion"]

fig, ax = plt.subplots(figsize=(7.0, 4.0))

# Trajectory line, colored as a gradient by epoch
points = np.array([eps, final]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
norm = Normalize(vmin=epoch.min(), vmax=epoch.max())
cmap = plt.get_cmap("viridis")
lc = LineCollection(segments, cmap=cmap, norm=norm, linewidth=2.0,
                    capstyle="round", zorder=3)
lc.set_array((epoch[:-1] + epoch[1:]) / 2)
ax.add_collection(lc)

# Points themselves, colored by epoch
sc = ax.scatter(eps, final, c=epoch, cmap=cmap, norm=norm,
                s=58, edgecolor="white", linewidth=0.9, zorder=5)

# Per-point epoch label (small, gray)
label_offsets = {
    0: (0.00, 0.55),
    10: (0.00, 0.55),
    22: (0.00, 0.55),
    31: (0.00, 0.55),
    40: (0.00, 0.55),
    49: (-0.25, 0.35),
    52: (0.00, 0.55),
    64: (-0.25, 0.45),
    68: (0.00, 0.55),
    74: (0.00, 0.65),
    79: (0.4, -0.1),
}

for i in range(len(epoch)):
    dx, dy = label_offsets.get(int(epoch[i]), (0.0, 0.55))
    ax.annotate(f"e{epoch[i]}",
                xy=(eps[i], final[i]),
                xytext=(eps[i] + dx, final[i] + dy),
                fontsize=8.0, color="0.30",
                ha="center", va="bottom")

# Highlight the knee point (e74)
ax.scatter([eps[peak_idx]], [final[peak_idx]],
           s=190, facecolor="none", edgecolor=C_HIGH, lw=1.8, zorder=6)
ax.annotate(
    f"e{epoch[peak_idx]}: Pareto knee\n($\\epsilon$={eps[peak_idx]:.2f}, Final={final[peak_idx]:.2f})",
    xy=(eps[peak_idx], final[peak_idx]),
    xytext=(eps[peak_idx] - 3.7, final[peak_idx] + 0.4 ),
    fontsize=9.5, color=C_HIGH, ha="left", va="center",
    arrowprops=dict(arrowstyle="-", color=C_HIGH, lw=0.9,
                    connectionstyle="arc3,rad=0.2",relpos=(1.0, 0.15),)
)

# Axis cosmetics
ax.set_xlabel(r"Privacy budget $\epsilon$ (cumulative)")
ax.set_ylabel("Final score (%)")
ax.set_xlim(0, 11.5)
ax.set_ylim(62, 75)
ax.grid(True)
ax.set_axisbelow(True)

# Direction-of-privacy hint above the x-axis
ax_top = ax.secondary_xaxis("top")
ax_top.set_xticks([])
ax.text(0.02, 1.04, r"$\leftarrow$ stronger privacy",
        transform=ax.transAxes, fontsize=9, color="0.35", ha="left")
ax.text(0.98, 1.04, r"weaker privacy $\rightarrow$",
        transform=ax.transAxes, fontsize=9, color="0.35", ha="right")

# Colorbar for epoch
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, fraction=0.038, pad=0.025, aspect=22)
cbar.set_label("Epoch", labelpad=4)
cbar.outline.set_linewidth(0.6)
cbar.ax.tick_params(labelsize=9)

fig.tight_layout()
save(fig, "fig_privacy_tradeoff")
