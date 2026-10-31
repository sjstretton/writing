"""Copy the working-paper series (sections 1 to 7) and the section 8 overviews and books to the website's papers/ folder.

Stable permalinks, one per paper and form, overwritten on each publish:
    papers/<PaperName>.docx         the academic working paper (current version)
    papers/Brief-<PaperName>.docx   the Climate Fiscal Policy Brief (current version)
    papers/Slides-<PaperName>.pptx  the four-slide deck, where it exists
    papers/Overview<Section>.docx   each section's overview, and papers/Slides-<Section>.pptx its theme deck

Papers in sections 5 to 7, and Rent Tax (2.1), are working paper and slides only (no brief); missing files are reported and skipped.
Folder and file names follow H Writing Instructions/NUMBERING.md; published names stay stable so links survive renumbering.

Run from anywhere:  python "H Writing Instructions/Scripts/Website/publish_series.py" (Compile-Website.bat at the repo root does this)
Then: quarto render, and deploy.bat (on Stephen's machine) to upload _site.
Log every publish in H Writing Instructions/Writing Standards/publishing-log.md.
"""
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
ROOTS = [REPO / "C Policy and FInance", REPO / "D Modelling"]   # the papers: sections 1-4, then 5-7
SITE = REPO / "E Website"          # the Quarto site


def find(name):
    """Locate a paper folder or overview file by name anywhere under the paper folders (ROOTS)."""
    hits = [p for r in ROOTS for p in r.rglob(name) if "8.PreviousVersions" not in p.parts and "A.Website" not in p.parts]
    # prefer the copy with real content (skips stale local folders holding only __pycache__)
    hits.sort(key=lambda p: -sum(1 for f in (p.rglob("*") if p.is_dir() else [p]) if "__pycache__" not in f.parts))
    return hits[0] if hits else ROOTS[0] / name

PAPERS = {
    "1.1.OpenEconomyCarbonPricing": "OpenEconomyCarbonPricing",
    "1.2.FeebatesAndOutputBasedRebating": "FeebatesAndOutputBasedRebating",
    "1.3.IronSteelCBAM": "IronSteelCBAM",
    "1.4.CarbonConsumptionTax": "CarbonConsumptionTax",
    "2.1.RentTax": "RentTax",
    "3.1.ClimateFinanceIntermediationForCleanPower": "ClimateFinanceIntermediationForCleanPower",
    "3.2.CleanPowerAssetClasses": "CleanPowerAssetClasses",
    "4.1.NotionalCapitalisedValueAndGuarantees": "NotionalCapitalisedValueAndGuarantees",
    "4.2.ClimateInvestmentTrust": "ClimateInvestmentTrust",
    "4.3.SustainabilityLinkedLending": "SustainabilityLinkedLending",
    "5.1.CPATMitigationMethods": "CPATMitigationMethods",
    "5.2.CPATAIImplementation": "CPATAIImplementation",
    "5.3.CPATValidation": "CPATValidation",
    "5.4.ElasticityValidation": "ElasticityValidation",
    "6.1.PolicyEquivalentCarbonPriceAndCES": "PolicyEquivalentCarbonPriceAndCES",
    "6.2.CBAMPolicyTool": "CBAMPolicyTool",
    "6.3.PublicInvestment": "PublicInvestment",
    "6.4.ActivityModelling": "ActivityModelling",
    "6.5.MacroFiscalEnergyScenarioTool": "MacroFiscalEnergyScenarioTool",
    "7.1.ExciseFiscalDiagnostic": "ExciseFiscalDiagnostic",
    "7.2.FiscalIndicatorsDashboard": "FiscalIndicatorsDashboard",
}
OVERVIEWS = {
    "1.0.OverviewClimateAndFiscalPolicy.docx": "OverviewClimateAndFiscalPolicy.docx",
    "2.0.OverviewOtherTaxAndFiscalPolicy.docx": "OverviewOtherTaxAndFiscalPolicy.docx",
    "3.0.OverviewMobilisingPrivateCapital.docx": "OverviewMobilisingPrivateCapital.docx",
    "4.0.OverviewSovereignIncentives.docx": "OverviewSovereignIncentives.docx",
    "5.0.OverviewModelling.docx": "OverviewModelling.docx",
    "6.0.OverviewModularUpgrades.docx": "OverviewModularUpgrades.docx",
    "7.0.OverviewAnalytics.docx": "OverviewAnalytics.docx",
    "8.0.OverviewAdditionalPolicyPapers.docx": "OverviewAdditional.docx",
    "8.5.0.OverviewBooks.docx": "OverviewBooks.docx",
    "8.6.0.OverviewPhilosophy.docx": "OverviewPhilosophy.docx",
    "8.7.0.OverviewPolitics.docx": "OverviewPolitics.docx",
    # Section theme decks
    "Slides-ClimateAndFiscalPolicy.pptx": "Slides-ClimateAndFiscalPolicy.pptx",
    "Slides-FinanceAndRisk.pptx": "Slides-FinanceAndRisk.pptx",
    "Slides-SovereignIncentives.pptx": "Slides-SovereignIncentives.pptx",
    "Slides-Modelling.pptx": "Slides-Modelling.pptx",
    "Slides-Analytics.pptx": "Slides-Analytics.pptx",
    # Books
    "Screwed.docx": "Screwed.docx",
}
out = SITE / "papers"
out.mkdir(exist_ok=True)
for folder, name in PAPERS.items():
    d = find(folder)
    for src, dst in [
        (d / f"{name}.docx", out / f"{name}.docx"),
        (d / "1.Presentation" / f"Brief-{name}.docx", out / f"Brief-{name}.docx"),
        (d / "1.Presentation" / f"Slides-{name}.pptx", out / f"Slides-{name}.pptx"),
    ]:
        if src.exists():
            shutil.copy2(src, dst)
            print(f"published {dst}")
        else:
            print(f"missing   {src}")
for src, dst in OVERVIEWS.items():
    s = find(src)
    if s.exists():
        shutil.copy2(s, out / dst)
        print(f"published {out / dst}")
    else:
        print(f"missing   {s}")
