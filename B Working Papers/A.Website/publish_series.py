"""Copy the working-paper series (sections 1 to 5) to the website's papers/ folder.

Stable permalinks, one per paper and form, overwritten on each publish:
    papers/<PaperName>.docx         the academic working paper (current version)
    papers/Brief-<PaperName>.docx   the Climate Fiscal Policy Brief (current version)
    papers/Slides-<PaperName>.pptx  the four-slide deck, where it exists
    papers/Overview<Section>.docx   each section's overview, and papers/Slides-<Section>.pptx its theme deck

Section 5 papers are working paper and slides only (no brief); missing briefs are reported and skipped.

Run from B Working Papers/A.Website:  python publish_series.py
Then: quarto render, and deploy.bat (on Stephen's machine) to upload _site.
Log every publish in A Writing Instructions/Writing Standards/publishing-log.md.
"""
import shutil
from pathlib import Path

ROOT = Path("..")


def find(name):
    """Locate a paper folder or overview file by name anywhere under B Working Papers."""
    hits = [p for p in ROOT.rglob(name) if "8.PreviousVersions" not in p.parts and "A.Website" not in p.parts]
    # prefer the copy with real content (skips stale local folders holding only __pycache__)
    hits.sort(key=lambda p: -sum(1 for f in (p.rglob("*") if p.is_dir() else [p]) if "__pycache__" not in f.parts))
    return hits[0] if hits else ROOT / name

PAPERS = {
    "1.1.OpenEconomyCarbonPricing": "OpenEconomyCarbonPricing",
    "1.2.FeebatesAndOutputBasedRebating": "FeebatesAndOutputBasedRebating",
    "1.3.IronSteelCBAM": "IronSteelCBAM",
    "1.6.CarbonConsumptionTax": "CarbonConsumptionTax",
    "4.5.PolicyEquivalentCarbonPriceAndCES": "PolicyEquivalentCarbonPriceAndCES",
    "2.1.ClimateFinanceIntermediationForCleanPower": "ClimateFinanceIntermediationForCleanPower",
    "2.2.CleanPowerAssetClasses": "CleanPowerAssetClasses",
    "3.1.NotionalCapitalisedValueAndGuarantees": "NotionalCapitalisedValueAndGuarantees",
    "3.2.ClimateInvestmentTrust": "ClimateInvestmentTrust",
    "3.3.SustainabilityLinkedLending": "SustainabilityLinkedLending",
    "4.1.CPATMitigationMethods": "CPATMitigationMethods",
    "4.2.CPATAIImplementation": "CPATAIImplementation",
    "4.3.CPATValidation": "CPATValidation",
    "4.4.ElasticityValidation": "ElasticityValidation",
    "4.5.CBAMPolicyTool": "CBAMPolicyTool",
    "4.6.PublicInvestment": "PublicInvestment",
    "4.7.ActivityModelling": "ActivityModelling",
    "5.1.ExciseFiscalDiagnostic": "ExciseFiscalDiagnostic",
    "5.2.MacroFiscalEnergyScenarioTool": "MacroFiscalEnergyScenarioTool",
    "5.3.FiscalIndicatorsDashboard": "FiscalIndicatorsDashboard",
}
OVERVIEWS = {
    "1.0.OverviewClimateAndFiscalPolicy.docx": "OverviewClimateAndFiscalPolicy.docx",
    "2.0.OverviewMobilisingPrivateCapital.docx": "OverviewMobilisingPrivateCapital.docx",
    "3.0.OverviewSovereignIncentives.docx": "OverviewSovereignIncentives.docx",
    "4.0.OverviewModelling.docx": "OverviewModelling.docx",
    "5.0.OverviewAnalytics.docx": "OverviewAnalytics.docx",
    # Section theme decks
    "Slides-ClimateAndFiscalPolicy.pptx": "Slides-ClimateAndFiscalPolicy.pptx",
    "Slides-FinanceAndRisk.pptx": "Slides-FinanceAndRisk.pptx",
    "Slides-SovereignIncentives.pptx": "Slides-SovereignIncentives.pptx",
    "Slides-Modelling.pptx": "Slides-Modelling.pptx",
    "Slides-Analytics.pptx": "Slides-Analytics.pptx",
    # Books
    "Screwed.docx": "Screwed.docx",
}
out = Path("papers")
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
