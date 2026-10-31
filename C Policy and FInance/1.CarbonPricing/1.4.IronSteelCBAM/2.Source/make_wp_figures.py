"""Calibration tables and figures for the working paper IronSteelCBAM.qmd (v0.4).

Data: EU CBAM default values, direct emissions, Annex I of Commission
Implementing Regulation (EU) 2025/2621 (checked against the Official Journal
text on 31 Oct 2026; the Commission workbook of 4 February 2026 reproduces it). The extract used here is the public CSV in
../../1.1.OpenEconomyCarbonPricing/2.Source/CBAM-default-values-steel-aluminium-cement.csv,
cross-checked against the workbook (route codes read from the workbook).

Everything else is stylized and labelled so: certificate price EUR 80/tCO2;
full phase-in (no free-allocation adjustment, as from 2034); 2028-onward
mark-up of 30 percent; scrap-EAF steel at 0.4 tCO2/t and blast-furnace steel
at 2.0 tCO2/t in the stylized exporter (IEA 2020, Box 1.3: 0.3 and 2.2 direct
plus indirect; 0.04 and 1.2 direct); abatement slope as in paper 1.1
(a EUR 50 rate cuts intensity by 30 percent, so k*e0 = EUR 166.7/tCO2).

Run from this folder:  python make_wp_figures.py
Writes figures/fig1_shuffling_model.png, figures/fig2_exporters.png,
figures/fig3_best_response.png and table_steel.csv, table_aluminium.csv.
"""
import csv
import os

import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "1.1.OpenEconomyCarbonPricing", "2.Source",
                    "CBAM-default-values-steel-aluminium-cement.csv")
FIG = os.path.join(HERE, "figures")
os.makedirs(FIG, exist_ok=True)

TAU = 80.0          # EUR per tCO2 (stylized certificate price)
MARKUP = 0.30       # 2028 onward, iron and steel and aluminium (Reg. 2025/2621)
E_SCRAP = 0.4       # tCO2/t, scrap-EAF steel (stylized; IEA 2020 gives 0.3 direct+indirect)
E_SECONDARY_AL = 0.36  # tCO2/t, lowest country default for unwrought aluminium
KE0 = 50 / 0.3      # EUR/tCO2: k*e0 from paper 1.1's calibration

STEEL = ["Indonesia", "Kazakhstan", "India", "South Africa", "Other countries", "China",
         "Ukraine", "Türkiye", "United Kingdom", "Vietnam", "Taiwan", "Japan", "Brazil"]
ALU = ["Mozambique", "China", "South Africa", "Other countries", "Russia", "India",
       "United Arab Emirates", "Bahrain", "Brazil", "Saudi Arabia"]

# ---------------------------------------------------------------- data
dv = {}
with open(DATA, encoding="utf-8") as f:
    rows = [r for r in f if not r.lstrip("\"").startswith("#")]
for r in csv.DictReader(rows):
    dv[(r["country"], r["cn_code"])] = float(r["direct"])


def steel_row(c):
    d = dv[(c, "7208")]
    lia_def = TAU * d * (1 + MARKUP)       # default value with 2028 mark-up
    lia_cs = TAU * d                       # country-sector average, no mark-up
    return dict(country=c, dv=d, dv_markup=d * (1 + MARKUP),
                liability_default=lia_def, liability_country=lia_cs,
                value_feebate40=lia_def - (TAU - 40) * d,   # rho = 1, t = 40
                value_feebate80=lia_def,                    # rho = 1, t = 80
                markup_part=lia_def - lia_cs, recognition40=40 * d,
                shuffle_vs_average=TAU * (d - E_SCRAP),
                shuffle_vs_default=TAU * (d * (1 + MARKUP) - E_SCRAP))


steel = [steel_row(c) for c in STEEL]
alu = []
for c in ALU:
    d = dv[(c, "7601")]
    alu.append(dict(country=c, dv=d, liability_default=TAU * d * (1 + MARKUP),
                    liability_country=TAU * d,
                    shuffle_vs_average=TAU * (d - E_SECONDARY_AL)))

for name, tab in (("table_steel.csv", steel), ("table_aluminium.csv", alu)):
    with open(os.path.join(HERE, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(tab[0].keys()))
        w.writeheader()
        for row in tab:
            w.writerow({k: (round(v, 3) if isinstance(v, float) else v) for k, v in row.items()})

print("Steel, CN 7208, EUR per tonne at EUR 80/tCO2 (full phase-in)")
print(f"{'country':18s} {'DV':>5s} {'def+mk':>7s} {'ctry':>6s} {'rec40':>6s} {'rec80':>6s} {'shufA':>6s} {'shufD':>6s}")
for r in steel:
    print(f"{r['country']:18s} {r['dv']:5.2f} {r['liability_default']:7.0f} {r['liability_country']:6.0f} "
          f"{r['value_feebate40']:6.0f} {r['value_feebate80']:6.0f} {r['shuffle_vs_average']:6.0f} {r['shuffle_vs_default']:6.0f}")
print("\nAluminium, CN 7601")
for r in alu:
    print(f"{r['country']:22s} {r['dv']:5.2f} {r['liability_default']:6.0f} {r['liability_country']:6.0f} {r['shuffle_vs_average']:6.0f}")

# ---------------------------------------------------------------- style
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
GREY = "#8a8984"
INK, MUTED, GRID, AXIS = "#0b0b0b", "#52514e", "#e6e5e0", "#b9b8b3"
plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans", "text.color": INK,
                     "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.edgecolor": AXIS})


def tidy(a, grid_axis="y"):
    a.spines[["top", "right"]].set_visible(False)
    a.spines[["left", "bottom"]].set_color(AXIS)
    getattr(a, f"{grid_axis}axis").grid(True, color=GRID, lw=0.6)
    a.set_axisbelow(True)


def label_bars(a, xs, vals, fmt):
    for x, v in zip(xs, vals):
        a.annotate(fmt.format(v), (x, v), textcoords="offset points", xytext=(0, 3),
                   ha="center", fontsize=8.5, color=INK)


# ---------------------------------------------------------------- figure 1
QB, QS, EB, ES, QEU = 8.0, 2.0, 2.0, 0.4, 1.0    # stylized exporter (Mt, tCO2/t)
total = QB * EB + QS * ES
avg = total / (QB + QS)
eu_prop, eu_shuf = QEU * avg, QEU * ES
fig, ax = plt.subplots(1, 3, figsize=(10, 3.5))
lab = ["Proportional\nsourcing", "Scrap-EAF\nto the EU"]
ax[0].bar([0, 1], [eu_prop, eu_shuf], color=[BLUE, ORANGE], width=0.55, edgecolor="white", lw=2)
label_bars(ax[0], [0, 1], [eu_prop, eu_shuf], "{:.2f}")
ax[0].set_title("A. Embodied carbon the border sees\n(MtCO₂ in 1 Mt of EU-bound steel)", loc="left", fontsize=9.5)
ax[0].set_ylim(0, 2.2)
ax[1].bar([0, 1], [total, total], color=[BLUE, ORANGE], width=0.55, edgecolor="white", lw=2)
label_bars(ax[1], [0, 1], [total, total], "{:.1f}")
ax[1].set_title("B. The exporter's emissions\n(MtCO₂ a year)", loc="left", fontsize=9.5)
ax[1].set_ylim(0, 20)
for a in ax[:2]:
    a.set_xticks([0, 1])
    a.set_xticklabels(lab, fontsize=8)
vals = [eu_prop * TAU, eu_shuf * TAU, avg * QEU * TAU]
ax[2].bar(range(3), vals, color=[BLUE, ORANGE, GREY], width=0.55, edgecolor="white", lw=2)
for x, v in enumerate(vals):
    ax[2].annotate(f"€{v:.0f}m", (x, v), textcoords="offset points", xytext=(0, 3), ha="center", fontsize=8.5)
ax[2].set_xticks(range(3))
ax[2].set_xticklabels(["Plant-level,\nproportional", "Plant-level,\nshuffled", "Country-sector,\neither routing"], fontsize=8)
ax[2].set_title("C. CBAM charge at €80/tCO₂\n(€ million a year)", loc="left", fontsize=9.5)
ax[2].set_ylim(0, 165)
for a in ax:
    tidy(a)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig1_shuffling_model.png"), dpi=200, facecolor="white")
plt.close(fig)

# ---------------------------------------------------------------- figure 2
fig, ax = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
names = [r["country"] for r in steel]
y = np.arange(len(names))[::-1]
h = 0.38
ax[0].barh(y + h / 2, [r["liability_default"] for r in steel], height=h, color=BLUE,
           edgecolor="white", lw=1, label="Default value with 30% mark-up")
ax[0].barh(y - h / 2, [r["liability_country"] for r in steel], height=h, color=AQUA,
           edgecolor="white", lw=1, label="Country-sector average, no mark-up")
ax[0].set_yticks(y)
ax[0].set_yticklabels([f"{n} ({r['dv']:.2f})" for n, r in zip(names, steel)], fontsize=8)
ax[0].set_title("A. CBAM liability on hot-rolled flat steel\n(€ per tonne, €80/tCO₂, full phase-in)", loc="left", fontsize=9.5)
ax[0].legend(frameon=False, fontsize=8, loc="lower right")
ax[1].barh(y, [r["shuffle_vs_average"] for r in steel], height=0.55, color=ORANGE, edgecolor="white", lw=1)
for yy, r in zip(y, steel):
    ax[1].annotate(f"€{r['shuffle_vs_average']:.0f}", (r["shuffle_vs_average"], yy), textcoords="offset points",
                   xytext=(3, -3), fontsize=8)
ax[1].set_title("B. Gain from supplying the EU from scrap-EAF\n(€ per tonne switched, against the country average)", loc="left", fontsize=9.5)
ax[1].set_xlim(0, 760)
for a in ax:
    tidy(a, "x")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig2_exporters.png"), dpi=200, facecolor="white")
plt.close(fig)

# ---------------------------------------------------------------- figure 3
mu = np.linspace(0, 1, 201)


def t_star(mu, rho):
    t = mu * (TAU + rho * KE0) / (1 + 2 * rho * mu)
    cap = TAU / rho if rho > 0 else np.inf
    return np.minimum(t, cap)


fig, ax = plt.subplots(1, 2, figsize=(10, 3.7))
for rho, col, nm in ((0, GREY, "Price paid only (ρ = 0)"), (1, BLUE, "Full signal (ρ = 1)")):
    ax[0].plot(mu * 100, t_star(mu, rho), color=col, lw=2, label=nm)
ax[0].axhline(TAU, color=MUTED, lw=0.8, ls="--")
ax[0].annotate("τ = €80", (100, TAU + 2), fontsize=8, color=MUTED, ha="right")
ax[0].set_xlabel("Share of the sector's output sold to the EU (%)")
ax[0].set_ylabel("€ per tCO₂")
ax[0].set_title("A. The exporting country's best feebate rate", loc="left", fontsize=9.5)
ax[0].set_ylim(0, 100)
ax[0].legend(frameon=False, fontsize=8, loc="lower right")
g0 = (TAU / KE0) * (mu - 0.5)              # net gain at t = tau, share of tau*e0, rho = 0
g1 = mu - TAU / (2 * KE0)                  # rho = 1
ax[1].plot(mu * 100, g0 * 100, color=GREY, lw=2, label="Price paid only (ρ = 0)")
ax[1].plot(mu * 100, g1 * 100, color=BLUE, lw=2, label="Full signal (ρ = 1)")
ax[1].axhline(0, color=MUTED, lw=0.8)
for m, col in ((0.5, GREY), (TAU / (2 * KE0), BLUE)):
    ax[1].plot([m * 100], [0], "o", ms=7, color=col, mec="white", mew=2)
    ax[1].annotate(f"{m*100:.0f}%", (m * 100, 0), textcoords="offset points", xytext=(4, -13), fontsize=8, color=INK)
ax[1].set_xlabel("Share of the sector's output sold to the EU (%)")
ax[1].set_ylabel("% of the baseline carbon bill τe₀")
ax[1].set_title("B. Net gain from a feebate at €80, per tonne of output", loc="left", fontsize=9.5)
ax[1].legend(frameon=False, fontsize=8, loc="upper left")
for a in ax:
    tidy(a)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig3_best_response.png"), dpi=200, facecolor="white")
plt.close(fig)
print("\nfigures written to", FIG)
for m in (0.1, 0.25, 0.5):
    print(f"mu={m}: t* rho=0 {t_star(m,0):.1f}, rho=0.5 {t_star(m,0.5):.1f}, rho=1 {t_star(m,1):.1f}")
