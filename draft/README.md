# A drafted search strategy for your review

The 24 records in the main workbook are raw material. This directory is what they were
collected for: a candidate search strategy for **ovarian cancer treatment and
patient-centred outcomes in older adults**, assembled from the best blocks in the
collection, with every line traced back to the review it came from.

**This is a draft for an information specialist to review, not a finished strategy.**

| File | What it is |
|---|---|
| `blocks_pubmed.yml` | Source of truth. Each block with its provenance and the combinations to size. |
| `pubmed.txt` | Runnable PubMed strategy, generated from the YAML. **The only version that has been executed.** |
| `counts.md` | Live PubMed yields for every block and combination. |
| `ovid_medline.txt` | Ovid MEDLINE translation. **Untested.** |
| `embase_ovid.txt` | Embase (Ovid) translation. **Untested.** |
| `web_of_science.txt` | Web of Science translation. **Untested.** |

Re-run the sizing at any time:

```bash
python3 scripts/test_draft.py --write
```

## What it yields

| Strategy | PubMed records | Comment |
|---|---:|---|
| Population only | 179,495 | — |
| Population AND treatment | **91,708** | Widest defensible. Too many to screen. |
| … AND any patient-centred outcome | **12,061** | **Recommended primary search.** |
| … AND age block as well | 4,075 | Comfortable, but see the warning below. |
| … AND design filter instead of outcome | 26,181 | If you would rather screen on outcome. |

Per outcome, intersected with population AND treatment:

| Outcome | Records |
|---|---:|
| Symptoms (the 12) | 7,184 |
| HRQOL | 3,273 |
| Functional status | 1,294 |
| Nutritional status | 1,266 |
| Cognition | 758 |
| Depression | 611 |
| Patient satisfaction | 321 |

## Three decisions you have to make, with the evidence for each

**1. Should the outcome be in the search at all?**

The evidence from the 24 reviews says usually not: population AND intervention, with the
outcome applied at screening, is the dominant pattern, and reviews that name an outcome in
the title still frequently omit it from the strategy (Molenaar, Cramer, Ream). The argument
against putting it in is that you lose studies whose abstracts report your outcome without
naming it — a trial reporting "QLQ-C30 scores" and nothing else is retrieved by Mishra's
instrument-name line but not by "quality of life".

The argument for putting it in is arithmetic: 91,708 records is not a screenable set for a
review team, and 12,061 is. The outcome block keeps 13% of the population-and-treatment set.

My recommendation: run `P AND I AND anyOutcome` as the primary search, and run `P AND I`
separately, restricted to the last five years, as a sensitivity check on what the outcome
block loses. If the check turns up eligible studies the primary search missed, the block is
too tight and the instrument-name lines are where to widen first.

**2. Should the age block be in the search?**

Probably not. MEDLINE indexes participant age inconsistently, and "older" and "elderly"
appear in abstracts erratically — a trial of women with a median age of 68 will often say
neither. Applying `A_older` drops the set from 12,061 to 4,075, which is a two-thirds
reduction that is very unlikely to be two-thirds irrelevance.

Note that only one review in the entire collection (Soong 2025) used an age block in the
search. Scheepers 2020, which is restricted to older adults, reached them through
"frailty" and "Geriatric Assessment"[Mesh] rather than through age terms — worth
considering as a middle path.

My recommendation: apply age at screening, and keep `A_older` for a sensitivity check.

**3. Which databases?**

Of the 24 reviews, 24 searched MEDLINE, 17 published an Embase strategy, and 4 searched
Web of Science (2 published the string). Given that spread, MEDLINE plus Embase plus
CENTRAL is the defensible minimum. Add Web of Science if you want citation-index coverage;
`web_of_science.txt` is modelled on Osanto 2024, the most complete published Web of Science
strategy found.

## Provenance

Every block names its sources in `blocks_pubmed.yml`. In summary:

| Block | Taken from |
|---|---|
| Population | Billson 2013, Elattar 2011 — **plus** fallopian tube and primary peritoneal terms I added |
| Treatment | Coleridge 2021, Elattar 2011, Faluyi 2010 — **plus** PARP, targeted and immunotherapy terms I added |
| Age | Soong 2025 — plus the standard Aged MeSH terms it omits |
| Functional status | Neo 2017 — taken over essentially whole |
| Cognition | Treanor 2016 |
| Depression | Kulchycki 2024 (trimmed), Vita 2023 |
| Nutritional status | Billson 2013, Takaoka 2024, Lovell 2025 |
| HRQOL | Osanto 2024 (concepts), Mishra 2012 (instrument names) |
| Symptoms | **Largely constructed.** No review in the collection enumerates the 12 symptoms; the block is built from the symptom names in Reeve 2014 plus the symptom terms inside Osanto 2024's PRO block. Scrutinise this one hardest. |
| Satisfaction | Jacobsen 2018 (narrowed — its full set 4 retrieves 5.3 million records), Alessy 2022 (instruments) |
| Design | Coleridge 2021, widened with Neo 2017's cohort terms |

Three additions are mine and are not in any of the 24 reviews. Each is flagged in the YAML
and each is a judgement you may want to reverse:

- **Fallopian tube and primary peritoneal terms** in the population block. Current
  classification treats these as one entity with ovarian high-grade serous carcinoma and
  trials recruit them together; strategies written before roughly 2010 do not reflect that.
- **PARP inhibitor, targeted therapy and immunotherapy terms** in the treatment block. The
  sheet-1 Cochrane strategies pre-date first-line PARP maintenance, so copying them
  unchanged would miss the trials that now define ovarian cancer treatment.
- **The symptom block**, which had to be constructed because no exemplar exists.

## Known limitations

- Only the PubMed version has been run. The Ovid, Embase and Web of Science files are
  translations written to convention and have not been executed against those platforms.
  Emtree headings in particular change often and must be checked.
- The strategy has not been peer reviewed against PRESS, which a submitted protocol should
  be.
- No grey literature, trial registry or conference-abstract component is included yet.
  Most of the 24 reviews searched ClinicalTrials.gov and WHO ICTRP; add those.
- Counts drift. `draft/counts.md` records the date-free snapshot; re-run
  `scripts/test_draft.py` before quoting any number.
