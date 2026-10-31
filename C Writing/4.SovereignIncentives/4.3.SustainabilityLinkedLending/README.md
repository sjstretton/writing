# 4.3 Sustainability-Linked Lending

**Codify Sustainability-Linked Sovereign Lending, Then Give It Scale.** Climate Fiscal Policy Brief No. 4.3 and working paper `StrettonWP43`.

## Status

- Version 0.1 (October 2026): first public draft of the brief and the working paper, written for the series 3 restructuring, now section 4 (`../4.0.Overview/SeriesArchitecture.md`). Awaiting Stephen's peer review.
- Guarantee leverage uses the series 4 cases shared with 4.1 and 4.2. Since 29 Oct 2026 the base case is the MDB sovereign loss record (GEMs 2025: 0.77% annual calls, 4.9% loss, 0.5% buffer; ratio about 80; funder cost of the coal reform about $10m); stress case 3% calls × 37% loss (9.3% buffer, ratio 2.7, cost $286m); middle 3% × 10% (ratio 10). Open items (Chile and Thailand terms against prospectuses; country calibration of guarantee leverage) are listed in appendix C of the working paper and in the `.bib` notes.

## Files

| File | What |
|---|---|
| `SustainabilityLinkedLending.qmd`, `.bib`, `.docx` | Working paper master (version 0.1) |
| `1.Presentation/Brief-SustainabilityLinkedLending.qmd`, `.bib`, `.docx` | Brief No. 4.3 |
| `1.Presentation/figures/make_figures.py` | Regenerates the brief's figure (reuses `2.Source`) |
| `2.Source/model.py` | Calibration: Uruguay loan arithmetic, size comparison, guarantee leverage. `python3 model.py` prints every number used |
| `2.Source/make_wp_figures.py` | Working paper figures, saved to `2.Source/figures/` |
| `3.RelatedPiecesAndLinks/SLIDIs/` | Source paper: SLIDIs (Estevão, Stretton and Zimmermann, 2024) and its archive drafts |
| `9.Archive/` | **Confidential World Bank internal material. Not used for, and must not be cited in, any public text.** |

## Lineage and co-authors

- Public facts only: World Bank press release (Nov 2023) and Uruguay's Ministry of Economy and Finance briefing note on the 2023 loan; Uruguay's 2023 SEC prospectus supplement; Chile, Thailand and market sources in the `.bib`.
- Design source: *Mobilizing Private Finance for the Climate Agenda: Introducing SLIDIs*, with **Marcello Estevão** and **Nils Zimmermann** (personal capacity, 2024); Estevão's earlier "bonds with KPIs" note. Estevão and Zimmermann's "Trusted Intermediaries" draft (marked draft for discussion) and its corrective-surcharge proposal were removed on 30 Oct 2026 under Stephen's ruling that draft-for-discussion documents are not cited. Both co-authors are credited in the first-page note of the working paper and the brief.
- Book material: *Time and Chance* (Stretton, manuscript), chapter 5 on commitment devices and the additionality requirement.
- Deliberately not used: the confidential World Bank discussion paper in `9.Archive/` and the internal MDB envelope note (`8.AdditionalPolicyPapers/8.3.SovereignIncentives/8.3.1.MDBClimateEnvelope`).
