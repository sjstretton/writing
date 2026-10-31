"""Figures for Climate Fiscal Policy Brief No. 1.1.

Stylized steel-like sector: e0 = 2 tCO2/t, p0 = $600/t, k chosen so that
t = $50/tCO2 cuts intensity by 30 percent (k = 50/0.6). Run from this folder.
"""
import numpy as np
import matplotlib.pyplot as plt

e0, p0 = 2.0, 600.0
k = 50 / 0.6
t = np.linspace(0, 120, 241)

plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans"})
fig, ax = plt.subplots(1, 3, figsize=(10, 3.2))

# Panel A: producer price increase, tax vs feebate
ax[0].plot(t, t * e0 - t**2 / (2 * k), color="#1f4e79", lw=2, label="Carbon tax")
ax[0].plot(t, t**2 / (2 * k), color="#2e7d32", lw=2, label="Revenue-neutral feebate")
ax[0].set_title("A. Rise in producer price (\\$/t)")
ax[0].set_xlabel("Rate t (\\$/tCO₂)")
ax[0].legend(frameon=False)
ax[0].axvline(50, color="grey", lw=0.6, ls=":")
ax[0].annotate("\\$85", (50, 85), textcoords="offset points", xytext=(4, 2))
ax[0].annotate("\\$15", (50, 15), textcoords="offset points", xytext=(4, 2))

# Panel B: country's net cost of a feebate with a crediting price pi = $50
pi = 50.0
Q = 1.0
net = Q * t * (t - 2 * pi) / (2 * k)
ax[1].plot(t, net, color="#2e7d32", lw=2)
ax[1].axhline(0, color="black", lw=0.6)
ax[1].axvline(pi, color="grey", lw=0.6, ls=":")
ax[1].set_title("B. Country's net cost (\\$/t of output),\ncrediting price π = \\$50/tCO₂")
ax[1].set_xlabel("Feebate rate t (\\$/tCO₂)")
ax[1].annotate("best response t = π", (pi, net.min()), textcoords="offset points", xytext=(6, -2))
ax[1].annotate("net gain while t < 2π", (20, 3), fontsize=8)

# Panel C: exporter delivered cost vs own feebate rate, for importer charges tau
for tau, c in [(25, "#9ecae1"), (50, "#4292c6"), (100, "#08519c")]:
    D = t**2 / (2 * k) + tau * (e0 - t / k)
    ax[2].plot(t, D, color=c, lw=2, label=f"importer charge τ = \\${tau}")
    ax[2].plot(tau, tau**2 / (2 * k) + tau * (e0 - tau / k), "o", color=c, ms=4)
ax[2].set_title("C. Exporter's delivered carbon cost (\\$/t)")
ax[2].set_xlabel("Exporter's feebate rate tᵢ (\\$/tCO₂)")
ax[2].legend(frameon=False, fontsize=7)

for a in ax:
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("fig1_two_track_results.png", dpi=200)
print("wrote fig1_two_track_results.png")
