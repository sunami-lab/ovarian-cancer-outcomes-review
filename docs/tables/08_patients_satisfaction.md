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

```
P: Individuals diagnosed with cancer.
I: Survivor or care-provider receipt of a survivorship care plan (SCP).
C: No receipt of an SCP, an alternative method of receiving an SCP, or no comparison
   (for non-randomised studies).
O: Patient-reported health outcomes (e.g. quality of life); health care use; health
   care costs; health outcomes (e.g. quality-adjusted life years); and health care
   experience (e.g. satisfaction with care).
```

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
Caveat before reuse: bare Understanding, Feasibility and Distress will retrieve very
widely, and AND-ing an outcome set into the strategy will drop trials whose abstracts
do not name the outcome.
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

- Impact factor: 8.8 (2023 JIF)
- URL: <https://doi.org/10.1002/14651858.CD007760.pub2>
- PMID: 23744578 | PMCID: PMC4473359
- Search strategy taken from: Appendices 1-5 of the review, read in full from PMC4473359

**Purpose.** To quantify the effect of home palliative care services on dying at home, and to examine their effect on other patient and caregiver outcomes including symptom control, quality of life, caregiver distress and satisfaction with care, together with resource use, costs and cost-effectiveness. Included as the large-scale contrast: satisfaction with care is named in objective 2, twelve databases were searched, and not one of the strategies contains a satisfaction term.

**PICO**

```
P: Adults with advanced illness (the majority of included participants had cancer)
   and their family caregivers.
I: Home palliative care services - specialist teams providing palliative care at home.
C: Usual care, or care without a home palliative care service.
O: Dying at home (primary); symptom burden and control; quality of life; caregiver
   distress and grief; satisfaction with care; resource use, costs and
   cost-effectiveness.
```

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
```

## Shao Q, 2025 - International Journal of Nursing Studies

**Development and application of patient-reported experience measures for cancer patients: a scoping review**

- Impact factor: 7.5 (2023 JIF)
- URL: <https://doi.org/10.1016/j.ijnurstu.2025.105077>
- PMID: 40292184 | PMCID: PMC12033920
- Search strategy taken from: Section 2.2 (Search strategy) of the article; the Web of Science strategy is Figure 1, an image

**Purpose.** To map the development, content and application of patient-reported experience measures (PREMs) for people with cancer, and to define what a PREM is relative to neighbouring constructs. Included for two reasons: it searched Web of Science, and it makes explicit a vocabulary problem that matters for your review - the authors deliberately excluded studies that measured patient satisfaction, quality of care or attitude scales rather than patient experience, treating satisfaction and experience as distinct constructs with distinct literatures.

**PICO**

```
P: Patients with cancer (any type, any stage).
Concept: Patient-reported experience measures - their development, psychometric
   evaluation and domains.
Context: National and international cancer-care initiatives; excluded were studies
   measuring patient satisfaction, quality of care, attitude scales or PROMs rather
   than patient experience, studies tied to one specific treatment, and studies where
   proxies completed the measure.
O: Number and identity of PREMs; definitions; evaluation status; domains of
   application.
```

**Search strategy - PubMed / MEDLINE**

```
[PubMed searched, from database inception to July 2024, using "a combination of
subject terms and free-text words". The Methods give the concept groups verbatim
rather than a line-numbered strategy:]
Group 1 (population): 'cancer, oncology, malignancy, neoplasms'
Group 2 (concept): 'patient experience, patient-reported experience,
                    patient-reported experience measure'
Group 3 (measurement): 'measure, tool, instrument, score, scale, survey,
                    questionnaire, psychometrics'
The paper states that the English terms "reported experience measure" and
"measure, tool, instrument, score, scale, survey, questionnaire, psychometrics" were
the ones applied in PubMed, Web of Science and MEDLINE. Reference lists of all
retrieved articles were checked and Google Scholar was hand-searched.
2216 records were reviewed and 24 included.
Note there is no satisfaction term: satisfaction was an explicit exclusion criterion,
not a search concept.
```

**Search strategy - Embase**

```
Not searched. The three databases searched were PubMed, Web of Science and MEDLINE.
```

**Search strategy - Web of Science**

```
Searched. The Web of Science strategy is reproduced in the paper as Figure 1
("Web of Science search strategies"), which is a bitmap image rather than text, so it
cannot be transcribed verbatim here. What the Methods state in text is that the same
three concept groups above were applied in Web of Science using a combination of
subject terms and free-text words, from database inception to July 2024. Consult
Figure 1 of the published article for the exact string.
```

