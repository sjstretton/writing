# 4.3 Sustainability-Linked Lending

**Codify Sustainability-Linked Sovereign Lending, Then Give It Scale.** Climate Fiscal Policy Brief No. 4.3 and working paper `StrettonWP43`.

## Status

- Working paper v0.2 and brief v1.0 (31 Oct 2026): peer-reviewed (`5.Notes/PeerReview-2026-10-31.md`), references checked (`5.Notes/BibCheck-2026-10-31.md`), executive summary added, Proposition 2 restated (a market bond buys commitment, not money), market facts updated to 2026 (Slovenia 2025, Thailand 2024 and 2026, Kenya reported), ten-slide deck rebuilt. Earlier versions are in `8.PreviousVersions/`.
- Guarantee leverage uses the series 4 cases shared with 4.1 and 4.2: base, the MDB sovereign loss record (GEMs 2025: 0.77% calls, 4.9% loss, 0.5% buffer; ratio about 80; funder cost of the coal reform about \$10m); middle 3% × 10% (ratio 10); stress 3% × 37% (9.3% buffer, ratio 2.7, cost \$286m). Holding the stress buffer at a 2% carry while pricing on the record gives about 13. A 200 bp sensitivity gives 53 and 1.8.
- Open: re-read Chile's Ministry of Finance report when its site is reachable; confirm Kenya's terms from a World Bank document; calibrate leverage for named countries.

## Files

| File | What |
|---|---|
| `SustainabilityLinkedLending.qmd`, `.bib`, `.docx` | Working paper master (version 0.2) |
| `1.Presentation/Brief-SustainabilityLinkedLending.qmd`, `.bib`, `.docx` | Brief No. 4.3 (version 1.0) |
| `1.Presentation/figures/make_figures.py` | Regenerates the brief's figure (reuses `2.Source`) |
| `2.Source/model.py` | Calibration: Uruguay loan arithmetic, size comparison, guarantee leverage. `python3 model.py` prints every number used |
| `2.Source/make_wp_figures.py` | Working paper figures, saved to `2.Source/figures/` |
| `1.Presentation/slides.json`, `Slides-SustainabilityLinkedLending.pptx` | Ten-slide deck (built with `make_deck.py`) |
| `5.Notes/` | Peer review and reference check, 31 Oct 2026 |
| `8.PreviousVersions/` | Working paper, brief and deck v0.1 |
| `3.RelatedPiecesAndLinks/SLIDIs/` | Source paper: SLIDIs (Estevão, Stretton and Zimmermann, 2024) and its archive drafts |
| `9.Archive/` | **Confidential World Bank internal material. Not used for, and must not be cited in, any public text.** |

## Lineage and co-authors

- Public facts only: World Bank press release (Nov 2023) and Uruguay's Ministry of Economy and Finance briefing note on the 2023 loan; Uruguay's 2023 SEC prospectus supplement; Chile, Thailand and market sources in the `.bib`.
- Design source: *Mobilizing Private Finance for the Climate Agenda: Introducing SLIDIs*, with **Marcello Estevão** and **Nils Zimmermann** (personal capacity, 2024); Estevão's earlier "bonds with KPIs" note (unpublished; acknowledged, not cited). Estevão and Zimmermann's "Trusted Intermediaries" draft (marked draft for discussion) and its corrective-surcharge proposal were removed on 30 Oct 2026 under Stephen's ruling that draft-for-discussion documents are not cited. Both co-authors are credited in the first-page note of the working paper and the brief.
- Book material: *Time and Chance* (Stretton, manuscript), chapter 5 on commitment devices and the additionality requirement.
- Deliberately not used: the confidential World Bank discussion paper in `9.Archive/` and the internal MDB envelope note (`8.AdditionalPolicyPapers/8.3.SovereignIncentives/8.3.1.MDBClimateEnvelope`).
