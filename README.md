# Ovarian cancer treatment and patient-centred outcomes: systematic review search strategies

Search strategies and evidence extraction from previously published systematic reviews of
ovarian cancer treatment and patient-centred outcomes in oncology.

This repository is a **methods scoping exercise**, not a systematic review. Its purpose is
to collect, verbatim, how earlier high-impact systematic reviews built their database
searches for (a) *treatment* of ovarian cancer and (b) each *patient-centred outcome* of
interest, so those search blocks can be reused or adapted when designing a new review of
ovarian cancer treatment and patient-centred outcomes in older adults.

## What is here

| Path | Contents |
|---|---|
| `output/search_strategies.xlsx` | The deliverable. One sheet per category, 3 reviews per sheet. |
| `data/*.yml` | Source of truth, one file per category. Long Boolean strings live in YAML block scalars so they stay diffable. |
| `docs/tables/*.md` | The same tables rendered as Markdown, readable on GitHub without downloading the workbook. |
| `docs/methods.md` | How reviews were found and selected; what was done when nothing matched. |
| `docs/impact_factors.md` | Every impact factor quoted, with its source. |
| `scripts/build.py` | Regenerates the workbook and the Markdown from `data/`. |

Rebuild after editing any YAML file:

```bash
pip install pyyaml openpyxl
python3 scripts/build.py
```

## Categories (one spreadsheet sheet each)

| # | Sheet | Population / cancer type searched |
|---|---|---|
| 1 | Ovarian cancer treatment (general, not a specific treatment) | Ovarian cancer, any age |
| 2 | Functional status | Any cancer, any age |
| 3 | Cognition | Any cancer, any age |
| 4 | Depression | Any cancer, any age |
| 5 | Nutritional status | Any cancer, any age |
| 6 | Health-related quality of life (HRQOL) | Any cancer, any age |
| 7 | Patients' symptoms (12 recommended symptoms) | Any cancer, any age |
| 8 | Patients' satisfaction | Any cancer, any age |

Category 1 asks how earlier reviews search for **treatment** in ovarian cancer, so ovarian
cancer was held fixed and the age restriction relaxed. Categories 2–8 ask how earlier
reviews search for each **outcome**, so cancer type and age were left open by design, with
reviews in older adults and in gynaecological/ovarian cancer preferred where they existed.

## Columns

`title` · `1st author/year` · `journal` · `impact factor` · `purpose of the study` ·
`PICO` · `search terms/strings for PubMed` · `…for Embase` · `…for Web of Science` · `url`

## Two things to know before using the search strings

1. **"PubMed" usually means Ovid MEDLINE.** Most systematic reviews search MEDLINE through
   Ovid, not PubMed, and the two syntaxes are not interchangeable (`exp Term/`, `.mp.`,
   `.fs.`, `adj5` have no PubMed equivalent). Every cell states which interface and which
   date range the strategy was actually run on. Nothing has been silently translated.
2. **A blank is reported as a blank.** Where a review did not search a database, or
   searched it but did not publish the string, the cell says so. Web of Science in
   particular is frequently searched with a strategy that is never printed. No search
   string in this repository has been reconstructed, inferred, or written by hand.

Provenance for every strategy — which appendix, supplement, or table it came from — is in
the `strategy_source` field of each YAML record and in `docs/tables/`.

## Selection rule

Reviews had to be published in a journal with a **Journal Impact Factor ≥ 5**, and had to
publish a search strategy that could be read in full. Where the ideal population (older
adults with ovarian cancer) had no review meeting that bar, the population was broadened as
specified above and the broadening is recorded in the category's YAML file and in
`docs/methods.md`.
