"""Figure 1 of paper 1.1 (v0.3): carbon charges by regime and trade flow.

Stylized home country with a rate of $80/tCO2. Home producers: default
intensity 2.4 tCO2/t (close to the Türkiye hot-rolled default value); foreign
supplier: 3.2 tCO2/t (close to China's). Base price $600/t; abatement slope
set so $50/tCO2 cuts intensity 30 percent. Foreign country prices nothing.
Run from 2.Source/.
"""
import numpy as np
import matplotlib.pyplot as plt

rate, c0 = 80.0, 600.0
eH, eF = 2.4, 3.2
kH, kF = 50 / (0.3 * eH), 50 / (0.3 * eF)
eH_star = eH - rate / kH
abate_H = kH / 2 * (eH - eH_star) ** 2          # resource cost of home abatement
# Each bar: [resource cost of abatement, carbon charge paid at home, carbon charge paid abroad]
flows = ["Home producer,\nsold at home", "Home producer,\nexported", "Foreign producer,\nimported"]
regimes = {
    "Origin carbon tax": [
        [abate_H, rate * eH_star, 0],
        [abate_H, rate * eH_star, 0],
        [0, 0, 0]],
    "Origin tax + border adjustment\n(CBAM-type)": [
        [abate_H, rate * eH_star, 0],
        [abate_H, rate * eH_star, 0],
        [0, rate * eF, 0]],
    "Two tracks: feebate +\ndestination charge": [
        [abate_H, rate * eH_star, 0],
        [abate_H, 0, 0],
        [0, rate * eF, 0]],
}
plt.rcParams.update({"font.size": 8.5, "font.family": "DejaVu Sans"})
fig, axes = plt.subplots(1, 3, figsize=(10, 3.4), sharey=True)
cols = ["#a5d6a7", "#1f4e79"]
for ax, (name, vals) in zip(axes, regimes.items()):
    x = np.arange(3)
    v = np.array(vals)
    ax.bar(x, v[:, 0], color=cols[0], label="Resource cost of abatement")
    ax.bar(x, v[:, 1], bottom=v[:, 0], color=cols[1], label="Carbon charge collected at home")
    ax.set_xticks(x, flows, fontsize=7.5)
    ax.set_title(name, fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    for i in range(3):
        tot = v[i, 0] + v[i, 1]
        ax.annotate(f"\\${tot:.0f}", (i, tot), ha="center", va="bottom", fontsize=8)
axes[0].set_ylabel("Carbon-related cost added to a tonne of steel (\\$)")
axes[0].legend(frameon=False, fontsize=7.5, loc="upper right")
fig.tight_layout()
fig.savefig("figures/fig1_incidence_by_regime.png", dpi=200)
print("home intensity after abatement %.2f; abatement cost $%.0f/t; charge on home sales $%.0f/t; on imports $%.0f/t"
      % (eH_star, abate_H, rate * eH_star, rate * eF))
