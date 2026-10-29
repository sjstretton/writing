# Sections 4 and 5 architecture: Modelling (CPAT) and Analytics (tools)

Agreed with Stephen on 29 Oct 2026. Section 4 is the paper-length companion to the CPAT-AI repository (`cpmodelai/cpat_ai`, public). Section 5 is the paper-length companion to the Climate Fiscal AI Tools (`cpmodelai/climate-fiscal-ai-tools`, private): one paper per tool.

## Form: one medium-length paper each

Each item is **one paper**, not a brief plus a working paper. Medium form: **about 4,000–6,000 words of body** (4.1 may run to about 9,000, or split the engineering detail into an appendix). Working-paper front matter (title that states the finding or what the tool does, subtitle, author in personal capacity, disclaimer, abstract of about 150 words, keywords, JEL), numbered sections, claim-first paragraphs, at least one table or figure, Chicago author-date from a `.bib`. Master `<Name>.qmd` at the folder root, rendered to `<Name>.docx` with the same pandoc pipeline as sections 1–3, so the docx looks like the rest of the series. Shorter is fine; finished beats long.

## Section 4: Modelling — the Climate Policy Assessment Tool

The argument: **a climate-fiscal model a finance ministry can use must be small enough to state on a few pages, rebuilt so every step can be tested, validated against data and other models, and extended only where policy needs it.**

| No. | Folder | Paper (working title) | Main sources |
|---|---|---|---|
| 4.0 | `4.0.OverviewModelling.qmd` | Models a Finance Ministry Can Audit (overview) | Written last |
| 4.1 | `4.1.CPATMitigationMethods` | The CPAT Mitigation Module: Methods in Brief | `cpat_ai/docs/CPAT_full_documentation_qmd/03_Mitigation.qmd` (57k words: condense to the core equations: prices, demand, elasticities, fuel switching, power-sector dispatch and investment, emissions, revenue); `02_Summary.qmd`; `3.RelatedPiecesAndLinks/PowerInvestmentEquations` (penalty-based investment allocation; the engineering model can be an appendix or a later split-out paper) |
| 4.2 | `4.2.CPATAIImplementation` | CPAT-AI: Rebuilding a Policy Model as a Transparent, Testable Tool | `cpat_ai/README.md`, `excel_ai/` (BUGS.md, ISSUES.md, workbook notes), `coded/`, `docs/CPAT_ai_documentation_qmd/` and `docs/CPAT_coded_documentation_qmd/` (architecture, testing, versions), `CAVEATS.md`, the existing 4.2 README and background notes; the rule "bugs are never replicated; issues are replicated and tracked" |
| 4.3 | `4.3.CPATValidation` | Validating CPAT: Baselines, Back-Casts and Model Comparisons | `03_Mitigation.qmd` "Validation" (line ~2761), "Testing and validation summary", Appendix H (EPM comparison); `06_Air_pollution.qmd` validation; power and emissions validation in `CPAT_ai_documentation_qmd/05_Power.qmd`, `07_Emissions.qmd` |
| 4.4 | `4.4.ElasticityValidation` | Are CPAT's Price Elasticities Right? A Check Against the Evidence | `cpat_ai/other/tecp_and_validation/CPATPriceElasticities.xlsx`, `All_data_TCP.xlsx`; elasticity sections of `03_Mitigation.qmd`; paper 1.7 (Total Effective Carbon Price) for the CES demand system; published meta-analyses (verify) |
| 4.5 | `4.5.CBAMPolicyTool` (moved from 6.Additional 4.3) | The CBAM Policy Tool: Exposure of Exporters to the EU Carbon Border Adjustment | Folder contents (guides, workbooks); `climate-fiscal-ai-tools/CBAMPolicyTool`; public EU default values (Implementing Regulation 2025/2621). Do not publish the Egypt workbook numbers or World Bank dashboard figures (series 1 treated them as internal); use public EU data for examples |
| 4.6 | `4.6.PublicInvestment` | Public Investment in CPAT: Investment Needs and the Efficiency of Public Spending | CDPM extensions in `3.RelatedPiecesAndLinks`: Global Investment Needs (SISEPUEDE), Public Spending Efficiency and CBA (docx and the markdown folder, including the SIDS worked example); `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/InvestmentNeeds` |
| 4.7 | `4.7.ActivityModelling` | Activity Levels Across CPAT, SISEPUEDE, CBAM and FTT | CDPM extension `CDPM-ActivityLevels-SISEPUEDE-CPAT-CBAM-FTT.docx`; CPAT activity drivers in `03_Mitigation.qmd` |

## Section 5: Analytics — one paper per tool

The argument: **analysis changes policy only when the ministry that holds the budget can reproduce it; each tool takes data the ministry already holds, puts it on a common scale and returns a sequenced answer.**

| No. | Folder | Paper (working title) | Main sources |
|---|---|---|---|
| 5.0 | `5.0.OverviewAnalytics.qmd` | Diagnostics on Data Ministries Already Hold (overview) | Written last |
| 5.1 | `5.1.ExciseFiscalDiagnostic` | The Excise-Fiscal Diagnostic: Reading an Excise System Against Its Externalities | Current 24,800-word master (becomes v0.1 in `8.PreviousVersions`); the newer `climate-fiscal-ai-tools/ExciseDiagnostic/Excise_Diagnostic_WorkingPaper_v0_9.docx`, `main_working_paper/`, user guide, cross-country workbook; background political-economy metric and externality questions |
| 5.2 | `5.2.MacroFiscalEnergyScenarioTool` | The Macro-Fiscal-Energy Scenario Tool | `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto` (README, VersionNotes, CAVEATS, briefings, InvestmentNeeds, MacroFiscalModels: GIMF-lite, DIGNAD/DIGNAR-lite, LIC-DSF-lite; PriceFeasibility) |
| 5.3 | `5.3.FiscalIndicatorsDashboard` | A Global Fiscal Indicators Dashboard for Climate-Fiscal Analysis | `climate-fiscal-ai-tools/TaxMacroFiscalDashboard` (README, VersionNotes, user guide deck, build pipeline) |

The older Additional analytics items (`6.Additional/5.Analytics/5.2–5.4`) keep their old numbers inside Additional; they are not part of this series.

## Rules specific to these sections

- **Confidentiality.** CPAT documentation is public. The Climate Fiscal AI Tools repository is private and some country results may be World Bank work. Write method and design from the repos; use only public data or clearly labelled stylized numbers for examples. Do not reproduce country results from the private repository, World Bank program or Public Finance Review material, the Egypt CBAM numbers, or files whose names say internal, unless Stephen clears them. List anything you held back in the folder README.
- **Name the tools consistently:** CPAT (the Climate Policy Assessment Tool); legacy CPAT (the Excel model); Excel-AI (the rebuilt Excel prototype); Coded CPAT (the Python model); CPAT-AI (the project and repository).
- **Cross-reference** sibling papers by number and title; cite section 1's Total Effective Carbon Price paper as @CFPB17 where the demand system matters.
