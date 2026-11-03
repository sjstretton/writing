# Global Incentives Model: documentation copies

The Global Incentives Model is the modelling backbone of the thesis (see `../ThesisPlan/ThesisPlan-SovereignIncentives.qmd`, section 1a). Its masters, code and data live in the AI tools repository, not here:

- Repository: `cpmodelai/climate-fiscal-ai-tools`, folder `GlobalIncentivesModel/` (on `main` since 1 November 2026).
- The Word files in this folder are **read-only copies**, rendered on 3 November 2026 from those masters in the house working-paper format (`../render_docx.py` logic, with the extension's `reference.docx`). Do not edit them here; edit the `.qmd` masters in the other repository and re-render.

| File | What it is | Master in `climate-fiscal-ai-tools` |
|---|---|---|
| `GlobalIncentivesModel_Plan.docx` | "Model Technology Where It Decides Emissions": the modelling plan. A country-by-sector model for 186 countries, 2024–2050, with a sector core and five modules: (a) policy, (b) investment taxonomy (who decides, who pays, through what contract), (c) cost of finance, (d) international incentives with a country timing layer, (e) national objectives and macro; plus a trade module (BACI bilateral flows with Armington substitution; input-output tier for consumption-based accounting). | `GlobalIncentivesModel/ModellingPlan/GlobalIncentivesModel_Plan.qmd` |
| `UseItOrLoseIt.docx` | "Use It or Lose It: Decaying Incentives That Pay Governments to Act Now": seven propositions on timing (a static reward must be (1 + g/r)K − H; decay at the rate costs fall cuts it by r/(r+g); a ratcheting baseline is a decaying incentive; decay is credible only with a common pool), with code that reproduces every number. | `GlobalIncentivesModel/UseItOrLoseIt/UseItOrLoseIt.qmd` (code in `code/uioli_model.py`) |
| `DataNeeds.docx` | "We Can Build It": 95 data needs by module, with source, status and fallback; 45 of 56 essential needs in hand. | `GlobalIncentivesModel/DataNeeds/DataNeeds.qmd` (catalogue built by `build_data_catalogue.py`) |
| `ComponentsNovember2026.docx` | "Components for the Month Ahead": the 17 components (have, extend, new) and the November build order, carbon-price measurement first. | `GlobalIncentivesModel/Roadmap/ComponentsNovember2026.qmd` |

## How it maps onto the thesis

| Thesis chapter | Model module |
|---|---|
| 2. Distance to the sovereign | (c) Cost of finance (equations 7–8) |
| 3–4. Contracts, relationships, collateral | (b) Investment taxonomy and (c) cost of finance |
| 5. Policy crediting and use it or lose it | (d) International incentives, country timing layer (equation 10) |
| 6. Coalition | Trade module (equation 9) |
| 7. Climate reserve | (d) Delivery form and donor cost |
| 8. Growth, debt and savings | (e) National objectives and macro (equations 11–13) |

## To align with the house format

The masters still carry a World Bank affiliation and the World Bank disclaimer. Under the house norm (`H Writing Instructions/NORMS.md`, section 13), the author line should read "Stephen J. Stretton, writing in a personal capacity" with the house disclaimer, and the YAML should add `series` and a plain `version` number. That change belongs in the other repository; it has not been made.

## Modelling plan source (added 3 November 2026)

`GlobalIncentivesModel_Plan.qmd` and `references.bib` are copies of the master in `cpmodelai/climate-fiscal-ai-tools`, `GlobalIncentivesModel/ModellingPlan/` (commit dd4ca59), which now opens with the central research question: zero-cost abatement at current interest rates, at World Bank rates, and with co-benefits. Edit the master there and re-copy. `GlobalIncentivesModel_Plan.docx` was re-rendered from it on 3 November 2026 and includes the question.
