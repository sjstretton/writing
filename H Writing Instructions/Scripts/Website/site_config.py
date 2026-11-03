"""One place that says how the website is laid out. The other website scripts import it.

The site has three research parts, each with its own top tab, home page, folder and sidebar:
    Policy and Finance        papers in "C Policy and FInance" (sections 1-4), pages in E Website/policy/,
                              home page policy/index.qmd
    Modelling and Analytics   papers in "D Modelling" (sections 5-7), pages in E Website/modelling/,
                              home page modelling/index.qmd
    New Research              papers in "B Theory and Research": new work awaiting Stephen's review, in section
                              folders named like the series (B Theory and Research/5.Modelling/5.5.<Name>), so each
                              paper keeps the number of the section it will join. Pages in E Website/new/,
                              home page new/index.qmd. Once reviewed, a paper moves to its section in C or D.
plus the site's home page, index.qmd (what the research covers), written by hand.
A section number can appear in more than one part (5 in Modelling and Analytics and in New Research), so scripts
find a paper's part and section from where its folder sits (locate) or by its number across all parts (find_paper).

Modelling and Analytics is due to move to its own repository. When it does, delete its entry in PARTS
(and its tab in _quarto.yml); nothing else depends on it.

WEB_PAPERS lists the papers that also get a web version, read on the site with a contents sidebar
(build_web_papers.py). Add a paper folder name to put another paper on the web.
WEB_BOOKS does the same for books, one web page per chapter.
"""
from pathlib import Path

# True: the site carries no author name or institutional affiliation (anonymise.py). The masters keep both;
# only the web pages, the PDFs and the slide PDFs made for the site are anonymised, and the books and earlier
# papers marked "named": True below (already published under the author's name) are left off the site.
ANONYMOUS = True

REPO = Path(__file__).resolve().parents[3]
SITE = REPO / "E Website"
ARCHIVE = SITE / "PaperArchive"   # every paper, brief, deck and overview, copied by publish_series.py; never uploaded
PAPERS = SITE / "papers"          # only the files the pages link to; uploaded

# section folder, page slug, name, one-line description, published overview file (or None), published series deck (or None)
# "aliases": False leaves out the redirects from the old research/ addresses (only the first two parts had them).
PARTS = [
    {
        "key": "policy",
        "title": "Policy and Finance",
        "root": REPO / "C Policy and FInance",
        "dir": "policy",
        "home": "policy/index.qmd",
        "intro": ("Papers on climate and fiscal policy and on climate finance, written for finance ministries and "
                  "development banks, in four sections. The modelling and analytics work is under "
                  "[Modelling and Analytics](../modelling/index.qmd)."),
        "more": None,
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
                  "them; and analytics on data ministries already hold. The policy papers are under "
                  "[Policy and Finance](../policy/index.qmd)."),
        "more": None,
        "sections": [
            ("5.Modelling", "5-modelling", "Modelling (CPAT)",
             "Models a finance ministry can audit: the Climate Policy Assessment Tool stated, rebuilt and validated.",
             "OverviewModelling.docx", "Slides-Modelling.pptx"),
            ("6.ModularUpgrades", "6-modular-upgrades", "Modular Upgrades",
             "Extensions to CPAT where policy needs them: carbon-price equivalents, CBAM, public investment, activity and macro-fiscal scenarios.",
             "OverviewModularUpgrades.docx", "Slides-ModularUpgrades.pptx"),
            ("7.AdditionalAnalytics", "7-analytics", "Analytics Tools",
             "Diagnostics on data ministries already hold: excise systems and fiscal indicators.",
             "OverviewAnalytics.docx", "Slides-Analytics.pptx"),
        ],
    },
    {
        "key": "new",
        "title": "New Research",
        "root": REPO / "B Theory and Research",
        "dir": "new",
        "home": "new/index.qmd",
        "aliases": False,
        "intro": ("Recent papers, not yet reviewed. Each keeps the number of the section it will join, and moves "
                  "there once it has been reviewed; each has a short policy brief as its page and the full working "
                  "paper one level below. The reviewed papers are under [Policy and Finance](../policy/index.qmd) "
                  "and [Modelling and Analytics](../modelling/index.qmd)."),
        "more": None,
        "sections": [
            ("5.Modelling", "5-modelling", "Modelling (CPAT)",
             "Evidence a carbon-pricing model should match: what real carbon taxes, fuel taxes and price shocks did to emissions.",
             None, None),
        ],
    },
]

# Books and earlier papers, listed at the end of their section's page (and in the sidebar under the section).
# Section folder -> list of entries: title, subtitle, by (co-authors, or None), one-paragraph description,
# the published PDF in papers/ (from publish_series.BOOKS) and, for a book read on the site, its WEB_BOOKS folder.
SECTION_EXTRAS = {
    "1.CarbonPricing": [
        {"title": "The Right Policy at the Wrong Time", "subtitle": "Carbon Pricing and the Order of Things",
         "kind": "Book", "by": None,
         "text": ("The case for a carbon price was won intellectually and lost operationally. This book makes the "
                  "case for feebates and for sequencing: price the margin first, and leave the carbon bill for later."),
         "pdf": "CarbonPricingRightPolicyWrongTime.pdf", "web": None},
    ],
    "2.OtherTaxAndFiscalPolicy": [
        {"title": "Plucked!", "subtitle": "A Guide to a Fair, Simple, Efficient and Politically Feasible Tax and Benefits System",
         "kind": "Book", "by": "with Gordon Styles, 2020", "named": True,
         "text": ("A case for reforming UK taxes and benefits, from the principles of a good tax system to welfare and "
                  "work, inequality, corporations, land and property, money and debt, and the environment, ending "
                  "with a set of proposals."),
         "pdf": "Plucked.pdf", "web": "8.5.3.Plucked"},
    ],
    "3.FinanceAndRisk": [
        {"title": "Time and Chance", "subtitle": "The Elements of Scale in the Green Transition",
         "kind": "Book", "by": None,
         "text": ("Why clean energy costs too much in the countries that need it most. The book works from the price of "
                  "money through contracts and instruments to the institutions that would carry them."),
         "pdf": "TimeAndChance.pdf", "web": None},
    ],
    "4.SovereignIncentives": [
        {"title": "Sustainability-Linked Intermediated Debt Instruments (SLIDIs)", "subtitle": None,
         "kind": "Earlier paper", "by": "with Marcello Estevão and Nils Zimmermann", "named": True,
         "text": ("Lowering developing countries' cost of borrowing while rewarding their governments for agreed "
                  "environmental, social and governance progress, through sustainability-linked debt issued via an "
                  "intermediary."),
         "pdf": "SLIDIs.pdf", "web": None},
    ],
}

# Paper folders kept off the site for now; delete a name to publish it on the next compile. (Drafts awaiting review
# go to "B Theory and Research" and the New Research tab instead.)
HOLD = set()

# Folders inside a section that hold books, not papers: listed through SECTION_EXTRAS, not as numbered papers.
BOOK_FOLDERS = {"3.3.TimeAndChance"}

WEB_PAPERS = [
    "1.1.OpenEconomyCarbonPricing",
    "1.2.FeebatesAndOutputBasedRebating",
    "1.3.CarbonConsumptionTax",
    "1.4.IronSteelCBAM",
    "2.1.RentTax",
    "2.2.LandPaysForTheCity",
    "3.1.ClimateFinanceIntermediationForCleanPower",
    "3.2.CleanPowerAssetClasses",
    "4.1.NotionalCapitalisedValueAndGuarantees",
    "4.2.ClimateInvestmentTrust",
    "4.3.SustainabilityLinkedLending",
    "5.1.CPATMitigationMethods",
    "5.2.CPATAIImplementation",
    "5.3.CPATValidation",
    "5.4.ElasticityValidation",
    "5.5.CarbonPriceNaturalExperiments",
    "6.1.PolicyEquivalentCarbonPriceAndCES",
    "6.2.CBAMPolicyTool",
    "6.3.PublicInvestment",
    "6.4.ActivityModelling",
    "6.5.MacroFiscalEnergyScenarioTool",
    "7.1.ExciseFiscalDiagnostic",
    "7.2.FiscalIndicatorsDashboard",
]

# Books that are also read on the site, one page per chapter, under <part dir>/books/<BookName>/
# (build_web_papers.py writes them; build_research_pages.py lists them in the sidebar under their section).
# Book folder -> the part it sits in and a one-paragraph description for the book's contents page.
WEB_BOOKS = {
    "8.5.3.Plucked": {
        "part": "policy",
        "named": True,
        "blurb": ("A book-length case for reforming UK taxes and benefits, written with Gordon Styles in 2020. "
                  "Its fourteen chapters run from the ideas behind taxation and the principles of a good tax system "
                  "to welfare and work, inequality, corporations, land and property, money and debt, and the "
                  "environment, and end with a set of proposals."),
    },
}

if ANONYMOUS:
    SECTION_EXTRAS = {k: [x for x in v if not x.get("named")] for k, v in SECTION_EXTRAS.items()}
    WEB_BOOKS = {k: v for k, v in WEB_BOOKS.items() if not v.get("named")}


def part_of_section(num):
    """The first part and section tuple for a section number such as '1'. A number can be in more than one part
    (5 is in Modelling and Analytics and in New Research): to place a paper, use locate() or find_paper()."""
    for part in PARTS:
        for sec in part["sections"]:
            if sec[0].split(".")[0] == str(num):
                return part, sec
    return None, None


def locate(folder):
    """The part and section a paper folder sits in, from its path."""
    folder = Path(folder).resolve()
    for part in PARTS:
        for sec in part["sections"]:
            if folder.parent == section_folder(part, sec).resolve():
                return part, sec
    return None, None


def find_paper(num):
    """(part, section, folder) for paper number num (e.g. '5.5'), searching every part."""
    for part in PARTS:
        for sec in part["sections"]:
            if sec[0].split(".")[0] != str(num).split(".")[0]:
                continue
            for pf in paper_folders(part, sec):
                if ".".join(pf.name.split(".")[:2]) == num:
                    return part, sec, pf
    return None, None, None


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
          if p.is_dir() and re.match(rf"^{num}\.[1-9]", p.name) and p.name not in BOOK_FOLDERS | HOLD]
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
