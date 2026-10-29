"""Copy the working-paper series (sections 1, 2 and 3) to the website's papers/ folder.

Stable permalinks, one per paper and form, overwritten on each publish:
    papers/<PaperName>.docx         the academic working paper (current version)
    papers/Brief-<PaperName>.docx   the Climate Fiscal Policy Brief (current version)
    papers/Slides-<PaperName>.pptx  the four-slide deck, where it exists

Run from B Working Papers/7.Website:  python publish_series.py
Then: quarto render, and deploy.bat (on Stephen's machine) to upload _site.
Log every publish in A Writing Instructions/Writing Standards/publishing-log.md.
"""
import shutil
from pathlib import Path

PAPERS = {
    "1.ClimateAndFiscalPolicy/1.1.OpenEconomyCarbonPricing": "OpenEconomyCarbonPricing",
    "1.ClimateAndFiscalPolicy/1.2.FeebatesAndOutputBasedRebating": "FeebatesAndOutputBasedRebating",
    "1.ClimateAndFiscalPolicy/1.3.IronSteelCBAM": "IronSteelCBAM",
    "1.ClimateAndFiscalPolicy/1.6.CarbonConsumptionTax": "CarbonConsumptionTax",
    "1.ClimateAndFiscalPolicy/1.7.PolicyEquivalentCarbonPriceAndCES": "PolicyEquivalentCarbonPriceAndCES",
    "2.FinanceAndRisk/2.1.ClimateFinanceIntermediationForCleanPower": "ClimateFinanceIntermediationForCleanPower",
    "2.FinanceAndRisk/2.2.CleanPowerAssetClasses": "CleanPowerAssetClasses",
    "3.SovereignIncentives/3.1.NotionalCapitalisedValueAndGuarantees": "NotionalCapitalisedValueAndGuarantees",
    "3.SovereignIncentives/3.2.ClimateInvestmentTrust": "ClimateInvestmentTrust",
    "3.SovereignIncentives/3.3.SustainabilityLinkedLending": "SustainabilityLinkedLending",
}
OVERVIEWS = {
    "2.FinanceAndRisk/2.0.OverviewMobilisingPrivateCapital.docx": "OverviewMobilisingPrivateCapital.docx",
    "3.SovereignIncentives/3.0.OverviewSovereignIncentives.docx": "OverviewSovereignIncentives.docx",
}
out = Path("papers")
out.mkdir(exist_ok=True)
for folder, name in PAPERS.items():
    d = Path("..") / folder
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
    s = Path("..") / src
    if s.exists():
        shutil.copy2(s, out / dst)
        print(f"published {out / dst}")
    else:
        print(f"missing   {s}")
