#!/usr/bin/env python3
"""Regenerate public summary figures/tables from cleaned derived CSVs.

No raw MedMNIST data, credentials, PHI, or local private paths are required.
"""
from pathlib import Path
import math
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)
summary = pd.read_csv(DATA / "table_primary_metric_summary.csv")
models = ["pixel_gray_28", "hog4x4_28", "pca128_gray_28"]
datasets = ["chestmnist", "octmnist", "organamnist"]

fig, ax = plt.subplots(figsize=(8.4, 4.7))
x = np.arange(len(datasets)); width = 0.24
for i, model in enumerate(models):
    vals=[]; errs=[]
    for ds in datasets:
        row = summary[(summary.dataset == ds) & (summary.model == model)].iloc[0]
        vals.append(row.primary_mean); errs.append(row.primary_sd)
    ax.bar(x + (i-1)*width, vals, width, label=model, yerr=errs, capsize=3)
ax.set_xticks(x); ax.set_xticklabels(["ChestMNIST", "OCTMNIST", "OrganAMNIST"])
ax.set_ylim(0.50, 1.0); ax.set_ylabel("Mean test macro-AUROC across 3 seeds")
ax.set_title("Dataset-dependent representation ranking")
ax.legend(fontsize=8); ax.grid(axis="y", alpha=0.25)
fig.tight_layout(); fig.savefig(FIG / "fig1-primary-metric-by-dataset.png", dpi=180); plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(9.3, 4.2))
for ax, metric_name, title in [(axes[0], "ece_10bin", "ECE-10 (lower is better)"), (axes[1], "brier", "Brier score (lower is better)")]:
    piv = summary.pivot(index="dataset", columns="model", values=metric_name).loc[datasets, models]
    im = ax.imshow(piv.values.astype(float), aspect="auto", cmap="viridis")
    ax.set_xticks(np.arange(len(models))); ax.set_xticklabels([m.replace("_", "\n") for m in models], fontsize=8)
    ax.set_yticks(np.arange(len(datasets))); ax.set_yticklabels(["ChestMNIST", "OCTMNIST", "OrganAMNIST"])
    ax.set_title(title)
    for yy in range(piv.shape[0]):
        for xx in range(piv.shape[1]):
            val = piv.values[yy, xx]
            if not pd.isna(val):
                ax.text(xx, yy, f"{val:.3f}", ha="center", va="center", fontsize=8)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
fig.tight_layout(); fig.savefig(FIG / "fig2-calibration-brier-summary.png", dpi=180); plt.close(fig)
print("regenerated public figures in", FIG)
