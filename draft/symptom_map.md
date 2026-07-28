# The 12 recommended symptoms, one by one

The core set from Reeve et al. 2014 (*JNCI*, PMID 25006191) names twelve patient-reported
symptoms for adult cancer treatment trials. Nothing in the main workbook addresses them
individually, and no review in it enumerates them as a search block — so this table does
it, and names the published block each part of `O6_symptoms` came from.

Verbatim source blocks: `draft/symptom_blocks_published.yml`.

| # | Symptom | MeSH in `O6_symptoms` | Text words in `O6_symptoms` | Block taken from |
|---|---|---|---|---|
| 1 | **Fatigue** | `Fatigue` | fatigue, tired*, weary, weariness, exhaustion, lassitude, lethargy, asthenia | Cramp 2012, Cochrane (exercise for cancer-related fatigue) |
| 2 | **Insomnia** | `Sleep Initiation and Maintenance Disorders`, `Sleep Wake Disorders` | insomnia*, hyposomnia, agrypnia, sleep disturbance(s), sleep quality | Cooper 2025, BMC Cancer (CBT-I in cancer survivors) |
| 3 | **Pain** | `Pain`, `Pain Measurement` | pain, pain* | Li 2021, Cochrane (hydromorphone for cancer pain) |
| 4 | **Anorexia (appetite loss)** | `Anorexia`, `Appetite` | anorexi*, appetite, appetite loss, loss of appetite | Ruiz Garcia 2013, Cochrane (megestrol for anorexia-cachexia) |
| 5 | **Dyspnea** | `Dyspnea` | dyspn*, breathless*, shortness of breath | Haywood 2019, Cochrane (corticosteroids for cancer breathlessness) |
| 6 | **Cognitive problems** | *(in `O2_cognition`)* | *(in `O2_cognition`)* | Treanor 2016, Cochrane — kept in its own block |
| 7 | **Anxiety (incl. worry)** | `Anxiety`, `Anxiety Disorders` | anxiet*, anxious*, panic*, phobia*, worry, worries | Salt 2017, Cochrane (drug therapy for anxiety in palliative care) |
| 8 | **Nausea** | `Nausea`, `Vomiting`, `Antiemetics` | nause*, vomit*, emesis, emetic*, retch* | Vayne-Bossert 2017, Cochrane (corticosteroids for nausea/vomiting) |
| 9 | **Depression (incl. sadness)** | *(in `O3_depression`)* | *(in `O3_depression`)* | Vita 2023, Cochrane — kept in its own block |
| 10 | **Sensory neuropathy** | `Peripheral Nervous System Diseases` | CIPN, neuropath*, neuralgia*, polyneuropath*, neurotoxic* | Sato 2023, BMJ Open (drug therapy for CIPN) |
| 11 | **Constipation** | `Constipation`, `Defecation` | constipat*, defecat* | Candy 2015, Cochrane (laxatives in palliative care) |
| 12 | **Diarrhea** | `Diarrhea` | diarrh* | Wei 2018, Cochrane (probiotics for treatment-related diarrhoea) |

All twelve are covered. Two — cognitive problems and depression — are deliberately left in
their own blocks (`O2`, `O3`) rather than duplicated into `O6`, because your brief treats
cognition and depression as outcome domains in their own right as well as as symptoms. The
recommended search unions all seven outcome blocks, so nothing is lost either way; it only
matters if you run a block in isolation.

## Three places I departed from the published blocks, and why

Each is a judgement you may want to reverse.

1. **`neuropath*` is not taken from Li 2021's pain block.** That block folds
   `neuropath*` into pain, which would blur symptoms 3 and 10 — the core set keeps them
   separate. Neuropathy terms sit only in the sensory-neuropathy portion.
2. **`stress*`, `nervous*` and `agitat*` are not taken from Salt 2017's anxiety block.**
   In a palliative-care review those are reasonable; in a cancer treatment review
   `stress*` alone would retrieve oxidative stress, stress testing and mechanical stress.
3. **Cachexia and weight-loss terms are not taken from Ruiz Garcia 2013's anorexia block.**
   That block is an anorexia-*cachexia* concept. Cachexia, sarcopenia and weight loss are
   already in `O4_nutrition`, and duplicating them into `O6` would make per-symptom counts
   uninterpretable.

## What this changed

Rebuilding the block from published sources rather than from symptom names made it
somewhat broader — `O6` alone goes from 2.15 to 2.63 million PubMed records, and
`P AND I AND O6` from 7,184 to 7,844. Recall of the recommended search is unchanged at
23/23. The gain is not in the numbers; it is that every term now traces to a strategy
someone published and peer review accepted.

## Known gaps

- **Insomnia has a better source coming.** Cochrane published two directly relevant reviews
  in 2025 — CBT for insomnia in people with cancer (PMID 41170811) and acupuncture for
  insomnia in people with cancer (PMID 41347621) — but neither is deposited in PMC yet, so
  their appendices could not be read. Cooper 2025 is used instead. Re-check in a few months.
- **There is no pure appetite-loss block anywhere in the Cochrane library.** Every candidate
  fuses appetite with cachexia and weight loss. Symptom 4 is therefore the least cleanly
  sourced of the twelve.
- **Sato 2023 is the only non-Cochrane source** and the only one already in PubMed syntax.
  It publishes a PubMed strategy only, so no Embase translation of the neuropathy concept
  was available to check against.
