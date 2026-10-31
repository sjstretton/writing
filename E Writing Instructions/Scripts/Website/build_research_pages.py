"""Build the website's Research pages from the papers themselves, so the site is never out of date.

Writes, in B Working Papers/A.Website:
    research.qmd                 the Research home: a short intro and, for each section, a line and its paper titles
    research/<n>-<slug>.qmd      one page per section: the overview abstract, then each paper's title,
                                 subtitle, current abstract and links (slides, policy brief, full paper)
research/more.qmd (More papers and books) is hand-written and left alone.

Titles, subtitles and abstracts are read from each paper's master .qmd; the links point at the files
publish_series.py copies into papers/, and only files that exist are linked.
Compile-Website.bat runs this after publish_series.py and before quarto render.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3] / "B Working Papers"
SITE = ROOT / "A.Website"
PAPERS = SITE / "papers"

# section folder, page slug, sidebar/menu name, one-line description for the Research home,
# published overview file, published series deck (or None)
SECTIONS = [
    ("1.CarbonPricing", "1-carbon-pricing", "Carbon Pricing",
     "Price production and consumption separately: a feebate on emissions intensity and a destination-based charge on consumption.",
     "OverviewClimateAndFiscalPolicy.docx", "Slides-ClimateAndFiscalPolicy.pptx"),
    ("2.OtherTaxAndFiscalPolicy", "2-other-tax", "Other Tax and Fiscal Policy",
     "Tax rent, not effort: land and corporate taxes that hold up when capital and people can move.",
     "OverviewOtherTaxAndFiscalPolicy.docx", None),
    ("3.FinanceAndRisk", "3-finance-and-risk", "Finance and Risk",
     "Make clean power an asset class: remove payment risk at source, then turn projects into standard securities.",
     "OverviewMobilisingPrivateCapital.docx", "Slides-FinanceAndRisk.pptx"),
    ("4.SovereignIncentives", "4-sovereign-incentives", "Sovereign Incentives",
     "Reward governments, not projects: guarantee capacity and held capital that pay for acting early.",
     "OverviewSovereignIncentives.docx", "Slides-SovereignIncentives.pptx"),
    ("5.Modelling", "5-modelling", "Modelling (CPAT)",
     "Models a finance ministry can audit: the Climate Policy Assessment Tool stated, rebuilt and validated.",
     "OverviewModelling.docx", "Slides-Modelling.pptx"),
    ("6.ModularUpgrades", "6-modular-upgrades", "Modular Upgrades",
     "Extensions to CPAT where policy needs them: carbon-price equivalents, CBAM, public investment, activity and macro-fiscal scenarios.",
     "OverviewModularUpgrades.docx", None),
    ("7.AdditionalAnalytics", "7-analytics", "Analytics Tools",
     "Diagnostics on data ministries already hold: excise systems and fiscal indicators.",
     "OverviewAnalytics.docx", "Slides-Analytics.pptx"),
]


def front_matter(qmd):
    text = qmd.read_text(encoding="utf-8-sig")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    meta, lines, i = {}, m.group(1).split("\n"), 0
    while i < len(lines):
        line = lines[i]
        km = re.match(r"^(title|subtitle|abstract):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            if val in ("|", ">", "|-", ">-"):
                block = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                    block.append(lines[i].strip())
                    i += 1
                meta[key] = " ".join(b for b in block if b)
                continue
            meta[key] = val.strip('"').strip("'")
        i += 1
    return meta


def master(folder):
    """The paper's master qmd: the .qmd at the folder root named like the folder (without its number)."""
    name = folder.name.split(".", 2)[-1]
    q = folder / f"{name}.qmd"
    if q.exists():
        return q
    qs = [p for p in folder.glob("*.qmd")]
    return qs[0] if qs else None


def link(label, fname):
    return f"[{label} →](../papers/{fname})" if (PAPERS / fname).exists() else None


def section_page(sec, papers_out):
    folder_name, slug, name, line, overview, deck = sec
    folder = ROOT / folder_name
    num = folder_name.split(".")[0]
    ov = next((folder / f"{num}.0.Overview").glob("*.qmd"), None)
    ovm = front_matter(ov) if ov else {}
    out = [f"---\ntitle: \"{num}. {name}\"\n---\n"]
    if ovm.get("abstract"):
        out.append(ovm["abstract"] + "\n")
    links = [l for l in (link("Section overview", overview), link("Series slides", deck) if deck else None) if l]
    if links:
        out.append(" · ".join(links) + "\n")
    titles = []
    for pf in sorted((p for p in folder.iterdir() if p.is_dir() and re.match(rf"^{num}\.[1-9]", p.name)),
                     key=lambda p: [int(x) for x in p.name.split(".")[:2]]):
        q = master(pf)
        if not q:
            continue
        meta = front_matter(q)
        pnum = ".".join(pf.name.split(".")[:2])
        stem = q.stem
        title = meta.get("title", stem)
        anchor = f"paper-{pnum.replace('.', '-')}"
        out.append(f"## {pnum} {title} {{#{anchor}}}\n")
        if meta.get("subtitle"):
            out.append(f"*{meta['subtitle']}*\n")
        if meta.get("abstract"):
            out.append(meta["abstract"] + "\n")
        ls = [l for l in (link("Slides", f"Slides-{stem}.pptx"), link("Policy brief", f"Brief-{stem}.docx"),
                          link("Full paper", f"{stem}.docx")) if l]
        if ls:
            out.append(" · ".join(ls) + "\n")
        titles.append((pnum, title.split(":")[0].strip(), anchor))
    (SITE / "research" / f"{slug}.qmd").write_text("\n".join(out), encoding="utf-8")
    papers_out.append((sec, titles))


def main():
    (SITE / "research").mkdir(exist_ok=True)
    index = []
    for sec in SECTIONS:
        section_page(sec, index)
    home = ["---\ntitle: \"Research\"\n---\n",
            "Papers on climate policy and climate finance for finance ministries and development banks, in seven "
            "series. Each series page gives the abstracts and the slides, policy brief and full paper for every "
            "paper. Older papers, books and essays are under [More papers and books](research/more.qmd).\n"]
    for (folder_name, slug, name, line, *_), titles in index:
        num = folder_name.split(".")[0]
        home.append(f"### [{num}. {name}](research/{slug}.qmd)\n")
        home.append(line + "\n")
        if titles:
            home.append("\n".join(f"- [{p} {t}](research/{slug}.qmd#{a})" for p, t, a in titles) + "\n")
    home.append("### [More papers and books](research/more.qmd)\n")
    home.append("The tax book *Screwed?!*, *Time and Chance*, *The Right Policy at the Wrong Time*, earlier finance "
                "papers, and essays on philosophy and politics.\n")
    (SITE / "research.qmd").write_text("\n".join(home), encoding="utf-8")
    print("wrote research.qmd and", len(SECTIONS), "section pages")


if __name__ == "__main__":
    main()
