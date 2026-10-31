# The Paper Standard

Every working paper in this repo is brought to one standard, modeled on the World Bank Policy Research Working Paper (PRWP). The PRWP form suits the work: it is the format colleagues already read, it puts the finding first, and it converts easily to a journal submission. A paper "meets the standard" only when it passes the checklist at the end.

> The structure below follows common PRWP practice. The exact current PRWP submission rules (abstract word limit, cover format) were not confirmed from an official source: check the [PRWP page](https://www.worldbank.org/prwp) before formal submission. [VERIFY]

## Front matter

1. **Title.** Says what the paper finds or proposes, not just its topic. Under about 15 words. A subtitle may add the method or setting.
   - Weak: "Carbon Pricing in Open Economies"
   - Strong: "Open Economy Carbon Pricing: Taxing Carbon Where It Is Consumed"
2. **Author and affiliation.**
3. **Disclaimer.** Use the standard wording: *"The findings, interpretations, and conclusions expressed in this paper are entirely those of the author. They do not necessarily represent the views of the World Bank and its affiliated organizations, or those of the Executive Directors of the World Bank or the governments they represent."*
4. **Abstract.** One paragraph, about 150–200 words. It gives the problem, what the paper does, the main finding with a number if there is one, and the policy implication. No citations, no acronyms, no "this paper discusses". A reader who reads only the abstract should know the answer.
5. **Keywords** (4–6) and **JEL codes** (2–4).

## Body

### 1. Introduction (about 10% of the paper)

The introduction does five jobs, in roughly this order. Most readers stop here, so it must stand alone.

1. **Motivation.** The problem in the world, who has it and what it costs. Use a concrete fact with a number.
2. **Question.** One sentence.
3. **Answer.** The main finding or proposal, stated plainly, early.
4. **Contribution.** What this adds to the two or three closest pieces of work, named.
5. **Roadmap.** At most one sentence. Omit it in short papers.

### 2. Context or literature

Only what the reader needs to see the gap. Organize by idea, not by author. End with the gap this paper fills.

### 3. Framework, model or proposal

The core of the paper. Define every term on first use, then never vary it. State results as numbered propositions with their conditions. Put derivations in appendices and intuition in the text.

### 4. Evidence, application or illustration

Show it working: data, a calibration, a country case or a worked example with real numbers. Every number has a source.

### 5. Policy implications

What a finance ministry or development bank should do differently, concretely. Include costs, risks and the conditions under which the recommendation fails.

### 6. Conclusion

Short. Say what is now known that was not before, the main limitation and the next step. Do not restate the abstract.

### References

Chicago author-date, generated from a `.bib` file. Every entry verified to exist and to say what the text claims.

### Appendices

Proofs, derivations, data sources, robustness checks.

## Paragraph and sentence rules

- **First-sentence rule.** Every paragraph opens with its claim. The rest gives evidence, elaboration, examples or qualification.
- **Headings say something.** Prefer "Feebates keep average costs flat" over "Feebate properties".
- **One idea per paragraph.** Typically 3–6 sentences.
- **Tables and figures stand alone.** Each has a title stating its message, units, a source line and notes.
- **Acronyms.** Define on first use. Avoid any used fewer than five times. Keep a list only if there are more than about ten.

## Length

6,000–12,000 words for the body. If a paper is longer, split it or move material to appendices or a background paper. If a journal target has a limit, that limit wins.

## Files

- Master in Quarto (`.qmd`) with a `.bib` alongside. Start from `templates/working-paper-template.qmd`.
- Render to docx and PDF from the qmd. Never hand-edit the rendered files.

## Checklist (all must pass before the paper is "standard")

**The argument**
- [ ] The question and answer can each be stated in one sentence, and both appear in the abstract and the introduction.
- [ ] The contribution is stated against named prior work.
- [ ] Results are stated as propositions with conditions, not asserted.
- [ ] The strongest objection is stated and answered.

**Readability**
- [ ] Skim test: title, abstract, headings and first sentences alone give the whole argument.
- [ ] Self-contained: a reader with no context knows the topic and why it matters by the end of paragraph one.
- [ ] Every key term is defined once and used consistently.
- [ ] Every abstraction has a concrete example nearby.
- [ ] No item from `ai-tells.md` remains.

**Accuracy**
- [ ] Every citation key resolves, and every reference has been checked to exist and to support the claim.
- [ ] Every number has a unit, a year and a source.
- [ ] No `[VERIFY]`, `TODO` or placeholder text remains.
- [ ] Numbers and terms agree with the other papers in `H Writing Instructions/PAPERS.md`.

**Form**
- [ ] Front matter complete: title, author, disclaimer, abstract, keywords, JEL.
- [ ] Tables and figures stand alone.
- [ ] One spelling system throughout (see `H Writing Instructions/NORMS.md`).
- [ ] Renders cleanly from the qmd to docx and PDF.
- [ ] No confidential or World Bank internal material.
