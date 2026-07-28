# Estimating the real screening burden

Summing the per-database hit counts overestimates the work, sometimes badly. This is what
the reviews in the collection actually reported, so the planning figure comes from observed
practice rather than a guess.

## Observed deduplication, from the reviews' own reported yields

Every figure below was read from the review's published supplement or results section, not
estimated.

| Review | Databases | Records before dedup | After dedup | Duplicates removed |
|---|---|---:|---:|---:|
| **Balitsky 2024** (original search) | MEDLINE, Embase, PsycInfo, CENTRAL, CINAHL | 10,510 | 7,156 | 3,354 (**32%**) |
| **Balitsky 2024** (2022 update) | same five | 13,857 → 3,554 after limits | 2,505 | 1,049 (**30%** of the limited set) |
| **McDonald 2023** (trials search) | MEDLINE, Embase, CENTRAL | 8,166 | 5,998 | 2,168 (**27%**) |
| **McDonald 2023** (cohort search) | MEDLINE, Embase | 3,949 | 3,190 | 759 (**19%**) |
| **Scheepers 2020** | MEDLINE (832), EMBASE (3,797) | 4,629 | 4,226 | 403 (**9%**) |

**Observed range: 9–32%.** The spread is explained by how much the databases overlap for
the topic. Scheepers is the low outlier because its MEDLINE yield was tiny relative to
Embase (832 versus 3,797), so there was little to duplicate. Where MEDLINE and Embase
contribute comparably — Balitsky, McDonald — the ratio settles around 25–32%.

## Applying it to the drafted strategy

The drafted PubMed search retrieves **18,472** records
(`P AND anyOutcome`, `draft/counts.md`). A rough projection for a
MEDLINE + Embase + CENTRAL search of the same concepts:

| Step | Estimate |
|---|---|
| MEDLINE (measured) | 18,472 |
| Embase — typically 1.3–2× the MEDLINE yield in these reviews | ~24,000–37,000 |
| CENTRAL | ~2,000–4,000 |
| Raw total | ~45,000–60,000 |
| **After deduplication at the observed 25–30%** | **~32,000–44,000 to screen** |

That is a large but not unprecedented title-and-abstract screen. Two levers, both already
measured:

- The **treatment block** takes the MEDLINE yield from 18,472 to 12,590 (32% less) at a
  cost of 1 of 23 known items — see `draft/README.md` decision 1b.
- The **age block** takes it to 4,194 but costs 8 of 23 known items. Not recommended.

If the projected burden is beyond the team, the honest options are to accept the treatment
block and record it as a pragmatic restriction, to restrict by date, or to narrow the
outcome set — not to add the age filter.

## Caveats

- Five data points from four reviews is a small base. Treat 25–30% as a planning
  assumption, not a constant.
- The Embase multiplier is inferred from the same reviews' per-database yields and is the
  softest number here. Once the Embase strategy is actually run, replace the estimate.
- These are title-and-abstract counts. Full-text screening volume depends on the inclusion
  criteria, which are not settled yet.
