"""
Unified plotting style for the experiments-section figures.
Goal: clean, modern, journal-quality look without per-figure ad hoc tweaks.

Design choices:
- Helvetica (system) as the sans-serif face -- crisp, neutral, journal-standard.
- Okabe-Ito 8-color palette: colorblind-safe, perceptually balanced,
  recommended by Nature Methods for figures.
- Hairline axes, no top/right spines, minimal grid only on the value axis.
- No bold value labels on glyphs by default -- the table holds the numbers,
  the figure shows the trend.
- Vector PDF + high-DPI PNG output via the same call.
"""

from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PLOTS_DIR    = PROJECT_ROOT / "images" / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

# Okabe-Ito palette (https://jfly.uni-koeln.de/color/)
PALETTE = {
    "black":      "#000000",
    "orange":     "#E69F00",
    "skyblue":    "#56B4E9",
    "green":      "#009E73",
    "yellow":     "#F0E442",
    "blue":       "#0072B2",
    "vermillion": "#D55E00",
    "purple":     "#CC79A7",
    "grey":       "#999999",
}

# Semantic colors used across figures
C_BASELINE = PALETTE["grey"]
C_OURS     = PALETTE["vermillion"]
C_DFE      = PALETTE["blue"]
C_ARC      = PALETTE["green"]
C_HIGHLIGHT = PALETTE["vermillion"]
C_MUTED    = "#BFBFBF"


def use_style():
    """Apply the unified rcParams. Call this at the top of every figure script."""
    mpl.rcParams.update({
        # Fonts
        "font.family":          "sans-serif",
        "font.sans-serif":      ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size":            10.5,
        "axes.titlesize":       11.5,
        "axes.labelsize":       10.5,
        "xtick.labelsize":      9.8,
        "ytick.labelsize":      9.8,
        "legend.fontsize":      9.8,
        "figure.titlesize":     12,

        # Lines & markers
        "lines.linewidth":      1.6,
        "lines.markersize":     5.0,
        "lines.markeredgewidth": 0.8,

        # Axes
        "axes.linewidth":       0.7,
        "axes.spines.top":      False,
        "axes.spines.right":    False,
        "axes.titleweight":     "regular",
        "axes.titlepad":        10,
        "axes.labelpad":        4,
        "axes.edgecolor":       "0.25",
        "axes.labelcolor":      "0.15",

        # Ticks
        "xtick.color":          "0.25",
        "ytick.color":          "0.25",
        "xtick.major.width":    0.7,
        "ytick.major.width":    0.7,
        "xtick.major.size":     3.0,
        "ytick.major.size":     3.0,
        "xtick.direction":      "out",
        "ytick.direction":      "out",

        # Grid
        "grid.color":           "0.85",
        "grid.linestyle":       "-",
        "grid.linewidth":       0.5,
        "grid.alpha":           0.7,

        # Legend
        "legend.frameon":       False,
        "legend.borderpad":     0.4,
        "legend.handletextpad": 0.6,

        # Saving
        "savefig.dpi":          300,
        "savefig.bbox":         "tight",
        "savefig.pad_inches":   0.05,
        "pdf.fonttype":         42,
        "ps.fonttype":          42,
    })


def save(fig, name):
    """Save fig as both vector PDF (LaTeX) and high-DPI PNG (preview)."""
    out_pdf = PLOTS_DIR / f"{name}.pdf"
    out_png = PLOTS_DIR / f"{name}.png"
    fig.savefig(out_pdf)
    fig.savefig(out_png, dpi=240)
    print(f"saved: {out_pdf}")
    print(f"saved: {out_png}")
