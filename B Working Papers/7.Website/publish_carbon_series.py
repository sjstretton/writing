"""Copy the carbon-pricing series to the website's papers/ folder.

Stable permalinks, one per paper and form, overwritten on each publish:
    papers/<PaperName>.docx         the academic working paper (current version)
    papers/Brief-<PaperName>.docx   the Climate Fiscal Policy Brief (current version)
    papers/Slides-<PaperName>.pptx  the four-slide deck, where it exists

Run from B Working Papers/7.Website:  python publish_carbon_series.py
Then: quarto render, and deploy.bat (on Stephen's machine) to upload _site.
Log every publish in A Writing Instructions/Writing Standards/publishing-log.md.
"""
import shutil
from pathlib import Path

SERIES = Path("../1.ClimateAndFiscalPolicy")
PAPERS = {
    "1.1.OpenEconomyCarbonPricing": "OpenEconomyCarbonPricing",
    "1.2.FeebatesAndOutputBasedRebating": "FeebatesAndOutputBasedRebating",
    "1.3.IronSteelCBAM": "IronSteelCBAM",
    "1.6.CarbonConsumptionTax": "CarbonConsumptionTax",
    "1.7.PolicyEquivalentCarbonPriceAndCES": "PolicyEquivalentCarbonPriceAndCES",
}
out = Path("papers")
out.mkdir(exist_ok=True)
for folder, name in PAPERS.items():
    d = SERIES / folder
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
