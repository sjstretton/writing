# Corrections to `OpenEconomyCarbonPricing.bib` (29 Oct 2026)

**Scope.** This note checks the 42 entries in the v0.3 `.bib`: the original 30, plus EU2025DV, BushnellChenZaragozaWatkins2014, FischerFox2011, Markusen1975, Hoel1996, Armington1969, Kydland1977 and HelmHepburnMash2003, plus four CFPB entries.

**Method.** Each entry was checked against Crossref (api.crossref.org) by DOI or by bibliographic search. World Bank items were checked against the World Bank Open Knowledge Repository API. The `.bib` itself has not been edited.

**Status codes.** "Fix" means a change to the entry. "Confirm" means the details are right as they stand: replace the `VERIFY` note with the confirmation shown and add the DOI. "Text" means a problem with how the paper cites the source, not with the entry.

**Summary.**

- **8 corrections** to entries, covering wrong or missing fields and wrong metadata in the companion download list.
- **4 text-level problems** with how a source is cited.
- **24 entries** move from `VERIFY` to confirmed, with the DOI added.
- **6 entries** remain unverifiable from here.

## Corrections (change the entry)

| # | Key | Problem | Correction |
|---|---|---|---|
| 1 | ParryRoafBlack2021 | Author order and title | Crossref: **Parry, Ian; Black, Simon; Roaf, James**. Title "Proposal for an International Carbon Price Floor Among Large Emitters" (no leading "A"). June 2021. Add `doi = {10.5089/9781513583204.066}`. Key can stay. |
| 2 | Klenert2018 | Missing issue | Add `number = {8}` and `doi = {10.1038/s41558-018-0201-2}`. Authors and pages 669–677 confirmed. |
| 3 | HLCCP2017 | Wrong DOI in the series download list | `Downloads-OpenEconomyCarbonPricing.csv` gives DOI 10.1596/32419. That DOI belongs to the 2019 *Report of the High-Level Commission on Carbon Pricing and Competitiveness*, a different report. The 2017 report has no Crossref DOI. Publisher: Carbon Pricing Leadership Coalition / World Bank. The "\$50–100 by 2030" range matches my recollection of the report (with \$40–80 by 2020), but it is still VERIFY. |
| 4 | WorldBank2025 | Edition details and figures | Add `doi = {10.1596/978-1-4648-2255-1}` and `url = {https://openknowledge.worldbank.org/handle/10986/43277}`. Issued 10 June 2025. Make it `@book` with `publisher`. **Text:** coverage is "around 28%", up from 24% after China's ETS expansion, not "about a quarter". The global emissions-weighted average price is about USD 5. The series CSV gives DOI 10.1596/40700, which does not match the OKR record for the 2025 edition. VERIFY which edition that DOI is. |
| 5 | WorldBankTCAF | No verifiable source | No TCAF policy-crediting methodology document is reachable (tcafwb.org returns 403, and there are no OKR hits). Replace with, or add, **Strand (2020), PRWP 9443**, doi:10.1596/1813-9450-9443, on results-based payments for carbon taxes. It derives the same ½·t threshold as Proposition 6. Add **PMR (2017)**, *Establishing Scaled-Up Crediting Program Baselines under the Paris Agreement*, doi:10.1596/28785. Both are in `5.Notes/LiteratureAppendix.bib`. Keep the TCAF entry only if Klaus Oppermann supplies a document. |
| 6 | Kydland1977 | Key style | The series uses `KydlandPrescott1977` (the 1.6 brief). Use one key across the series. Details confirmed: JPE 85(3), 473–491, doi:10.1086/260580. |
| 7 | Auerbach2017 | Not in Crossref | OUCBT WP 17/01 cannot be confirmed here (SSRN record 10.2139/ssrn.2908158 exists; SSRN is blocked). Add or replace with the open-access chapter: Devereux, Auerbach, Keen, Oosterhuis, Schön and Vella (2021), "Destination-Based Cash Flow Taxation", in *Taxing Profit in a Global Economy*, OUP, 267–334, doi:10.1093/oso/9780198808060.003.0007. |
| 8 | KeenParryRoaf2022 | Wrong DOI in the series download list | The `.bib` entry is right: *Fiscal Studies* 43(3), 209–234. Add `doi = {10.1111/1475-5890.12307}`. The download CSV lists 10.5089/9781557752567.001.a001, which is the IMF working-paper chapter record. The working paper's own citation is IMF WP/21/239. |

## Text-level problems (how the paper uses a source)

| # | Where in v0.3 | Problem | Suggested fix |
|---|---|---|---|
| T1 | Related literature: "leakage rates … cluster between 5 and 25 percent [@BrangerQuirion2014; @BoehringerBalistreriRutherford2012]" | The 5–25 percent range (mean 14) is Branger and Quirion's. EMF 29 reports its own range, which I have not confirmed. | Cite B&Q for the range. Cite EMF 29 separately, after checking its numbers. |
| T2 | Related literature: pass-through "typically under half [@NeuhoffRitz2019]" | Ganapati, Shapiro and Walker (2020, *AEJ: Applied* 12(2)) find 70 percent pass-through of energy costs in US manufacturing. NeuhoffRitz2019 (EPRG WP 1935) is not in Crossref and was not read. | Report the range and attribute each end to its source. |
| T3 | Related literature and race-to-the-top: VAT spread "to more than 170 countries … because a destination tax does not disadvantage exporters [@KeenLockwood2010]" | Keen and Lockwood (2010) study the determinants and revenue effects of VAT adoption. The causal "because" may not be in the paper (not read; IMF copy refused). Lockwood and Whalley (2010) show that for a *uniform* tax, destination versus origin is trade-neutral. | Keep KeenLockwood2010 for the fact of spread. Cite LockwoodWhalley2010 for neutrality. Say that Proposition 7 rests on the charge varying with intensity, not on the destination basis as such. |
| T4 | What is new / Equivalence | The two closest precedents are not cited. Holland (2012, *JEEM* 63(3)) shows an intensity standard plus a consumption tax can reach the first best under leakage. Strand (2020) derives the ½·t crediting threshold. | Cite both (see the literature appendix synthesis). |

## Confirmed via Crossref: replace `VERIFY` and add the DOI

| Key | Confirmed details | DOI |
|---|---|---|
| KeenKotsogiannis2014 | *JIE* 94(1), 119–128 | 10.1016/j.jinteco.2014.03.002 |
| FischerFox2012 | *JEEM* 64(2), 199–216 | 10.1016/j.jeem.2012.01.005 |
| FischerFox2007 | *Land Economics* 83(4), 575–599; title as in .bib | 10.3368/le.83.4.575 |
| Fischer2001 | RFF DP 01-22, July 2001; title confirmed from the PDF | (none) |
| HollandHughesKnittel2009 | *AEJ: Economic Policy* 1(1), 106–146 | 10.1257/pol.1.1.106 |
| FowlieReguantRyan2016 | *JPE* 124(1), 249–302 | 10.1086/684484 |
| BoehringerBalistreriRutherford2012 | *Energy Economics* 34(S2), S97–S110 | 10.1016/j.eneco.2012.10.003 |
| BrangerQuirion2014 | *Ecological Economics* 99, 29–39 | 10.1016/j.ecolecon.2013.12.010 |
| IsmerNeuhoff2007 | *EJLE* 24(2), 137–164 | 10.1007/s10657-007-9032-8 |
| Mehling2019 | *AJIL* 113(3), 433–481; five authors as in .bib | 10.1017/ajil.2019.22 |
| Cosbey2019 | *REEP* 13(1), 3–22 | 10.1093/reep/rey020 |
| Grubb2022 | *ARER* 47, 753–795; 11 authors as in .bib (confirmed in Crossref and on the article PDF) | 10.1146/annurev-environ-120820-053625 |
| PetersHertwich2008 | *ES&T* 42(5), 1401–1407; title as in .bib | 10.1021/es072023k |
| Nordhaus2015 | *AER* 105(4), 1339–1370 | 10.1257/aer.15000001 |
| HelmHepburnRuta2012 | *OxREP* 28(2), 368–394 | 10.1093/oxrep/grs013 |
| KeenLockwood2010 | *JDE* 92(2), 138–151 | 10.1016/j.jdeveco.2009.01.012 |
| BushnellChenZaragozaWatkins2014 | *Energy Policy* 64, 313–323 | 10.1016/j.enpol.2013.08.065 |
| FischerFox2011 | *AER* 101(3), 258–262 | 10.1257/aer.101.3.258 |
| Markusen1975 | *JIE* 5(1), 15–29 | 10.1016/0022-1996(75)90025-2 |
| Hoel1996 | *JPubE* 59(1), 17–32 | 10.1016/0047-2727(94)01490-6 |
| Armington1969 | *IMF Staff Papers* 16(1), 159–178 | 10.2307/3866403 |
| Kydland1977 | *JPE* 85(3), 473–491 | 10.1086/260580 |
| HelmHepburnMash2003 | *OxREP* 19(3), 438–450 | 10.1093/oxrep/19.3.438 |
| KeenParryRoaf2022 | *Fiscal Studies* 43(3), 209–234 | 10.1111/1475-5890.12307 |

## Still unverifiable here (leave `VERIFY`)

- **NeuhoffRitz2019** (EPRG WP 1935): not in Crossref. Check on the EPRG website.
- **EU2023**: Article 9 ("carbon price paid in a country of origin"). EUR-Lex returned an empty page to a plain request, so the article number is still VERIFY. The OJ reference L 130, 16.5.2023, matches the 1.6 bibliography (pp. 52–104).
- **EU2025DV**: the Implementing Regulation 2025/2621 ELI page returned HTTP 202 (a bot check), so it is not confirmed.
- **HLCCP2017**: the range quoted. See correction 3.
- **StrettonCCT, StrettonFeebates, StrettonIndustrialFeebates, StrettonTECP, StrettonCBAM**: v0.3's text uses the CFPB keys instead. These five entries look unused and can be deleted once confirmed.
- **CFPB12, CFPB13, CFPB14, CFPB61**: series entries, not checkable. Titles should follow the series spec.

## Download-list cross-check

`Downloads-OpenEconomyCarbonPricing.csv` was not edited, at the coordinator's request. Its DOIs for HLCCP2017 and WorldBank2025 look wrong (corrections 3–4). It gives an SSRN DOI for KeenKotsogiannis2014 where the journal DOI is 10.1016/j.jinteco.2014.03.002. The Tokyo College URL for KeenParryRoaf2022 works and was used here.
