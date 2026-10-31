"""One place that says how the website is laid out. The other website scripts import it.

The site has two research parts, each with its own top tab, home page, folder and sidebar:
    Policy and Finance        papers in "C Policy and FInance" (sections 1-4), pages in E Website/policy/,
                              home page index.qmd (the site's landing page)
    Modelling and Analytics   papers in "D Modelling" (sections 5-7), pages in E Website/modelling/,
                              home page modelling/index.qmd
plus About (about.qmd).

Modelling and Analytics is due to move to its own repository. When it does, delete its entry in PARTS
(and its tab in _quarto.yml); nothing else depends on it.

WEB_PAPERS lists the papers that also get a web version, read on the site with a contents sidebar
(build_web_papers.py). Add a paper folder name to put another paper on the web.
WEB_BOOKS does the same for books, one web page per chapter.
"""
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SITE = REPO / "E Website"
ARCHIVE = SITE / "PaperArchive"   # every paper, brief, deck and overview, copied by publish_series.py; never uploaded
PAPERS = SITE / "papers"          # only the files the pages link to; uploaded

# section folder, page slug, name, one-line description, published overview file, published series deck (or None)
PARTS = [
    {
        "key": "policy",
        "title": "Policy and Finance",
        "root": REPO / "C Policy and FInance",
        "dir": "policy",
        "home": "index.qmd",
        "intro": ("Papers on climate and fiscal policy and on climate finance, written for finance ministries and "
                  "development banks, in four sections. Each section page gives the abstract of every paper with its "
                  "slides, policy brief and full paper; papers marked *Read online* can be read here in full. "
                  "Books and earlier papers are under [Books and other papers](policy/more.qmd). The modelling and "
                  "analytics work is under [Modelling and Analytics](modelling/index.qmd)."),
        "more": "policy/more.qmd",
        "sections": [
            ("1.CarbonPricing", "1-carbon-pricing", "Carbon Pricing",
             "Price production and consumption separately: a feebate on emissions intensity, a destination carbon tax through VAT, and recognition of both at the border.",
             "OverviewClimateAndFiscalPolicy.docx", "Slides-ClimateAndFiscalPolicy.pptx"),
            ("2.OtherTaxAndFiscalPolicy", "2-other-tax", "Other Tax and Fiscal Policy",
             "Tax rent, not effort: land and corporate taxes that hold up when capital and people can move.",
             "OverviewOtherTaxAndFiscalPolicy.docx", "Slides-OtherTaxAndFiscalPolicy.pptx"),
            ("3.FinanceAndRisk", "3-finance-and-risk", "Finance and Risk",
             "Make clean power an asset class: remove payment risk at source, then turn projects into standard securities.",
             "OverviewMobilisingPrivateCapital.docx", "Slides-FinanceAndRisk.pptx"),
            ("4.SovereignIncentives", "4-sovereign-incentives", "Sovereign Incentives",
             "Reward governments, not projects: guarantee capacity and held capital that pay for acting early.",
             "OverviewSovereignIncentives.docx", "Slides-SovereignIncentives.pptx"),
        ],
    },
    {
        "key": "modelling",
        "title": "Modelling and Analytics",
        "root": REPO / "D Modelling",
        "dir": "modelling",
        "home": "modelling/index.qmd",
        "intro": ("Models and diagnostics a finance ministry can audit, in three sections: the Climate Policy "
                  "Assessment Tool (CPAT) stated, rebuilt and validated; modular upgrades to CPAT where policy needs "
                  "them; and analytics on data ministries already hold. Each section page gives the abstract of every "
                  "paper with its slides and full paper. The policy papers are under "
                  "[Policy and Finance](../index.qmd)."),
        "more": None,
        "sections": [
            ("5.Modelling", "5-modelling", "Modelling (CPAT)",
             "Models a finance ministry can audit: the Climate Policy Assessment Tool stated, rebuilt and validated.",
             "OverviewModelling.docx", "Slides-Modelling.pptx"),
            ("6.ModularUpgrades", "6-modular-upgrades", "Modular Upgrades",
             "Extensions to CPAT where policy needs them: carbon-price equivalents, CBAM, public investment, activity and macro-fiscal scenarios.",
             "OverviewModularUpgrades.docx", None),
            ("7.AdditionalAnalytics", "7-analytics", "Analytics Tools",
             "Diagnostics on data ministries already hold: excise systems and fiscal indicators.",
             "OverviewAnalytics.docx", "Slides-Analytics.pptx"),
        ],
    },
]

# Folders inside a section that hold books, not papers: listed under Books (policy/more.qmd), not in the section.
BOOK_FOLDERS = {"3.3.TimeAndChance"}

WEB_PAPERS = [
    "1.1.OpenEconomyCarbonPricing",
    "1.2.FeebatesAndOutputBasedRebating",
    "1.3.CarbonConsumptionTax",
    "1.4.IronSteelCBAM",
    "2.1.RentTax",
    "3.1.ClimateFinanceIntermediationForCleanPower",
    "3.2.CleanPowerAssetClasses",
]

# Books that are also read on the site, one page per chapter, under <part dir>/books/<BookName>/
# (build_web_papers.py writes them; build_research_pages.py lists them in the sidebar under Books and other papers).
# Book folder -> the part it sits in and a one-paragraph description for the book's contents page.
WEB_BOOKS = {
    "8.5.3.Plucked": {
        "part": "policy",
        "blurb": ("A book-length case for reforming UK taxes and benefits, written with Gordon Styles in 2020. "
                  "Its fourteen chapters run from the ideas behind taxation and the principles of a good tax system "
                  "to welfare and work, inequality, corporations, land and property, money and debt, and the "
                  "environment, and end with a set of proposals. The manuscript is kept as written in 2020; only the "
                  "title has changed."),
    },
}


def part_of_section(num):
    """The part and section tuple for a section number such as '1'."""
    for part in PARTS:
        for sec in part["sections"]:
            if sec[0].split(".")[0] == str(num):
                return part, sec
    return None, None


def section_folder(part, sec):
    return part["root"] / sec[0]


def paper_folders(part, sec):
    """The numbered paper folders of a section, in order (books and overviews left out)."""
    import re
    folder = section_folder(part, sec)
    num = sec[0].split(".")[0]
    if not folder.is_dir():
        return []
    fs = [p for p in folder.iterdir()
          if p.is_dir() and re.match(rf"^{num}\.[1-9]", p.name) and p.name not in BOOK_FOLDERS]
    return sorted(fs, key=lambda p: [int(x) for x in p.name.split(".")[:2]])


def paper_name(folder):
    return folder.name.split(".", 2)[-1]


def master_qmd(folder):
    q = folder / f"{paper_name(folder)}.qmd"
    if q.exists():
        return q
    qs = list(folder.glob("*.qmd"))
    return qs[0] if qs else None


def web_page(part, sec, name):
    """Site-relative path of a paper's web version (whether or not it exists)."""
    return f"{part['dir']}/{sec[1]}/{name}/index.qmd"


def part_by_key(key):
    return next(p for p in PARTS if p["key"] == key)


def book_name(folder_name):
    """'8.5.3.Plucked' -> 'Plucked' (book folders can have three number parts)."""
    return folder_name.rsplit(".", 1)[-1]


def book_dir(part, name):
    """Site-relative folder of a book's web version: its contents page is index.qmd, one .qmd per chapter."""
    return f"{part['dir']}/books/{name}"
