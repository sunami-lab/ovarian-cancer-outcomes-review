# PRESS self-assessment of the drafted strategy

PRESS (Peer Review of Electronic Search Strategies, McGowan et al., *J Clin Epidemiol*
2016;75:40–46) is the instrument a journal or an information specialist will apply to a
submitted protocol. This is a **self-assessment**, which is not what PRESS is for — the
whole point is review by someone who did not write the strategy. It is recorded here so
that whoever does review it starts from a known position rather than from scratch, and so
the failures are on the record rather than discovered at peer review.

Verdict by domain: **3 pass, 2 pass with reservations, 1 fail.**

---

## 1. Translation of the research question — pass with reservations

The question ("in older adults with ovarian cancer receiving any anticancer treatment, what
patient-centred outcomes have been measured, and what do they show?") is translated into
population, intervention, age and seven outcome concepts, each block traceable to a named
published strategy in `blocks_pubmed.yml`.

Two deliberate departures, both evidence-based rather than accidental:

- **The intervention concept is not in the recommended search.** `draft/recall.md` shows it
  costs a known item and drops a whole class of paper (PRO secondary analyses that never
  restate the intervention). Justified, but a reviewer will ask, so it is documented in
  `draft/README.md` decision 1b.
- **The age concept is not in the search either.** It costs 8 of 23 known items. Age is
  applied at screening instead.

*Reservation:* a strategy that searches only population AND outcome is unusual, and the
justification rests on a 23-item recall test rather than on a larger sample.

## 2. Boolean and proximity operators — pass

Sets are combined with explicit `AND`/`OR`; every OR chain in the drafted files is
parenthesised. `scripts/lint_strategies.py` checks parenthesis and quote balance in all
three untested translations and currently reports zero problems.

One platform difference is handled explicitly rather than assumed: an unparenthesised OR
chain is safe in PubMed (measured — `docs/validation.md` shows identical translation and
identical hit count with and without brackets) but is **not** safe in Ovid or Web of
Science, and the Web of Science file says so.

Proximity is used only where the source strategy used it (`NEAR/5` in Web of Science,
`adj5` in Ovid, mirroring Billson 2013 and Neo 2017).

## 3. Subject headings — pass

Every concept pairs controlled vocabulary with free text. MeSH headings were checked to
exist by execution: PubMed reports unmatched terms in its `errorlist`/`warninglist`, and
`draft/counts.md` shows **no unmatched terms in any block**. An invented or retired MeSH
heading would have surfaced there.

Explosion is used where the tree warrants it and avoided where it would over-retrieve.
`"Carcinoma, Ovarian Epithelial"[Mesh]` is included alongside `"Ovarian Neoplasms"[Mesh]`
because the former is not a descendant of the latter.

*Not yet done:* the Emtree headings in `draft/embase_ovid.txt` have **not** been verified
against current Emtree, because that needs Embase access. Emtree changes more often than
MeSH. This is listed as a limitation, not a pass.

## 4. Text word searching — pass with reservations

Free-text terms cover synonyms, British and American spellings (`tumour`/`tumor`,
`dyspnea`/`dyspnoea`, `diarrhea`/`diarrhoea`), acronyms (ADL, IADL, HRQOL, PROM) and
**measurement instrument names** (QLQ-C30, FACT-G, FACT-O, FACIT, SF-36, EQ-5D, PROMIS,
MDASI, MSAS, PRO-CTCAE, CAHPS, AOPSS, CPES). The instrument-name line is taken from
Mishra 2012 and is the highest-value borrowing in the whole exercise — it retrieves trials
whose abstracts never use the concept word.

Truncation is applied at sensible stems (`ovar*`, `chemotherap*`, `cachexi*`).

*Reservations, in order of seriousness:*

1. **The symptom block (O6) is largely constructed**, not transcribed — no review in the
   collection enumerates the 12 recommended symptoms. It is the least evidence-based block
   here and needs a specialist's eye most.
2. Some single words are broad in isolation: `pain[tiab]`, `anxiety[tiab]`, `anorexia[tiab]`
   contribute most of O6's 2.15 million records. They are defensible inside an
   AND-ed strategy but would be indefensible alone.
3. No adjacency is used in the PubMed outcome blocks, because PubMed has no `adj`
   operator. The Ovid translations use `adj` where the source strategies did.

## 5. Spelling, syntax and line numbers — pass

- Spelling variants: covered (see domain 4).
- Syntax: checked by execution for PubMed, and statically for the three translations.
- Line numbers: `scripts/lint_strategies.py` verifies that every `or/N-M` range and every
  `N and M` set reference in the Ovid and Embase files points at a line that exists. This
  is precisely the error class found in two of the *published* strategies transcribed into
  this repository (Cramer 2017's PubMed appendix combines the wrong set numbers), so it is
  worth checking rather than assuming.
- Curly quotation marks: checked for and absent from the drafted files. They are present in
  Soong 2025's and Balitsky 2024's published strategies, and are flagged there.

## 6. Limits and filters — FAIL

This is the domain the draft genuinely fails, and it fails on omission rather than error.

- **No study-design filter is applied** in the recommended search. `D_design` exists in
  `blocks_pubmed.yml` but is not used, because the review is likely to be a scoping review
  or evidence map (see `docs/existing_reviews.md`), where design filters are inappropriate.
  That is a defensible choice but it must be stated in the protocol, not left implicit.
- **No language limit.** Deliberate — Coleridge 2021 sought papers in all languages and
  carried out translations, and Lawrie 2019 applied no language restriction to any of its
  searches — but it has a cost in screening effort that the team must accept in advance.
- **No date limit.** The population block alone reaches back to the 1950s. Consider whether
  pre-platinum-era ovarian cancer treatment is within scope.
- **No animal-study exclusion in the PubMed version.** The Ovid and Embase translations
  include `exp animals/ not humans.sh.`; the PubMed draft does not. This should be added.
- **No grey literature, trial registry or conference-abstract component at all.** Almost
  every review in the collection searched ClinicalTrials.gov and WHO ICTRP; Mishra 2012 also
  searched PEDRO, LILACS, SIGLE, SportDiscus and OTSeeker. The draft searches none of them.
  For a review of older adults — chronically under-represented in published trials — this is
  the most consequential omission on the page.

## What to fix before this goes to a real peer reviewer

In priority order:

1. Add a grey-literature and trial-registry component (domain 6). Start with
   ClinicalTrials.gov and WHO ICTRP.
2. Have the symptom block rebuilt or ratified by an information specialist (domain 4).
3. Verify the Emtree headings against live Embase (domain 3).
4. Add the animal-exclusion line to the PubMed version and decide on date and language
   limits explicitly (domain 6).
5. Then send it for actual PRESS review by someone who did not write it. This document does
   not substitute for that.
