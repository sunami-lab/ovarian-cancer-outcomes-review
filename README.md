# Ovarian cancer treatment and patient-centred outcomes: systematic review search strategies

Search strategies and evidence extraction from previously published systematic reviews of
ovarian cancer treatment and patient-centred outcomes in oncology.

This repository is a **methods scoping exercise**, not a systematic review. Its purpose is
to collect, verbatim, how 24 earlier high-impact systematic reviews built their database
searches for (a) *treatment* of ovarian cancer and (b) each *patient-centred outcome* of
interest, so those search blocks can be reused or adapted when designing a new review of
ovarian cancer treatment and patient-centred outcomes in older adults.

## What is here

| Path | Contents |
|---|---|
| `output/search_strategies.xlsx` | **The deliverable.** One sheet per category, three reviews per sheet. |
| `data/*.yml` | Source of truth, one file per category. Long Boolean strings live in YAML block scalars so they stay diffable. |
| `docs/tables/*.md` | The same tables as Markdown, readable on GitHub without downloading the workbook. |
| `docs/methods.md` | How reviews were found and selected, what was done when nothing matched, and what the extraction found. |
| `docs/impact_factors.md` | Every impact factor quoted, with its source and confidence, plus the reviews the ≥5 rule excluded. |
| `scripts/build.py` | Regenerates the workbook and the Markdown from `data/`. |

Rebuild after editing any YAML file:

```bash
pip install pyyaml openpyxl
python3 scripts/build.py
```

## The eight sheets

| # | Sheet | Reviews | Population searched |
|---|---|---|---|
| 1 | Ovarian cancer treatment (general, not a specific treatment) | Coleridge 2021, Faluyi 2010, Elattar 2011 | Ovarian cancer, any age |
| 2 | Functional status | Molenaar 2023, McDonald 2023, Scheepers 2020 | Any cancer; Scheepers is older adults |
| 3 | Cognition | Treanor 2016, Lawrie 2019, Jim 2012 | Any cancer, any age |
| 4 | Depression | Soong 2025, Vita 2023, Kulchycki 2024 | Any cancer; Soong is older adults |
| 5 | Nutritional status | Billson 2013, Takaoka 2024, Lovell 2025 | Billson is **ovarian cancer** |
| 6 | Health-related quality of life | Mishra 2012, Osanto 2024, Cramer 2017 | Any cancer; Cramer is women only |
| 7 | Patients' symptoms (12 recommended) | Reeve 2014, Balitsky 2024, Ream 2020 | Any cancer, any age |
| 8 | Patients' satisfaction | Jacobsen 2018, Gomes 2013, Alessy 2022 | Any cancer, any age |

Category 1 asks how earlier reviews search for **treatment** in ovarian cancer, so ovarian
cancer was held fixed and the age restriction relaxed. Categories 2–8 ask how earlier
reviews search for each **outcome**, so cancer type and age were left open by design, with
ovarian/gynaecological and older-adult reviews preferred wherever one existed above the
impact-factor threshold.

## Columns

`title` · `1st author/year` · `journal` · `impact factor` · `purpose of the study` ·
`PICO` · `search terms/strings for PubMed` · `…for Embase` · `…for Web of Science` · `url`

## Three things to know before using the search strings

1. **"PubMed" usually means Ovid MEDLINE.** Most of these reviews searched MEDLINE through
   Ovid, not PubMed, and the two syntaxes are not interchangeable (`exp Term/`, `.mp.`,
   `.fs.`, `adj5` have no PubMed equivalent). Every cell states which interface and which
   date range the strategy was actually run on. Nothing has been silently translated.
   Six reviews do give native PubMed syntax: Treanor 2016, Molenaar 2023, Scheepers 2020,
   Soong 2025, Jacobsen 2018 and Alessy 2022.
2. **A blank is reported as a blank.** Where a review did not search a database, or searched
   it but did not publish the string, the cell says so. No search string in this repository
   has been reconstructed, inferred, or written by hand — every one was read from the
   published appendix, supplement or Methods section named in that record's
   `strategy_source` field.
3. **Errors in the published strategies are flagged, not silently repaired.** Several
   appendices contain transposed instrument names (`qlc-c30` for QLQ-C30, `sta1` for STAI),
   typos (`choriocrcinoma*`, `yora`, `.mp3`), truncation inside Emtree explosions, or wrong
   line-number combinations — Cramer 2017's published PubMed appendix combines three
   single lines where it should combine three set unions. Each is noted in the cell.

## Selection rule

Reviews had to be in a journal with a **Journal Impact Factor ≥ 5**, and had to publish a
search strategy that could be read in full. See `docs/impact_factors.md` for the values used
and their confidence, and `docs/methods.md` for the retrieval routes and for the reviews
that were dropped because their strategy was paywalled.

One consequence of the ≥5 rule is worth stating plainly: the ovarian-specific and
geriatric-oncology literature sits almost entirely in the 2.4–4.8 impact band, so the
threshold is in practice a rule that trades ovarian cancer specificity for journal
prestige. Ten reviews excluded on that basis — several of them ovarian-specific — are
listed in `docs/impact_factors.md` in case the threshold is ever relaxed.

## What the 24 strategies show

- **Most reviews do not search on the outcome.** Population AND intervention (AND design)
  is the dominant structure; the outcome is applied at screening. Molenaar 2023 has
  functional capacity as its lead outcome and no functional term in the search; Cramer 2017
  has HRQOL first in its title and no quality-of-life term; Ream 2020 asks "which symptoms
  respond" and searches for no symptom.
- **Where the outcome is searched, sensitivity varies by an order of magnitude.** The three
  depression blocks in sheet 4 run from four words (Soong) to eight controlled-vocabulary
  terms plus a 20-term text-word line (Kulchycki). Impact factor does not predict search
  quality: the thinnest strategy in the collection is in the highest-impact journal in it.
- **Searching on instrument names is the most transferable idea here.** Mishra 2012
  retrieves HRQOL trials via QLQ-C30, FACIT, SF-36, HADS, POMS and MSAS; Alessy 2022
  retrieves patient-experience studies via CPES, CAHPS and AOPSS. Both catch papers whose
  abstracts never use the concept word.
- **Web of Science is rarely searched and more rarely published.** Four of 24 searched it;
  two published the string — Takaoka 2024 (sheet 5, a clean `TS=` topic search) and
  Osanto 2024 (sheet 6, a full `TI=`/`AB=`/`TS=` strategy with `NEAR/5`, `DT=`, `la=`,
  `py=`). Alessy 2022 (sheet 8) adds a third. Those are the templates to adapt.
- **No review in this impact band enumerates the 12 recommended symptoms as a search
  block.** Reeve 2014, the paper that defines those 12 symptoms, found them with a two-term
  search. The nearest reusable material is the 40-term PRO block in Osanto 2024.
