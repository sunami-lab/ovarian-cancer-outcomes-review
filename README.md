# Ovarian cancer treatment and patient-centred outcomes: systematic review search strategies

Search strategies and evidence extraction from previously published systematic reviews of
ovarian cancer treatment and patient-centred outcomes in oncology.

Two things live here:

1. **The extraction** — how 24 earlier high-impact systematic reviews built their database
   searches for ovarian cancer *treatment* and for each *patient-centred outcome*, recorded
   verbatim.
2. **A drafted strategy** — `draft/`, which applies that material to a review of **ovarian
   cancer treatment and patient-centred outcomes in older adults**, block by block, sized
   against live PubMed.

This is a methods scoping exercise, not a systematic review.

## What is here

| Path | Contents |
|---|---|
| `output/search_strategies.xlsx` | **The extraction deliverable.** 8 category sheets + an annex sheet. |
| `draft/` | **A candidate search strategy for your review**, with measured yields. Start at `draft/README.md`. |
| `data/NN_*.yml` | Source of truth for the workbook, one file per category. |
| `strategies/` | Complete unabbreviated search strategies for the 7 reviews whose workbook cells are condensed. |
| `docs/tables/*.md` | The workbook as Markdown, readable on GitHub, with no display truncation. |
| `docs/methods.md` | How reviews were found, retrieved and verified; what the extraction found; the collection's biases. |
| `docs/impact_factors.md` | Every impact factor quoted, with source and confidence. |
| `docs/validation.md` | Live PubMed run of every transcribed strategy — hit counts, query translations, unmatched terms. |
| `scripts/` | `build.py` (workbook + Markdown), `validate_pubmed.py`, `test_draft.py`. |

```bash
pip install pyyaml openpyxl
python3 scripts/build.py                      # rebuild workbook and tables
python3 scripts/validate_pubmed.py --write    # re-check the transcriptions against PubMed
python3 scripts/test_draft.py --write         # re-size the drafted strategy
```

## The nine sheets

| # | Sheet | Reviews |
|---|---|---|
| 1 | Ovarian cancer treatment (general, not a specific treatment) | Coleridge 2021, Faluyi 2010, Elattar 2011 |
| 2 | Functional status | **Neo 2017**, McDonald 2023, Scheepers 2020 |
| 3 | Cognition | Treanor 2016, Lawrie 2019, Jim 2012 |
| 4 | Depression | Soong 2025, Vita 2023, Kulchycki 2024 |
| 5 | Nutritional status | **Billson 2013** (ovarian), Takaoka 2024, Lovell 2025 |
| 6 | Health-related quality of life | Mishra 2012, Osanto 2024, Cramer 2017 |
| 7 | Patients' symptoms (12 recommended) | Reeve 2014, Balitsky 2024, Ream 2020 |
| 8 | Patients' satisfaction | Jacobsen 2018, Gomes 2013, Alessy 2022 |
| 9 | **Annex** — 10 reviews the IF ≥ 5 rule excluded | Six ovarian/gynaecological, two older-adult |

Category 1 asks how earlier reviews search for **treatment** in ovarian cancer, so ovarian
cancer was held fixed and the age restriction relaxed. Categories 2–8 ask how earlier
reviews search for each **outcome**, so cancer type and age were left open by design.

## Columns

`title` · `1st author/year` · `journal` · `impact factor` · `purpose of the study` ·
`PICO` · `search terms/strings for PubMed` · `…for Embase` · `…for Web of Science` · `url`

## How to trust what is in here

- **Nothing was reconstructed.** Every string was read from the published appendix,
  supplement or Methods section named in that record's `strategy_source` field.
- **Every DOI was resolved through CrossRef** and its title and journal compared with the
  recorded values. This caught two errors, including a record that was in a lower-impact
  companion journal with an almost identical name.
- **Every native-PubMed strategy was executed** against E-utilities (`docs/validation.md`).
  All ten parse, all retrieve, and PubMed dropped no terms. The run also *disproved* one of
  my own annotations — an operator-precedence warning that turned out not to apply in
  PubMed — which is now corrected.
- **A blank is reported as a blank.** Where a review did not search a database, or searched
  it without publishing the string, the cell says so: 24/24 records give a MEDLINE or
  PubMed strategy, 16/24 an Embase strategy, 7/24 anything for Web of Science.
- **Published errors are flagged, not silently repaired** — `qlc-c30` for QLQ-C30,
  `choriocrcinoma*`, `yora`, `.mp3`, truncation inside Emtree explosions, and Cramer 2017's
  mis-numbered set combinations.

## Known biases, stated plainly

- **11 of 24 records are Cochrane reviews.** Partly a retrieval artifact — Cochrane prints
  appendices in-line and PMC serves them, while Elsevier and OUP do not. Partly real: on
  sheet 1 all three are Cochrane because every non-Cochrane ovarian review above the
  threshold is about a *specific* treatment, which the category excludes.
- **Vintage skews old**: 7 records pre-date 2015, 5 are 2015–2019, 12 are 2020 or later.
- **The IF ≥ 5 rule cost population relevance.** The ovarian and geriatric-oncology
  literature sits almost entirely at IF 2.4–4.8. Sheet 9 lists what that excluded, including
  Martin 2020 (older women, gynaecological cancer surgery, functional recovery) — the best
  population-and-outcome match in the whole candidate pool.
- **Two reviews remain unobtainable** (Zeng 2020, Ho 2025), plus Zimmermann 2008. All need a
  subscription copy. Everything else that could be recovered legally, was — Unpaywall
  retrieved Neo 2017, which is now the lead record on sheet 2.

## What the 24 strategies show

- **Most reviews do not search on the outcome.** Population AND intervention, with the
  outcome applied at screening, is the dominant structure. `draft/counts.md` prices it:
  adding an outcome block to an ovarian cancer treatment search keeps 13% of the records.
  Neo 2017 is the counter-example — no intervention concept at all, and a thirteen-synonym
  functional-disability block instead.
- **Where the outcome is searched, sensitivity varies by an order of magnitude.** The three
  depression blocks on sheet 4 run from four words to a 20-term text-word line. Impact
  factor does not predict search quality: the thinnest strategy in the collection is in the
  highest-impact journal in it.
- **Searching on instrument names is the most transferable idea here.** Mishra 2012
  retrieves via QLQ-C30, FACIT, SF-36, HADS, POMS and MSAS; Alessy 2022 via CPES, CAHPS and
  AOPSS. Both catch papers whose abstracts never use the concept word.
- **Web of Science is rarely published.** Three usable strategies: Takaoka 2024, Osanto 2024
  (the most complete) and Alessy 2022.
- **No review in this impact band enumerates the 12 recommended symptoms as a search
  block** — including Reeve 2014, the paper that defined them, which used a two-term search.

## A note on the Excel file

Some strategy cells are longer than Excel's maximum row height (409.5 pt) can display. The
**content is complete** — click the cell and read the formula bar. For unclipped text use
`docs/tables/*.md` or `strategies/*.txt`. Each affected sheet carries a note saying which
rows are affected.
