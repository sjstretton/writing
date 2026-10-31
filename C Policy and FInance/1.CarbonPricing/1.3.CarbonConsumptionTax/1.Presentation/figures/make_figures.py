"""Figures and check calculations for Climate Fiscal Policy Brief No. 1.3.

Run from any directory:  python3 make_figures.py
Prints every number used in the brief's tables and writes fig1-effective-rates.png
beside this script.

Units: carbon intensity e in kg CO2 per euro of value (net of VAT); carbon price
P in EUR per tonne CO2. A carbon component of P EUR/t on a good of intensity e
equals P * e / 1000 euros per euro of value, i.e. P * e / 10 percentage points.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
YEARS = list(range(2027, 2038))


def value_vat(year, start=15.0, step=0.5):
    """Value component of VAT, percent: falls `step` pp a year from 2027."""
    return start - step * (year - 2027)


def carbon_price(year, step=20.0):
    """Carbon component price, EUR/tCO2: rises `step` a year from zero in 2027."""
    return step * (year - 2027)


def carbon_pp(price, e):
    """Carbon component in percentage points of value."""
    return price * e / 10.0


def total_rate(year, e):
    return value_vat(year) + carbon_pp(carbon_price(year), e)


def main():
    # 1. What a VAT rate is "worth" per tonne at a given intensity.
    print("1. Implied EUR/tCO2 of a VAT rate = rate / intensity")
    for e in (0.10, 0.25, 0.30, 0.35, 0.50, 1.00):
        print(f"   e={e:.2f} kg/EUR: 15% -> {0.15 / (e / 1000):6.0f} EUR/t;"
              f" 20% -> {0.20 / (e / 1000):6.0f} EUR/t")

    # 2. Break-even intensity: carbon component exactly replaces value VAT cut.
    #    0.5 pp per year == 20 EUR/t * e / 10  ->  e = 0.25 kg/EUR
    print("2. Break-even intensity (kg/EUR):", 0.5 * 10 / 20)

    # 3. Effective rate by product intensity.
    print("3. Total effective VAT rate (%) by intensity")
    grid = (0.05, 0.10, 0.15, 0.25, 0.40, 1.00)
    for y in (2027, 2030, 2032, 2035, 2037):
        row = "  ".join(f"{total_rate(y, e):5.2f}" for e in grid)
        print(f"   {y}: V={value_vat(y):5.2f} P={carbon_price(y):4.0f}  {row}")

    # 4. Source paper's EU-producer and China-exporter paths (linear intensities).
    print("4. Source check: EU 0.20->0.15, China 0.40->0.25, linear")
    peak = (0, None)
    for y in YEARS:
        k = (y - 2027) / 10
        e_eu = 0.20 - 0.05 * k
        e_cn = 0.40 - 0.15 * k
        t_eu, t_cn = total_rate(y, e_eu), total_rate(y, e_cn)
        if t_cn - 15 > peak[0]:
            peak = (t_cn - 15, y)
        print(f"   {y}: EU e={e_eu:.3f} total={t_eu:6.3f} | CN e={e_cn:.3f} total={t_cn:6.3f}")
    print(f"   China peak excess over 15%: {peak[0]:.3f} pp in {peak[1]}")

    # 5. Fiscal: net revenue change in 2037, pp of the taxed base, by basket intensity;
    #    and the VAT cut that would be revenue-neutral at 200 EUR/t.
    print("5. 2037 net revenue change (pp of base) and neutral VAT cut at EUR 200/t")
    for e in (0.10, 0.15, 0.20, 0.25, 0.30):
        net = carbon_pp(200, e) - 5.0
        print(f"   basket e={e:.2f}: net {net:+.1f} pp; neutral cut {carbon_pp(200, e):.1f} pp")
    # Source's round numbers on an assumed EUR 9 trillion base at 0.3 kg/EUR.
    base = 9e12
    print(f"   0.5 pp of EUR 9tn = EUR {0.005 * base / 1e9:.0f}bn;"
          f" EUR 20/t at 0.3 kg/EUR = EUR {20 * 0.3e-3 * base / 1e9:.0f}bn")

    # 6. Worked example: EUR 100 good (net of VAT) in 2032.
    print("6. Worked example, 2032, EUR 100 good")
    v, p = value_vat(2032), carbon_price(2032)
    for label, e in (("default 0.25", 0.25), ("dirty 0.40", 0.40), ("verified 0.10", 0.10)):
        c = p * e * 100 / 1000
        print(f"   {label}: value VAT {v:.2f} + carbon {c:.2f} = {v + c:.2f} EUR")

    # 7. Energy example: natural gas ~0.202 kgCO2/kWh (IPCC default 56.1 tCO2/TJ).
    ef = 56.1 / 277.78  # tCO2 per MWh
    print(f"7. Gas: {ef:.3f} tCO2/MWh -> EUR {ef * 200:.1f}/MWh at EUR 200/t;"
          f" EUR {ef * 100:.1f}/MWh at EUR 100/t")

    make_figure()


def make_figure():
    # Ordinal blue ramp (reference palette, steps 250 -> 700), light = clean.
    series = [
        (0.10, "#86b6ef"),
        (0.15, "#5598e7"),
        (0.25, "#2a78d6"),
        (0.40, "#1c5cab"),
        (0.60, "#0d366b"),
    ]
    ink, muted, grid = "#0b0b0b", "#52514e", "#e4e3df"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, ax = plt.subplots(figsize=(7.0, 4.2), dpi=200)
    fig.patch.set_facecolor("white")
    for e, col in series:
        ys = [total_rate(y, e) for y in YEARS]
        ax.plot(YEARS, ys, color=col, lw=2, zorder=3)
        tag = ", break-even" if e == 0.25 else ""
        ax.text(2037.15, ys[-1], f"{e:.2f} kg/€  ({ys[-1]:.0f}%{tag})", va="center",
                fontsize=8.5, color=ink)
    ax.plot(YEARS, [value_vat(y) for y in YEARS], color=muted, lw=1.2, zorder=2)
    ax.text(2037.15, value_vat(2037), "Value component only (10%)", va="center",
            color=muted, fontsize=8.5)
    ax.set_xlim(2027, 2040.4)
    ax.set_ylim(8, 23)
    ax.set_xticks(range(2027, 2038, 2))
    ax.set_ylabel("Total VAT rate on the good (%)", color=ink)
    ax.grid(axis="y", color=grid, lw=0.8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(muted)
    ax.tick_params(colors=muted)
    ax.set_title("Effective VAT rate by embodied-carbon intensity, 2027–2037",
                 loc="left", fontsize=11, color=ink)
    fig.text(0.01, 0.01,
             "Value component falls 0.5 pp a year (15% to 10%); carbon component rises "
             "€20/tCO₂ a year (€0 to €200).\nIntensity in kg CO₂ per euro of value. "
             "Goods at 0.25 kg/€ pay 15% throughout. Stylized.",
             fontsize=7.5, color=muted)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    out = HERE / "fig1-effective-rates.png"
    fig.savefig(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
