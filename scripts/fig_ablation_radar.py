"""
Figure: Ablation radar charts (supplements Table 6).
Two polar panels side by side: (a) Monocular and (b) Binocular,
both on ODIR Off-site. 4 metrics per axis: Kappa / F1 / AUC / Final.

Style: light-grey filled background, white concentric rings, saturated
per-method colors. Radial scale starts above zero (data-driven inner
ring) so spikes do not pile up near the rim.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    "font.family":     "DejaVu Sans",
    "font.size":       11,
    "pdf.fonttype":    42,
    "ps.fonttype":     42,
})

metrics = ["Kappa", "F1", "AUC", "Final"]

# (model_name, monocular[K,F1,AUC,Final], binocular[K,F1,AUC,Final], color, marker)
models = [
    ("ResNet50",
     np.array([58.52, 90.18, 89.40, 79.37]),
     np.array([52.75, 87.83, 88.00, 76.19]),
     "#999999", "o"),
    ("ResNet50 + DFE",
     np.array([62.09, 91.04, 91.64, 81.59]),
     np.array([56.20, 88.80, 90.10, 78.37]),
     "#1976D2", "s"),
    ("ResNet50 + ARC",
     np.array([59.41, 90.14, 91.74, 80.43]),
     np.array([53.19, 87.45, 90.29, 76.98]),
     "#7B3FA0", "^"),
    ("Ours (DFE + ARC)",
     np.array([62.61, 91.08, 92.33, 82.00]),
     np.array([57.05, 89.03, 90.48, 78.85]),
     "#E53935", "D"),
]

# Per-axis normalization range (in radial-fraction units), chosen so the
# innermost polygon (baseline) sits visibly inside, and the outermost
# (Ours) clearly stretches outward without touching the rim.
INNER_R, OUTER_R = 0.30, 0.92
PAD_LO, PAD_HI = 0.20, 0.20

def norm_per_axis(values_per_model):
    """Map each axis independently from [min - pad, max + pad] -> [INNER_R, OUTER_R].
    Returns the normalized matrix and the per-axis (mins, maxs) of the raw data."""
    raw = np.array(values_per_model)
    mins = raw.min(axis=0)
    maxs = raw.max(axis=0)
    spans = np.maximum(maxs - mins, 1e-9)
    lo = mins - spans * PAD_LO
    hi = maxs + spans * PAD_HI
    norm = (raw - lo) / (hi - lo)
    return INNER_R + norm * (OUTER_R - INNER_R), mins, maxs

mono_raw  = np.array([m[1] for m in models])
bino_raw  = np.array([m[2] for m in models])
mono_norm, mono_mins, mono_maxs = norm_per_axis(mono_raw)
bino_norm, bino_mins, bino_maxs = norm_per_axis(bino_raw)

N = len(metrics)
angles        = np.linspace(0, 2 * np.pi, N, endpoint=False)
angles_closed = np.append(angles, angles[0])

fig = plt.figure(figsize=(11.6, 5.6))
ax_mono = fig.add_subplot(1, 2, 1, projection="polar")
ax_bino = fig.add_subplot(1, 2, 2, projection="polar")


def plot_panel(ax, raw, norm_data, mins, maxs, title):
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Light grey filled circular background
    ax.set_facecolor("#ECECEC")

    # White concentric guide rings + spokes
    theta_dense = np.linspace(0, 2 * np.pi, 200)
    ring_levels = [0.2, 0.4, 0.6, 0.8, 1.0]
    for r in ring_levels:
        ax.plot(theta_dense, [r] * 200, color="white", lw=1.0, zorder=1)
    for a in angles:
        ax.plot([a, a], [0, 1.0], color="white", lw=0.9, zorder=1)

    # Plot each model -- line + markers only, no fill
    baseline_idx, ours_idx = 0, 3
    for i, (name, _, _, color, mk) in enumerate(models):
        v = norm_data[i]
        v_closed = np.append(v, v[0])
        is_ours = name.startswith("Ours")
        is_baseline = name == "ResNet50"
        if is_baseline:
            ax.plot(angles_closed, v_closed, color=color, lw=1.6, ls="--",
                    marker=mk, ms=6, mfc="white", mec=color, mew=1.2,
                    label=name, zorder=3)
        else:
            lw = 2.6 if is_ours else 1.8
            z  = 6 if is_ours else 4
            ax.plot(angles_closed, v_closed, color=color, lw=lw,
                    marker=mk, ms=7, mfc=color, mec="white", mew=0.9,
                    label=name, zorder=z)

    # Per-axis vertex value labels: write the raw value of baseline (low)
    # and Ours (high) outside the polygon, in a free area along that spoke.
    # Vertical axes (Kappa top, AUC bottom): nudge tangentially LEFT/RIGHT.
    # Horizontal axes (F1 right, Final left): nudge tangentially UP/DOWN.
    base_color = models[baseline_idx][3]
    ours_color = models[ours_idx][3]
    for i, ang in enumerate(angles):
        base_v = raw[baseline_idx, i]
        ours_v = raw[ours_idx,    i]
        base_r = norm_data[baseline_idx, i]
        ours_r = norm_data[ours_idx,    i]
        # baseline labels are pulled toward the center so they don't touch
        # the inner polygon boundary; Ours labels nudge slightly outward.
        if i == 0:        # Kappa (top)
            ax.text(ang + 0.35, base_r + 0.07, f"{base_v:.2f}",
                    fontsize=8.6, color=base_color, ha="center", va="center",
                    style="italic")
            ax.text(ang + 0.16, ours_r + 0.04, f"{ours_v:.2f}",
                    fontsize=9.0, color=ours_color, ha="center", va="center",
                    weight="bold")
        elif i == 2:      # AUC (bottom)
            ax.text(ang , base_r + 0.08, f"{base_v:.2f}",
                    fontsize=8.6, color=base_color, ha="center", va="center",
                    style="italic")
            ax.text(ang - 0.16, ours_r + 0.04, f"{ours_v:.2f}",
                    fontsize=9.0, color=ours_color, ha="center", va="center",
                    weight="bold")
        elif i == 1:      # F1 (right)
            ax.text(ang - 0.17, base_r + 0.05, f"{base_v:.2f}",
                    fontsize=8.6, color=base_color, ha="center", va="center",
                    style="italic")
            ax.text(ang - 0.10, ours_r + 0.05, f"{ours_v:.2f}",
                    fontsize=9.0, color=ours_color, ha="center", va="center",
                    weight="bold")
        else:             # Final (left)
            ax.text(ang , base_r - 0.15, f"{base_v:.2f}",
                    fontsize=8.6, color=base_color, ha="center", va="center",
                    style="italic")
            ax.text(ang + 0.10, ours_r + 0.05, f"{ours_v:.2f}",
                    fontsize=9.0, color=ours_color, ha="center", va="center",
                    weight="bold")

    # Metric labels at the rim, with [min – max] positioned per-metric so
    # it doesn't collide with the metric name OR with the polygon edges.
    # Kappa(top)             : [..] just BELOW the metric name (closer to center)
    # AUC (bottom)           : [..] just ABOVE the metric name (closer to center)
    # F1 (right) / Final(left): [..] BELOW in cartesian sense -- reached by
    #   placing it at a slightly different angle (toward AUC) AND smaller r,
    #   so it sits in the empty space outside the polygon, below the metric.
    ax.set_xticks(angles)
    ax.set_xticklabels([])

    # ----------------------------------------------------------------
    # 指标名的径向距离：上下指标共享一组（Kappa/AUC），左右指标共享一组（F1/Final）
    # 数值越大 = 离圆心越远（往外推）
    # ----------------------------------------------------------------
    METRIC_R_VERT = 1.15   # 上下：Kappa（顶）与 AUC（底）共用
    METRIC_R_HORZ = 1.25   # 左右：F1（右）与 Final（左）共用

    # ----------------------------------------------------------------
    # [low-high] 范围标签的径向距离：同样按上下/左右分两组
    # ----------------------------------------------------------------
    BRACKET_R_VERT = 1.05  # 上下：靠近指标名内侧（Kappa 下方 / AUC 上方）
    BRACKET_R_HORZ = 1.00  # 左右：在指标名"下方"的空白区域

    # ----------------------------------------------------------------
    # F1/Final 的 [..] 角度偏移（让它落在指标名下方的空白处，不和雷达接触）
    # 数值越大 = 越往 AUC 方向偏（视觉上更"下方"）
    # ----------------------------------------------------------------
    BRACKET_ANG_F1    =  0.10   # F1 在右侧，正值 = 往下偏
    BRACKET_ANG_FINAL = -0.10   # Final 在左侧，负值 = 往下偏

    for i, (ang, m) in enumerate(zip(angles, metrics)):
        is_vert = (i == 0 or i == 2)  # Kappa / AUC
        metric_r  = METRIC_R_VERT  if is_vert else METRIC_R_HORZ
        bracket_r = BRACKET_R_VERT if is_vert else BRACKET_R_HORZ

        # 指标名
        ax.text(ang, metric_r, m,
                fontsize=12, ha="center", va="center",
                color="0.01", weight="medium")

        # [low – high] 范围
        bracket_text = f"[{mins[i]:.2f} – {maxs[i]:.2f}]"
        if i == 0:        # Kappa（顶）：和指标名共轴，半径更小（在下方）
            ax.text(ang, bracket_r, bracket_text,
                    fontsize=8.5, ha="center", va="center",
                    color="0.40", style="italic")
        elif i == 2:      # AUC（底）：同理（半径更小 = 视觉上方）
            ax.text(ang, bracket_r, bracket_text,
                    fontsize=8.5, ha="center", va="center",
                    color="0.40", style="italic")
        elif i == 1:      # F1（右）：偏向 AUC 方向
            ax.text(ang + BRACKET_ANG_F1, bracket_r, bracket_text,
                    fontsize=8.5, ha="left", va="center",
                    color="0.40", style="italic")
        else:             # Final（左）
            ax.text(ang + BRACKET_ANG_FINAL, bracket_r, bracket_text,
                    fontsize=8.5, ha="right", va="center",
                    color="0.40", style="italic")

    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.spines["polar"].set_visible(False)
    ax.grid(False)
    ax.set_title(title, pad=57, fontsize=12, weight="semibold")


plot_panel(ax_mono, mono_raw, mono_norm, mono_mins, mono_maxs, "(a) Monocular")
plot_panel(ax_bino, bino_raw, bino_norm, bino_mins, bino_maxs, "(b) Binocular")

handles, labels = ax_mono.get_legend_handles_labels()
leg = fig.legend(handles, labels, loc="lower center",
                 bbox_to_anchor=(0.5, -0.125), ncol=2,
                 handlelength=1.8, columnspacing=2.2, handletextpad=0.6,
                 frameon=True, framealpha=0.95, edgecolor="0.7",
                 fontsize=11)
leg.get_frame().set_linewidth(0.8)
leg.get_frame().set_boxstyle("Square,pad=0.4")

fig.suptitle("Ablation comparison on ODIR Off-site (per-axis normalized)",
             fontsize=13, weight="semibold", y=1)

fig.tight_layout()

out_dir = Path(__file__).resolve().parents[1] / "images" / "plots"
out_pdf = out_dir / "fig_ablation_radar.pdf"
out_png = out_dir / "fig_ablation_radar.png"
fig.savefig(out_pdf, bbox_inches="tight")
fig.savefig(out_png, bbox_inches="tight", dpi=240)
print(f"saved: {out_pdf}\nsaved: {out_png}")
