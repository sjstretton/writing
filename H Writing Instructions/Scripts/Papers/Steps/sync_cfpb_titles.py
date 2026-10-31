"""Set the Climate Fiscal Policy Brief (CFPB) bib entries to their final titles.

Usage: python sync_cfpb_titles.py file1.bib [file2.bib ...]
Replaces any one-line @techreport{CFPB<section><paper>, ...} entry for the carbon-pricing briefs
(CFPB11-CFPB13 and CFPB61, numbered per H Writing Instructions/NUMBERING.md) with the canonical one.
"""
import re
import sys

TITLES = {
    "CFPB11": "Price Production and Consumption Separately: A Two-Track Architecture for Carbon Pricing in Open Economies",
    "CFPB12": "Feebates: The Full Carbon Price at the Margin, Without the Carbon Bill",
    "CFPB14": "Credit the Price Signal, Not the Payment: Carbon Price Recognition and Scrap Shuffling under the {EU}'s Carbon Border Adjustment Mechanism",
    "CFPB13": "Converting a {VAT} into a Destination Carbon Tax: A Carbon Component in {VAT} and a Forward Obligation on Energy Suppliers in the {European Union}",
    "CFPB61": "Measure Carbon Pricing by the Emissions It Cuts: The Total Effective Carbon Price",
}


def entry(key):
    return (f"@techreport{{{key}, author={{Stretton, Stephen J.}}, title={{{TITLES[key]}}}, "
            f"institution={{Climate Fiscal Policy Briefs}}, number={{{key[4]}.{key[5]}}}, year={{2026}}}}")


for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    for key in TITLES:
        text = re.sub(r"@techreport\{" + key + r",[^\n]*", lambda m: entry(key), text)
    open(path, "w", encoding="utf-8").write(text)
    print("updated", path)
