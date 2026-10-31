"""Calibrated steel illustration for paper 1.1 (working paper v0.4).

Intensities: EU CBAM default values for hot-rolled flat steel (CN 7208),
direct emissions, tCO2/t, from CBAM-default-values-steel-aluminium-cement.csv
(Implementing Regulation (EU) 2025/2621). Everything else is stylized and
labelled so in the paper:
  - base price c0 = $600/t for every exporter [stylized: between the 2025 world export price of hot-rolled band,
    about $440-485/t FOB, and the Western European ex-works price, about $630-750/t (SteelBenchmarker)]
  - abatement slope k_i set so that a $50/tCO2 rate cuts intensity by 30 percent
  - Armington elasticity sigma = 5.9 among import sources: the estimate for ferrous metals in Hertel, Hummels,
    Ivanic and Keeney (2007, Table 1). The working paper reports sigma = 4 as a sensitivity check.
  - equal preference weights (equal shares before any carbon charge)
  - abatement floor: intensity cannot fall below 30 percent of the default value
    within the horizon considered [stylized]
Outputs: figures/fig2_*.png, figures/fig4_*.png and table1_price_effects.csv.
Run from this folder.
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

EXPORTERS = ["Japan", "South Korea", "Vietnam", "Türkiye", "China", "South Africa", "India", "Indonesia"]
e0 = {}
with open("CBAM-default-values-steel-aluminium-cement.csv") as f:
    for row in csv.reader(f):
        if len(row) > 4 and row[1].startswith("7208") and row[0] in EXPORTERS:
            e0[row[0]] = float(row[3])
E = np.array([e0[c] for c in EXPORTERS])
c0, sigma = 600.0, 5.9
k = 50 / (0.3 * E)                     # k_i: $50/t cuts intensity by 30%

FLOOR = 0.3 * E

def intensity(t):
    return np.maximum(E - t / k, FLOOR)

def delivered(t, tau):
    e = intensity(t)
    return c0 + k / 2 * (E - e) ** 2 + tau * e   # resource cost + destination charge

def shares(p):
    w = p ** (-sigma)
    return w / w.sum()

# Table 1: price effect of a tax vs a feebate at $80/tCO2
rate = 80.0
e_star = intensity(rate)
tax_rise = rate * e_star + k / 2 * (E - e_star) ** 2
fee_rise = k / 2 * (E - e_star) ** 2
with open("table1_price_effects.csv", "w", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["exporter", "default_intensity_tCO2_per_t", "intensity_after_80", "price_rise_tax_usd", "price_rise_feebate_usd", "tax_pct", "feebate_pct"])
    for i, c in enumerate(EXPORTERS):
        w.writerow([c, f"{E[i]:.2f}", f"{e_star[i]:.2f}", f"{tax_rise[i]:.0f}", f"{fee_rise[i]:.0f}",
                    f"{100*tax_rise[i]/c0:.0f}", f"{100*fee_rise[i]/c0:.1f}"])

# Race to the top: importer destination charge tau from 0 to 150
taus = np.linspace(0, 150, 151)
avg_e_passive, avg_e_br, share_clean_p, share_clean_br, share_dirty_p, share_dirty_br = [], [], [], [], [], []
clean, dirty = EXPORTERS.index("Japan"), EXPORTERS.index("Indonesia")
for tau in taus:
    p_passive = delivered(np.zeros_like(E), tau)
    s_p = shares(p_passive)
    t_br = np.full_like(E, tau)            # Proposition 5: best response t_i = tau
    p_br = delivered(t_br, tau)
    s_b = shares(p_br)
    avg_e_passive.append((s_p * E).sum())
    avg_e_br.append((s_b * intensity(t_br)).sum())
    share_clean_p.append(s_p[clean]); share_clean_br.append(s_b[clean])
    share_dirty_p.append(s_p[dirty]); share_dirty_br.append(s_b[dirty])

plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans"})
fig, ax = plt.subplots(1, 2, figsize=(9, 3.3))
ax[0].plot(taus, avg_e_passive, color="#9e9e9e", lw=2, label="Exporters do nothing")
ax[0].plot(taus, avg_e_br, color="#2e7d32", lw=2, label="Exporters set feebate t = τ")
ax[0].set_title("A. Average embodied intensity of imports (tCO₂/t)")
ax[0].set_xlabel("Importer's destination charge τ (\\$/tCO₂)")
ax[0].legend(frameon=False)
for lab, sp_, sb_, col in [("Japan (2.1)", share_clean_p, share_clean_br, "#1f4e79"), ("Indonesia (8.2)", share_dirty_p, share_dirty_br, "#c62828")]:
    ax[1].plot(taus, np.array(sp_) * 100, color=col, lw=1.2, ls="--")
    ax[1].plot(taus, np.array(sb_) * 100, color=col, lw=2, label=lab)
ax[1].set_title("B. Import market share (%), solid = with feebates")
ax[1].set_xlabel("Importer's destination charge τ (\\$/tCO₂)")
ax[1].legend(frameon=False, title="Default intensity", fontsize=8, title_fontsize=8)
for a in ax:
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("figures/fig4_race_to_top.png", dpi=200)

fig, ax = plt.subplots(figsize=(6.5, 3.2))
x = np.arange(len(EXPORTERS))
ax.bar(x - 0.2, tax_rise, 0.4, color="#1f4e79", label="Carbon tax at \\$80/tCO₂")
ax.bar(x + 0.2, fee_rise, 0.4, color="#2e7d32", label="Feebate at \\$80/tCO₂")
ax.set_xticks(x, [f"{c}\n{E[i]:.1f}" for i, c in enumerate(EXPORTERS)], fontsize=7)
ax.set_ylabel("Rise in producer price (\\$/t)")
ax.set_title("Price effect of a carbon tax and a feebate, hot-rolled steel")
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("figures/fig2_price_effects_by_exporter.png", dpi=200)
print("intensities:", dict(zip(EXPORTERS, E.round(2))))
print("avg intensity at tau=100: passive %.2f, feebates %.2f" % (avg_e_passive[100], avg_e_br[100]))
print("Indonesia share at tau=100: passive %.1f%%, feebates %.1f%%" % (100*share_dirty_p[100], 100*share_dirty_br[100]))
