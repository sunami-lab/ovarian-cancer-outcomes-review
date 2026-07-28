# 08. Patients' satisfaction

**Focus of this category.** How do previously published systematic reviews of cancer treatment build the patient satisfaction concept in their database search strategies?

**Population scope applied.** Cancer type and age left open, per the brief. The most on-topic review found - Wells 2018, "Effects of patient navigation on satisfaction with cancer care: a systematic review and meta-analysis", Supportive Care in Cancer - was excluded on the JIF >= 5 threshold (JIF ~2.8) and is worth reading alongside these three.

## Jacobsen PB, 2018 - Journal of Clinical Oncology

**Systematic Review of the Impact of Cancer Survivorship Care Plans on Health Outcomes and Health Care Delivery**

- Impact factor: 42.1 (2023 JIF)
- URL: <https://doi.org/10.1200/JCO.2018.77.7482>
- PMID: 29775389 | PMCID: PMC6036622
- Search strategy taken from: Appendix (PICO Framework and PubMed/MEDLINE Search Strategy) of the article

**Purpose.** To determine what impact providing a survivorship care plan has on health outcomes and health care delivery for people diagnosed with cancer, with satisfaction with care as one of the health-care-experience outcomes. Included because its fourth search set is an explicit patient-centred outcome block - the clearest published example in this collection of retrieving on satisfaction rather than screening for it.

**PICO**

| | |
|---|---|
| **P** — Population | Individuals diagnosed with cancer. |
| **I** — Intervention / exposure | Survivor or care-provider receipt of a survivorship care plan (SCP). |
| **C** — Comparison | No receipt of an SCP, an alternative method of receiving an SCP, or no comparison (for non-randomised studies). |
| **O** — Outcome | Patient-reported health outcomes (e.g. quality of life); health care use; health care costs; health outcomes (e.g. quality-adjusted life years); and health care experience (e.g. satisfaction with care). |

**Search strategy - PubMed / MEDLINE**

```
[PubMed/MEDLINE searched natively. Search strategy printed in the Appendix, verbatim -
four sets combined as 1 AND 2 AND 3 AND 4:]
1 (Cancer OR Cancers OR Neoplasm OR Neoplasms OR Neoplasia OR "Neoplasms"[Mesh])
2 (("care planning" OR "care plan*" OR "survivorship care plan*" OR "Follow-up care"
  OR "follow up care" OR ("follow up" AND care) OR (follow-up AND care)
  OR "continuity of care" OR "continual care" OR "continuous care"
  OR "longitudinal care" OR "Patient Care Planning"[Mesh]
  OR "Continuity of Patient Care"[Mesh]) AND (Survivor* OR Survivorship
  OR "Survivors"[Mesh])
3 ("Randomized controlled trial" OR "Non-randomized controlled trial"
  OR "non-randomized controlled trial" OR "Randomized Controlled Trial"
  [Publication Type] OR "Non-Randomized Controlled Trials as Topic"[Mesh])
4 ("patient satisfaction" OR "quality of life" OR QOL OR Distress OR Understanding
  OR "screening compliance" OR Feasibility OR ("care coordination" AND rating*)
  OR "disease recurrence" OR "serious clinical event*" OR "social support"
  OR "survival rate" OR "Treatment Outcome"[Mesh] OR "Patient Outcome
  Assessment"[Mesh] OR "Patient Satisfaction"[Mesh] OR "Quality of Life"[Mesh]
  OR "Stress, Psychological"[Mesh] OR "Comprehension"[Mesh]
  OR "Patient Compliance"[Mesh] OR "Feasibility Studies"[Mesh]
  OR "Recurrence"[Mesh] OR "Social Support"[Mesh] OR "Survival Rate"[Mesh])
1 AND 2 AND 3 AND 4
Set 4 is the reusable part: it pairs each free-text outcome phrase with its MeSH
equivalent, so "patient satisfaction" and "Patient Satisfaction"[Mesh] both appear.
Caveat before reuse, now measured: set 4 on its own retrieves 5,302,230 PubMed
records (docs/validation.md). Bare Understanding, Feasibility, Distress and Social
Support do almost all of that work, so the block adds very little precision - its
value is that it names patient satisfaction explicitly, not that it narrows.
AND-ing an outcome set in also drops trials whose abstracts never name the outcome.
The full four-set strategy returns 846 records.
```

**Search strategy - Embase**

```
Not reported. Only a PubMed/MEDLINE strategy is printed. The review states the search
was supplemented by expert input on relevant publications.
```

**Search strategy - Web of Science**

```
Not reported. See above.
```

## Gomes B, 2013 - Cochrane Database of Systematic Reviews

**Effectiveness and cost-effectiveness of home palliative care services for adults with advanced illness and their caregivers**

- Impact factor: 8.4 (2023 JIF, Cochrane Library)
- URL: <https://doi.org/10.1002/14651858.CD007760.pub2>
- PMID: 23744578 | PMCID: PMC4473359
- Search strategy taken from: Appendices 1-5 of the review, read in full from PMC4473359

**Purpose.** To quantify the effect of home palliative care services on dying at home, and to examine their effect on other patient and caregiver outcomes including symptom control, quality of life, caregiver distress and satisfaction with care, together with resource use, costs and cost-effectiveness. Included as the large-scale contrast: satisfaction with care is named in objective 2, twelve databases were searched, and not one of the strategies contains a satisfaction term.

**PICO**

| | |
|---|---|
| **P** — Population | Adults with advanced illness (the majority of included participants had cancer) and their family caregivers. |
| **I** — Intervention / exposure | Home palliative care services - specialist teams providing palliative care at home. |
| **C** — Comparison | Usual care, or care without a home palliative care service. |
| **O** — Outcome | Dying at home (primary); symptom burden and control; quality of life; caregiver distress and grief; satisfaction with care; resource use, costs and cost-effectiveness. |

**Search strategy - PubMed / MEDLINE**

```
[Not searched as PubMed. MEDLINE via Ovid, 1950 to 21 November 2012; strategies
refined with the Cochrane PaPaS Trials Search Co-ordinator. Appendix 1, verbatim
(population/setting blocks in full; design filter summarised):]
1  exp Palliative Care/
2  exp Terminal Care/
3  exp Terminally Ill/
4  palliat*.mp.
5  (terminal* and (care or caring or ill*)).mp.
6  ((advanced or end stage or terminal*) adj4 (disease* or illness* or cancer*
   or malignan*)).mp.
7  (last year of life or LYOL or life's end or end of life).mp.
8  or/1-7
9  exp Home Care Services/
10 exp Home Care Agencies/
11 exp Mobile Health Units/
12 exp Community Health Nursing/
13 (home adj4 (hospital or palliat*)).mp.
14 ((macmillan or marie curie or district) adj nurs*).mp.
15 ((home or in-home or domicile or outreach or residential or housing or posthospital
   or post-hospital or communit* or mobile or ambulatory or door to door) adj2
   (team* or center* or centre* or treat* or care or interven* or therap* or
   management or model* or program or programs or programme* or service* or base*
   or nurs*)).mp.
16 (homecare or home-care or homebased or home-based).mp.
17 or/9-16
18 hospice*.mp.
19 18 or (8 and 17)
20 (child* or adolescent* or infant* or baby or babies or neonat* or juvenil*
   or pediatric* or paediatric* or young person* or young people or youth*
   or young adult* or matern*).ti.
21 19 not 20
22-33 [randomised and controlled-trial design filter: clinical trial/ or controlled
      clinical trial/ or multicenter study/ or randomized controlled trial/; the same
      as publication types; chi-square distribution/ or chi-square?.ti,ab.;
      "random*".ab,ti.; controlled.ti.; trial.ti.; Control Groups/; (control* adj2
      (clinical or group* or trial* or study or studies or design* or method*)).ti,ab.;
      ((multicent* or multi-cent* or multisite? or multi-site?) adj (study or studies
      or trial*)).ti,ab.; double-blind method/ or single-blind method/;
      ((single or double or triple or treble) adj blind*).ti,ab.]
34-51 [non-randomised design filter: intervention?/pre-post/before-after/
      quasi-experiment* terms, unioned]
52 33 or 41 or 51
53 groups.ab.
54 52 or 53
55 humans.sh.
56 54 and 55
57 56 and 21
Line 19 is the useful pattern: hospice* alone, OR (palliative concept AND home
setting concept) - a "named-entity OR concept-intersection" construction that is
worth borrowing whenever one word reliably identifies the topic.
There is no satisfaction, quality-of-life or symptom term anywhere in the strategy.
[Complete unabbreviated strategy, all databases: strategies/08_gomes2013_home-palliative-care.txt]
```

**Search strategy - Embase**

```
[EMBASE, 1980 to 21 November 2012. Appendix 5, verbatim (population/setting blocks;
design filter from line 25):]
1  exp palliative therapy/
2  exp palliative nursing/
3  exp cancer palliative therapy/
4  exp terminal care/
5  exp terminal disease/
6  exp terminally ill patient/
7  palliat*.mp
8  terminal* and (care or caring or ill*).mp
9  ((advanced or end stage or terminal*) adj4 (disease* or illness* or cancer*
   or malignan*)).mp
10 last year of life or LYOL or or end of life.mp
11 or/1-10
12 exp home care/
13 exp home health agency/
14 exp community care/
15 exp community health nursing/
16 home adj4 (hospital or palliat*).mp
17 (macmillan or marie curie or district) adj nurs*.mp
18 (home or in-home or domicile or outreach or residential or housing or posthospital
   or post-hospital or communit* or mobile or ambulatory or door to door) adj2
   (team* or center* or centre* or treat* or care or interven* or therap* or
   management or model* or program or programs or programme* or service* or base*
   or nurs*).mp
19 homecare or home-care or homebased or home-based.mp
20 or/12-19
21 hospice*.mp
22 21 or (11 and 20)
23 (child* or adolescent* or infant* or baby or babies or neonat* or juvenil*
   or pediatric* or paediatric* or young person* or young people or youth*
   or young adult* or matern*).ti.
24 22 not 23
25 onwards [Embase design filter: clinical trial/ or controlled clinical trial/ or
   multicenter study/ or randomized controlled trial/; chi-square distribution/ or
   chi-square?.ti,ab.; "random*".ab,ti.; controlled.ti.; and the rest as in MEDLINE]
(Line 10 is printed with a duplicated "or".)
[Complete unabbreviated strategy, all databases: strategies/08_gomes2013_home-palliative-care.txt]
```

**Search strategy - Web of Science**

```
Not searched. Twelve databases were searched: CENTRAL (21 November 2012), EMBASE
(1980 to 21 November 2012), MEDLINE (1950 to 21 November 2012), the Cochrane PaPaS
Trials Register and EPOC Trials Register (both 11 May 2010), CINAHL (1981 to
13 April 2010), EURONHEED (1980 to 13 April 2010), PsycINFO (1806 to 13 April 2010),
CDSR, DARE, the HTA Database and NHS EED (all 7 April 2010). Web of Science was not
used.
[The CENTRAL/CDSR/DARE/HTA/NHS EED strategy (Appendix 4) is the same design in
Cochrane Library proximity syntax, and the shortest usable version of the concept is
the PaPaS Trials Register line (Appendix 2), verbatim:
hospice* or ((palliat* or terminal* or "end stage") and (home or community or
outreach or ambulatory))]
[Complete unabbreviated strategy, all databases: strategies/08_gomes2013_home-palliative-care.txt]
```

## Alessy SA, 2022 - eClinicalMedicine

**Factors influencing cancer patients' experiences of care in the USA, United Kingdom and Canada: A systematic review**

- Impact factor: 9.6 (2023 JIF)
- URL: <https://doi.org/10.1016/j.eclinm.2022.101405>
- PMID: 35497061 | PMCID: PMC9046116
- Search strategy taken from: Table 1 (Mesh terms used in PubMed and Web of Science) of the article

**Purpose.** To identify which patient, clinical and health-system factors are consistently associated with cancer patients' reported experiences of care across three national survey programmes in three countries. Included because it publishes a Web of Science strategy alongside its PubMed strategy, and because it shows the instrument-name route into this literature: rather than searching the concept "satisfaction" or "experience", it searches the named survey instruments (CPES, CAHPS/SEER-CAHPS, AOPSS), which is the same trick Mishra 2012 uses for HRQOL in category 6.

**PICO**

| | |
|---|---|
| **P** — Population | Adults with cancer responding to a national patient-experience survey in the USA, United Kingdom or Canada. |
| **I** — Intervention / exposure | Patient, clinical and health-system characteristics (age, sex, ethnicity, socioeconomic position, cancer type and stage, comorbidity, provider and hospital factors). |
| **C** — Comparison | Patients with the contrasting characteristic within the same survey. |
| **O** — Outcome | Reported experience of cancer care, as measured by the National Cancer Patient Experience Survey (CPES), the Consumer Assessment of Healthcare Providers and Systems (CAHPS/SEER-CAHPS) or the Ambulatory Oncology Patient Satisfaction Survey (AOPSS). |

**Search strategy - PubMed / MEDLINE**

```
[PubMed searched, no year restriction, English only; last search 27 February 2022.
Table 1, verbatim - three parallel searches, one per survey instrument:]
1 "CPES" OR "National Cancer Patient Experience Survey"
  OR "Cancer Patient Experience Survey" AND (cancer)
2 "Consumer Assessments of Healthcare Providers and Systems" OR "SEER-CAHPS"
  OR "HCAHPS" AND (Cancer)
3 "Ambulatory Oncology Patient Satisfaction Survey" OR "AOPSS" AND (cancer)
Google Scholar's "with the exact phrase" advanced search was used in addition, plus
reference lists of identified studies and of three earlier reviews.
The unparenthesised OR chain looks like an operator-precedence hazard, but it is
not one in PubMed: running the string as printed and with the OR group explicitly
parenthesised returns the identical translation and the identical 109 records
(see docs/validation.md). PubMed's parser groups the OR chain before applying AND.
The same construction is genuinely unsafe in Ovid and in Web of Science, so
parenthesise if you port it.
```

**Search strategy - Embase**

```
Not searched. Only PubMed, Web of Science and Google Scholar were used.
```

**Search strategy - Web of Science**

```
[Web of Science searched, all years, English. Table 1, verbatim - three parallel
searches, one per survey instrument:]
1 (TI=("CPES") OR TI=("National Cancer Patient Experience Survey")
  OR TI=("Cancer Patient Experience Survey") AND TS=(cancer))
  Databases = WOS, MEDLINE, SCIELO   Timespan = All years   Search language = English
2 AB=("Consumer Assessments of Healthcare Providers and Systems")
  OR AB=("SEER-CAHPS") OR AB=("CAHPS") AND TS=(cancer)
3 AB=("Ambulatory Oncology Patient Satisfaction Survey") OR AB=("AOPSS")
  AND TS=(cancer)
This is the second of only two full Web of Science strategies in the collection (the
other is Osanto 2024, category 6). It illustrates the cross-database search set
feature - Databases = WOS, MEDLINE, SCIELO. Unlike the PubMed version, the
unparenthesised OR chain here is a real hazard: Web of Science does not group it
the way PubMed does, so parenthesise before running.
One caveat about scope: the review explicitly excluded studies that focused on
patient satisfaction, on the grounds that satisfaction and experience are different
constructs, even though one of its three instruments is a satisfaction survey. If
your review needs both, search both vocabularies.
```

