# 6.6 Global Incentives Model

Paper 6.6, **Model Technology Where It Decides Emissions**: the modelling plan for the Global Incentives Model, the modelling backbone of the thesis (see `../ThesisPlan/ThesisPlan-SovereignIncentives.qmd`, section 1a). Its central research question: how much emissions can fall at zero cost at current interest rates, at the IBRD lending rate, and when domestic co-benefits are counted. New research awaiting review; it will join `D Modelling/6.ModularUpgrades/` after review.

- **Master:** `GlobalIncentivesModel.qmd` (v0.2, house format), with `GlobalIncentivesModel.bib`; `GlobalIncentivesModel.docx` is rendered from it with `../render_docx.py`. Version 0.1 is in `8.PreviousVersions/`.
- **Model code and data:** `cpmodelai/climate-fiscal-ai-tools`, folder `GlobalIncentivesModel/`. Its `ModellingPlan/GlobalIncentivesModel_Plan.qmd` carries the same text in the old format; make content changes here and copy them across.
- **Related documents** (`3.RelatedPiecesAndLinks/`): read-only Word copies of the model's other documents, whose masters are in `climate-fiscal-ai-tools`.

| File | What it is | Master in `climate-fiscal-ai-tools` |
|---|---|---|
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

The plan (this folder's master) is now in the house format. The other masters still carry a World Bank affiliation and the World Bank disclaimer. Under the house norm (`H Writing Instructions/NORMS.md`, section 13), the author line should read "Stephen J. Stretton, writing in a personal capacity" with the house disclaimer, and the YAML should add `series` and a plain `version` number. That change belongs in the other repository; it has not been made.
