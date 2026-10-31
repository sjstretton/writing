"""Check which references the carbon-pricing series needs, and where each can be got.

For every entry in the series' .bib files, plus a list of key works the working
papers still need (SUPPLEMENT below), this script:
  1. finds the DOI on Crossref (if the .bib has none),
  2. asks Unpaywall for a free, legal copy,
  3. tries to download that copy from wherever the script runs.
It writes 5.Notes/Downloads-<paper>.csv in each paper folder with
  key,title,doi,url_tried,status,local_file
where status is one of
  downloaded            fetched here (copy in --pdf-dir)
  open-blocked-here     a free copy exists but this machine could not fetch it
  paywalled-manual      no free copy found: needs a library login
  not-found             no DOI or record found
Then build_download_list.py turns the CSVs into the .bat file and the manual list.

Run from the repo root:
  python "H Writing Instructions/Scripts/Papers/Steps/check_literature_access.py" --pdf-dir <folder>
"""
import argparse
import csv
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

EMAIL = "sjstretton@gmail.com"
# The paper roots, from the repo root: sections 1-4 and 5-7 (see NUMBERING.md). Folders below are relative to whichever
# root holds them. The one place to change when D Modelling moves to its own repository.
PAPER_ROOTS = [Path("C Policy and FInance"), Path("D Modelling")]


def paper_dir(folder):
    """The paper folder for a section/paper path such as 1.CarbonPricing/1.1.OpenEconomyCarbonPricing."""
    for root in PAPER_ROOTS:
        if (root / folder).is_dir():
            return root / folder
    return PAPER_ROOTS[0] / folder


BIBS = {
    "1.CarbonPricing/1.1.OpenEconomyCarbonPricing": ["OpenEconomyCarbonPricing.bib", "1.Presentation/Brief-OpenEconomyCarbonPricing.bib"],
    "1.CarbonPricing/1.2.FeebatesAndOutputBasedRebating": ["FeebatesAndOutputBasedRebating.bib", "1.Presentation/Brief-FeebatesAndOutputBasedRebating.bib"],
    "1.CarbonPricing/1.4.IronSteelCBAM": ["IronSteelCBAM.bib", "1.Presentation/Brief-IronSteelCBAM.bib"],
    "1.CarbonPricing/1.3.CarbonConsumptionTax": ["CarbonConsumptionTax.bib", "1.Presentation/Brief-CarbonConsumptionTax.bib"],
    "6.ModularUpgrades/6.1.PolicyEquivalentCarbonPriceAndCES": ["PolicyEquivalentCarbonPriceAndCES.bib", "1.Presentation/Brief-PolicyEquivalentCarbonPriceAndCES.bib"],
}
# Key works the working papers still need (from the 1.1 review and the literature plan).
SUPPLEMENT = {
    "1.CarbonPricing/1.1.OpenEconomyCarbonPricing": [
        ("FowlieReguant2022", "Mitigating Emissions Leakage in Incomplete Carbon Markets", "Fowlie Reguant"),
        ("Grubb2022", "Carbon Leakage, Consumption, and Trade", "Grubb"),
        ("JakobSteckelEdenhofer2014", "Consumption- versus Production-Based Emission Policies", "Jakob Steckel Edenhofer"),
        ("Fischer2001", "Rebating Environmental Policy Revenues: Output-Based Allocations and Tradable Performance Standards", "Fischer"),
        ("KeenKotsogiannis2014", "Coordinating climate and trade policies: Pareto efficiency and the role of border tax adjustments", "Keen Kotsogiannis"),
        ("BohringerCarboneRutherford2012", "Unilateral climate policy design: Efficiency and equity implications of alternative instruments to reduce carbon leakage", "Bohringer Carbone Rutherford"),
        ("Aldy2017", "Frameworks for evaluating policy approaches to address the competitiveness concerns of mitigating greenhouse gas emissions", "Aldy"),
        ("Markusen1975", "International externalities and optimal tax structures", "Markusen"),
    ],
    "1.CarbonPricing/1.2.FeebatesAndOutputBasedRebating": [
        ("SternerHoglund2006", "Refunded emission payments theory, distribution of costs, and Swedish experience of NOx abatement", "Sterner Hoglund"),
        ("DHaultfoeuilleGivordBoutin2014", "The environmental effect of green taxation: the case of the French bonus/malus", "D'Haultfoeuille Givord Boutin"),
        ("Johnson2006", "Feebates: An effective regulatory instrument for cost-constrained environmental policy", "Johnson"),
        ("GoulderHafsteadWilliams2016", "General equilibrium impacts of a federal clean energy standard", "Goulder Hafstead Williams"),
        ("FowlieReguantRyan2016", "Market-Based Emissions Regulation and Industry Dynamics", "Fowlie Reguant Ryan"),
    ],
    "1.CarbonPricing/1.4.IronSteelCBAM": [
        ("BushnellChenZaragozaWatkins2014", "Downstream regulation of CO2 emissions in California's electricity sector", "Bushnell Chen Zaragoza-Watkins"),
        ("CaronRausch2013", "A global general equilibrium analysis of the effects of the border carbon adjustment", "Caron"),
        ("Cosbey2019", "Developing Guidance for Implementing Border Carbon Adjustments: Lessons, Cautions, and Research Needs from the Literature", "Cosbey Droege Fischer Munnings"),
        ("Mehling2019", "Designing Border Carbon Adjustments for Enhanced Climate Action", "Mehling van Asselt"),
    ],
    "1.CarbonPricing/1.3.CarbonConsumptionTax": [
        ("KeenLockwood2010", "The value added tax: Its causes and consequences", "Keen Lockwood"),
        ("Neuhoff2016Inclusion", "Inclusion of consumption of carbon intensive materials in emissions trading", "Neuhoff"),
        ("PetersHertwich2008", "CO2 Embodied in International Trade with Implications for Global Climate Policy", "Peters Hertwich"),
    ],
    "6.ModularUpgrades/6.1.PolicyEquivalentCarbonPriceAndCES": [
        ("Labandeira2017", "A meta-analysis on the price elasticity of energy demand", "Labandeira Labeaga Lopez-Otero"),
        ("Stern2012", "Interfuel substitution: a meta-analysis", "Stern"),
        ("GillinghamStock2018", "The Cost of Reducing Greenhouse Gas Emissions", "Gillingham Stock"),
        ("AldyPizer2016", "Alternative Metrics for Comparing Domestic Climate Change Mitigation Efforts and the Emerging International Climate Policy Architecture", "Aldy Pizer"),
        ("GoulderJacobsenvanBenthem2012", "Unintended consequences from nested state and federal regulations: The case of the Pavley greenhouse-gas-per-mile limits", "Goulder Jacobsen van Benthem"),
        ("ParryBlackVernon2021", "Still Not Getting Energy Prices Right: A Global and Country Update of Fossil Fuel Subsidies", "Parry Black Vernon"),
    ],
}


def get_json(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": f"literature-check (mailto:{EMAIL})"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def parse_bib(path):
    out = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,]+),(.*?)\n\}", text, re.S):
        kind, key, body = m.group(1).lower(), m.group(2).strip(), m.group(3)
        if key.startswith("CFPB") or key.startswith("Stretton"):
            continue
        field = lambda f: (re.search(rf"\b{f}\s*=\s*[{{\"](.+?)[}}\"]\s*,?\s*\n", body, re.S) or [None, ""])[1]
        title = re.sub(r"[{}]", "", field("title")).strip()
        out.append({"key": key, "title": title, "author": re.sub(r"[{}]", "", field("author")),
                    "doi": field("doi").strip(), "url": field("url").strip(), "kind": kind})
    return out


def crossref_doi(title, author):
    q = urllib.parse.quote(f"{title} {author}"[:250])
    try:
        items = get_json(f"https://api.crossref.org/works?rows=3&query.bibliographic={q}&mailto={EMAIL}")["message"]["items"]
    except Exception:
        return ""
    t0 = re.sub(r"\W+", " ", title.lower()).split()
    for it in items:
        t1 = re.sub(r"\W+", " ", " ".join(it.get("title", [""])).lower()).split()
        common = len(set(t0) & set(t1)) / max(1, len(set(t0)))
        if common >= 0.7:
            return it.get("DOI", "")
    return ""


def try_download(url, dest):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": f"literature-check (mailto:{EMAIL})"})
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read(30_000_000)
        if data[:4] == b"%PDF":
            dest.write_bytes(data)
            return True
    except Exception:
        pass
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-dir", required=True)
    a = ap.parse_args()
    pdf_dir = Path(a.pdf_dir)
    pdf_dir.mkdir(parents=True, exist_ok=True)
    seen = {}
    for folder, bibs in BIBS.items():
        entries = []
        for b in bibs:
            p = paper_dir(folder) / b
            if p.exists():
                entries += parse_bib(p)
        entries += [{"key": k, "title": t, "author": au, "doi": "", "url": "", "kind": "supplement"} for k, t, au in SUPPLEMENT.get(folder, [])]
        rows = []
        for e in entries:
            tkey = re.sub(r"\W+", "", e["title"].lower())[:60]
            if not tkey or tkey in seen:
                if tkey in seen:
                    rows.append(seen[tkey])
                continue
            doi = e["doi"] or (crossref_doi(e["title"], e["author"]) if e["kind"] not in ("misc", "unpublished") else "")
            status, url_tried, local = "not-found", e["url"], ""
            if doi:
                try:
                    up = get_json(f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}")
                    loc = up.get("best_oa_location") or {}
                    url_tried = loc.get("url_for_pdf") or loc.get("url") or ""
                except Exception:
                    url_tried = ""
                if url_tried:
                    dest = pdf_dir / (re.sub(r"[^A-Za-z0-9_-]", "", e["key"]) + ".pdf")
                    if try_download(url_tried, dest):
                        status, local = "downloaded", dest.name
                    else:
                        status = "open-blocked-here"
                else:
                    status, url_tried = "paywalled-manual", f"https://doi.org/{doi}"
            elif url_tried:
                dest = pdf_dir / (re.sub(r"[^A-Za-z0-9_-]", "", e["key"]) + ".pdf")
                status = "downloaded" if try_download(url_tried, dest) else "open-blocked-here"
                local = dest.name if status == "downloaded" else ""
            row = {"key": e["key"], "title": e["title"], "doi": doi, "url_tried": url_tried, "status": status, "local_file": local}
            seen[tkey] = row
            rows.append(row)
            print(f"{status:18} {e['key']}")
            time.sleep(0.3)
        out = paper_dir(folder) / "5.Notes"
        out.mkdir(exist_ok=True)
        with open(out / f"Downloads-{Path(folder).name.split('.', 2)[-1]}.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["key", "title", "doi", "url_tried", "status", "local_file"])
            w.writeheader()
            w.writerows(rows)


if __name__ == "__main__":
    main()
