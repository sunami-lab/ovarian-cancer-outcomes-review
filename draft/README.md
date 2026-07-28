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
| `recall.md` | Known-item recall test — does the strategy find what it must? |
| `ovid_medline.txt` | Ovid MEDLINE translation. **Untested.** |
| `embase_ovid.txt` | Embase (Ovid) translation. **Untested.** |
| `web_of_science.txt` | Web of Science translation. **Untested.** |

Re-run either test at any time:

```bash
python3 scripts/test_draft.py --write     # how much is there to screen
python3 scripts/recall_test.py --write    # what does it miss
```

## What it yields, and what it finds

Two numbers matter for a search: how much you have to screen, and how much you miss.
`scripts/test_draft.py` gives the first, `scripts/recall_test.py` the second — the latter
against 23 verified studies a review of this question must not miss (`draft/recall.md`).

| Strategy | Records to screen | Known items found | Recall |
|---|---:|---:|---:|
| Population only | 179,495 | 23/23 | 100% |
| **Population AND any outcome** | **17,623** | **23/23** | **100%** ← recommended |
| Population AND treatment AND any outcome | 12,061 | 22/23 | 96% |
| Population AND treatment | 91,708 | 22/23 | 96% |
| … AND age block as well | 4,075 | 15/23 | 65% |

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

## The decisions, and the evidence for each

**1. Should the outcome be in the search at all?** — Yes.

The evidence from the 24 reviews says most reviews do not: population AND intervention,
with the outcome applied at screening, is the dominant pattern. But that pattern is for
reviews whose population block is already narrow. Here the arithmetic settles it: the
outcome block cuts 179,495 records to 17,623 and loses none of the 23 known items. There is
no sensitivity argument against it in this particular review.

**1b. Should the *treatment* block be in the search?** — Probably not, and this is the one
place the recall test changed my recommendation.

Adding it takes 17,623 records down to 12,061 — 32% less screening — but drops a known
item: Wenzel 2021 (JNCI), a quality-of-life and adverse-event analysis of GOG-0218. That
paper carries **no treatment MeSH heading at all**, and its abstract never names a drug or
a procedure; it says only "post-treatment" and reports FACT-O-TOI scores. It is not an
oddity — it is the signature of a whole class of paper this review needs: **patient-reported
outcome secondary analyses of trials, which describe the outcome in detail and take the
intervention as read**. A treatment block systematically drops them.

Since every study of ovarian cancer patients is, in practice, a study of treated ovarian
cancer patients, the treatment block buys precision rather than validity here.

My recommendation: run `P AND anyOutcome` as the primary search. If 17,623 abstracts is
beyond the team's capacity, `P AND I AND anyOutcome` is a defensible fallback — but record
in the protocol that it is a pragmatic restriction, not a conceptual one, and consider
running `P AND (O5_hrqol OR O6_symptoms)` without the treatment block as a top-up to
recover the PRO secondary analyses.

**2. Should the age block be in the search?** — No. This is now measured, not argued.

Applying `A_older` drops the known-item recall from 100% to **65%**: eight of the 23 items
disappear, and they are almost all the trial quality-of-life papers — SOLO1's and PAOLA-1's
PRO publications, the AURELIA QoL substudy, ARIEL3's PROs, PRIMA's updated PROs. Those
trials enrolled plenty of older women; their PRO papers simply do not use the words "older"
or "elderly" and are not indexed under Aged.

Note also that only one review in the whole collection (Soong 2025) used an age block in
the search. Scheepers 2020, which is restricted to older adults, reached them through
"frailty" and "Geriatric Assessment"[Mesh] instead — a middle path worth considering, though
the recall test suggests even that will lose PRO papers.

My recommendation: apply age at screening. Keep `A_older` only for a sensitivity check.

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
