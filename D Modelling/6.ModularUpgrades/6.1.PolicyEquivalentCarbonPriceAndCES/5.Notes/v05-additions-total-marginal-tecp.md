# Proposed additions for v0.5 of paper 6.1

*Prepared 11 November 2026. These sections are designed to be inserted into the existing paper. Stephen to review and decide placement.*

## Addition 1: New section — "Total and marginal TECP" (insert after §5, before §6 Calibration)

Suggested section heading: **Total, marginal and locked-in TECP**

### Proposed text

**The TECP can be decomposed into a locked-in component and a marginal component.** Define the *total TECP* as the TECP of Definition 1, measured against a static-shares baseline — the fuel mix held at a reference year, scaled to current output. Define the *marginal TECP* as the emissions increase that would occur if all current policies were removed, expressed in the same units. The *locked-in TECP* is the difference: the portion of abatement that would persist even without policy, because technology has crossed the tipping point or capital is physically committed.

**Corollary 3 (total-marginal decomposition).** *Let $R_{\text{total}}$ be the emission cut of the current policy mix against a static-shares baseline and $R_{\text{marginal}}$ the cut that depends on ongoing policy (i.e., that would be reversed if policy were removed, holding technology costs constant). Then*

$$
\tau^*_{\text{total}} = R_{\text{total}} / \Lambda, \qquad
\tau^*_{\text{marginal}} = R_{\text{marginal}} / \Lambda, \qquad
\tau^*_{\text{locked-in}} = \tau^*_{\text{total}} - \tau^*_{\text{marginal}}.
$$

*The locked-in share $\tau^*_{\text{locked-in}} / \tau^*_{\text{total}}$ is a measure of transition maturity.*

**The decomposition classifies instruments by reversibility.** Price instruments on flow decisions — fuel excises, carbon prices affecting dispatch, biofuel mandates — are high-marginal, low-locked-in: removing them causes immediate behavioural reversion. Standards on stock decisions — building codes, appliance MEPS, the LED lighting phase-out, vehicle emission standards for the existing fleet — are high-locked-in, low-marginal: their contribution accumulates irreversibly as long-lived capital turns over.

**The locked-in share varies by sector.** Buildings are approximately 70 percent locked-in (efficient buildings and appliances last decades). Power is approximately 55 percent locked-in (existing renewable plants run at zero marginal cost regardless of policy). Transport is approximately 35 percent locked-in (the efficient fleet depreciates; fuel taxes affect behaviour immediately; EVs remain a small share outside China).

**The gap between total and marginal TECP is a diagnostic of transition success.** A country with a high total TECP and a low marginal TECP has successfully triggered self-sustaining transitions. A country with equal total and marginal TECP is still fully dependent on ongoing policy. The trajectory from high-marginal to high-locked-in is the mark of a successful energy transition.


## Addition 2: Strengthen §5 (non-price instruments) — static-shares baseline for mandates

Insert after the "mandates, procurement rules" paragraph:

**For quantity mandates — RE targets, coal phase-out dates, EV sales targets — the back-out route simplifies when the baseline uses static shares.** Define the baseline as the fuel mix held at a reference year. The mandated fuel mix implies a known emission level. The emissions reduction is $\Delta E = E_{\text{static}} - E_{\text{mandate}}$, and the first-order TECP contribution is $\Delta E / \Lambda$. This avoids estimating the mandate's shadow price entirely and is robust to uncertainty about compliance costs. The static-shares baseline isolates the policy effect from autonomous trends and correctly attributes the full transition — including self-reinforcing dynamics triggered by the mandate — to the policy.


## Addition 3: Strengthen Appendix C.5 — technical efficiency with capital costs

Expand C.5 with:

**When capital costs differ across technologies, the CES should operate over total cost of service, not fuel cost alone.** Define the total cost per GJ of service from fuel $f$ as $\hat{p}^{\text{total}}_{fs} = p_{fs}/\varphi_{fs} + k_{fs}$, where $k_{fs}$ is the annualised capital cost per GJ of service. The semi-elasticities then divide by total cost rather than fuel cost, which is smaller for capital-intensive clean technologies (electricity in transport, heat pumps in buildings). The substitution elasticity $\sigma_s$ should be recalibrated to the total-cost specification; it will be higher than the fuel-only $\sigma_s$ because the capital cost barrier has been moved out of $\sigma$ and into the price. Where capital costs include a behavioural discount rate different from the social rate (§A, deviation B), the wedge between the two rates is itself a market failure that a technology standard corrects.
