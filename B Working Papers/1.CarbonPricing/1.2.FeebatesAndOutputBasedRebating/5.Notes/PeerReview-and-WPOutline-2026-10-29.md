# Paper 1.2: peer review of the brief, and outline of the working paper

Review of *Climate Fiscal Policy Brief No. 1.2* (`1.Presentation/Brief-FeebatesAndOutputBasedRebating.qmd`, Oct 2026), written as a referee report. The outline that follows is the plan for the academic working paper (master `FeebatesAndOutputBasedRebating.qmd`, to become v0.3; the current v0.2 moves to `8.PreviousVersions/`).

## Part 1. Referee report

**Summary.** The brief argues that a feebate on emissions intensity, a fee above a sector benchmark and a rebate below it, gives the full marginal carbon incentive without the average-cost burden of a tax. It applies this to coal-heavy power and to trade-exposed industry. It is well evidenced and honest about the abatement penalty: the IMF puts feebate packages at 50–70 percent of a tax's cuts. The working paper must fix one substantive gap and add the dynamics.

**Major comments**

1. **"Keeps power cheap" depends on how the price is set.** Under cost-of-service regulation or a single buyer, common in coal-heavy developing countries, the consumer price follows average generation cost, and a revenue-neutral feebate leaves it nearly unchanged. In a wholesale market priced at marginal cost, the price is set by the marginal plant. If that plant is coal, dirtier than the benchmark, the feebate raises the wholesale price by $t(e_{\text{coal}} - \bar e)$, and infra-marginal clean plants keep the rebate as rent. Consumers then pay more even though net feebate payments sum to zero. Model both market designs and state when the brief's claim holds. This is the power-sector version of the sign condition in paper 1.1 (heterogeneous firms, the price-setting producer).
2. **Dispatch versus investment.** The brief treats the switch from coal to gas and renewables as one effect. Separate short-run dispatch (merit order: a feebate and a tax at equal rates give the same dispatch order) from long-run investment and retirement, where capital turnover, financing costs and contract structures dominate. The investment response should use a logit or CES adoption model, as in the toy model in `6.Additional/5.Analytics/5.4…`, and cite the evidence on carbon prices and coal retirement.
3. **Benchmark dynamics.** An updating benchmark (the sector average) lowers the marginal incentive slightly: a firm's cut lowers next year's benchmark by its output share. That is negligible for small firms and not for dominant state utilities with 50+ percent shares. Quantify it. Also discuss the ratchet and gaming (holding intensity up before the base year), and fuel-specific versus single benchmarks: single is right, with time-limited, closure-linked transfers for stranded coal.
4. **A calibrated example.** Replace the stylized grid with two or three country cases using published generation mixes and IPCC emission factors (for example India, Indonesia, South Africa). Show the system price effect under both market designs, plus fiscal flows and dispatch.
5. **Industry and the border.** Link explicitly to paper 1.1 (two tracks; Propositions 1–3 there) and paper 1.3: under CBAM as drafted, a revenue-neutral feebate earns no deduction because no net carbon price is paid. Say what an exporter loses and how recognition through carbon-price equivalents (1.7) fixes it.

**Minor comments**

6. Evidence section: give effect sizes with confidence intervals where available (Swedish NOx: Sterner and Höglund; Sterner and Isaksson. French bonus-malus: D'Haultfœuille et al.; Durrmeyer. Canada OBPS: any ex-post evaluation).
7. The political feasibility metric in the v0.2 paper (Part 3) is worth keeping in compressed form, as an appendix, if its calculation is documented; otherwise drop it.
8. Household electricity prices: present the distributional point carefully. Under a single buyer a feebate protects households; under a market it may not.
9. Make clear that output-based rebating of an existing tax and a stand-alone feebate are the same instrument, and that full abatement-cost offsetting ("standard OBR" in the industrial background paper) is a different, revenue-negative variant.
10. Resolve VERIFY items (Finance Canada 2025, IEA NZE, CBAM Art. 9).

**Recommendation:** major revision: the market-design distinction, investment dynamics, benchmark dynamics and calibrated country cases.

## Part 2. Outline of the working paper (about 8,000–10,000 words plus appendices)

**Front matter.** Title as the brief: "Feebates: The Full Carbon Price at the Margin, Without the Carbon Bill", subtitle "Decarbonizing Coal-Heavy Power and Trade-Exposed Industry". Personal capacity. Abstract of about 150 words. JEL (H23, L94, Q41, Q48, Q54, Q58).

1. **Introduction** (900 words). Two signals of a carbon price; the political cost of the average-cost signal in coal-heavy power and trade-exposed industry; the feebate; contributions: market-design result, investment dynamics, benchmark dynamics, calibrated cases; place in the series (1.1 production track).
2. **Related literature** (900 words; Appendix A for the full review).
3. **A power-sector model** (1,600 words). Plants of types $j$ (coal, gas, renewables) with marginal cost $c_j$ and intensity $e_j$; merit-order dispatch; two market designs: (a) a single buyer or average-cost regulation, (b) a uniform-price wholesale market. **Proposition 1:** equal dispatch under a tax and a feebate at equal rates. **Proposition 2:** under (a), the consumer price rises only by the resource cost of re-dispatch. **Proposition 3:** under (b), the wholesale price rises by $t(e_m - \bar e)$ plus re-dispatch cost, where $m$ is the marginal plant; the feebate transfers rent to infra-marginal clean plants. Conditions and proofs in Appendix B.
4. **Investment, retirement and capital turnover** (1,200 words). A logit investment share; how the feebate changes the clean share of new capacity; coal retirement; stranded-asset transfers.
5. **Benchmark design and dynamics** (1,000 words). Updating; dominant-firm effect (the marginal incentive is $t(1 - s_i)$ for a firm with output share $s_i$); a single versus fuel-specific benchmark; gaming; verification.
6. **Calibrated country cases** (1,300 words). Two or three grids, published mixes, IPCC factors and stylized costs; Table 1 and Figures 1–2 (price effect under the two designs; fiscal flows by plant type).
7. **Trade-exposed industry** (900 words). The intensity metric per tonne of product; competitiveness; the border (1.3); the two tracks (1.1).
8. **Evidence from feebates in use** (900 words). Swedish NOx, French bonus-malus, Canada OBPS, China's intensity-based ETS allocation, India PAT where relevant.
9. **Political economy and fiscal effects** (600 words). Zero treasury cost; the abatement penalty (the IMF's 50–70 percent); pairing with a consumption charge.
10. **Conclusion** (300 words).

**Appendices.** A: literature review (from `5.Notes/LiteratureAppendix-draft.md`). B: proofs. C: calibration data and code. D (optional): the political feasibility metric from v0.2.
