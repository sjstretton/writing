"""Paper 3.4, section "First estimates for Egypt": a rapid transition by sector at two costs of capital.

Illustrative results from the tools, not official estimates. Public data only.

What it does
  1. Runs the national investment model of the Climate Fiscal AI Tools for Egypt (private repository,
     read only; the model's inputs for Egypt are public: IMF fossil fuel subsidies data 2024, Ember,
     IMF WEO, IRENA, Steffen et al.). Two paths, 2025-2050: current trends and a rapid transition
     (fossil-free power by 2045, all new vehicles electric by 2040, 80 percent of industrial fuel abated by 2050).
  2. Prices the incremental capital of the rapid transition, sector by sector, at
       (a) the local cost of capital: the observed market WACC for Egypt, 10.3 percent, and a high case, 14.8 percent;
       (b) the de-risked cost of capital: 6 percent, the World Bank rate used across papers 6.3, 6.5 and 6.8.
     Net cost = capital charge + other spending + change in running cost - fuel saved (at supply cost).
     Electricity bought by electrified end uses is charged to them at the average cost of the incremental
     clean power (capital charge on generation, grids and storage per MWh of extra wind and solar), and
     credited to power, so each sector's line stands alone and the lines add to the total.
  3. Splits investment by who pays (the five payer types of paper 6.5) at each cost of capital, and with
     cost-recovery tariffs and no fuel subsidies.
  4. Unit costs in power: solar, wind and solar with storage at both costs of capital, against the fuel
     cost of gas-fired power; grid cost per MWh of wind and solar connected.
  5. The time path: investment (local and imported parts) against fuel saved, as shares of GDP.
  6. The macro models of the tools (a GIMF-type and a DIG-type model) on the same program.

Two changes to the tool's defaults, both from Egyptian facts; the tool's own treatment is reported as a sensitivity.
  1. Capital at world prices. The tool scales capital costs by the local price level to the power 0.5 (for
     Egypt 0.41 after the 2024 float). Note 6.8 (v0.3) drops price-level scaling, and Egyptian contract prices
     agree with world prices, not 41 percent of them.
  2. No new gas plant on either path. The tool replaces a thirtieth of the fossil fleet each year and adds
     plant as demand grows; Egypt has surplus gas-fired capacity, so on current trends that plant is not
     needed in the years covered, and counting it would credit the transition with a saving it does not make.

Run:  python3 egypt_estimates.py [--tools /home/user/climate-fiscal-ai-tools] [--no-macro]
Writes: egypt_estimates_output.txt, egypt_sector_table.csv, egypt_paths.csv, egypt_payer_table.csv,
        egypt_power_unit_costs.csv, egypt_waiting.csv, egypt_sensitivities.csv, returns_illustration.csv
"""
import argparse
import contextlib
import csv
import io
import os
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--tools", default="/home/user/climate-fiscal-ai-tools")
ap.add_argument("--no-macro", action="store_true", help="skip the macro models (about a minute)")
args = ap.parse_args()
ROOT = Path(args.tools) / "MacFiscEnergyScenarioProto"
sys.path.insert(0, str(ROOT / "InvestmentNeeds" / "national_model"))
sys.path.insert(0, str(ROOT / "MacroFiscalModels"))
import nmim_v0_2 as m  # noqa: E402  (the investment model's engine)

ISO = "EGY"
GAS_CAPEX_TOOL = m.P["capex_gas"]
# Central case: two changes to the tool's defaults, both from Egyptian facts.
#   phi = 0        capital at world prices (the tool scales by the local price level, 0.41 for Egypt)
#   capex_gas = 0  no new gas plant on either path: Egypt has surplus gas-fired capacity, so the tool's
#                  replacement builds on the current-trends path would credit the transition with plant not needed
CENTRAL = {"phi": 0.0, "capex_gas": 0.0}
R_LOCAL, R_HIGH, R_DERISKED = 0.10343, 0.14843, 0.06   # (a) observed market WACC, (a) high case, (b) de-risked
IMPORT_SHARE = 0.5                                      # share of capital spending that is imported equipment
YEARS = m.YEARS
YI = {y: i for i, y in enumerate(YEARS)}
LIFE = {"gen": m.P["life_vre"], "grid": m.P["life_grid"], "trn": m.P["veh_life"],
        "bld": m.P["life_bld"], "ind": m.P["life_ind"]}
SECTORS = [("power", "Power generation, grids and storage"), ("trn", "Transport"), ("bld", "Buildings"),
           ("ind", "Industry"), ("oth", "Methane, land use and other")]

out_lines = []


def say(*a):
    s = " ".join(str(x) for x in a)
    out_lines.append(s)
    print(s)


def crf(r, n):
    return r / (1 - (1 + r) ** -n)


with contextlib.redirect_stdout(io.StringIO()):
    D, _cal = m.load_calibrated()


def run(params=None, wacc=None, cr=None, ffs=None):
    d = dict(D[ISO])
    if wacc is not None:
        d["wacc"] = wacc
    if cr is not None:
        d["cr_ecy"] = cr
    if ffs is not None:
        d["ffs_exp"] = ffs
    return m.run_country(d, params={**CENTRAL, **(params or {})}) + (d,)


def v(V, code, y):
    return V[code][YI[y]]


def fuel_saved(V, d, y):
    """Fuel saved (current trends less transition), USD bn at 2024 supply costs, by where it is burned."""
    def s(pairs):
        return sum((v(V, f"mit.con.{f}.{sec}.1", y) - v(V, f"mit.con.{f}.{sec}.2", y)) * d[f"sp_{f}_{sec}"]
                   for f, sec in pairs) / 1000
    return {"power": s([("coa", "pow"), ("nga", "pow"), ("oil", "pow")]),
            "trn": s([("gso", "rod"), ("die", "rod")]),
            "bld": s([(f, "res") for f in ("coa", "nga", "lpg", "ker")]),
            "ind": s([(f, "ind") for f in ("coa", "nga", "oil")]), "oth": 0.0}


def sector_costs(V, d, y, r):
    """Net cost by sector in year y at cost of capital r (USD bn a year, 2024 prices)."""
    K = {k: v(V, f"mit.alive.{k}", y) for k in LIFE}
    chg = {k: K[k] * crf(r, LIFE[k]) for k in LIFE}
    fs = fuel_saved(V, d, y)
    dom_pow = v(V, "mit.om.pow.2", y) - v(V, "mit.om.pow.1", y)
    dom_trn = v(V, "mit.om.trn.2", y) - v(V, "mit.om.trn.1", y)
    # extra wind and solar, and the electricity bought by electrified end uses (TWh)
    vre = sum(v(V, f"mit.gen.{t}.2", y) - v(V, f"mit.gen.{t}.1", y) for t in ("sol", "wnd"))
    gcr = v(V, "mit.gen.tot.2", y) / (v(V, "mit.dem.ecy.2", y) / 3.6)
    el = {"trn": (v(V, "mit.con.ecy.ev.2", y) - v(V, "mit.con.ecy.ev.1", y)) / 3.6 * gcr,
          "bld": v(V, "mit.con.ecy.hp.2", y) / 3.6 * gcr, "ind": v(V, "mit.con.ecy.ix.2", y) / 3.6 * gcr}
    c_el = (chg["gen"] + chg["grid"]) / vre * 1000 if vre > 0 else 0.0   # USD/MWh of extra wind and solar
    pay = {k: el[k] * c_el / 1000 for k in el}
    spend = v(V, "mit.dinv.nco", y) + v(V, "mit.dinv.oth", y)
    rows = {
        "power": dict(K=K["gen"] + K["grid"], charge=chg["gen"] + chg["grid"], other=dom_pow - sum(pay.values()),
                      fuel=fs["power"]),
        "trn": dict(K=K["trn"], charge=chg["trn"], other=dom_trn + pay["trn"], fuel=fs["trn"]),
        "bld": dict(K=K["bld"], charge=chg["bld"], other=pay["bld"], fuel=fs["bld"]),
        "ind": dict(K=K["ind"], charge=chg["ind"], other=pay["ind"], fuel=fs["ind"]),
        "oth": dict(K=0.0, charge=0.0, other=spend, fuel=0.0)}
    for k in rows:
        rows[k]["net"] = rows[k]["charge"] + rows[k]["other"] - rows[k]["fuel"]
    return rows, dict(c_el=c_el, vre=vre, el=el, K_gen=K["gen"], K_grid=K["grid"],
                      chg_gen=chg["gen"], chg_grid=chg["grid"])


def inv_by_sector(V, y, sc):
    g = lambda c: v(V, c, y) if c in V else 0.0
    return {"power": g(f"mit.inv.gen.{sc}") + g(f"mit.inv.grid.{sc}"), "trn": g(f"mit.inv.trn.{sc}"),
            "bld": g(f"mit.inv.bld.{sc}"), "ind": g(f"mit.inv.ind.{sc}"),
            "oth": g(f"mit.inv.nco.{sc}") + g(f"mit.inv.oth.{sc}"), "cal": g(f"mit.inv.cal.{sc}")}


def budget_by_sector(S, V, y):
    """Direct budget need of the transition path (P1 plus the public gap of P4), USD bn, by sector."""
    gap = m.P["ty_p4_gap"]
    g = lambda c: v(V, c, y)
    b = lambda x: S[f"ty_{x}_p1"] + gap * S[f"ty_{x}_p4"]
    nc, lu = g("mit.spd.nc.2"), g("mit.spd.lu.2")
    return {"power": g("mit.inv.gen.2") * b("gen") + g("mit.inv.grid.2") * b("grid"),
            "trn": g("mit.inv.trn.2") * b("trn"), "bld": g("mit.inv.bld.2") * b("bld"),
            "ind": gap * (g("mit.inv.ixh.2") * S["ty_ih_p4"] + g("mit.inv.ccs.2")),
            "oth": S["ty_nc_p1"] * nc + S["ty_lu_p1"] * lu
                   + gap * (nc * (1 - S["ty_nc_p1"] - S["ty_nc_p5"]) + lu * (1 - S["ty_lu_p1"]) + g("mit.inv.oth.2")),
            "cal": g("mit.inv.cal.2") * b("cal")}


# ----------------------------------------------------------------------------------------------------
S, V, d = run()
gdp = lambda y: v(V, "mit.gdp.lvl", y)
say("EGYPT: a rapid transition by sector at two costs of capital (illustrative tool results; USD bn, 2024 prices)")
say(f"Costs of capital: (a) local {100 * R_LOCAL:.1f}% (high case {100 * R_HIGH:.1f}%); (b) de-risked {100 * R_DERISKED:.0f}%")
say(f"Capital at world prices (price factor {S['pf']:.2f}); no new gas plant on either path. GDP 2024 USD {gdp(2024):.0f} bn; "
    f"2030 {gdp(2030):.0f}; 2035 {gdp(2035):.0f}; 2040 {gdp(2040):.0f}")

say("\n1. THE PATHS")
say("year | fossil share of generation: trends, transition | solar GW, wind GW (transition) | EV share of sales | GHG Mt: trends, transition")
for y in (2024, 2030, 2035, 2040, 2045):
    say(f"{y} | {100 * v(V, 'mit.gen.fsh.1', y):.0f}%, {100 * v(V, 'mit.gen.fsh.2', y):.0f}% | "
        f"{v(V, 'mit.cap.sol.2', y):.0f}, {v(V, 'mit.cap.wnd.2', y):.0f} | {100 * v(V, 'mit.ev.shs.2', y):.0f}% | "
        f"{v(V, 'mit.ghg.tot.1', y):.0f}, {v(V, 'mit.ghg.tot.2', y):.0f}")
say(f"renewable share of generation in 2030 on the transition path: {100 * (1 - v(V, 'mit.gen.fsh.2', 2030)):.0f}% "
    f"(wind and solar additions 2026-2030: "
    f"{sum(v(V, 'mit.add.sol.2', y) + v(V, 'mit.add.wnd.2', y) for y in range(2026, 2031)) / 5:.1f} GW a year)")

say("\n2. INVESTMENT (USD bn a year; % of GDP)")
for y in (2030, 2035, 2040):
    i1, i2 = v(V, "mit.inv.tot.1", y), v(V, "mit.inv.tot.2", y)
    say(f"{y}: current trends {i1:.1f} ({100 * i1 / gdp(y):.1f}%), transition {i2:.1f} ({100 * i2 / gdp(y):.1f}%), "
        f"incremental {i2 - i1:.1f} ({100 * (i2 - i1) / gdp(y):.1f}%)")
rng = range(2026, 2036)
cum1 = {k: sum(inv_by_sector(V, y, 1)[k] for y in rng) for k in ("power", "trn", "bld", "ind", "oth", "cal")}
cum2 = {k: sum(inv_by_sector(V, y, 2)[k] for y in rng) for k in ("power", "trn", "bld", "ind", "oth", "cal")}
say("cumulative 2026-2035 by sector: sector | current trends | transition | incremental")
for k, nm in SECTORS + [("cal", "Other clean investment, same on both paths")]:
    say(f"  {nm} | {cum1[k]:.0f} | {cum2[k]:.0f} | {cum2[k] - cum1[k]:.0f}")
tot1, tot2 = sum(cum1.values()), sum(cum2.values())
gdp_cum = sum(gdp(y) for y in rng)
say(f"  TOTAL | {tot1:.0f} | {tot2:.0f} | {tot2 - tot1:.0f}  = {100 * (tot2 - tot1) / gdp_cum:.1f}% of 2026-2035 GDP "
    f"(transition {100 * tot2 / gdp_cum:.1f}%)")
for k, nm in (("gen", "generation"), ("grid", "grids and storage")):
    a1 = sum(v(V, f"mit.inv.{k}.1", y) for y in rng)
    a2 = sum(v(V, f"mit.inv.{k}.2", y) for y in rng)
    say(f"  of power, {nm}: current trends {a1:.0f}, transition {a2:.0f}, incremental {a2 - a1:.0f}")
say(f"  share of industry in the increment {100 * (cum2['ind'] - cum1['ind']) / (tot2 - tot1):.0f}%; "
    f"current trends {100 * tot1 / gdp_cum:.1f}% of GDP")

say("\n3. NET COST BY SECTOR (USD bn a year): capital charge + other - fuel saved")
table = []
for y in (2030, 2035, 2040):
    A, xa = sector_costs(V, d, y, R_LOCAL)
    H, _ = sector_costs(V, d, y, R_HIGH)
    B, xb = sector_costs(V, d, y, R_DERISKED)
    say(f"-- {y} (GDP {gdp(y):.0f}) --")
    say("sector | capital in service | charge (a) | charge (b) | saving from de-risking | fuel saved | other (a) | "
        "net (a) | net (a) high | net (b)")
    tot = dict(K=0, ca=0, cb=0, fuel=0, oa=0, na=0, nh=0, nb=0)
    for k, nm in SECTORS:
        a, h, b = A[k], H[k], B[k]
        say(f"  {nm} | {a['K']:.1f} | {a['charge']:.2f} | {b['charge']:.2f} | {a['charge'] - b['charge']:.2f} | "
            f"{a['fuel']:.2f} | {a['other']:.2f} | {a['net']:.2f} | {h['net']:.2f} | {b['net']:.2f}")
        table.append(dict(year=y, sector=nm, capital_in_service=a["K"], charge_local=a["charge"],
                          charge_high=h["charge"], charge_derisked=b["charge"], fuel_saved=a["fuel"],
                          other_local=a["other"], other_derisked=b["other"], net_local=a["net"],
                          net_high=h["net"], net_derisked=b["net"]))
        for kk, val in (("K", a["K"]), ("ca", a["charge"]), ("cb", b["charge"]), ("fuel", a["fuel"]),
                        ("oa", a["other"]), ("na", a["net"]), ("nh", h["net"]), ("nb", b["net"])):
            tot[kk] += val
    say(f"  TOTAL | {tot['K']:.1f} | {tot['ca']:.2f} | {tot['cb']:.2f} | {tot['ca'] - tot['cb']:.2f} | {tot['fuel']:.2f} | "
        f"{tot['oa']:.2f} | {tot['na']:.2f} | {tot['nh']:.2f} | {tot['nb']:.2f}")
    say(f"  as % of GDP: net (a) {100 * tot['na'] / gdp(y):.2f}, net (a) high {100 * tot['nh'] / gdp(y):.2f}, "
        f"net (b) {100 * tot['nb'] / gdp(y):.2f}; saving from de-risking {100 * (tot['ca'] - tot['cb']) / gdp(y):.2f}; "
        f"fuel saved {100 * tot['fuel'] / gdp(y):.2f}")
    say(f"  check against the model's own totals: (a) {v(V, 'mit.ic.a', y):.2f}, (b) {v(V, 'mit.ic.b', y):.2f}; "
        f"air pollution avoided {v(V, 'mit.dap', y):.1f}; GHG abated {v(V, 'mit.ghg.abt', y):.0f} Mt "
        f"-> USD {1000 * tot['na'] / v(V, 'mit.ghg.abt', y):.0f}/t at (a), {1000 * tot['nb'] / v(V, 'mit.ghg.abt', y):.0f}/t at (b)")
    assert abs(tot["na"] - v(V, "mit.ic.a", y)) < 1e-6 and abs(tot["nb"] - v(V, "mit.ic.b", y)) < 1e-6
    say(f"  clean power for end uses charged at USD {xa['c_el']:.0f}/MWh (a), {xb['c_el']:.0f}/MWh (b); "
        f"extra wind and solar {xa['vre']:.0f} TWh, of which sold to transport {xa['el']['trn']:.0f}, "
        f"buildings {xa['el']['bld']:.0f}, industry {xa['el']['ind']:.0f} TWh")
with open(HERE / "egypt_sector_table.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(table[0]))
    w.writeheader()
    for r_ in table:
        w.writerow({k: (round(x, 4) if isinstance(x, float) else x) for k, x in r_.items()})

say("\n   Present value 2025-2050 of the net cost (USD bn; negative = net saving), discounted at each lens rate:")
for lab, r in (("(a) local", R_LOCAL), ("(a) high", R_HIGH), ("(b) de-risked", R_DERISKED)):
    pv = sum(sum(x["net"] for x in sector_costs(V, d, y, r)[0].values()) * (1 + r) ** -(y - 2024) for y in range(2025, 2051))
    say(f"   {lab}: {pv:.0f}")
say("   Break-even cost of capital (net cost = 0) by sector and year:")
for y in (2030, 2035):
    res = []
    for k, nm in SECTORS[:4]:
        lo, hi = 0.001, 1.0
        f0 = lambda r: sector_costs(V, d, y, r)[0][k]["net"]
        if f0(hi) < 0:
            res.append(f"{nm}: above 100%")
            continue
        if f0(lo) > 0:
            res.append(f"{nm}: none (net cost at any rate)")
            continue
        for _ in range(60):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if f0(mid) < 0 else (lo, mid)
        res.append(f"{nm}: {100 * lo:.1f}%")
    say(f"   {y}: " + "; ".join(res))

say("\n4. WHAT GAS, WHAT FUEL")
for y in (2030, 2035, 2040):
    gas = v(V, "mit.con.nga.pow.1", y) - v(V, "mit.con.nga.pow.2", y)
    oil = v(V, "mit.con.oil.pow.1", y) - v(V, "mit.con.oil.pow.2", y)
    fs = fuel_saved(V, d, y)
    say(f"{y}: gas saved in power {gas:.0f} PJ = {gas / 36.0:.1f} bcm (at 36 MJ/m3) = {gas / 1.055:.0f} mn MMBtu; "
        f"fuel oil in power {oil:.0f} PJ; fuel saved by sector: " + ", ".join(f"{k} {x:.1f}" for k, x in fs.items() if x)
        + f"; total {sum(fs.values()):.1f} = {100 * sum(fs.values()) / gdp(y):.1f}% of GDP")
say(f"supply costs used (USD/GJ): gas for power {d['sp_nga_pow']:.2f} (= USD {d['sp_nga_pow'] * 1.055:.1f}/MMBtu), "
    f"fuel oil {d['sp_oil_pow']:.1f}, gasoline {d['sp_gso_rod']:.1f}, diesel {d['sp_die_rod']:.1f}, "
    f"LPG {d['sp_lpg_res']:.1f}, gas for industry {d['sp_nga_ind']:.1f}")
say(f"gas heat rate {S['hr_nga']:.2f} GJ/MWh -> fuel cost of gas power USD {S['hr_nga'] * d['sp_nga_pow']:.0f}/MWh; "
    f"capacity factors: solar {100 * S['cf_sol']:.1f}%, wind {100 * S['cf_wnd']:.1f}%")

say("\n5. WHO PAYS (transition path, USD bn; direct budget need = pure public + 30% of viability-gap investment)")
cases = [("(a) local cost of capital, tariffs and subsidies as today", dict(wacc=R_LOCAL)),
         ("(b) de-risked cost of capital, tariffs and subsidies as today", dict(wacc=R_DERISKED)),
         ("(b) de-risked, cost-recovery tariffs and no fuel subsidies", dict(wacc=R_DERISKED, cr=1.0, ffs=0.0))]
payer_rows = []
for lab, kw in cases:
    S_, V_, d_ = run(**kw)
    for y in (2030, 2035):
        typ = [v(V_, f"mit.typ.p{k}.2", y) for k in range(1, 6)]
        bud, dbud = v(V_, "mit.typ.bud.2", y), v(V_, "mit.dtyp.bud", y)
        bs = budget_by_sector(S_, V_, y)
        assert abs(sum(bs.values()) - bud) < 1e-6
        say(f"{lab}, {y}: P1 {typ[0]:.1f}, P2 {typ[1]:.1f}, P3 {typ[2]:.1f}, P4 {typ[3]:.1f}, P5 {typ[4]:.1f} "
            f"(sum {sum(typ):.1f}); budget need {bud:.1f} = {100 * bud / gdp(y):.2f}% of GDP "
            f"(incremental {dbud:.1f} = {100 * dbud / gdp(y):.2f}%); by sector: "
            + ", ".join(f"{k} {x:.2f}" for k, x in bs.items()))
        payer_rows.append(dict(case=lab, year=y, P1=typ[0], P2=typ[1], P3=typ[2], P4=typ[3], P5=typ[4],
                               budget_need=bud, budget_need_pct_gdp=100 * bud / gdp(y), incremental_budget_need=dbud,
                               **{f"budget_{k}": x for k, x in bs.items()}))
    say(f"   pressure indices: utility {S_['ty_u']:.2f}, cost of capital {S_['ty_h']:.2f}, subsidies {S_['ty_v']:.2f}")
with open(HERE / "egypt_payer_table.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(payer_rows[0]))
    w.writeheader()
    for r_ in payer_rows:
        w.writerow({k: (round(x, 4) if isinstance(x, float) else x) for k, x in r_.items()})

say("\n6. UNIT COSTS IN POWER (USD/MWh, 2024 prices)")
unit_rows = []


def lcoe(capex, cf, r, life=25, om=0.015):
    return capex * (crf(r, life) + om) / (cf * 8.76)


def storage_adder(r, capex_kwh, share, life=15, om=0.02, eff=0.88, cycles=350):
    """Extra cost per MWh of solar when `share` of its output passes through a battery cycled once a day."""
    lcos = capex_kwh * 1000 * (crf(r, life) + om) / (cycles * eff)       # USD per MWh discharged
    return share * lcos, lcos


sol26, wnd26 = v(V, "mit.cap.sol.cost", 2026), v(V, "mit.cap.wnd.cost", 2026)
gas_fuel = S["hr_nga"] * d["sp_nga_pow"]
say(f"capital costs 2026: solar USD {sol26:.0f}/kW, wind USD {wnd26:.0f}/kW; battery USD 125-250/kWh installed (range)")
for lab, r in (("(a) local 10.3%", R_LOCAL), ("(a) high 14.8%", R_HIGH), ("(b) de-risked 6%", R_DERISKED)):
    ls, lw = lcoe(sol26, S["cf_sol"], r), lcoe(wnd26, S["cf_wnd"], r)
    add_lo, lcos_lo = storage_adder(r, 125, 0.5)
    add_hi, lcos_hi = storage_adder(r, 250, 0.5)
    say(f"{lab}: solar {ls:.0f}, wind {lw:.0f}; storage per MWh discharged {lcos_lo:.0f}-{lcos_hi:.0f}; "
        f"solar with half its output stored {ls + add_lo:.0f}-{ls + add_hi:.0f} "
        f"(x{(ls + add_lo) / ls:.1f}-{(ls + add_hi) / ls:.1f} of plain solar)")
    unit_rows.append(dict(lens=lab, solar=ls, wind=lw, solar_plus_storage_low=ls + add_lo,
                          solar_plus_storage_high=ls + add_hi, storage_per_mwh_low=lcos_lo, storage_per_mwh_high=lcos_hi))
say(f"gas-fired power, fuel only: USD {gas_fuel:.0f}/MWh at USD {d['sp_nga_pow'] * 1.055:.1f}/MMBtu; "
    f"at USD 12/MMBtu (LNG) {S['hr_nga'] * 12 / 1.055:.0f}; at USD 6/MMBtu {S['hr_nga'] * 6 / 1.055:.0f}; "
    f"plus running cost USD {1000 * m.P['om_fos']:.1f}/MWh")
for u in unit_rows:
    u["gas_fuel_only"] = gas_fuel
with open(HERE / "egypt_power_unit_costs.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(unit_rows[0]))
    w.writeheader()
    for r_ in unit_rows:
        w.writerow({k: (round(x, 2) if isinstance(x, float) else x) for k, x in r_.items()})
say("grids and storage (incremental capital in service, annual charge, per MWh of extra wind and solar):")
for y in (2030, 2035):
    _, xa = sector_costs(V, d, y, R_LOCAL)
    _, xb = sector_costs(V, d, y, R_DERISKED)
    say(f"  {y}: capital {xa['K_grid']:.1f} bn; charge (a) {xa['chg_grid']:.2f}, (b) {xb['chg_grid']:.2f} bn; "
        f"per MWh of extra wind and solar USD {1000 * xa['chg_grid'] / xa['vre']:.0f} (a), "
        f"{1000 * xb['chg_grid'] / xb['vre']:.0f} (b); fuel and running cost saved per MWh displaced USD "
        f"{gas_fuel + 1000 * m.P['om_fos']:.0f}; break-even: the grid pays if it carries "
        f"{100 * xa['chg_grid'] / xa['vre'] * 1000 / (gas_fuel + 1000 * m.P['om_fos'] - lcoe(sol26, S['cf_sol'], R_LOCAL)):.0f}% (a) / "
        f"{100 * xb['chg_grid'] / xb['vre'] * 1000 / (gas_fuel + 1000 * m.P['om_fos'] - lcoe(sol26, S['cf_sol'], R_DERISKED)):.0f}% (b) "
        f"of that output's net saving")
add5 = sum(v(V, "mit.add.sol.2", y) + v(V, "mit.add.wnd.2", y) for y in range(2026, 2031)) / 5
twh_per_gw = (0.6 * S["cf_sol"] + 0.4 * S["cf_wnd"]) * 8.76
say(f"  cost of delay: a year's additions ({add5:.1f} GW, {add5 * twh_per_gw:.0f} TWh a year) left unconnected for one "
    f"year burn gas worth USD {add5 * twh_per_gw * gas_fuel / 1000:.2f} bn")

say("\n7. THE TIME PATH (% of GDP): investment arrives first, fuel savings later")
say("year | incremental investment | of which imported equipment (50%) | spent in Egypt | fuel saved | "
    "fuel saved less imported equipment | net cost (a) | net cost (b)")
path_rows = []
for y in range(2025, 2046):
    g = gdp(y)
    di = v(V, "mit.dinv.tot", y)
    capex = di - v(V, "mit.dinv.nco", y) - v(V, "mit.dinv.oth", y)
    imp = IMPORT_SHARE * capex
    fs = v(V, "mit.dfuel", y)
    na, nb = v(V, "mit.ic.a", y), v(V, "mit.ic.b", y)
    path_rows.append(dict(year=y, gdp=g, incremental_investment=di, imported_equipment=imp, spent_locally=di - imp,
                          fuel_saved=fs, net_cost_local=na, net_cost_derisked=nb,
                          transition_investment=v(V, "mit.inv.tot.2", y), trends_investment=v(V, "mit.inv.tot.1", y)))
    if y in (2025, 2026, 2027, 2028, 2029, 2030, 2032, 2035, 2040, 2045):
        say(f"{y} | {100 * di / g:.2f} | {100 * imp / g:.2f} | {100 * (di - imp) / g:.2f} | {100 * fs / g:.2f} | "
            f"{100 * (fs - imp) / g:.2f} | {100 * na / g:.2f} | {100 * nb / g:.2f}")
first = next((r_["year"] for r_ in path_rows if r_["fuel_saved"] > r_["imported_equipment"]), None)
first2 = next((r_["year"] for r_ in path_rows if r_["fuel_saved"] > r_["incremental_investment"]), None)
say(f"fuel saved exceeds imported equipment from {first}; exceeds all incremental investment from {first2}")
with open(HERE / "egypt_paths.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(path_rows[0]))
    w.writeheader()
    for r_ in path_rows:
        w.writerow({k: (round(x, 4) if isinstance(x, float) else x) for k, x in r_.items()})

say("\n8. SENSITIVITIES (net cost, USD bn a year; all sectors unless stated)")
sens_rows = []


def sens(lab, Sx, Vx, dx):
    for y in (2030, 2035):
        A, _ = sector_costs(Vx, dx, y, R_LOCAL)
        B, _ = sector_costs(Vx, dx, y, R_DERISKED)
        ta, tb = sum(x["net"] for x in A.values()), sum(x["net"] for x in B.values())
        say(f"  {lab}, {y}: all sectors (a) {ta:+.1f}, (b) {tb:+.1f}; power (a) {A['power']['net']:+.1f}, (b) {B['power']['net']:+.1f}; "
            f"transition investment {v(Vx, 'mit.inv.tot.2', y):.1f} ({100 * v(Vx, 'mit.inv.tot.2', y) / gdp(y):.1f}% of GDP), "
            f"extra {v(Vx, 'mit.dinv.tot', y):.1f}; renewable share {100 * (1 - v(Vx, 'mit.gen.fsh.2', y)):.0f}%; "
            f"budget need {v(Vx, 'mit.typ.bud.2', y):.1f}")
        sens_rows.append(dict(case=lab, year=y, net_local=ta, net_derisked=tb, power_local=A["power"]["net"],
                              power_derisked=B["power"]["net"]))


sens("central (world prices, no new gas plant)", S, V, d)
Sg, Vg, dg = run(params={"capex_gas": GAS_CAPEX_TOOL})
sens("current trends must build gas plant (tool treatment)", Sg, Vg, dg)
S0, V0, d0 = run(params={"phi": 0.5, "capex_gas": GAS_CAPEX_TOOL})
sens("tool defaults (capital at 41% of world prices, gas plant built)", S0, V0, d0)
d1 = dict(D[ISO])
S1, V1 = m.run_country(d1, params={**CENTRAL, "pow_T_emdc": 2040, "ev_T_emdc": 2035})
sens("faster (fossil-free power by 2040, all new vehicles electric by 2035)", S1, V1, d1)
dgas = dict(D[ISO]); dgas["sp_nga_pow"] = 12 / 1.055; dgas["sp_nga_ind"] = dgas["sp_nga_ind"] + (12 / 1.055 - D[ISO]["sp_nga_pow"])
Sp, Vp = m.run_country(dgas, params=dict(CENTRAL))
sens("gas at USD 12/MMBtu (imported LNG) in power and industry", Sp, Vp, dgas)
with open(HERE / "egypt_sensitivities.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(sens_rows[0]))
    w.writeheader()
    for r_ in sens_rows:
        w.writerow({k: (round(x, 3) if isinstance(x, float) else x) for k, x in r_.items()})

say("\n8b. THE COST OF WAITING: every milestone reached five years later (world prices)")
dl = dict(D[ISO])
SL, VL = m.run_country(dl, params={**CENTRAL, "pow_T_emdc": 2050, "ev_T_emdc": 2045, "bld_T_emdc": 2055,
                                    "ind_a_emdc": 0.8 * 26 / 31})


def pv(Vx, dx, r, keys=None, y0=2025, y1=2050):
    tot = 0.0
    for y in range(y0, y1 + 1):
        rows, _ = sector_costs(Vx, dx, y, r)
        tot += sum(x["net"] for k, x in rows.items() if keys is None or k in keys) * (1 + r) ** -(y - 2024)
    return tot


say("present value 2025-2050 of net cost, USD bn (negative = net saving): on time | five years late | cost of waiting")
wait_rows = []
for lab, r in (("(a) local 10.3%", R_LOCAL), ("(b) de-risked 6%", R_DERISKED)):
    for keys, nm in ((None, "all sectors"), (("power", "trn"), "power and transport"), (("bld", "ind", "oth"), "buildings, industry, other")):
        a, b = pv(V, d, r, keys), pv(VL, dl, r, keys)
        say(f"  {lab}, {nm}: {a:.0f} | {b:.0f} | {b - a:+.0f}  (per year of delay {(b - a) / 5:+.1f})")
        wait_rows.append(dict(lens=lab, sectors=nm, pv_on_time=a, pv_five_years_late=b, cost_of_waiting=b - a))
cum = lambda Vx, c: sum(v(Vx, c, y) for y in range(2025, 2051))
gas_on = cum(V, "mit.con.nga.pow.2"); gas_late = cum(VL, "mit.con.nga.pow.2")
say(f"  extra gas burned in power 2025-2050: {(gas_late - gas_on) / 36.0:.0f} bcm; extra fuel bill "
    f"{cum(VL, 'mit.fuel.bill.2') - cum(V, 'mit.fuel.bill.2'):.0f} bn (undiscounted); extra emissions "
    f"{cum(VL, 'mit.ghg.tot.2') - cum(V, 'mit.ghg.tot.2'):.0f} MtCO2e; extra air pollution cost "
    f"{cum(VL, 'mit.airpol.2') - cum(V, 'mit.airpol.2'):.0f} bn")
say(f"  renewable share 2030: on time {100 * (1 - v(V, 'mit.gen.fsh.2', 2030)):.0f}%, late {100 * (1 - v(VL, 'mit.gen.fsh.2', 2030)):.0f}%")
gas_lock = sum(v(V, "mit.add.fos.1", y) for y in range(2026, 2036))
say(f"  (the tool's replacement rule would have current trends build {gas_lock:.0f} GW of gas plant in 2026-2035, "
    f"USD {gas_lock * GAS_CAPEX_TOOL / 1000:.0f} bn; switched off in the central case)")
with open(HERE / "egypt_waiting.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(wait_rows[0]))
    w.writeheader()
    for r_ in wait_rows:
        w.writerow({k: (round(x, 2) if isinstance(x, float) else x) for k, x in r_.items()})

say("\n8c. SCALE: what must be built and financed, against what Egypt builds and saves today")
say(f"  wind and solar additions 2026-2030: {add5:.1f} GW a year; installed at the start (Ember, 2025): "
    f"solar {d['cap_sol']:.1f} GW, wind {d['cap_wnd']:.1f} GW")
GCF = 12.997      # gross capital formation, % of GDP, 2024 (World Bank WDI, via the fiscal indicators panel)
CAB = -5.431      # current account balance, % of GDP, 2024 (IMF WEO, via the panel)
for y in (2030, 2035):
    i2, di = v(V, "mit.inv.tot.2", y), v(V, "mit.dinv.tot", y)
    say(f"  {y}: transition investment {100 * i2 / gdp(y):.1f}% of GDP = {100 * (i2 / gdp(y)) / (GCF / 100):.0f}% of the 2024 "
        f"investment rate ({GCF:.1f}% of GDP); extra investment {100 * di / gdp(y):.1f}% of GDP = "
        f"{100 * (di / gdp(y)) / (GCF / 100):.0f}% of it; imported equipment {100 * IMPORT_SHARE * (di - v(V, 'mit.dinv.nco', y) - v(V, 'mit.dinv.oth', y)) / gdp(y):.1f}% of GDP "
        f"against a current account balance of {CAB:.1f}% of GDP in 2024")
say(f"  generation: {v(V, 'mit.gen.tot.2', 2024):.0f} TWh in 2024 -> {v(V, 'mit.gen.tot.2', 2030):.0f} (2030) -> "
    f"{v(V, 'mit.gen.tot.2', 2040):.0f} (2040) on the transition path; current trends {v(V, 'mit.gen.tot.1', 2040):.0f} in 2040")

say("\n8e. DIMINISHING RETURNS OF PRICE, INCREASING RETURNS OF DEPLOYMENT (illustration)")
EPS = -0.5                                  # long-run price elasticity of road fuel demand (illustrative)
p0 = d["sp_gso_rod"] * 34.2 / 1000          # gasoline supply cost, USD per litre
co2_l = m.P["ef_gso"] * 34.2                # kg CO2 per litre
ret_rows = []
prev = 0.0
for tau in (50, 100, 150, 200, 250, 300):
    cut = 1 - ((p0 + tau * co2_l / 1000) / p0) ** EPS
    say(f"  carbon price USD {tau}/t: gasoline {p0:.2f} -> {p0 + tau * co2_l / 1000:.2f} USD/l; cut in fuel use {100 * cut:.1f}% "
        f"(this step {100 * (cut - prev):.1f} points)")
    ret_rows.append(dict(kind="price", x=tau, value=100 * cut, step=100 * (cut - prev)))
    prev = cut
for lr, nm in ((0.20, "learning rate 20%"),):
    for n in range(0, 7):
        c = 100 * (1 - lr) ** n
        ret_rows.append(dict(kind="learning", x=n, value=c, step=(100 * (1 - lr) ** (n - 1) - c) if n else 0.0))
    say(f"  {nm}: cost index after 0..6 doublings of cumulative deployment: "
        + ", ".join(f"{100 * (1 - lr) ** n:.0f}" for n in range(0, 7)))
with open(HERE / "returns_illustration.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(ret_rows[0]))
    w.writeheader()
    for r_ in ret_rows:
        w.writerow({k: (round(x, 3) if isinstance(x, float) else x) for k, x in r_.items()})

if not args.no_macro:
    say("\n9. MACRO MODELS on the same program (illustrative calibrations; % deviation of GDP from no program)")
    try:
        import integrated as it  # noqa: E402
        from nmim_bridge import _nmim
        for lab, phi, cg in (("central", 0.0, 0.0), ("tool defaults", 0.5, GAS_CAPEX_TOOL)):
            mm, _D = _nmim()
            mm.P["phi"], mm.P["capex_gas"] = phi, cg
            with contextlib.redirect_stdout(io.StringIO()):
                p = {}
                r_ = it.run(ISO, paths=p)
            say(f"{lab}: program in 2030: budget {r_['budget_need_2030_pct_gdp']:.2f}% of GDP, private "
                f"{r_['private_2030_pct_gdp']:.2f}%; energy saving 2050 {r_['energy_saving_2050_pct_gdp']:.1f}% of GDP")
            say(f"   {r_['model']}: GDP {r_.get('gdp_dev_2030_pct', float('nan')):+.1f}% (2030), "
                f"{r_.get('gdp_dev_2050_pct', float('nan')):+.1f}% (2050); debt {r_['debt_2024_pct_gdp']:.0f}% -> "
                f"{r_.get('debt_2030_pct_gdp', float('nan')):.0f}% (2030), {r_.get('debt_2050_pct_gdp', float('nan')):.0f}% (2050); "
                f"status {r_['status']}")
            say(f"   {r_.get('alt_model')}: GDP {r_.get('alt_gdp_dev_2030_pct', float('nan')):+.1f}% (2030), "
                f"{r_.get('alt_gdp_dev_2050_pct', float('nan')):+.1f}% (2050); debt "
                f"{r_.get('alt_debt_2030_pct_gdp', float('nan')):.0f}% (2030), {r_.get('alt_debt_2050_pct_gdp', float('nan')):.0f}% (2050); "
                f"status {r_.get('alt_status')}")
            if "gdp_dev_pct" in p:
                say("   GDP path, first model: " + ", ".join(f"{y}: {p['gdp_dev_pct'][y - 2025]:+.1f}" for y in (2026, 2028, 2030, 2035, 2040)))
        mm.P["phi"], mm.P["capex_gas"] = 0.5, GAS_CAPEX_TOOL
    except Exception as e:  # the macro models are optional for the tables above
        say(f"macro models not run: {type(e).__name__}: {e}")

(HERE / "egypt_estimates_output.txt").write_text("\n".join(out_lines) + "\n", encoding="utf-8")
