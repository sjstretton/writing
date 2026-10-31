"""Figure for Climate Fiscal Policy Brief No. 1.3 (scrap shuffling).

Stylized exporter: 10 Mt of crude steel a year, 8 Mt by blast furnace-basic
oxygen furnace (BF-BOF) at 2.0 tCO2/t and 2 Mt by scrap-based electric arc
furnace (scrap-EAF) at 0.4 tCO2/t. It sells 1 Mt to the EU. CBAM certificate
price EUR 80/tCO2; free-allocation adjustment and default mark-ups ignored
(the position once CBAM is fully phased in, 2034). All numbers stylized.

Run from this folder:  python make_figures.py
"""
import matplotlib.pyplot as plt

# Stylized inputs
Q_BOF, Q_EAF = 8.0, 2.0          # Mt crude steel
E_BOF, E_EAF = 2.0, 0.4          # tCO2 per tonne
Q_EU = 1.0                       # Mt sold to the EU
P = 80.0                         # EUR per tCO2

total = Q_BOF * E_BOF + Q_EAF * E_EAF            # MtCO2, 16.8
avg = total / (Q_BOF + Q_EAF)                     # 1.68 tCO2/t

eu_prop = Q_EU * avg                              # 1.68 MtCO2
eu_shuf = Q_EU * E_EAF                            # 0.40 MtCO2

charge_inst_prop = eu_prop * P                    # EUR m
charge_inst_shuf = eu_shuf * P
charge_country = Q_EU * avg * P                   # same either way

print(f"average intensity {avg:.2f}; total {total:.1f} MtCO2")
print(f"EU-bound emissions: proportional {eu_prop:.2f}, shuffled {eu_shuf:.2f}")
print(f"charges EUR m: installation prop {charge_inst_prop:.0f}, "
      f"installation shuffled {charge_inst_shuf:.0f}, country basis {charge_country:.0f}")

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED = "#0b0b0b", "#52514e"
plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans",
                     "text.color": INK, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED})

fig, ax = plt.subplots(1, 3, figsize=(10, 3.4))
labels = ["Exports drawn\nfrom the average mix", "Exports drawn\nfrom scrap-EAF only"]
cols = [BLUE, ORANGE]


def bars(a, vals, fmt, title, ylim):
    xs = range(len(vals))
    b = a.bar(xs, vals, color=cols[:len(vals)], width=0.55, edgecolor="white", linewidth=2)
    for x, v in zip(xs, vals):
        a.annotate(fmt.format(v), (x, v), textcoords="offset points", xytext=(0, 3),
                   ha="center", fontsize=9, color=INK)
    a.set_xticks(list(xs))
    a.set_title(title, fontsize=9.5, loc="left", color=INK)
    a.set_ylim(0, ylim)
    a.spines[["top", "right"]].set_visible(False)
    a.spines[["left", "bottom"]].set_color("#b9b8b3")
    a.yaxis.grid(True, color="#e6e5e0", lw=0.6)
    a.set_axisbelow(True)
    return b


bars(ax[0], [eu_prop, eu_shuf], "{:.2f}", "A. What the border sees:\nemissions in EU-bound steel (MtCO₂)", 2.2)
ax[0].set_xticklabels(labels, fontsize=8)

bars(ax[1], [total, total], "{:.1f}", "B. What the atmosphere sees:\nthe exporter's total emissions (MtCO₂)", 20)
ax[1].set_xticklabels(labels, fontsize=8)

vals = [charge_inst_prop, charge_inst_shuf, charge_country]
b = ax[2].bar(range(3), vals, color=[BLUE, ORANGE, "#8a8984"], width=0.55,
              edgecolor="white", linewidth=2)
for x, v in enumerate(vals):
    ax[2].annotate(f"€{v:.0f}m", (x, v), textcoords="offset points", xytext=(0, 3),
                   ha="center", fontsize=9, color=INK)
ax[2].set_xticks(range(3))
ax[2].set_xticklabels(["Installation\nbasis, average\nmix", "Installation\nbasis,\nshuffled",
                       "Country-sector\nbasis, either\nrouting"], fontsize=8)
ax[2].set_title("C. CBAM charge on 1 Mt of exports\nat €80/tCO₂ (€ million)", fontsize=9.5,
                loc="left", color=INK)
ax[2].set_ylim(0, 165)
ax[2].spines[["top", "right"]].set_visible(False)
ax[2].spines[["left", "bottom"]].set_color("#b9b8b3")
ax[2].yaxis.grid(True, color="#e6e5e0", lw=0.6)
ax[2].set_axisbelow(True)

fig.tight_layout()
fig.savefig("fig1_scrap_shuffling.png", dpi=200, facecolor="white")
