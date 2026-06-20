"""
Figure: SOTA comparison grouped bar chart (supplements Table 7).
5 methods x 4 metrics, with two subplots: (a) Off-site, (b) On-site.
Y-axis is broken-style (custom lower bound) so the differences between
methods are visible despite all values living in the 35-92 range.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# ---- Data from Table 7 (SOTA comparison) ----
methods = ["Li et al. [46]", "Gour & Khanna [49]", "He et al. [20]", "Ou et al. [50]", "Ours"]
metrics = ["Kappa", "F1", "AUC", "Final"]
offsite = np.array([
    [35.45, 84.83, 83.72, 68.00],
    [43.30, 85.30, 84.90, 71.20],
    [52.00, 88.60, 90.30, 77.00],
    [53.50, 89.20, 91.20, 78.00],
    [57.05, 89.03, 90.48, 78.85],
])
onsite = np.array([
    [36.97, 85.35, 84.08, 68.80],
    [42.00, 84.90, 83.40, 70.10],
    [50.00, 87.70, 89.70, 75.80],
    [51.30, 88.60, 90.30, 76.70],
    [54.03, 88.38, 90.07, 77.49],
])

# Per-method colors (Ours as the dark accent)
METHOD_COLORS = ["#A8B5BE", "#F2CC8F", "#81B29A", "#6E7BD9", "#3D405B"]
HATCHES        = ["", "", "", "", "//"]  # subtle pattern only on Ours

# Style
mpl.rcParams.update({
    "font.family":     "DejaVu Sans",
    "font.size":       11,
    "axes.linewidth":  0.9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype":    42,
    "ps.fonttype":     42,
})

fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.4), dpi=200, sharey=True)

def plot_panel(ax, data, title):
    n_metrics = len(metrics)
    n_methods = len(methods)
    group_w = 1.4
    bar_w = group_w / n_methods
    x = np.arange(n_metrics) * 1.6  # widen gap between metric groups

    for i, (m, color, hatch) in enumerate(zip(methods, METHOD_COLORS, HATCHES)):
        offset = (i - (n_methods - 1) / 2) * bar_w
        ax.bar(x + offset, data[i], width=bar_w * 0.9,
               color=color, edgecolor="white", linewidth=0.8,
               hatch=hatch, label=m, zorder=3)

    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=11)
    ax.set_ylim(30, 100)
    ax.set_yticks(np.arange(30, 101, 10))
    ax.grid(True, axis="y", ls=":", lw=0.6, color="0.7", alpha=0.6, zorder=0)
    ax.set_title(title, fontsize=12, pad=8, weight="semibold")
    ax.set_axisbelow(True)

plot_panel(axes[0], offsite, "(a) Off-site test")
plot_panel(axes[1], onsite, "(b) On-site test")
axes[0].set_ylabel("Score (%)")

# Single legend below both panels
handles, labels = axes[0].get_legend_handles_labels()
leg = fig.legend(handles, labels,
                 loc="lower center", bbox_to_anchor=(0.5, -0.04),
                 ncol=5, frameon=True, framealpha=0.95, edgecolor="0.85",
                 fontsize=10, handlelength=1.8, columnspacing=4.5)
leg.get_frame().set_linewidth(0.6)

fig.suptitle("Comparison with prior multi-label fundus disease recognition methods on ODIR",
             fontsize=12.5, weight="semibold", y=1.02)
fig.tight_layout()

out_dir = Path(__file__).resolve().parents[1] / "images" / "plots"
out_pdf = out_dir / "fig_sota_compare.pdf"
out_png = out_dir / "fig_sota_compare.png"
fig.savefig(out_pdf, bbox_inches="tight")
fig.savefig(out_png, bbox_inches="tight", dpi=220)
print(f"saved: {out_pdf}\nsaved: {out_png}")
