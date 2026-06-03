"""
Figure: Privacy training epsilon-performance evolution (replaces Table 4).
Dual-axis line chart with the unified style.
"""

import matplotlib.pyplot as plt
import numpy as np
from _style import use_style, save, PALETTE, C_HIGHLIGHT

use_style()

# ---- Data from Table 4 ----
epoch = np.array([0, 10, 22, 31, 40, 49, 52, 64, 68, 74, 79])
eps   = np.array([0.94, 3.28, 4.91, 5.91, 6.81, 7.65, 7.92, 8.94, 9.27, 9.76, 10.15])
kappa = np.array([29.39, 34.24, 36.42, 39.70, 40.62, 40.64, 42.16, 42.45, 43.59, 45.12, 43.16])
f1    = np.array([84.70, 85.77, 85.85, 86.28, 86.13, 87.01, 87.46, 87.38, 87.76, 87.91, 87.51])
auc   = np.array([78.70, 81.27, 82.83, 83.56, 84.08, 85.17, 85.00, 85.89, 86.18, 86.42, 86.47])
final = np.array([64.26, 67.09, 68.36, 69.85, 70.28, 70.94, 71.54, 71.91, 72.51, 73.15, 72.38])
peak_idx = int(np.argmax(final))

C_FINAL = PALETTE["vermillion"]
C_KAPPA = PALETTE["orange"]
C_F1    = PALETTE["green"]
C_AUC   = PALETTE["skyblue"]
C_EPS   = PALETTE["blue"]

fig, ax_perf = plt.subplots(figsize=(7.0, 3.6))
ax_eps = ax_perf.twinx()

# Right-axis spine on (only one we want visible besides bottom-left)
ax_eps.spines["right"].set_visible(True)
ax_eps.spines["right"].set_color("0.25")
ax_eps.spines["right"].set_linewidth(0.7)
ax_eps.spines["top"].set_visible(False)

# --- Performance lines ---
ax_perf.plot(epoch, kappa, color=C_KAPPA, marker="s", label="Kappa", lw=1.4)
ax_perf.plot(epoch, f1,    color=C_F1,    marker="^", label="micro-F1", lw=1.4)
ax_perf.plot(epoch, auc,   color=C_AUC,   marker="D", label="AUC", lw=1.4)
ax_perf.plot(epoch, final, color=C_FINAL, marker="o", label="Final", lw=2.2, ms=6, zorder=5)

ax_perf.set_xlabel("Epoch")
ax_perf.set_ylabel("Monocular performance (\\%)" if False else "Monocular performance (%)")
ax_perf.set_ylim(25, 95)
ax_perf.set_xlim(-3, 82)
ax_perf.grid(True, axis="y")
ax_perf.set_axisbelow(True)

# --- Epsilon line on right axis ---
ax_eps.plot(epoch, eps, color=C_EPS, marker="o", ms=4, lw=1.3, ls="--",
            mfc="white", mec=C_EPS, mew=1.0, label=r"$\epsilon$")
ax_eps.set_ylabel(r"Privacy budget $\epsilon$", color=C_EPS)
ax_eps.tick_params(axis="y", colors=C_EPS)
ax_eps.set_ylim(0, max(eps) * 1.35)

# --- Highlight peak (e74) ---
ax_perf.axvline(epoch[peak_idx], color=C_HIGHLIGHT, lw=0.8, ls=":", alpha=0.6)
ax_perf.scatter([epoch[peak_idx]], [final[peak_idx]],
                s=110, facecolor="none", edgecolor=C_HIGHLIGHT, lw=1.4, zorder=6)
ax_perf.annotate(
    f"e{epoch[peak_idx]}: best privacy ckpt",
    xy=(epoch[peak_idx], final[peak_idx]),
    xytext=(epoch[peak_idx] - 28, final[peak_idx] + 7),
    fontsize=9, color=C_HIGHLIGHT,
    arrowprops=dict(arrowstyle="-", color=C_HIGHLIGHT, lw=0.7,
                    connectionstyle="arc3,rad=0.15"),
)

# --- Combined legend ---
h1, l1 = ax_perf.get_legend_handles_labels()
h2, l2 = ax_eps.get_legend_handles_labels()
ax_perf.legend(h1 + h2, l1 + l2, loc="lower right", ncol=5,
               handlelength=1.6, columnspacing=1.4, borderaxespad=0.4)

fig.tight_layout()
save(fig, "fig_privacy_evolution")
