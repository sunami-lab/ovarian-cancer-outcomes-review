# Has this review already been done?

Checked before investing further: is a review of **ovarian cancer treatment and
patient-centred outcomes in older adults** already registered or published?

**Bottom line: no. The review is not taken.** The age axis and the patient-centred-outcome
axis both exist in this literature, but they have not been crossed for ovarian cancer.
Every age-restricted ovarian review stops at progression-free survival, perioperative
mortality or Clavien-Dindo grade. Every patient-centred ovarian review is open to all ages.

One live registration could collide and is worth acting on now — see *The one to watch*.

## How this was checked, and how far to trust it

PROSPERO's public site is a JavaScript shell that returns nothing to a plain fetch, but its
JSON API is reachable: `GET https://www.crd.york.ac.uk/PROSPERO/api/view/<CRD>` with header
`prospero-auth-token: base64(epoch-milliseconds)`. PubMed was searched through E-utilities.

**Every registration number and PMID below was fetched and its title read.** The CRD numbers
were resolved individually against the register and the returned titles compared with what
was claimed; the PMIDs were resolved through esummary. Nothing here is reconstructed from
memory. Where a detail comes from reading the full PROSPERO record rather than the title, it
is marked.

## Direct overlap

None.

## The one to watch

**CRD420251249910 — "Psychosocial concerns among the elderly women diagnosed with
gynecological cancer"** (registered 11 Dec 2025, ongoing, at data extraction).
<https://www.crd.york.ac.uk/prospero/view/CRD420251249910>

The closest live competitor. From the full record: population is gynaecological cancer aged
**over 60**; the intervention is "planned/undergoing/underwent **curative** cancer
treatment"; it **excludes palliative treatment and treatment for recurrence**; there is no
comparator. Outcomes span psychological distress, depression, anxiety, social support,
cognitive function, dependency, body image and quality of life.

That takes roughly half of the planned outcome list. What it leaves:

- it pools all gynaecological sites rather than being ovarian-specific;
- it is not organised by treatment received;
- it excludes palliative treatment and recurrence — so it cannot speak to best supportive
  care or to the recurrent setting, both of which matter most in older patients;
- it omits functional status, nutritional status, symptom burden and satisfaction.

It is far enough along that the decision is now, not later: differentiate deliberately, or
contact the authors.

## Partial overlap

| Record | What it is | What it does not do |
|---|---|---|
| **Martin FE, 2020** — *Functional recovery in older women undergoing surgery for gynaecological malignancies*, J Geriatr Oncol. PMID 32601003 | Closest published analogue on population and outcome philosophy. Already in annex sheet 9. | Surgery only; all gynaecological sites (2 of 15 included studies ovarian); searched to 2018; functional recovery alone. Its own conclusion was that cognition, frailty and comorbidity were almost never reported. |
| **CRD42024547400** — Cognitive and neuropsychological interventions to improve cognitive functioning and quality of life among older adults with gynaecological cancer (ongoing to Nov 2026) | Same population framing, two of your outcomes. | Intervention is cognitive/psychological rehabilitation, not anticancer treatment. |
| **CRD420261355022** — Cytoreductive surgery for advanced ovarian cancer in elderly women | Ovarian, older, treatment. | Outcomes are survival and 30-day morbidity/mortality. No patient-reported outcome. |
| **CRD420261461644** — NACT-IDS versus primary debulking in women ≥70 with advanced EOC | Ovarian, older, treatment comparison. | Perioperative mortality, Clavien-Dindo ≥3, R0, OS, PFS. |
| **CRD420261389113** — Role of age on postoperative complications after surgery for advanced ovarian cancer | Ovarian, age, treatment. | Complications only. |
| **CRD42021261039** / **Maiorano BA, 2022** (PMID 36229080), **Liang L, 2026** (PMID 42494613) | PARP inhibitors in older patients with advanced ovarian cancer. | PFS and adverse events. Not patient-centred outcomes. |
| **Masvidal Hernandez M, 2025** (PMID 39030437) | Narrative review of first-line PARP maintenance in older women. | Not systematic — but it reports that PARP inhibitor trials **do not report quality of life in older women**, which is direct evidence of the gap. |
| Frailty cluster — Di Donato 2021 (PMID 33414025), Li K 2022 (PMID 36324564), Jin 2026 (PMID 41606619), CRD420261325447 | Frailty as an age proxy in ovarian/gynaecological surgery. | Survival and complication endpoints throughout. |

## Adjacent

- **Ovarian/gynaecological patient-centred reviews with no age restriction**:
  CRD420251240990 (EQ-5D utilities in ovarian cancer), CRD42024516737 (ePROs in
  gynaecological cancers), CRD420261361358 (measurement properties of PROMs for symptom
  burden), CRD420261293476 (quality-adjusted and patient-reported outcomes of PARP
  maintenance), CRD420251181643 (treatment-related cognitive impairment in gynaecological
  cancers), CRD420251071481 (nutritional intervention and postoperative prognosis).
- **Narrative overviews of ovarian cancer in older women**: Tew 2016 (PMID 27499341),
  Dumas 2016 (PMID 27664393), Yunokawa 2022 (PMID 35640242). Useful for framing; none
  applies systematic methods.
- **Primary evidence being generated now**: FRAGINOC (PMID 38326125), a multicentre RCT of
  comprehensive geriatric assessment plus exercise in patients ≥70 with EOC on neoadjuvant
  chemotherapy. Also de Arruda 2019 (PMID 30935716), determinants of HRQoL in EOC ≥65, and
  Montégut 2025 (PMID 39673779), the PAOLA-1 older-patient subgroup — the latter is already
  in the known-item set for the recall test.

## What would differentiate the planned review

Four things, and the first three are cheap:

1. **Restrict to ovarian cancer** rather than pooling all gynaecological sites. Every close
   competitor pools.
2. **Stratify by treatment received, including best supportive care.** No existing review
   does this, and CRD420251249910 explicitly excludes palliative treatment.
3. **Carry the outcome domains nobody has combined** — functional status, nutritional
   status, symptom burden and satisfaction, alongside cognition and HRQoL.
4. **Consider framing it as a scoping review or evidence map rather than a meta-analysis.**
   Martin 2020 found the data inadequate for synthesis and Masvidal 2025 confirmed that PARP
   trials do not report quality of life by age. Mapping what is measured, in whom, after
   which treatment — and naming the reporting gap — may be the more defensible contribution,
   and it is what the FRAGINOC trial is being run to fill.
