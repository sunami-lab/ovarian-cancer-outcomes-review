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
   blocks automated access, so this route did most of the work for the twelve Cochrane
   records.

Where a route failed, the review was dropped rather than guessed at. Three reviews were
excluded for this reason despite clearing the impact-factor threshold and being on-topic:
Neo 2017 (Cancer Treatment Reviews, ADL disability in adults with cancer), Zeng 2020
(International Journal of Nursing Studies, network meta-analysis of interventions for
cancer-related cognitive impairment), and Ho 2025 (JNCI, network meta-analysis for
cancer-related cognitive impairment) — all Elsevier or OUP paywalled with no accessible
supplement.

One limitation is recorded rather than worked around: the 2025 update of the Cochrane
neoadjuvant-chemotherapy review (Shawky 2025, CD005343.pub7) moved its search strategy from
an in-line appendix to a downloadable supplement that PMC serves behind a challenge page and
that is not in the open-access subset. The 2021 version (pub6) is cited instead, because its
strategy could be read in full.

## What the extraction found

Three things recur across the eight categories and are worth knowing before writing your own
protocol.

**1. Most reviews do not search on the outcome.** Population AND intervention (AND study
design) is the dominant structure. Functional capacity is the lead outcome of Molenaar 2023
and appears nowhere in its search; physical function is the entire subject of McDonald 2023
and appears nowhere in its search; Cramer 2017 has HRQOL first in its title and searches for
no quality-of-life term; Ream 2020 asks "which symptoms respond" and searches for no symptom.
The outcome is applied at screening. If you plan to retrieve on your outcomes, you are doing
something most of this literature does not do, and you should expect it to cost you
sensitivity.

**2. Where reviews do search the outcome, the blocks vary by an order of magnitude in
sensitivity.** Compare the three depression blocks in category 4: four words (Soong), four
MeSH terms plus one adjacency (Vita), and eight controlled-vocabulary terms plus a 20-term
text-word line reaching into mood, distress, hopelessness and wellbeing (Kulchycki). All
three are in journals above the threshold. Impact factor does not predict search quality —
the thinnest search in the collection (Jim 2012, seven unstructured keyword pairings) is in
the highest-impact journal in it.

**3. Web of Science is rarely searched and even more rarely published.** Of 24 reviews, four
searched Web of Science and two published the string: Takaoka 2024 (a clean `TS=` topic
search, category 5) and Osanto 2024 (a full `TI=`/`AB=`/`TS=` strategy with `NEAR/5`, `DT=`,
`la=` and `py=`, category 6). Shao 2025 searched it but published the strategy only as a
bitmap figure. Mishra 2012 used it for citation searching of key authors rather than with a
subject strategy. If you add Web of Science, Osanto 2024 is the template.

## Reproducing this

`data/*.yml` is the source of truth; `scripts/build.py` regenerates
`output/search_strategies.xlsx` and `docs/tables/*.md` from it.

```bash
pip install pyyaml openpyxl
python3 scripts/build.py
```

Each YAML record carries `pmid`, `pmcid`, `doi` and `strategy_source` — the last naming the
specific appendix, supplement or section the strategy was read from — so any entry can be
checked against the original.
