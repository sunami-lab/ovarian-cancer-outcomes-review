# How the 24 reviews were found and selected

## The brief

Eight categories, three previously published systematic reviews each, all from high-impact
journals, extracted into one spreadsheet with the columns: title, 1st author/year, journal,
impact factor, purpose of the study, PICO, search terms/strings for PubMed, Embase and Web
of Science, and URL.

- **Category 1** asks how earlier reviews search for *treatment* in ovarian cancer. Ovarian
  cancer was therefore held fixed and the population broadened.
- **Categories 2–8** ask how earlier reviews search for each *patient-centred outcome*.
  Cancer type and age were left open by design, with ovarian/gynaecological and
  older-adult reviews preferred wherever one existed above the impact-factor threshold.

## Selection rule

Two criteria, applied in this order:

1. **Journal Impact Factor ≥ 5** (a hard floor set by the requester). See
   [impact_factors.md](impact_factors.md), including the list of topically closer reviews
   this rule excluded.
2. **The search strategy must be readable in full.** A record whose search cannot be
   reproduced is useless for this exercise, so among journals clearing the threshold,
   preference went to reviews that publish their strategies in appendices or supplements
   that are actually retrievable.

Within those two constraints, preference went to (a) ovarian or gynaecological cancer,
(b) older adults, (c) reviews that put the outcome in the search rather than applying it at
screening, and (d) reviews searching Web of Science, which almost none do.

## How candidates were found

Searching was done against PubMed (NCBI E-utilities) and Europe PMC. Typical searches
combined an outcome concept in the title with a cancer concept in the title, a
systematic-review filter, and an explicit list of journals known to sit above the threshold.
For example, for functional status:

```
(systematic review[ti] OR meta-analysis[ti])
AND (cancer[ti] OR oncolog*[ti] OR chemotherapy[ti] OR neoplas*[ti])
AND (functional status[tiab] OR physical function*[tiab] OR "activities of daily
     living"[tiab] OR functional decline[tiab] OR physical performance[tiab])
AND (older[tiab] OR elderly[tiab] OR geriatric[tiab] OR aged[tiab])
```

Europe PMC's section-restricted search was also used to find reviews that put an outcome
term inside a runnable search string, by looking for the outcome term co-occurring with
PubMed field-tag syntax in the Methods section:

```
METHODS:"activities of daily living" AND METHODS:"tiab" AND METHODS:"cancer"
```

This is a good trick and a limited one — Europe PMC only indexes sections for
open-access full text, so it under-reports.

## How the strategies were obtained

Every strategy in this repository was read from the source document. Nothing was
reconstructed from a description, translated between syntaxes, or written by hand.
Retrieval routes, in the order tried:

1. **Europe PMC full-text XML** — `/{PMCID}/fullTextXML`. Fast, but only open-access.
2. **Europe PMC supplementary files** — `/{PMCID}/supplementaryFiles` returns a zip. This
   is how the JAMA Network Open eTables, the JCSM `.docx` appendix, the Advances in
   Nutrition supplemental tables and the eClinicalMedicine supplementary tables were read.
3. **The PMC website HTML** — this is the route that works for Cochrane reviews, whose
   in-line appendices carry the MEDLINE, Embase and CENTRAL strategies in full. Cochrane
   content is not in the Europe PMC open-access subset and the Cochrane Library itself
   blocks automated access, so this route did most of the work for the eleven Cochrane
   records.

4. **Unpaywall** (`api.unpaywall.org`) — added on a second pass, and it should have been
   the first thing tried. Given a DOI it reports whether any *legal* open-access copy
   exists and where. It recovered two reviews previously recorded here as unobtainable:

   - **Neo 2017** (Cancer Treatment Reviews) — gold OA, CC BY-NC-ND, in the King's College
     London repository, with its supplementary Appendix 1 on the Elsevier CDN. This is now
     the lead record on sheet 2 and carries the best functional-status block in the
     collection.
   - **Chan 2023** (CA: A Cancer Journal for Clinicians) — free at the publisher, but every
     mirror returned 403 to an automated request, so it remains unused.

   Nine candidate DOIs were checked this way. Two were legally OA; seven were not.

Where every route failed, the review was dropped rather than guessed at. Two reviews
remain excluded for this reason despite clearing the impact-factor threshold and being
on-topic: Zeng 2020 (International Journal of Nursing Studies, network meta-analysis of
interventions for cancer-related cognitive impairment) and Ho 2025 (JNCI, network
meta-analysis for the same). Zimmermann 2008 (JAMA, specialized palliative care, with
patient satisfaction as a primary outcome) is likewise closed. All three would need a
subscription copy.

One limitation is recorded rather than worked around: the 2025 update of the Cochrane
neoadjuvant-chemotherapy review (Shawky 2025, CD005343.pub7) moved its search strategy from
an in-line appendix to a downloadable supplement that PMC serves behind a challenge page and
that is not in the open-access subset. The 2021 version (pub6) is cited instead, because its
strategy could be read in full.

## Verification

Two automated checks run against the finished collection.

**Bibliographic.** Every DOI is resolved through CrossRef and its title and container title
compared with the recorded values. This caught two errors, both from DOIs I had inferred
rather than read: a wrong eClinicalMedicine DOI, and — more seriously — a record recorded
as *International Journal of Nursing Studies* that is actually in *International Journal of
Nursing Studies Advances*, a separate companion journal below the impact threshold. That
record was replaced.

**Executable.** `scripts/validate_pubmed.py` runs the ten strategies published in native
PubMed syntax against E-utilities and records the hit count, PubMed's own query translation
and any term PubMed could not match, in `docs/validation.md`. All ten parse and retrieve;
no term was dropped. The run also disproved a claim I had made: I had flagged an
operator-precedence hazard in Alessy 2022's unparenthesised OR chain, and running it both
ways returns an identical translation and an identical 109 records. The warning is now
corrected and redirected to Ovid and Web of Science, where the construction really is
unsafe.

## What the extraction found

Three things recur across the eight categories and are worth knowing before writing your own
protocol.

**1. Most reviews do not search on the outcome.** Population AND intervention (AND study
design) is the dominant structure. Physical function is the entire subject of McDonald 2023
and appears nowhere in its search; Cramer 2017 has HRQOL first in its title and searches for
no quality-of-life term; Ream 2020 asks "which symptoms respond" and searches for no symptom.
The outcome is applied at screening. If you plan to retrieve on your outcomes, you are doing
something most of this literature does not do, and you should expect it to cost you
sensitivity — `draft/counts.md` puts a number on it: adding the outcome block to an ovarian
cancer treatment search keeps 13% of the records.

Neo 2017 (sheet 2) is the counter-example worth studying: it has no intervention concept at
all, and carries a thirteen-synonym functional-disability block instead.

**2. Where reviews do search the outcome, the blocks vary by an order of magnitude in
sensitivity.** Compare the three depression blocks in category 4: four words (Soong), four
MeSH terms plus one adjacency (Vita), and eight controlled-vocabulary terms plus a 20-term
text-word line reaching into mood, distress, hopelessness and wellbeing (Kulchycki). All
three are in journals above the threshold. Impact factor does not predict search quality —
the thinnest search in the collection (Jim 2012, seven unstructured keyword pairings) is in
the highest-impact journal in it.

**3. Web of Science is rarely searched and even more rarely published.** Of 24 reviews,
seven searched Web of Science and three published the string: Takaoka 2024 (a clean `TS=`
topic search, category 5), Osanto 2024 (a full `TI=`/`AB=`/`TS=` strategy with `NEAR/5`,
`DT=`, `la=` and `py=`, category 6) and Alessy 2022 (category 8). Neo 2017 and Shao 2025
searched it without publishing a string; Mishra 2012 used it for citation searching of key
authors rather than with a subject strategy. If you add Web of Science, Osanto 2024 is the
template.

## Composition of the collection, and its biases

Stated plainly, because they affect how far the findings generalise.

- **11 of the 24 records are Cochrane reviews.** Partly this is a retrieval artifact:
  Cochrane prints full appendices in-line and PMC serves them, while Elsevier and OUP do
  not, so the requirement that a strategy be readable selects for Cochrane. Partly it is
  real: on sheet 1 all three records are Cochrane because every non-Cochrane ovarian
  cancer review above the threshold is about a *specific* treatment (PARP inhibitors,
  HIPEC, bevacizumab, dose-dense chemotherapy), which the category definition excludes.
- **Database coverage is uneven**: 24/24 records give a MEDLINE or PubMed strategy, 16/24
  an Embase strategy, 7/24 anything for Web of Science.
- **Vintage skews old**: 7 records pre-date 2015, 5 are 2015–2019, 12 are 2020 or later.
  Pre-PRISMA-S reporting conventions show, which is part of why several strategies contain
  the typographical errors flagged in the workbook.
- **The impact-factor threshold cost population relevance.** Ten reviews closer to ovarian
  cancer or to older adults were excluded on it and are listed in annex sheet 9.

## The drafted strategy

`draft/` applies all of this to the review the exercise was run for. It assembles a
candidate strategy for ovarian cancer treatment and patient-centred outcomes in older
adults from the best blocks in the collection, sizes every block and combination against
live PubMed, and argues the three design decisions (whether to search the outcome, whether
to search age, which databases) from those numbers. See `draft/README.md`.

## Reproducing this

`data/NN_*.yml` is the source of truth; `scripts/build.py` regenerates
`output/search_strategies.xlsx` and `docs/tables/*.md` from it.

```bash
pip install pyyaml openpyxl
python3 scripts/build.py            # workbook + Markdown tables
python3 scripts/validate_pubmed.py --write   # re-run the transcription checks
python3 scripts/test_draft.py --write        # re-size the drafted strategy
```

Each YAML record carries `pmid`, `pmcid`, `doi` and `strategy_source` — the last naming the
specific appendix, supplement or section the strategy was read from — so any entry can be
checked against the original.
