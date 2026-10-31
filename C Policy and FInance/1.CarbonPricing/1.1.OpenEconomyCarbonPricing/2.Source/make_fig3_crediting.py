"""Figure 3 of paper 1.1 (v0.4): the adopting country's net cost of a feebate under a crediting payment.

Calibrated to the steel illustration (Section 5): a sector at Türkiye's EU default intensity for hot-rolled steel,
2.43 tCO2/t, with the abatement slope set so that $50/tCO2 cuts intensity by 30 percent (k = 50 / (0.3 * 2.43)).
An outside buyer pays pi = $50 per tonne abated below the unpriced baseline. Net cost per tonne of steel:
N(t)/Q = t (t - 2 pi) / 2k  (Proposition 6). Run from 2.Source/.
"""
import numpy as np
import matplotlib.pyplot as plt

e0, pi = 2.43, 50.0
k = 50 / (0.3 * e0)
t = np.linspace(0, 120, 241)
net = t * (t - 2 * pi) / (2 * k)

plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans"})
fig, ax = plt.subplots(figsize=(6, 3.2))
ax.axhline(0, color="#9e9e9e", lw=0.8)
ax.plot(t, net, color="#2e7d32", lw=2)
ax.fill_between(t, net, 0, where=net < 0, color="#a5d6a7", alpha=0.6, label="Country gains")
best = pi
ax.plot([best], [best * (best - 2 * pi) / (2 * k)], "o", color="#1f4e79")
ax.annotate(f"Best rate t = π = \\${pi:.0f}: gain \\${-best*(best-2*pi)/(2*k):.0f} per tonne of steel",
            (best, best * (best - 2 * pi) / (2 * k)), xytext=(14, 10), textcoords="offset points", fontsize=8)
ax.annotate("Break-even at t = 2π = \\$100", (2 * pi, 0), xytext=(-60, 14), textcoords="offset points", fontsize=8,
            arrowprops=dict(arrowstyle="-", color="#6b7b6e", lw=0.8))
ax.set_xlabel("Feebate rate t (\\$/tCO₂)")
ax.set_ylabel("Net cost to the country (\\$ per tonne of steel)")
ax.set_title("Net cost of a feebate with a crediting payment of \\$50/tCO₂", fontsize=9.5)
ax.legend(frameon=False, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("figures/fig3_crediting.png", dpi=200)
print("k = %.1f; gain at t = pi: $%.1f per tonne of steel" % (k, -pi * (pi - 2 * pi) / (2 * k)))
