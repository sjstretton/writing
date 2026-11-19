"""Write Appendix B of note 6.8 (SISEPUEDE transformations mapped to CPAT) from the transformation table.

    python make_appendix_b.py TABLE_CSV public   > appendix_b_public.md
    python make_appendix_b.py TABLE_CSV internal GROUP_XLSX FIGURE_PATH > appendix_b_internal.md

TABLE_CSV is SISEPUEDE_transformations_to_CPAT.csv, made by build_transformation_table.py (kept with the
CPAT-SISEPUEDE project files). The public edition reports only public inputs: the SISEPUEDE repository, the
cost-benefit module and CPAT's public data. The internal edition adds the abatement costs of one SISEPUEDE country run.
"""
import csv
import sys

TABLE, MODE = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(TABLE, encoding="utf-8")))
ok = [r for r in rows if r["MAC alone, USD/tCO2e (SISEPUEDE run)"]]


def base(r):
    b = r["Base size in CPAT, median across countries (p10 to p90)"]
    if not b:
        return "–"
    unit = "energy" if "energy" in r["Base unit"] else "GHG"
    return f"{b.split(' (')[0]}% {unit}"


def mapping(r):
    return r["Mapping"].replace("; gap", " (gap").replace("(gap (", "(gap: ") + (")" if "; gap" in r["Mapping"] else "")


def status(r):
    s = r["Status alone"]
    if r["MAC alone, USD/tCO2e (SISEPUEDE run)"]:
        return r["MAC alone, USD/tCO2e (SISEPUEDE run)"]
    return {"not in run": "not in run", "blank": "–"}.get(s, "raises emissions" if s.startswith("increases") else
                                                        "no abatement" if s.startswith("no_") else "–")


def default(r):
    d = r["Default magnitude (transformers.py)"]
    return (d[:38] + "…") if len(d) > 39 else (d or "–")



MODEL = (
    "**A semi-elasticity model turns the curve into a response to taxes, fees and subsidies.** A carbon tax $\\tau$, a sector "
    "fee $f_g$ (the $\\tau_o$ of @sec-nonenergy) and a sector payment $b_g$ per tonne abated all add to the price that a "
    "sector's measures respond to. The tax and the fee also raise the price of the sector's output and so cut demand; the "
    "payment does not. For sector group $g$, measure $m$ and CPAT base $b$:\n\n"
    "$$\n\\pi_g = \\tau + f_g + b_g, \\qquad \\ell_m = \\min\\!\\Big(1, \\max\\!\\Big(0, \\frac{\\pi_g - \\max(c_m, \\underline{c})}{h}\\Big)\\Big), \\qquad d_m = M_m\\,\\omega_m,\n$$ {#eq-semi-uptake}\n\n"
    "where $c_m$ is the measure's standalone abatement cost, $\\underline{c}$ a floor (zero by default, so that no measure "
    "is taken up without a price), $M_m$ SISEPUEDE's default magnitude and $\\omega_m$ the share of the CPAT base it "
    "reaches. Measures on one base combine multiplicatively, bases add up within the group, and demand responds to the "
    "priced instruments only:\n\n"
    "$$\nA_g = \\min\\!\\Big(1, \\frac{1}{S_g}\\sum_{b \\in g} s_b\\Big[1 - \\prod_{m \\in b}(1 - d_m \\ell_m)\\Big]\\Big), \\qquad E_g = E^{B}_g\\,(1 - A_g)\\,e^{\\varepsilon^{D}_g(\\tau + f_g)},\n$$ {#eq-semi-emissions}\n\n"
    "where $s_b$ is the size of base $b$ in CPAT, $S_g$ that of the group, $E^B_g$ baseline emissions and "
    "$\\varepsilon^D_g$ the demand semi-elasticity. The semi-elasticities of the sector's emissions follow:\n\n"
    "$$\n\\frac{\\partial \\ln E_g}{\\partial \\tau} = \\frac{\\partial \\ln E_g}{\\partial f_g} = -\\frac{\\partial A_g/\\partial \\pi_g}{1 - A_g} + \\varepsilon^{D}_g, \\qquad \\frac{\\partial \\ln E_g}{\\partial b_g} = -\\frac{\\partial A_g/\\partial \\pi_g}{1 - A_g},\n$$ {#eq-semi}\n\n"
    "with $\\partial A_g/\\partial\\pi_g = S_g^{-1}\\sum_b s_b R_b \\sum_{m\\in b} d_m\\,\\mathbb{1}[\\text{$m$ in its ramp}]/[h(1 - d_m\\ell_m)]$ "
    "and $R_b = \\prod_{m\\in b}(1 - d_m\\ell_m)$. Revenue is $(\\tau + f_g)E_g$ and the payment costs $b_g A_g E^B_g$, paid on "
    "every adopter as in @eq-nonenergy-fiscal. A payment buys abatement only through the technology term, so per dollar "
    "it cuts less than a tax wherever demand responds; but it raises no prices. The model is implemented as a workbook "
    "with every input editable; the reach $\\omega_m$ and the demand semi-elasticities are labelled assumptions.\n")

out = []
out.append("# Appendix B: SISEPUEDE transformations mapped to CPAT {#sec-appendix-transformations .appendix}\n")
out.append(
    "**Every SISEPUEDE transformation has a CPAT sector, a base in CPAT whose size can be measured, and a place on an "
    "abatement cost curve.** @tbl-app-transformations lists the 74 transformations in SISEPUEDE's own list "
    "(`attributes/attribute_transformer_code.csv` in the SISEPUEDE repository, commit 9bf976c; the baseline is left out) [@SISEPUEDECode]. "
    "For each it gives the CPAT sector it maps to and the type of match (@tbl-mapping), the part of CPAT's energy use or "
    "emissions it acts on, and how big that base is: the median share across countries of national energy use (2022) or "
    "of national emissions excluding land use (2024), from CPAT's public data [@CPATAI2026]. Energy use is end-use "
    "non-electric fuel plus all inputs to power. The table also gives the transformation's default magnitude in "
    "SISEPUEDE's code (`transformers/transformers.py`) and the number of cost lines the cost-benefit module holds for it "
    "(Appendix A gives the factors) [@CBSSPCode].\n")
out.append(
    "**An abatement cost curve follows from running each transformation alone.** Each transformation is run on its own "
    "against the baseline, and also left out of the full package. Its abatement cost is @eq-mac on the run's costs and "
    "tonnes, and its potential is the tonnes it abates. Under the uptake rule of @eq-uptake, half of a measure's "
    "potential is taken up at its *half-potential carbon price*, its abatement cost plus half the ramp width "
    "($c_m + h_m/2$, 25 dollars per tonne at the default). For a group of measures, the potential taken up at carbon "
    "price $\\tau$ is $\\sum_m \\bar E_m\\,\\ell_m(\\tau)$; the group's half-potential price is where that sum reaches half "
    "the group's potential, and the slope there is the share of potential added per dollar. Measures run alone overlap, "
    "so their potentials describe relative size and are not added for policy totals; the leave-one-out run shows where "
    "the overlaps are.\n")
out.append(MODEL)
if MODE == "public":
    out.append(
        "**Results of a country run are held separately.** The method has been applied to one SISEPUEDE country run; "
        "its abatement costs are not reported here, in line with this note's rule of reporting no country results.\n")
    cols = ["Transformation", "CPAT sector", "Map", "Base in CPAT", "Default magnitude", "Cost lines"]
    out.append("| " + " | ".join(cols) + " |")
    out.append("|:--|:--|:--|:--|:--|--:|")
    for r in rows:
        out.append("| " + " | ".join([r["Transformation (SISEPUEDE)"][4:].replace("_", "\\_"), r["CPAT sector"], mapping(r),
                                       base(r), default(r).replace("_", "\\_"), r["CB transformation-cost rows"]]) + " |")
    out.append("\n: Every SISEPUEDE transformation maps to a CPAT sector whose base can be sized from CPAT's data; four "
               "non-energy sectors take most transformations. Base in CPAT: median share across countries of national "
               "energy use (energy) or of emissions excluding land use (GHG). Map: M:1 many transformations to one CPAT "
               "sector; 1:M one to several; gap as in @tbl-mapping. Cost lines: transformation-cost rows in the "
               "cost-benefit module. Sources: SISEPUEDE repository (commit 9bf976c); cost-benefit module (commit adc22ba); "
               "CPAT public data. {#tbl-app-transformations}\n")
else:
    import openpyxl
    grp, fig = sys.argv[3], sys.argv[4]
    out.append(
        "**In one SISEPUEDE country run, half the energy sector's potential is taken up at about 87 dollars per tonne, "
        "against about 20 to 30 for industrial processes and agriculture.** *Internal edition: the results below come "
        "from a SISEPUEDE run held with the CPAT–SISEPUEDE project files (`tornado_vs_whirlpool (1).csv`); the file "
        "does not state the country. Abatement is cumulative MtCO2e. The run's costs carry the cost-benefit module's "
        "open issues, notably missing fuel-cost lines, which may overstate net costs. Not for publication.*\n")
    wb = openpyxl.load_workbook(grp, read_only=True)
    ws = wb["Group summary"]
    data = [list(r) for r in ws.iter_rows(values_only=True)]
    out.append("| Group | Measures | Potential, Mt | Taken up at 0 / 25 / 50 / 100 / 200 USD/t, % | Half-potential price, USD/t | Slope, % per USD/t |")
    out.append("|:--|--:|--:|:--|--:|--:|")
    for d in data[1:]:
        out.append(f"| {d[0]} | {d[1]} | {d[2]:,.0f} | {d[3]:.0f} / {d[4]:.0f} / {d[5]:.0f} / {d[6]:.0f} / {d[7]:.0f} | {d[8]:g} | {d[9]:.2f} |")
    out.append("\n: Half the energy sector's potential is taken up at about 87 dollars per tonne; industrial processes and "
               "agriculture are cheaper, and waste stalls at half its potential. One SISEPUEDE country run; standalone "
               "potentials, cumulative; uptake rule of @eq-uptake with a 50-dollar ramp. {#tbl-app-groups}\n")
    out.append(f"![Measures ranked by standalone abatement cost in one SISEPUEDE country run. Bar width is standalone "
               f"abatement, cumulative MtCO2e; widths overlap and are not additive. Costs clipped to −500 to 1,000 "
               f"dollars per tonne.]({fig}){{#fig-macc width=100%}}\n")
    if len(sys.argv) > 5:
        mw = openpyxl.load_workbook(sys.argv[5], data_only=True, read_only=True)
        res = [list(r) for r in mw["Results"].iter_rows(min_row=1, max_row=7, values_only=True)]
        out.append("**At a carbon tax of 50 dollars per tonne, the model cuts about a third of these sectors' emissions, and a further dollar of tax cuts them by about half a percent.** "
                   "Default inputs: no fees or payments, placeholder demand semi-elasticities and a placeholder country of 100 MtCO2e a year split by median sector shares.\n")
        out.append("| Sector group | Technology cut, % | Cut from baseline, % | Semi-elasticity to tax or fee, % per USD/t | Semi-elasticity to payment, % per USD/t |")
        out.append("|:--|--:|--:|--:|--:|")
        for d in res[1:]:
            out.append(f"| {d[0]} | {(100*d[2] if d[2] is not None else ''):.1f} | {d[5]:.1f} | {d[7]:.2f} | {d[8]:.2f} |" if d[2] is not None else f"| {d[0]} | – | {d[5]:.1f} | {d[7]:.2f} | {d[8]:.2f} |")
        out.append("\n: At 50 dollars a tonne the model cuts about a third of emissions outside land use, waste the most. Semi-elasticities by @eq-semi; the payment's is smaller by the demand term. One SISEPUEDE country run for costs; base sizes from CPAT public data; default inputs of the model workbook. {#tbl-app-semi}\n")
        bp = [list(r) for r in mw["By price"].iter_rows(values_only=True)]
        n = (len(bp[0]) - 1) // 2
        out.append("| Carbon tax, USD/t | " + " | ".join(h.split(":")[0] for h in bp[0][1:n+1]) + " |")
        out.append("|--:|" + "--:|" * n)
        for r in bp[1:]:
            if r[0] in (25, 50, 100, 150, 200, 300):
                out.append(f"| {r[0]} | " + " | ".join(f"{x:.0f}% ({y:.2f})" for x, y in zip(r[1:n+1], r[n+1:])) + " |")
        out.append("\n: The cut from baseline rises with the carbon tax; the semi-elasticity falls as each sector's cheaper measures are used up and jumps where a large measure's ramp begins, such as the renewable target near 200 dollars. Each cell: cut from baseline, % (semi-elasticity to the tax, % per USD/t). Default inputs, no fees or payments. {#tbl-app-semi-price}\n")
    cols = ["Transformation", "CPAT sector", "Base in CPAT", "MAC alone, USD/t", "Abatement alone, Mt", "Half-potential price, USD/t", "Cost lines"]
    out.append("| " + " | ".join(cols) + " |")
    out.append("|:--|:--|:--|--:|--:|--:|--:|")
    for r in rows:
        ab = r["Abatement alone, MtCO2e cumulative (SISEPUEDE run)"]
        ab = "" if ab in ("", "-0.0", "0.0") else ab
        out.append("| " + " | ".join([r["Transformation (SISEPUEDE)"][4:].replace("_", "\\_"), r["CPAT sector"], base(r),
                                       status(r), ab, r["Half-potential carbon price, USD/tCO2e (MAC + H/2)"],
                                       r["CB transformation-cost rows"]]) + " |")
    out.append("\n: Every SISEPUEDE transformation with its CPAT sector, the size of its base in CPAT and its standalone "
               "abatement cost in one country run. Base in CPAT: median share across countries of national energy use "
               "(energy) or of emissions excluding land use (GHG), CPAT public data. MAC and abatement: the "
               "transformation run alone against the baseline. Half-potential price: MAC + 25. Cost lines: "
               "transformation-cost rows in the cost-benefit module. {#tbl-app-transformations}\n")
print("\n".join(out))
