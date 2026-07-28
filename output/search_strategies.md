# Search strategies — browsable companion to `search_strategies.xlsx`

Same content as the workbook, generated from the same source (`data/NN_*.yml`) by
`scripts/build.py`, so the two cannot drift apart. Here so you can read the tables on
GitHub without downloading the spreadsheet.

**24 systematic reviews across 8 categories, plus an annex of 10 reviews excluded by the impact-factor rule.**

Each sheet below gives a table of the descriptive columns, then the full verbatim
search strategies in collapsible blocks — click to expand. Where a review did not
search a database, or searched it without publishing the string, the cell says so.

## Contents

- [01. Ovarian cancer treatment (general, not a specific treatment)](#01-ovarian-cancer-treatment-general-not-a-specific-treatment)
- [02. Functional status](#02-functional-status)
- [03. Cognition](#03-cognition)
- [04. Depression](#04-depression)
- [05. Nutritional status](#05-nutritional-status)
- [06. Health-related quality of life (HRQOL)](#06-health-related-quality-of-life-hrqol)
- [07. Patients' symptoms (fatigue, insomnia, pain, anorexia, dyspnea, cognitive problems, anxiety, nausea, depression, sensory neuropathy, constipation, diarrhea)](#07-patients-symptoms-fatigue-insomnia-pain-anorexia-dyspnea-cognitive-problems-anxiety-nausea-depression-sensory-neuropathy-constipation-diarrhea)
- [08. Patients' satisfaction](#08-patients-satisfaction)
- [09. Annex: reviews excluded by the JIF >= 5 rule](#09-annex-reviews-excluded-by-the-jif--5-rule)

---

## 01. Ovarian cancer treatment (general, not a specific treatment)

**Focus.** How do previously published systematic reviews operationalise the concept of "treatment" for ovarian cancer in their database search strategies?

**Population scope applied.** Ovarian cancer was held fixed (it is the object of interest for this category). Reviews restricted to older adults were sought first; none were found in a journal meeting the JIF >= 5 threshold, so the age restriction was dropped and the population was broadened to all adults with ovarian cancer. See docs/methods.md for the searches run.

| Title | 1st author / year | Journal | Impact factor | Purpose of the study | P — Population | I — Intervention / exposure | C — Comparison | O — Outcome | URL |
|---|---|---|---|---|---|---|---|---|---|
| Neoadjuvant chemotherapy before surgery versus surgery followed by chemotherapy for initial treatment in advanced epithelial ovarian cancer | Coleridge SL, 2021 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To assess whether there is an advantage to treating women with advanced epithelial ovarian cancer with chemotherapy before debulking surgery (neoadjuvant chemotherapy, NACT) compared with conventional treatment where chemotherapy follows debulking surgery (primary debulking surgery, PDS). Included as an exemplar because the search builds two separate treatment-modality blocks (chemotherapy AND surgery) and intersects them with the ovarian cancer population block. | Women with advanced (FIGO stage III/IV) epithelial ovarian cancer. | Platinum-based chemotherapy before cytoreductive surgery (neoadjuvant chemotherapy). | Platinum-based chemotherapy following cytoreductive surgery (primary debulking surgery). | Overall survival; progression-free survival; adverse events; quality of life; surgical morbidity/mortality. | https://doi.org/10.1002/14651858.CD005343.pub6 |
| Interventions for the treatment of borderline ovarian tumours | Faluyi O, 2010 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To evaluate the benefits and harms of different interventions (surgery, chemotherapy, radiotherapy, observation) in women with borderline ovarian tumours. Included as an exemplar of the broadest possible treatment concept: the review has no drug- or procedure-named intervention block at all. Instead, treatment is captured through floating subheadings (drug therapy, surgery, therapy, radiotherapy) folded into the study-design block, so that any treatment is retrievable. | Women with borderline (low malignant potential) ovarian tumours. | Any intervention for treatment - surgery (including fertility-sparing and radical), chemotherapy, radiotherapy. | An alternative intervention, or observation/no further treatment. | Overall survival; recurrence/disease-free survival; fertility outcomes; adverse events; quality of life. | https://doi.org/10.1002/14651858.CD007696.pub2 |
| Optimal primary surgical treatment for advanced epithelial ovarian cancer | Elattar A, 2011 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To assess the impact of the extent of primary cytoreductive surgery (residual disease after surgery) on overall and progression-free survival in women with advanced epithelial ovarian cancer. Included as an exemplar of a single-modality treatment block that is deliberately layered: a broad surgery concept (MeSH + truncated free text + the surgery floating subheading) is intersected with a narrow procedure concept (debulk*/cytoreduc*). | Women with advanced (FIGO stage III/IV) epithelial ovarian cancer undergoing primary cytoreductive surgery. | Primary cytoreductive surgery achieving a given level of residual disease (e.g. microscopic / < 1 cm / optimal). | Primary cytoreductive surgery achieving a greater level of residual disease (e.g. suboptimal, > 1 cm). | Overall survival; progression-free survival; adverse events; quality of life. | https://doi.org/10.1002/14651858.CD007565.pub2 |

### Search strategies

<details>
<summary><b>Coleridge SL, 2021</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-3 of the review, read in full from PMC8406953

**PubMed / MEDLINE**

```
[Not searched as PubMed. MEDLINE was searched via Silver Platter/Ovid,
1966 to October week 1 2020; searches run 9 October 2020. Appendix 2, verbatim:]
1  exp Ovarian Neoplasms/
2  (ovar* adj5 (neoplas* or tumor* or tumour* or cancer* or malignan* or carcinoma*)).mp.
3  1 or 2
4  chemotherap*.mp.
5  drug therapy.fs.
6  exp Antineoplastic Agents/
7  Antineoplastic Combined Chemotherapy Protocols/
8  Neoadjuvant Therapy/
9  4 or 5 or 6 or 7 or 8
10 surg*.mp.
11 surgery.fs.
12 exp Surgical Procedures, Operative/
13 10 or 11 or 12
14 3 and 9 and 13
15 randomized controlled trial.pt.
16 controlled clinical trial.pt.
17 randomized.ab.
18 placebo.ab.
19 clinical trials as topic.sh.
20 randomly.ab.
21 trial.ti.
22 15 or 16 or 17 or 18 or 19 or 20 or 21
23 14 and 22
key: mp = title, original title, abstract, name of substance word, subject heading
word, unique identifier; fs = floating subheading; pt = publication type; ab = abstract.
[An earlier Silver Platter search, 1966 to Sept 2006, was reported as:
(ovar*) and (cancer* or carcinoma* or malignan* or neoplas* or tumour* or tumor*)
and (chemotherap*) and (surg*) and (rct or random* or study or studies or trial*
or investigation*) and (advanced or stage III or stage IV)]
```

**Embase**

```
[Embase via Ovid, 1980 to 2020 week 40; searches run 9 October 2020.
Appendix 1, verbatim:]
1  exp ovary tumor/
2  (ovar* adj5 (neoplas* or tumor* or tumour* or cancer* or malignan* or carcinoma*)).mp.
3  1 or 2
4  chemotherap*.mp.
5  dt.fs.
6  exp antineoplastic agent/
7  exp cancer chemotherapy/
8  adjuvant chemotherapy/
9  4 or 5 or 6 or 7 or 8
10 surg*.mp.
11 su.fs.
12 exp surgery/
13 10 or 11 or 12
14 3 and 9 and 13
15 random*.ti,ab.
16 factorial*.ti,ab.
17 (crossover* or cross over* or cross-over*).ti,ab.
18 placebo*.ti,ab.
19 (doubl* adj blind*).ti,ab.
20 (singl* adj blind*).ti,ab.
21 assign*.ti,ab.
22 allocat*.ti,ab.
23 volunteer*.ti,ab.
24 crossover procedure/
25 double blind procedure/
26 randomised controlled trial/
27 single blind procedure/
28 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27
29 14 and 28
[An earlier Embase(R) 1980 to Sept 2006 search was reported as:
(ovar*) and (cancer* or carcinoma* or malignan* or neoplas* or tumour* or tumor*)
and (chemotherap*) and (surg*) and (rct or random* or study or studies or trial*
or investigation*) and (advanced or stage III or stage IV)]
```

**Web of Science**

```
Not searched. Databases searched were CENTRAL (2020, Issue 10), Embase via Ovid,
MEDLINE (Silver Platter/Ovid), PDQ and MetaRegister; reference lists and trial
investigators were also checked. Web of Science was not used.
[For completeness, the CENTRAL strategy (Appendix 3) was:
#1 MeSH descriptor Ovarian Neoplasms explode all trees
#2 ovar* near/5 (neoplas* or tumor* or tumour* or cancer* or malignan* or carcinoma*)
#3 (#1 OR #2)
#4 chemotherap*
#5 Any MeSH descriptor with qualifier: DT
#6 MeSH descriptor Antineoplastic Agents explode all trees
#7 MeSH descriptor Antineoplastic Combined Chemotherapy Protocols explode all trees
#8 MeSH descriptor Neoadjuvant Therapy explode all trees
#9 (#4 OR #5 OR #6 OR #7 OR #8)
#10 surg*
#11 Any MeSH descriptor with qualifier: SU
#12 MeSH descriptor Surgical Procedures, Operative explode all trees
#13 (#10 OR #11 OR #12)
#14 (#3 AND #9 AND #13)]
```

</details>

<details>
<summary><b>Faluyi O, 2010</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-3 of the review, read in full from PMC4164822

**PubMed / MEDLINE**

```
[Not searched as PubMed. MEDLINE via Ovid, 1950 to week 3 2009. Appendix 1, verbatim:]
1  exp Ovarian Neoplasms/
2  (ovar* adj5 (cancer* or neoplas* or carcinom* or malignan* or tumor* or tumour*)).mp.
3  1 or 2
4  (atypical adj proliferative).mp.
5  borderline.mp.
6  micropapillary.mp.
7  (low adj malignan*).mp.
8  (semi adj malignan*).mp.
9  4 or 5 or 6 or 7 or 8
10 3 and 9
11 (ovar* adj5 cystadeno*).mp.
12 10 or 11
13 "randomized controlled trial".pt.
14 "controlled clinical trial".pt.
15 randomized.ab.
16 placebo.ab.
17 "drug therapy".fs.
18 "surgery".fs.
19 "therapy".fs.
20 "radiotherapy".fs.
21 randomly.ab.
22 trial.ab.
23 groups.ab.
24 exp Cohort Studies/
25 cohort*.mp.
26 (case adj series).mp.
27 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26
28 12 and 27
29 Animals/
30 Humans/
31 29 not (29 and 30)
32 28 not 31
key: mp = title, original title, abstract, name of substance word, subject heading
word; ab = abstract; fs = floating subheading.
```

**Embase**

```
[Embase via Ovid, 1980 to 2009 week 2. Appendix 2, verbatim:]
1  Ovary Tumor/
2  (ovar* adj5 (cancer* or neoplas* or carcinom* or malignan* or tumor* or tumour*)).mp.
3  1 or 2
4  (atypical adj proliferative).mp.
5  borderline.mp.
6  micropapillary.mp.
7  (low adj malignan*).mp.
8  (semi adj malignan*).mp.
9  4 or 5 or 6 or 7 or 8
10 3 and 9
11 (ovar* adj5 cystadeno*).mp.
12 10 or 11
13 exp Controlled Clinical Trial/
14 randomized.ab.
15 placebo.ab.
16 dt.fs.
17 su.fs.
18 th.fs.
19 rt.fs.
20 randomly.ab.
21 trial.ab.
22 groups.ab.
23 exp Cohort Analysis/
24 cohort*.mp.
25 (case adj series).mp.
26 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25
27 12 and 26
28 exp Animal/
29 Human/
30 28 not (28 and 29)
31 27 not 30
key: mp = title, abstract, subject headings, heading word, drug trade name, original
title, device manufacturer, drug manufacturer name; fs = floating subheading;
ab = abstract.
Note: the treatment concept is carried entirely by the floating subheadings
dt (drug therapy), su (surgery), th (therapy) and rt (radiotherapy).
```

**Web of Science**

```
Not searched. Databases searched were the Cochrane Gynaecological Cancer Group
Trials Register, CENTRAL, MEDLINE and EMBASE, plus reference lists and trial
registers. Web of Science was not used.
[CENTRAL strategy (Appendix 3), Issue 4 2008:
#1 MeSH descriptor Ovarian Neoplasms explode all trees
#2 ovar* near/5 (cancer* or neoplas* or carcinom* or malignan* or tumor* or tumour*)
#3 (#1 OR #2)
#4 atypical adj proliferative
#5 borderline
#6 micropapillary
#7 low adj malignan*
#8 semi adj malignan*
#9 (#4 OR #5 OR #6 OR #7 OR #8)
#10 (#3 AND #9)
#11 ovar* near/5 cystadeno*
#12 (#10 OR #11)]
```

</details>

<details>
<summary><b>Elattar A, 2011</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-3 of the review, read in full from PMC6457688

**PubMed / MEDLINE**

```
[Not searched as PubMed. MEDLINE via Ovid, 1950 to July week 3 2010
(databases searched to August 2010). Appendix 1, verbatim:]
1  exp Ovarian Neoplasms/
2  (ovar* adj5 cancer*).mp.
3  (ovar* adj5 neoplas*).mp.
4  (ovar* adj5 carcinom*).mp.
5  (ovar* adj5 malignan*).mp.
6  (ovar* adj5 tumor*).mp.
7  (ovar* adj5 tumour*).mp.
8  1 or 2 or 3 or 4 or 5 or 6 or 7
9  exp Surgical Procedures, Operative/
10 surg*.mp.
11 "surgery".fs.
12 9 or 10 or 11
13 debulk*.mp.
14 cytoreduc*.mp.
15 13 or 14
16 8 and 12 and 15
17 "randomized controlled trial".pt.
18 "controlled clinical trial".pt.
19 random*.mp.
20 trial*.mp.
21 group*.mp.
22 exp Cohort Studies/
23 cohort*.mp.
24 series.mp.
25 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24
26 16 and 25
27 Animals/
28 Humans/
29 27 not (27 and 28)
30 26 not 29
key: mp = title, original title, abstract, name of substance word, subject heading
word; fs = floating subheading; pt = publication type.
```

**Embase**

```
[Embase via Ovid, 1980 to week 30 2010. Appendix 2, verbatim:]
1  exp Ovary Tumor/
2  (ovar* adj5 cancer*).mp.
3  (ovar* adj5 neoplas*).mp.
4  (ovar* adj5 carcinom*).mp.
5  (ovar* adj5 malignan*).mp.
6  (ovar* adj5 tumor*).mp.
7  (ovar* adj5 tumour*).mp.
8  1 or 2 or 3 or 4 or 5 or 6 or 7
9  exp Surgery/
10 surg*.mp.
11 su.fs.
12 9 or 10 or 11
13 debulk*.mp.
14 cytoreduc*.mp.
15 13 or 14
16 8 and 12 and 15
17 exp Controlled Clinical Trial/
18 random*.mp.
19 trial*.mp.
20 group*.mp.
21 exp Cohort Analysis/
22 cohort*.mp.
23 series.mp.
24 17 or 18 or 19 or 20 or 21 or 22 or 23
25 16 and 24
key: mp = title, abstract, subject headings, heading word, drug trade name, original
title, device manufacturer, drug manufacturer name; fs = floating subheading.
```

**Web of Science**

```
Not searched. Databases searched were the Cochrane Gynaecological Cancer
Collaborative Review Group Trials Register, CENTRAL (The Cochrane Library 2010,
Issue 3), MEDLINE (to August 2010) and EMBASE (to August 2010). Web of Science
was not used.
[CENTRAL strategy (Appendix 3), Issue 3 2010:
#1 MeSH descriptor Ovarian Neoplasms explode all trees
#2 ovar* near/5 cancer*
#3 ovar* near/5 neoplas*
#4 ovar* near/5 carcinom*
#5 ovar* near/5 malignan*
#6 ovar* near/5 tumor*
#7 ovar* near/5 tumour*
#8 (#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7)
#9 MeSH descriptor Surgical Procedures, Operative explode all trees
#10 surg*
#11 Any MeSH descriptor with qualifier: SU
#12 (#9 OR #10 OR #11)
#13 debulk*
#14 cytoreduc*
#15 (#13 OR #14)
#16 (#8 AND #12 AND #15)]
```

</details>

---

## 02. Functional status

**Focus.** How do previously published systematic reviews of cancer treatment operationalise functional status (functional capacity, physical function, activities of daily living) in their database search strategies?

**Population scope applied.** Cancer type and age left open, per the brief. No systematic review of functional status in ovarian cancer specifically, or in older adults with ovarian cancer, was published in a journal meeting the JIF >= 5 threshold; the closest was Martin 2020 (J Geriatr Oncol, JIF ~3.0, functional recovery after gynaecological cancer surgery). Scheepers 2020 is retained because it is restricted to older adults.

**Note.** Read these three as a spectrum. Neo 2017 is the one to copy: thirteen functional-disability synonyms plus the "Activities of Daily Living" MeSH explosion, with no intervention concept at all. McDonald 2023 is the opposite - physical function is the entire subject of the review and appears nowhere in the search, which is applied at screening instead. Scheepers 2020 is the common middle case: functional status is reached indirectly through "frailty" and "Geriatric Assessment"[Mesh], with no ADL or physical-function term. Not searching the outcome is the dominant pattern across categories 2-8, so Neo is the exception worth learning from rather than the norm.

| Title | 1st author / year | Journal | Impact factor | Purpose of the study | P — Population | I — Intervention / exposure | C — Comparison | O — Outcome | URL |
|---|---|---|---|---|---|---|---|---|---|
| Disability in activities of daily living among adults with cancer: a systematic review and meta-analysis | Neo J, 2017 | Cancer Treatment Reviews | 9.6 (2023 JIF) | To determine the prevalence of disability in activities of daily living among adults with cancer, which ADL items are most often affected, and which instruments are used to measure it. The best functional-status search block available in this impact band: the review has no intervention concept at all, and instead intersects a two-term cancer population with a thirteen-synonym functional-disability block and an observational-design filter. If you take one outcome block for functional status, take this one. | Adults with cancer (any type, any stage, any treatment setting). | Nil - the review deliberately has no intervention concept. | Nil. | Disability in activities of daily living (ADL) and instrumental activities of daily living (IADL) - prevalence, affected items, and measurement instruments. | https://doi.org/10.1016/j.ctrv.2017.10.006 |
| Physical function endpoints in cancer cachexia clinical trials: Systematic Review 1 of the cachexia endpoints series | McDonald J, 2023 | Journal of Cachexia, Sarcopenia and Muscle | 9.4 (2023 JIF) | To assess the frequency and diversity of physical function endpoints used in cancer cachexia clinical trials, and how often they change with intervention. Included as an exemplar of a librarian-built Ovid strategy in which physical function is the whole point of the review yet appears nowhere in the search: retrieval is population (cancer) AND condition (cachexia) AND study design, with physical function applied as an eligibility criterion. | Adults (>= 18 years) with cancer cachexia. | Any cachexia intervention lasting more than 14 days (nutritional, pharmacological, exercise, multimodal), in controlled trials with more than 40 participants. | Control arm as defined by each trial. | Physical function endpoints - handgrip strength, 6-minute walk test, timed up-and-go, physical activity, patient-reported physical function. | https://doi.org/10.1002/jcsm.13321 |
| Geriatric assessment in older patients with a hematologic malignancy: a systematic review | Scheepers ERM, 2020 | Haematologica | 8.2 (2023 JIF) | To summarise what geriatric assessment adds in older patients with a haematologic malignancy - the prevalence of geriatric impairments (including impaired activities of daily living) and their association with treatment decisions, chemotherapy toxicity, healthcare utilisation, physical functioning after treatment, quality of life and mortality. Included as the one review of the three restricted to older adults, and because it shows the common substitute for a functional-status block: retrieval on "frailty OR geriatric assessment", with functional status captured only downstream. | Older patients with a haematologic malignancy (leukaemia, lymphoma, multiple myeloma, myelodysplastic syndrome, myeloproliferative neoplasms). | Geriatric assessment (any validated multidomain instrument), applied before or during antineoplastic treatment. | No geriatric assessment, or patients without the impairment identified. | Prevalence of geriatric impairments; treatment decision-making; chemotherapy toxicity; healthcare utilisation; physical functioning after treatment; quality of life; mortality. | https://doi.org/10.3324/haematol.2019.245803 |

### Search strategies

<details>
<summary><b>Neo J, 2017</b> — Cancer Treatment Reviews</summary>

Taken from: Online supplement Appendix 1 (Search terms used in review; example MEDLINE strategy), obtained from the King's College London institutional repository copy (gold OA, CC BY-NC-ND) identified via Unpaywall

**PubMed / MEDLINE**

```
[Not searched as PubMed. MEDLINE(R) via Ovid, 1946 to June 2016; search alerts run to
November 2016. Online supplement, Appendix 1, verbatim - the review labels this the
"example search strategy", adapted for the other 11 databases:]
1  Cancer*.mp.
2  exp Carcinoma/
3  Carcinoma*.mp.
4  1 or 2 or 3
5  Function* disabilit*.mp.
6  Function* outcome*.mp.
7  Function* impairment*.mp.
8  Function* status.mp.
9  Function* performance.mp.
10 Function* limitation*.mp.
11 exp "Activities of Daily Living"/
12 ADL.mp.
13 (Activit* adj2 daily living).mp.
14 (Instrumental Activit* adj2 daily living).mp.
15 IADL.mp.
16 Activit* limitation*.mp.
17 Participation restriction*.mp.
18 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17
19 Epidemiologic studies/
20 exp case control studies/
21 exp cohort studies/
22 Case control.tw.
23 (Cohort adj (study or studies)).tw.
24 Cohort analy$.tw.
25 (Follow up adj (study or studies)).tw.
26 (Observational adj (study or studies)).tw.
27 Longitudinal.tw.
28 Retrospective.tw.
29 Cross sectional.tw.
30 Cross-sectional studies/
31 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30
32 4 and 18 and 31
33 Limit 32 to (English language and humans and "all adult (19 plus years)")
key: adj = adjacent; exp = explode; mp = title, original title, abstract, subject
heading, name of substance, and registry word; tw = text word.
The supplement also gives the concept table the strategy was built from - Population:
cancer, carcinoma. Intervention: nil. Comparison: nil. Outcome: functional
disability, functional disabilities, functional outcome, functional impairment,
functional limitation, functional status, functional performance, activities of daily
living, ADL, instrumental activities of daily living, IADL, activity limitation,
participation restriction. Study type: observational/epidemiologic/case-control/
cohort/cohort analysis/longitudinal/retrospective/cross-sectional/follow-up/
prospective/correlational studies.
```

**Embase**

```
Searched, but no Embase-specific string was published. The Methods state that the
strategy "was developed for MEDLINE and adapted where necessary for all other
databases", and only the MEDLINE example is reproduced (Appendix 1). Twelve
databases were searched from inception to June 2016: MEDLINE, EMBASE, CINAHL, ASSIA,
PsycINFO, Social Policy and Practice, IBSS, ScienceDirect, Social Service Abstracts,
Sociological Abstracts, Scopus and Web of Science Core Collection.
```

**Web of Science**

```
Searched (Web of Science Core Collection, and Web of Science Conference Proceedings
for grey literature), but no Web of Science-specific string was published - only the
MEDLINE example strategy, adapted. Grey literature was additionally searched in
OpenGrey, ProQuest Dissertations & Theses, Scopus Conference Proceedings, HMIC and
Global Health. No date restriction; limited to human studies published in English.
This is one of only four reviews in the collection that searched Web of Science, and
one of two that searched it without publishing the string.
```

</details>

<details>
<summary><b>McDonald J, 2023</b> — Journal of Cachexia, Sarcopenia and Muscle</summary>

Taken from: Supporting Information Appendix S1 (Documentation of literature search)

**PubMed / MEDLINE**

```
[Not searched as PubMed. Ovid MEDLINE(R) ALL 1946 to 1 July 2021; search run
2 June 2021 by a research librarian, University of Oslo. Appendix S1, verbatim:]
1  exp Neoplasms/ or (neoplasm* or cancer* or tumor* or tumour* or oncol* or malign*
   or carcinom* or adenocarcinom* or adenoma or metasta*).ti,ab,kf.
2  Cachexia/ or Emaciation/ or Malnutrition/ or Starvation/ or Wasting syndrome/
   or Thinness/ or Sarcopenia/ or Anorexia/ or *Weight Loss/
3  and/1-2
4  ((cachexia or cachexic or anorexia or anorectic or emaciat* or malnutrition or
   underweight or starvation* or thiness or leanness or sarcopenia or wasting syndrome*
   or wasting disease* or weightloss* or ((appetite* or weight) adj2 (loss or loosing
   or losing))) adj4 (neoplasm* or cancer* or tumor* or tumour* or oncol* or malign*
   or carcinom* or adenocarcinom* or adenoma or metasta*)).ti,ab,kf.
5  ((cachexia or cachexic or anorexia or ... [same term list as line 4] ...) and
   (neoplasm* or cancer* or tumor* or tumour* or oncol* or malign* or carcinom*
   or adenocarcinom* or adenoma or metasta*)).ti.
6  or/3-5
7  randomized controlled trial.pt.
8  controlled clinical trial.pt.
9  randomized.ab.
10 placebo.ab.
11 drug therapy.fs.
12 randomly.ab.
13 trial.ab.
14 groups.ab.
15 or/7-14
16 exp animals/ not humans.sh.
17 15 not 16
18 6 and 17
19 limit 18 to yr="1990 -Current"
20 cohort studies/ or follow-up studies/ or longitudinal studies/ or "national
   longitudinal study of adolescent health"/ or prospective studies/
   or retrospective studies/
21 (cohort* or longitudinal or prospective* or retrospective*).tw.
22 or/20-21
23 and/6,22
24 limit 23 to yr="1990 -Current"
25 24 not 19
26 19 or 24
Note: no physical-function terms appear in the strategy.
[Complete unabbreviated strategy, all databases: strategies/02_mcdonald2023_cachexia-physical-function.txt]
```

**Embase**

```
[Embase Classic+Embase 1947 to 1 July 2021 via Ovid; run 2 June 2021.
Appendix S1, verbatim (population/condition block; the design block is a long
standard Embase RCT/observational filter, lines 7-45):]
1  exp neoplasm/ or (neoplasm* or cancer* or tumor* or tumour* or oncol* or malign*
   or carcinom* or adenocarcinom* or adenoma or metasta*).ti,ab,kw.
2  cachexia/ or emaciation/ or *malnutrition/ or starvation/ or wasting syndrome/
   or *anorexia/ or sarcopenia/ or *weight loss/
3  and/1-2
4  ((cachexia or cachexic or anorexia or anorectic or emaciat* or malnutrition or
   underweight or starvation* or thiness or leanness or sarcopenia or wasting syndrome*
   or wasting disease* or weightloss* or ((appetite* or weight) adj2 (loss or loosing
   or losing))) adj3 (neoplasm* or cancer* or tumor* or tumour* or oncol* or malign*
   or carcinom* or adenocarcinom* or adenoma or metasta*)).ti,ab,kw.
5  ((cachexia or cachexic or anorexia or ... [same term list] ...) and (neoplasm*
   or cancer* or tumor* or tumour* or oncol* or malign* or carcinom* or adenocarcinom*
   or adenoma or metasta*)).ti.
6  or/3-5
7-25   [Embase RCT filter: Randomized controlled trial/; Controlled clinical trial/;
       random$.ti,ab.; randomization/; intermethod comparison/; placebo.ti,ab.;
       (compare or compared or comparison).ti.; ((evaluated or evaluate or evaluating
       or assessed or assess) and (compare or compared or comparing or comparison)).ab.;
       (open adj label).ti,ab.; ((double or single or doubly or singly) adj (blind or
       blinded or blindly)).ti,ab.; double blind procedure/; parallel group$1.ti,ab.;
       (crossover or cross over).ti,ab.; ((assign$ or match or matched or allocation)
       adj5 (alternate or group$1 or intervention$1 or patient$1 or subject$1 or
       participant$1)).ti,ab.; (assigned or allocated).ti,ab.; (controlled adj7 (study
       or design or trial)).ti,ab.; (volunteer or volunteers).ti,ab.; human experiment/;
       trial.ti.]
26 or/7-25
27-39  [exclusion filter for non-trial designs and animal studies]
40 or/27-39
41 26 not 40
42 and/6,41
43 limit 42 to yr="1990 -Current"
44 limit 43 to conference abstracts
45 43 not 44
46 cohort analysis/ or follow up/ or longitudinal study/ or "national longitudinal
   study of adolescent health"/ or prospective study/ or retrospective study/
47 ((cohort adj (study or studies)) or cohort analy* or longitudinal).tw.
48 or/46-47
49 and/6,48
50 limit 49 to yr="1990 -Current"
51 limit 50 to conference abstracts
52 50 not 51
53 52 not 45
[Complete unabbreviated strategy, all databases: strategies/02_mcdonald2023_cachexia-physical-function.txt]
```

**Web of Science**

```
Not searched. Databases searched were MEDLINE (Ovid), Embase (Ovid) and the Cochrane
Central Register of Controlled Trials, 1990 to 2 June 2021. Web of Science was not used.
[CENTRAL strategy, verbatim:
#1 [mh Neoplasms]
#2 ((neoplasm* or cancer* or tumor* or tumour* or oncol* or malign* or carcinom*
   or adenocarcinom* or adenoma or metasta*)):ti,ab,kw
#3 #1 or #2
#4 [mh Cachexia] or [mh ^Emaciation] or [mh ^Malnutrition] or [mh Starvation]
   or [mh ^"Wasting syndrome"] or [mh Thinness] or [mh Sarcopenia] or [mh Anorexia]
#5 MeSH descriptor: [Weight Loss] this term only
#6 #3 and (#4 or #5)
#7 (((cachexia or cachexic or anorexia or anorectic or emaciat* or malnutrition or
   underweight or starvation* or thiness or leanness or sarcopenia or "wasting syndrome"
   or "wasting syndromes" or "wasting disease" or "wasting diseases" or weightloss*
   or ((appetite* or weight) near/2 (loss or loosing or losing))) near/3 (neoplasm*
   or cancer* or tumor* or tumour* or oncol* or malign* or carcinom* or adenocarcinom*
   or adenoma or metasta*))):ti,ab,kw
#8 [same term list combined with AND rather than near/3]:ti
#9 #6 or #7 or #8 with Publication Year from 1990 to 2021, in Trials]
[Complete unabbreviated strategy, all databases: strategies/02_mcdonald2023_cachexia-physical-function.txt]
```

</details>

<details>
<summary><b>Scheepers ERM, 2020</b> — Haematologica</summary>

Taken from: Methods section of the article (single search string), read from PMC7271571

**PubMed / MEDLINE**

```
[MEDLINE, searched 4 March 2019 and updated 20 January 2020; results limited to
studies published after 1 January 2013. Reported in native PubMed syntax as a single
string in the Methods, verbatim:]
((("Hematologic Neoplasms"[Mesh] OR "Leukemia"[Mesh] OR "Lymphoma"[Mesh]
OR "Multiple Myeloma"[Mesh] OR "Myelodysplastic Syndromes"[Mesh] OR leukemia[tiab]
OR leukaemia[tiab] OR lymphoma*[tiab] OR hodgkin*[tiab] OR non-hodgkin*[tiab]
OR (multiple myeloma[tiab]) OR myelodysplas*[tiab] OR (haematolog* AND malignan*[tiab])
OR (hematolog* AND malignan*[tiab]) OR (myeloid[tiab] OR lymphoid[tiab]
AND neoplas*[tiab]) OR myeloproliferative[tiab] OR (plasma cell neoplas*[tiab])
OR plasma cell dyscrasia*[tiab] OR (myeloid[tiab] AND sarcoma*[tiab])
OR waldenstrom[tiab] OR myelofibrosis[tiab] OR mastocystosis[tiab]
OR (polycyth* AND vera[tiab]) OR (essential AND thrombocyt*[tiab])))
AND (("frailty"[All Fields] OR "Geriatric Assessment"[Mesh] OR frail*[tiab]
OR vulnerabl*[tiab] OR geriatric assessment*[tiab] OR geriatric*[tiab]))
No age or language limitations were applied.
Note: functional status enters only through "Geriatric Assessment"[Mesh] and
frail*/vulnerabl*; there are no ADL, IADL or physical-function terms.
```

**Embase**

```
Searched, but no separate Embase string was published. The Methods state that "the
following search was performed ... in both MEDLINE and EMBASE" and then give one
strategy in PubMed syntax; the Emtree translation is not reported. Yield is reported
by database (832 citations from MEDLINE, 3797 from EMBASE, 4629 total).
```

**Web of Science**

```
Not searched. Databases searched were MEDLINE and EMBASE only, supplemented by
cross-referencing the reference lists of included studies and by carrying forward
eligible studies from the earlier 2013 review by Hamaker et al.
```

</details>

---

## 03. Cognition

**Focus.** How do previously published systematic reviews of cancer treatment build the cognition concept in their database search strategies?

**Population scope applied.** Cancer type and age left open, per the brief. No systematic review of cognition in ovarian cancer, or in older adults with ovarian cancer, was published in a journal meeting the JIF >= 5 threshold.

**Note.** Cognition is one of the few outcomes that reviews reliably do search on, because cancer-related cognitive impairment is usually the topic of the review rather than a downstream outcome. The three reviews here show three different structures for the same concept: a full stand-alone cognition block (Treanor), cognition folded into a late-/adverse-effects adjacency block (Lawrie), and unstructured keyword pairings (Jim).

| Title | 1st author / year | Journal | Impact factor | Purpose of the study | P — Population | I — Intervention / exposure | C — Comparison | O — Outcome | URL |
|---|---|---|---|---|---|---|---|---|---|
| Non-pharmacological interventions for cognitive impairment due to systemic cancer treatment | Treanor CJ, 2016 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To evaluate the cognitive effects, non-cognitive effects, duration and safety of non-pharmacological interventions aimed at maintaining cognitive function or ameliorating cognitive impairment resulting from cancer or systemic cancer treatment. The most complete cognition search block found in this exercise: one core adjacency statement generates the cross-product of nine cognition terms and ten impairment terms, sitting alongside five controlled-vocabulary terms and a chemo-fog/chemo-brain phrase. Reproduced in six database syntaxes, including a native PubMed version. | Adults with cancer receiving or having received systemic cancer treatment (chemotherapy or hormonal therapy, alone or with other treatments). | Non-pharmacological interventions targeting cognitive function (compensatory strategy training, cognitive rehabilitation/training, exercise, mind-body). | Wait-list, usual care, attention control or an alternative non-pharmacological intervention. | Objective and subjective cognitive function; non-cognitive effects (quality of life, physical and psychological well-being, fatigue, mood); duration of effect; adverse events. | https://doi.org/10.1002/14651858.CD011325.pub2 |
| Long-term neurocognitive and other side effects of radiotherapy, with or without chemotherapy, for glioma | Lawrie TA, 2019 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To evaluate the long-term (at least two years after diagnosis) neurocognitive and other side effects of radiotherapy, with or without chemotherapy, in people with glioma, and to write a brief economic commentary. Included as an exemplar of the alternative structure: rather than a stand-alone cognition block, cognit* is one term inside a generic late-effects adjacency, so cognition is retrieved as a species of treatment harm. | People with glioma (any grade), followed at least two years from diagnosis. | Radiotherapy, with or without chemotherapy. | No radiotherapy, or a different type/dose/schedule of radiotherapy. | Long-term neurocognitive function (primary); other late side effects; quality of life; survival; costs (brief economic commentary). | https://doi.org/10.1002/14651858.CD013047.pub2 |
| Meta-analysis of cognitive functioning in breast cancer survivors previously treated with standard-dose chemotherapy | Jim HSL, 2012 | Journal of Clinical Oncology | 42.1 (2023 JIF) | To quantify cognitive deficits in breast cancer survivors at least six months after completing standard-dose chemotherapy, and to examine demographic and clinical moderators (age, education, time since chemotherapy, endocrine therapy). Included deliberately as the counter-example: a meta-analysis in the highest-impact journal in this collection, whose entire search is seven short keyword pairings with no structured concept blocks, no truncation discipline and no design filter. | Women who had completed standard-dose chemotherapy for breast cancer at least six months previously. | Standard-dose chemotherapy (past exposure). | Healthy controls, patients not treated with chemotherapy, or the patient's own pre-treatment/normative scores. | Objective neuropsychological test performance across cognitive domains (verbal ability, memory, executive function, processing speed, attention, visuospatial). | https://doi.org/10.1200/JCO.2011.39.5640 |

### Search strategies

<details>
<summary><b>Treanor CJ, 2016</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-6 of the review, read in full from PMC8734151

**PubMed / MEDLINE**

```
[PubMed searched natively (via NCBI); 1980 to 29 September 2015. Appendix 6, verbatim:]
#1  neoplasm*[MeSH Terms]
#2  (cancer* or neoplas* or tumor* or tumour* or carcinoma* or adenocarcinoma*
    or malignan* or leukemia* or leukaemia*)
#3  #1 or #2
#4  cognition disorders[MeSH Terms]
#5  neurobehavioral manifestations[MeSH Terms]
#6  mental processes[MeSH Terms]
#7  neuropsychological tests[MeSH Terms]
#8  attention[MeSH Terms]
#9  "chemo* fog"
#10 "chemo* brain"
#11 (("cognit* deficit*") OR "cognit* declin*" OR "cognit* disorder*"
    OR "cognit* function*" OR "cognit* dysfunction*" OR "cognit* impair*"
    OR "cognit* decrement*" OR "cognit* problem*" OR "cognit* sequelae*")
#12 (("memory deficit*") OR "memory declin*" OR "memory disorder*"
    OR "memory function*" OR "memory dysfunction*" OR "memory impair*"
    OR "memory decrement*" OR "memory problem*" OR "memory sequelae*")
#13 [same nine-suffix pattern applied to neurobehavior*]
#14 [same nine-suffix pattern applied to neurobehaviour*]
#15 [same nine-suffix pattern applied to "problem solving"]
#16 [same nine-suffix pattern applied to attention]
#17 [same nine-suffix pattern applied to concentrat*]
#18 #4 or #5 or #6 or #7 or #8 or #9 or #10 or #11 or #12 or #13 or #14 or #15
    or #16 or #17
#19 #3 and #17
#20 randomized controlled trial[pt]
#21 controlled clinical trial[pt]
#22 randomized[tiab]
#23 placebo[tiab]
#24 clinical trials as topic[mesh:noexp]
#25 randomly[tiab]
#26 #20 or #21 or #22 or #23 or #24
#27 animals [mh] NOT humans [mh]
#28 #26 NOT #27
#29 #19 AND #28
Note as printed: line #19 combines #3 with #17 (concentrat* only) rather than with the
full #18 union, and line #26 omits #25 - both appear to be typographical slips in the
published appendix. Reproduce with care.
[The Ovid MEDLINE version, Appendix 2, is the cleaner statement of the same concept:
1  exp Neoplasms/
2  (cancer* or neoplas* or tumor* or tumour* or carcinoma* or adenocarcinoma*
   or malignan* or leukemia* or leukaemia*).mp
3  1 or 2
4  exp Cognition Disorders/
5  exp Neurobehavioral Manifestations/
6  exp Mental Processes/
7  exp Neuropsychological Tests/
8  Attention/
9  (chemo* adj5 (fog or brain)).mp.
10 ((cognit* or neurocognit* or neuropsycholog* or memory or neurobehavior*
   or neurobehaviour* or problem solving or attention or concentrat*) adj5
   (deficit* or declin* or disorder* or function* or dysfunction* or impair*
   or decrement* or disturb* or problem* or sequelae*)).mp.
11 4 or 5 or 6 or 7 or 8 or 9 or 10
12 3 and 11
13 randomized controlled trial.pt.
14 controlled clinical trial.pt.
15 randomized.ab.
16 placebo.ab.
17 clinical trials as topic.sh.
18 randomly.ab.
19 trial.ti.
20 13 or 14 or 15 or 16 or 17 or 18 or 19
21 12 and 20
22 exp animals/ not humans.sh.
23 21 not 22]
```

**Embase**

```
[Embase via OvidSP, 1980 to 29 September 2015. Appendix 3, verbatim:]
1  exp neoplasm/
2  (cancer* or neoplas* or tumor* or tumour* or carcinoma* or adenocarcinoma*
   or malignan* or leukemia* or leukaemia*).mp.
3  1 or 2
4  exp cognitive defect/
5  cognition/
6  neuropsychological test/
7  attention/
8  (chemo* adj5 (fog or brain)).mp.
9  ((cognit* or neurocognit* or neuropsycholog* or memory or neurobehavior*
   or neurobehaviour* or problem solving or attention or concentrat*) adj5
   (deficit* or declin* or disorder* or function* or dysfunction* or impair*
   or decrement* or disturb* or problem* or sequelae*)).mp.
10 4 or 5 or 6 or 7 or 8 or 9
11 3 and 10
12 crossover procedure/
13 double-blind procedure/
14 randomized controlled trial/
15 single-blind procedure/
16 random*.mp.
17 factorial*.mp.
18 (crossover* or cross over* or cross-over*).mp.
19 placebo*.mp.
20 (double* adj blind*).mp.
21 (singl* adj blind*).mp.
22 assign*.mp.
23 allocat*.mp.
24 volunteer*.mp.
25 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24
26 11 and 25
key: mp = title, abstract, subject headings, heading word, drug trade name, original
title, device manufacturer, drug manufacturer, device trade name, keyword.
```

**Web of Science**

```
Not searched. Databases searched were CENTRAL, MEDLINE (OvidSP), Embase (OvidSP),
PsycINFO (OvidSP), CINAHL (EBSCO) and PubMed, 1980 to 29 September 2015, plus trial
registries and grey literature (theses, dissertations, conference proceedings).
Web of Science was not used.
[The CINAHL version (Appendix 5, EBSCOhost syntax) is the closest analogue to a
Web of Science-style proximity search and may be the most useful template if you
do add Web of Science:
S13 (MH "Cognition Disorders+") S14 (MH "Neurobehavioral Manifestations+")
S15 (MH "Mental Processes+") S16 (MH "Neuropsychological Tests+") S17 (MH "Attention+")
S18 "chemo*" S19 "fog" S20 "brain" S21 (S19 or S20) S22 (S18 N2 S21)
S23 "cognit*" S24 "neurocognit*" S25 "neuropsycholog*" S26 "memory"
S27 "neurobehavior*" S28 "neurobehaviour*" S29 "problem solving" S30 "attention"
S31 "concentrat*" S32 (S23 or S24 or S25 or S26 or S27 or S28 or S29 or S30)
S33 "deficit*" S34 "declin*" S35 "disorder*" S36 "function*" S37 "dysfunction*"
S38 "impair*" S39 "decrement*" S40 "disturb*" S41 "problem*" S42 "sequelae*"
S43 (S33 or S34 or ... or S42) S44 (S32 N2 S43)
S45 (S13 or S14 or S15 or S16 or S17 or S22 or S44) S46 (S12 and S45)
S47 MH "Randomized controlled trials" S48 MH "Clinical trials" S49 MH "Placebos"
S50 (S47 or S48 or S49) S51 (S44 and S50)]
```

</details>

<details>
<summary><b>Lawrie TA, 2019</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendix 1 of the review, read in full from PMC6699681

**PubMed / MEDLINE**

```
[Not searched as PubMed. MEDLINE via Ovid, 1946 to October week 5 2018; searched
16 February 2018 and updated 14 November 2018. Appendix 1, verbatim:]
1  exp Glioma/
2  (glioma* or astrocytoma* or medulloblastoma* or ependymoma* or craniophyrangioma*
   or oligodendroglioma* or glioblastoma* or GBM*).ti,ab.
3  1 or 2
4  exp Radiotherapy/
5  radiotherapy.fs.
6  (radiotherap* or radiat* or irradiat*).ti,ab.
7  exp Antineoplastic Agents/
8  Antineoplastic Combined Chemotherapy Protocols/
9  chemotherap*.mp.
10 exp Chemoradiotherapy/
11 (radiochemo* or chemoradio*).mp.
12 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11
13 3 and 12
14 Radiation Effects/
15 exp Radiation Injuries/
16 adverse effects.fs.
17 ((late or adverse* or long term or side or long-term or chronic* or residual*
   or delay* or undesirable or unexpected) adj5 (effect* or event* or outcome*
   or reaction* or complication* or harm* or injur* or toxic* or cognit*)).ti,ab.
18 (adrs or tolerab*).ti,ab.
19 (radiation induced* or radiation-induced).ti,ab.
20 14 or 15 or 16 or 17 or 18 or 19
21 randomized controlled trial.pt.
22 controlled clinical trial.pt.
23 randomized.ab.
24 placebo.ab.
25 clinical trials as topic.sh.
26 randomly.ab.
27 trial.ti.
28 exp Cohort Studies/
29 cohort*.tw.
30 longitudinal*.tw.
31 prospective*.tw.
32 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30 or 31
33 13 and 20 and 32
34 exp animals/ not humans.sh.
35 33 not 34
key: mp = title, abstract, original title, name of substance word, subject heading
word, keyword heading word, protocol supplementary concept word, rare disease
supplementary concept word, unique identifier; ab = abstract; sh = subject heading;
ti = title; pt = publication type.
[A parallel MEDLINE run replaced the design filter (lines 21-32) with a health-economics
filter for the economic commentary.]
```

**Embase**

```
[Embase via Ovid, 1980 to 2018 week 46. Appendix 1, verbatim:]
1  exp Glioma/
2  (glioma* or astrocytoma* or medulloblastoma* or ependymoma* or craniophyrangioma*
   or oligodendroglioma* or glioblastoma* or GBM*).ti,ab.
3  1 or 2
4  exp radiotherapy/
5  radiotherapy.fs.
6  (radiotherap* or radiat* or irradiat*).ti,ab.
7  exp chemotherapy/
8  exp antineoplastic agent/
9  chemotherap*.mp.
10 exp chemoradiotherapy/
11 (radiochemo* or chemoradio*).mp.
12 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11
13 3 and 12
14 radiation response/
15 exp radiation injury/
16 ae.fs.
17 ((late or adverse* or long term or side or long-term or chronic* or residual*
   or delay* or undesirable or unexpected) adj5 (effect* or event* or outcome*
   or reaction* or complication* or harm* or injur* or toxic* or cognit*)).ti,ab.
18 (adrs or tolerab*).ti,ab.
19 (radiation induced* or radiation-induced).ti,ab.
20 14 or 15 or 16 or 17 or 18 or 19
21 crossover procedure/
22 randomized controlled trial/
23 single blind procedure/
24 random*.mp.
25 factorial*.mp.
26 (crossover* or cross over* or cross-over).mp.
27 placebo*.mp.
28 (doubl* adj blind*).mp.
29 (singl* adj blind*).mp.
30 assign*.mp.
31 allocat*.mp.
32 volunteer*.mp.
33 exp cohort analysis/
34 cohort*.tw.
35 longitudinal*.tw.
36 prospective*.tw.
37 21 or 22 or ... or 36
38 13 and 20 and 37
[A parallel Embase run substituted a health-economics filter for lines 21-37.]
```

**Web of Science**

```
Not searched. Databases searched were CENTRAL (2018, Issue 11), MEDLINE via Ovid and
Embase via Ovid, plus ClinicalTrials.gov and the WHO ICTRP for ongoing trials.
No language restrictions. Web of Science was not used.
[CENTRAL strategy, verbatim:
#1 MeSH descriptor: [Glioma] explode all trees
#2 glioma* or astrocytoma* or medulloblastoma* or ependymoma* or craniophyrangioma*
   or oligodendroglioma* or glioblastoma* or GBM*
#3 #1 or #2
#4 MeSH descriptor: [Radiotherapy] explode all trees
#5 radiotherap* or radiat* or irradiat*
#6 MeSH descriptor: [Antineoplastic Agents] explode all trees
#7 MeSH descriptor: [Antineoplastic Combined Chemotherapy Protocols] this term only
#8 Any MeSH descriptor with qualifier(s): [Radiotherapy - RT]
#9 Any MeSH descriptor with qualifier(s): [Drug therapy - DT]
#10 Chemotherap*
#11 MeSH descriptor: [Chemoradiotherapy] explode all trees
#12 radiochemo* or chemoradio*
#13 #4 or #5 or #6 or #7 or #8 or #9 or #10 or #11 or #12
#14 #3 AND #13
#15 MeSH descriptor: [Radiation Effects] this term only
#16 MeSH descriptor: [Radiation Injuries] explode all trees
#17 Any MeSH descriptor with qualifier(s): [Adverse effects - AE]
#18 ((late or adverse* or long term or side or long-term or chronic* or residual*
    or delay* or undesirable or unexpected) near/5 (effect* or event* or outcome*
    or reaction* or complication* or harm* or injur* or toxic* or cognit*))
#19 adrs or tolerab*
#20 radiation induced* or radiation-induced
#21 #15 or #16 or #17 or #18 or #19 or #20
#22 #14 AND #21]
```

</details>

<details>
<summary><b>Jim HSL, 2012</b> — Journal of Clinical Oncology</summary>

Taken from: Methods section (Search Strategy), read from PMC3462044

**PubMed / MEDLINE**

```
[PubMed searched natively; studies published 1937 to June 2011; English only.
Seven search-term sets, verbatim from the Methods:]
(1) cognitive effects AND cancer patients AND chemotherapy
(2) cognition AND cancer AND chemotherapy
(3) cognition disorders/chemically induced AND cancer AND chemotherapy
(4) [cognition disorders/chemically induced OR cognition disorders]
    AND [neoplasms/drug therapy OR neoplasms/radiotherapy OR neoplasms]
(5) [cognition disorders or cognition or cognitive effects and cancer] AND chemotherapy
(6) chemobrain AND cancer
(7) cognitive impairment AND breast cancer
Reference lists of retrieved publications and of relevant earlier systematic reviews
and meta-analyses were also examined.
Note: no field tags, no explicit MeSH explosion and no truncation are given, so these
strings are not reproducible in the sense PRISMA-S requires. They are recorded here
exactly as published.
```

**Embase**

```
Not searched. Databases searched were PubMed, PsycINFO, CINAHL and the Cochrane
Library.
[The terms used for PsycINFO, CINAHL and the Cochrane Library, verbatim:
(1) cognitive disorders AND chemotherapy AND cancer
(2) cognition AND chemotherapy AND cancer
(3) chemobrain OR chemobrain OR chemo-brain
(4) cognitive effects and chemotherapy and cancer
Set (3) is printed with "chemobrain" twice; presumably one instance was intended to be
a different spelling variant.]
```

**Web of Science**

```
Not searched. Databases searched were PubMed, PsycINFO, CINAHL and the Cochrane
Library only.
```

</details>

---

## 04. Depression

**Focus.** How do previously published systematic reviews of cancer treatment build the depression concept in their database search strategies?

**Population scope applied.** Cancer type left open, per the brief. Two of the three reviews are restricted to older adults with cancer or use age as an explicit search block, so the age dimension is covered here. The one ovarian-specific option identified (Watts 2015, "Depression and anxiety in ovarian cancer: a systematic review and meta-analysis of prevalence rates", BMJ Open) was excluded on the JIF >= 5 threshold (BMJ Open JIF ~2.4) - it is worth reading anyway if you want an ovarian-specific comparator.

**Note.** Depression is searched on, and searched on well, in all three reviews - unlike functional status. Compare the three depression blocks directly: Soong's is four words long, Vita's is four controlled-vocabulary terms plus one adjacency, and Kulchycki's spans eight controlled-vocabulary terms plus a 20-term text-word line that deliberately reaches into mood, distress, hopelessness and wellbeing. Sensitivity differs by roughly an order of magnitude.

| Title | 1st author / year | Journal | Impact factor | Purpose of the study | P — Population | I — Intervention / exposure | C — Comparison | O — Outcome | URL |
|---|---|---|---|---|---|---|---|---|---|
| Exercise Interventions for Depression, Anxiety, and Quality of Life in Older Adults With Cancer: A Systematic Review and Meta-Analysis | Soong RY, 2025 | JAMA Network Open | 10.5 (2023 JIF) | To determine whether exercise interventions are associated with improvements in psychological outcomes - depression, anxiety and health-related quality of life - among older adults with cancer. The closest match in this whole collection to the population of interest (older adults with cancer, patient-centred outcomes), and the only review here whose search carries an explicit older-adults block. The trade-off is sensitivity: the outcome block is four terms with no controlled vocabulary in PubMed. | Older adults with cancer (mean age >= 60 years), any cancer type, any comorbidity. | Exercise interventions - aerobic, resistance and strength training, or mind-body exercise (qigong, yoga, tai chi). | Usual care. | Depression severity; anxiety severity; health-related quality of life (HRQOL). | https://doi.org/10.1001/jamanetworkopen.2024.57859 |
| Antidepressants for the treatment of depression in people with cancer | Vita G, 2023 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To evaluate the efficacy, tolerability and acceptability of antidepressants for treating depressive symptoms in adults (18 years or older) with cancer of any site and stage. Included as the reference-standard structure for this outcome: population AND depression AND antidepressant, where the depression block pairs three MeSH terms with one adjacency that catches adjustment, reactive and dysthymic disorders, and the drug block names roughly 70 individual agents alongside five exploded drug classes. | Adults (>= 18 years) with any primary cancer diagnosis and depression (major depressive disorder, adjustment disorder, dysthymic disorder, or depressive symptoms measured on a validated scale). | Any antidepressant. | Placebo, or another antidepressant. | Efficacy (change in depressive symptoms, response, remission); tolerability (adverse events, dropouts due to adverse events); acceptability (dropouts for any reason). | https://doi.org/10.1002/14651858.CD011006.pub4 |
| Aerobic Physical Activity and Depression Among Patients With Cancer: A Systematic Review and Meta-Analysis | Kulchycki M, 2024 | JAMA Network Open | 10.5 (2023 JIF) | To determine whether aerobic physical activity is associated with reduced depression among patients with cancer, and to examine patient, cancer, intervention and methodological moderators. Included because the strategy was built by a named research librarian and is the most sensitive depression block in this collection - it is the one to copy if you want maximum recall on the outcome, including a Scopus/citation-index translation in proximity syntax. | Patients with any cancer diagnosis, including haematopoietic stem cell transplant recipients. | Aerobic physical activity interventions (randomised controlled trials). | Usual care or non-aerobic control. | Severity of depression on validated self-reported scales (CES-D, HADS, BDI and others), short- and long-term. | https://doi.org/10.1001/jamanetworkopen.2024.37964 |

### Search strategies

<details>
<summary><b>Soong RY, 2025</b> — JAMA Network Open</summary>

Taken from: eTable 1 (Search Strategy) in Supplement 1

**PubMed / MEDLINE**

```
[PubMed searched natively, database inception to 5 November 2024.
eTable 1 in Supplement 1, verbatim:]
#1 "Geriatrics"[Mesh] OR "Aged"[Mesh] OR Aging OR Aged OR Centenarians
   OR Nonagenarians OR Octogenarians OR Elder* OR Gerontology OR 'older adult*'
#2 Neoplas*[title/abstract] OR Cancer[title/abstract] OR Malignan*[title/abstract]
#3 Exercis*[title/abstract] OR Exerciz*[title/abstract]
   OR (Physical*[title/abstract] AND Interven*[title/abstract])
   OR (Physical*[title/abstract] AND Activit*[title/abstract])
#4 depress* OR anxi* OR burden* OR Stress* OR 'quality of life'
The four sets are combined with AND. Note the curly quotation marks as printed;
PubMed will not parse 'older adult*' or 'quality of life' as phrases unless the
quotes are replaced with straight double quotes.
```

**Embase**

```
[Embase, database inception to 5 November 2024. eTable 1, verbatim:]
#1 'geriatrics'/exp OR 'aged'/exp OR 'aging'/exp OR 'senescence'/exp
   OR 'older adult*' OR 'aging' OR 'centenarians' OR 'nonagenarians'
   OR 'octogenarians' OR 'gerontology' OR 'older people'/exp
#2 'neoplas*'/exp OR 'cancer'/exp OR 'malignan*'/exp
#3 'exercis*' OR 'exerciz*' OR (physical* NEAR/2 (intervent* OR activit*))
#4 'depress*' OR 'depression'/exp OR 'anxi*' OR 'anxiety'/exp OR 'disease burden*'
   OR 'physiological stress*' OR 'quality of life'
Note: 'neoplas*'/exp and 'malignan*'/exp are printed with truncation inside an
Emtree explosion, which Embase does not accept; these lines will need repair
before reuse.
```

**Web of Science**

```
Not searched. Databases searched were PubMed, Embase, PsycINFO and the Cochrane
Library, from inception to 5 November 2024.
[Cochrane Library version, verbatim:
#1 MeSH descriptor: [Geriatrics] explode all trees OR ((Aging OR Aged OR Centenarians
   OR Nonagenarians OR Octogenarians OR Elder* OR Gerontology OR 'older adult*'):ti,ab,kw)
#2 (neoplas*):ti,ab,kw OR (cancer):ti,ab,kw OR (malignan*):ti,ab,kw
#3 MeSH descriptor: [Exercise] explode all trees OR (exercis*' OR 'exerciz*'
   OR (physical* NEAR/2 (intervent* OR activit*)):ti,ab,kw)
#4 MeSH descriptor: [Depression] explode all trees OR (anxi* OR burden* OR Stress*
   OR 'quality of life'):ti,ab,kw)
PsycINFO version, verbatim:
#1 (Geriatrics OR Aged OR Aging OR Centenarians OR Nonagenarians OR Octogenarians
   OR Elder* OR Gerontology OR 'Older Adult*').mp.
#2 (neoplas* OR cancer OR malignan*).ti,ab.
#3 exp Exercise/ OR exercis*.ti,ab. OR exerciz*.ti,ab.
   OR (physical* adj2 (intervent*.ti,ab. or activit*.ti,ab.))
#4 (depress* OR anxi* OR burden* OR stress* OR 'quality of life').ti,ab.]
```

</details>

<details>
<summary><b>Vita G, 2023</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-4 of the review, read in full from PMC10065046

**PubMed / MEDLINE**

```
[Not searched as PubMed. MEDLINE via Ovid, 1946 to November 2022; latest search date
24 November 2022. Appendix 2, verbatim:]
1  exp Neoplasms/
2  (cancer* or tumor* or tumour* or neoplas* or malignan* or carcinoma*
   or adenocarcinoma* or choriocarcinoma* or lymphoma* or leukemia* or leukaemia*
   or metastat* or sarcoma* or teratoma*).mp.
3  1 or 2
4  Depression/
5  exp Depressive Disorder/
6  Adjustment Disorders/
7  (depress* or melanchol* or ((adjustment or reactive or dysthymic) adj5
   disorder*)).mp.
8  4 or 5 or 6 or 7
9  drug therapy.fs.
10 exp Antidepressive Agents/
11 exp Heterocyclic Compounds/
12 exp Serotonin Uptake Inhibitors/
13 exp Adrenergic Uptake Inhibitors/
14 exp Monoamine Oxidase Inhibitors/
15 (anti-depress* or antidepress* or drug therap* or pharmacotherap* or trycyclic*
   or TCA* or heterocyclic* or serotonin uptake or SSRI* or SNRI*
   or monoamine oxidase inhibitor* or MAOI*).mp.
16 (desipramine or imipramine or clomipramine or opipramol or trimipramine or
   lofepramine or dibenzepin or amitriptyline or nortriptyline or protriptyline or
   doxepin or iprindole or melitracen or butriptyline or dosulepin or amoxapine or
   dimetacrine or amineptine or maprotiline or quinupramine or zimeldine or
   fluoxetine or citalopram or paroxetine or sertraline or alaproclate or
   fluvoxamine or etoperidone or escitalopram or isocarboxazid or nialamide or
   phenelzine or tranylcypromine or iproniazide or iproclozide or moclobemide or
   toloxatone or oxitriptan or tryptophan or mianserin or nomifensine or trazodone
   or nefazodone or minaprine or bifemelane or viloxazine or oxaflozane or
   mirtazapine or bupropion or medifoxamine or tianeptine or pivagabine or
   venlafaxine or milnacipran or reboxetine or gepirone or duloxetine or
   agomelatine or desvenlafaxine or vilazodone or hyperici herba or
   hypericum perforatum or st john* wort* or saint john* wort*).mp.
17 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16
18 3 and 8 and 17
19 randomized controlled trial.pt.
20 controlled clinical trial.pt.
21 randomized.ab.
22 placebo.ab.
23 clinical trials as topic.sh.
24 randomly.ab.
25 trial.ti.
26 19 or 20 or 21 or 22 or 23 or 24 or 25
27 18 and 26
28 exp animals/ not humans.sh.
29 27 not 28
key: mp = title, abstract, original title, name of substance word, subject heading
word, keyword heading word, protocol supplementary concept, rare disease
supplementary concept, unique identifier; pt = publication type; ab = abstract;
sh = subject heading; ti = title.
[Complete unabbreviated strategy, all databases: strategies/04_vita2023_antidepressants.txt]
```

**Embase**

```
[Embase via Ovid, 1980 to November 2022. Appendix 3, verbatim:]
1  exp neoplasm/
2  (cancer* or tumor* or tumour* or neoplas* or malignan* or carcinoma*
   or adenocarcinoma* or choriocrcinoma* or leukemia* or leukaemia* or metastat*
   or sarcoma* or teratoma*).ti,ab.
3  1 or 2
4  exp depression/
5  adjustment disorder/
6  (depress* or melanchol* or ((adjustment or reactive or dysthymic) adj3
   disorder*)).ti,ab.
7  4 or 5 or 6
8  exp antidepressant agent/
9  exp heterocyclic compound/
10 exp serotonin uptake inhibitor/
11 exp adrenergic receptor affecting agent/
12 exp monoamine oxidase inhibitor/
13 (anti-depress* or antidepress* or drug therap* or pharmacotherap* or trycyclic*
   or TCA* or heterocyclic* or serotonin uptake or SSRI* or SNRI*
   or monoamine oxidase inhibitor* or MAOI*).ti,ab.
14 [the same ~70-agent drug-name line as MEDLINE line 16].ti,ab.
15 8 or 9 or 10 or 11 or 12 or 13 or 14
16 3 and 7 and 15
17 crossover procedure/
18 double-blind procedure/
19 randomized controlled trial/
20 single-blind procedure/
21 random*.mp.
22 factorial*.mp.
23 (crossover* or cross over* or cross-over*).mp.
24 placebo*.mp.
25 (double* adj blind*).mp.
26 (singl* adj blind*).mp.
27 assign*.mp.
28 allocat*.mp.
29 volunteer*.mp.
30 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29
31 16 and 30
32 (exp animal/ or nonhuman/ or exp animal experiment/) not human/
33 31 not 32
Note "choriocrcinoma*" is a typo for choriocarcinoma* in the published Embase and
CENTRAL appendices; the MEDLINE appendix spells it correctly.
[Complete unabbreviated strategy, all databases: strategies/04_vita2023_antidepressants.txt]
```

**Web of Science**

```
Not searched. Databases searched were CENTRAL (2022, Issue 11), MEDLINE Ovid,
Embase Ovid and PsycINFO Ovid, all to November 2022, supplemented by handsearching
the trial databases of the FDA, MHRA, EMA and other drug-approving agencies.
Web of Science was not used.
[CENTRAL strategy (Appendix 1), verbatim:
#1 MeSH descriptor: [Neoplasms] explode all trees
#2 (cancer* or tumor* or tumour* or neoplas* or malignan* or carcinoma* or
   adenocarcinoma* or choriocrcinoma* or leukemia* or leukaemia* or metastat*
   or sarcoma* or teratoma*)
#3 #1 or #2
#4 MeSH descriptor: [Depression] explode all trees
#5 MeSH descriptor: [Depressive Disorder] explode all trees
#6 MeSH descriptor: [Adjustment Disorders] explode all trees
#7 (depress* or melanchol* or ((adjustment or reactive or dysthymic) near/5 disorder*))
#8 #4 or #5 or #6 or #7
#9 Any MeSH descriptor with qualifier(s): [Drug therapy - DT]
#10-#16 [antidepressant class MeSH explosions and the ~70-agent drug-name list]
#17 #9 or #10 or #11 or #12 or #13 or #14 or #15 or #16
#18 #3 and #8 and #17]
[Complete unabbreviated strategy, all databases: strategies/04_vita2023_antidepressants.txt]
```

</details>

<details>
<summary><b>Kulchycki M, 2024</b> — JAMA Network Open</summary>

Taken from: eTable 1 (Search Strategy) in Supplement 1

**PubMed / MEDLINE**

```
[Not searched as PubMed. Ovid MEDLINE, publications 1 January 1980 to 5 July 2023;
strategy built by a research librarian. eTable 1 in Supplement 1, verbatim
(population and depression blocks; the exercise block is lines 8-19 and the design
filter lines 20-32):]
1  exp neoplasms/ or cancer survivors/ or psycho-oncology/ or exp hematopoietic stem
   cell transplantation/ or stem cell transplantation/ or hematopoietic stem cell
   mobilization/
2  (cancer* or neoplas* or tumo?r* or malignan* or metasta* or oncogen* or oncolog*
   or psychooncolog* or sarcoma* or leuk?emi* or lymphoma* or hodgkin* or nonhodgkin*
   or carcino* or melanoma* or thymoma* or myeloma* or blastoma* or hepatoblastoma*
   or mesenchymoma* or mesothelioma* or hepatoma* or adenocarcinoma*
   or glioma*).ti,ab,kf
3  (HSCT or ((h?ematopoietic or h?emato-poietic) adj3 (transplant* or sct or bct
   or mobili#ation)) or pbsct or pbct or psct or ((peripheral or pbsc or pbscs) adj3
   transplant*) or autohct or autopbsct or autopbsc or autopsc or cbsct or
   ((autologous or auto-logous or auto or allogeneic or allo-geneic or homologous
   or homo-logous) adj hct)).ti,ab,kf
4  or/1-3
5  depression/ or exp depressive disorder/ or sadness/ or demoralization/ or
   mental health/ or happiness/ or hope/ or resilience, psychological/
6  (depress* or dysthymi* or melanchol* or affective or mood or distress* or sadness
   or sad or hopeless* or demorali* or mental health or psych* health or wellbeing
   or wellness or contented or contentment or happiness or hope* or
   resilien*).ti,ab,kf
7  5 or 6
8-19  [exercise block: exp exercise/ or exp exercise movement techniques/ or exp
      exercise therapy/ or dancing/ or exp physical fitness/ or exp sports/ or
      aquatic therapy/; plus 11 text-word lines covering modality, dose, sport and
      exergaming terms]
20-30 [design filter: randomized controlled trial/ or Random Allocation/ or Double
      Blind Method/ or Single Blind Method/; trial publication types; exp Clinical
      Trials as topic/; (clinical adj trial$).tw,kf; (RCT or RCTs).tw,kf;
      ((singl$ or doubl$ or treb$ or tripl$) adj (blind$3 or dumm* or mask$3)).tw,kf;
      PLACEBOS/; (placebo$ or sham).tw,kf;
      (randomized or randomised or randomly).ab; trial.ti]
31 exp animals/ not humans.sh
32 30 not 31
33 4 and 7 and 19 and 32
   limit 33 to (english language and yr="1980 -Current")
[Complete unabbreviated strategy, all databases: strategies/04_kulchycki2024_aerobic-activity-depression.txt]
```

**Embase**

```
[Embase via Ovid, 1 January 1980 to 5 July 2023. eTable 1, verbatim (population and
depression blocks; exercise block lines 8-19, design filter lines 20-29):]
1  exp neoplasm/ or exp cancer patient/ or psycho-oncology/ or exp hematopoietic stem
   cell transplantation/ or stem cell transplantation/
2  (cancer* or neoplas* or tumo?r* or malignan* or metasta* or oncogen* or oncolog*
   or psychooncolog* or sarcoma* or leuk?emi* or lymphoma* or hodgkin* or nonhodgkin*
   or carcino* or melanoma* or thymoma* or myeloma* or blastoma* or hepatoblastoma*
   or mesenchymoma* or mesothelioma* or hepatoma* or adenocarcinoma*
   or glioma*).ti,ab,kw
3  [same HSCT line as MEDLINE, .ti,ab,kw]
4  or/1-3
5  exp depression/ or sadness/ or demoralization/ or mental health/ or psychological
   well-being/ or happiness/ or hope/ or hopelessness/ or unhappiness/ or
   psychological resilience/
6  (depress* or dysthymi* or melanchol* or affective or mood or distress* or sadness
   or sad or hopeless* or demorali* or mental health or psych* health or wellbeing
   or wellness or contented or contentment or happiness or hope* or
   resilien*).ti,ab,kw
7  5 or 6
8-19  [exercise block, Emtree equivalents plus the same 11 text-word lines]
20-28 [Embase design filter]
29 or/20-28
30 (exp animal/ or nonhuman/) not exp human/
31 29 not 30
32 4 and 7 and 19 and 31
33 limit 32 to (english language and yr="1980 -Current")
[Complete unabbreviated strategy, all databases: strategies/04_kulchycki2024_aerobic-activity-depression.txt]
```

**Web of Science**

```
Web of Science was not searched. Scopus was used as the citation-index equivalent,
alongside MEDLINE, Embase, CENTRAL, CINAHL and PsycINFO (1 January 1980 to
5 July 2023). The Scopus strategy is the closest available template for a Web of
Science translation, since Scopus proximity syntax (W/n) maps onto Web of Science
NEAR/n.
[Scopus strategy, verbatim (population and depression sets; the exercise block is
sets 5-15 and the design filter sets 16-24):
1 TITLE-ABS-KEY(cancer* or neoplas* or tumo*r* or malignan* or metasta* or oncogen*
  or oncolog* or psychooncolog* or sarcoma* or leuk*emi* or lymphoma* or hodgkin*
  or nonhodgkin* or carcino* or melanoma* or thymoma* or myeloma* or blastoma*
  or hepatoblastoma* or mesenchymoma* or mesothelioma* or hepatoma*
  or adenocarcinoma* or glioma*)
2 TITLE-ABS-KEY(HSCT or ((h*ematopoietic or h*emato-poietic) W/3 (transplant* or sct
  or bct or mobili?ation)) or pbsct or pbct or psct or ((peripheral or pbsc or pbscs)
  W/3 transplant*) or autohct or autopbsct or autopbsc or autopsc or cbsct or
  ((autologous or auto-logous or auto or allogeneic or allo-geneic or homologous
  or homo-logous) W/1 hct))
3 #1 or #2
4 TITLE-ABS-KEY(depress* or dysthymi* or melanchol* or affective or mood or distress*
  or sadness or sad or hopeless* or demorali* or "mental health" or (psych* W/1 health)
  or wellbeing or wellness or contented or contentment or happiness or hope*
  or resilien*)
...
25 #3 AND #4 AND #15 AND #24
26 #25 AND PUBYEAR AFT 1979 AND ( LIMIT-TO ( LANGUAGE , "English" ) )]
[Complete unabbreviated strategy, all databases: strategies/04_kulchycki2024_aerobic-activity-depression.txt]
```

</details>

---

## 05. Nutritional status

**Focus.** How do previously published systematic reviews of cancer treatment build the nutritional-status concept (malnutrition, nutritional assessment, cachexia, body composition) in their database search strategies?

**Population scope applied.** The first record is ovarian-cancer-specific and meets the JIF >= 5 threshold, so no broadening was needed for it. The other two broaden the cancer type in order to capture a published Web of Science strategy (Takaoka) and a PICO-structured nutritional-status block (Lovell). One further ovarian-specific option was found and rejected on the threshold: Rinninella 2019, "Nutritional Interventions to Improve Clinical Outcomes in Ovarian Cancer", Nutrients (JIF ~4.8).

**Note.** Takaoka 2024 is the only review across all eight categories that publishes a Web of Science strategy in full. Its TS= topic-search structure is the template to adapt if you add Web of Science to your own review.

| Title | 1st author / year | Journal | Impact factor | Purpose of the study | P — Population | I — Intervention / exposure | C — Comparison | O — Outcome | URL |
|---|---|---|---|---|---|---|---|---|---|
| Perioperative nutrition interventions for women with ovarian cancer | Billson HA, 2013 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To assess the effects of nutrition interventions during the perioperative period for women with ovarian cancer. The single most directly reusable record in this collection: an ovarian-cancer population block intersected with a 17-line nutrition block that includes Nutritional Status/ and Nutrition Assessment/ as explicit MeSH and Emtree terms, in a journal above the threshold. | Women with ovarian cancer undergoing surgery (perioperative period). | Any nutrition intervention - enteral or parenteral nutrition, oral supplements, immunonutrition, early feeding, dietary advice. | Standard perioperative care or an alternative nutrition intervention. | Postoperative complications and infection; length of hospital stay; nutritional status; quality of life; gastrointestinal function; mortality. | https://doi.org/10.1002/14651858.CD009884.pub2 |
| Prevalence of and Survival with Cachexia among Patients with Cancer: A Systematic Review and Meta-Analysis | Takaoka T, 2024 | Advances in Nutrition | 8.0 (2023 JIF) | To quantify how the reported prevalence of cachexia in patients with cancer varies by diagnostic criterion, and to estimate the association between cachexia and overall survival. Included because it is the only review in this collection that publishes a complete Web of Science strategy, set out side by side with the PubMed version so the MeSH-to-TS= translation is visible line for line. | Patients with cancer (any type, any stage). | Presence of cachexia, diagnosed by any published definitive criterion (Fearon, EPCRC, ASPEN/AND, Evans, GLIM and others). | Patients with cancer without cachexia. | Prevalence of cachexia by diagnostic criterion; overall survival. | https://doi.org/10.1016/j.advnut.2024.100282 |
| Nutritional status, body composition and chemotherapy dosing in children and young people with cancer: a systematic review | Lovell AL, 2025 | British Journal of Cancer | 6.4 (2023 JIF) | To determine whether nutritional status (undernutrition, overweight/obesity, altered body composition) alters the pharmacokinetics and pharmacodynamics of antineoplastic drugs in children and young people (< 21 years) with cancer. Included as the clearest example of a search laid out explicitly by PICO element, with nutritional status broken into three parallel sub-blocks - undernutrition, overnutrition, and neutral body-composition measures - which is the structure most likely to transfer to an ovarian cancer review where both directions matter. | Children and young people (< 21 years) with cancer receiving antineoplastic therapy. | Antineoplastic drug therapy (chemotherapy, alkylating agents, combination protocols). | Nutritional status groups - undernutrition/sarcopenia versus normal nutrition versus overweight/obesity/sarcopenic obesity, defined by body composition, BMI or nutritional status measures. | Pharmacokinetic and pharmacodynamic parameters; drug toxicity and adverse reactions; survival (overall, disease-free, progression-free). | https://doi.org/10.1038/s41416-025-03023-3 |

### Search strategies

<details>
<summary><b>Billson HA, 2013</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-3 of the review, read in full from PMC8730356

**PubMed / MEDLINE**

```
[Not searched as PubMed. Medline via Ovid, 1946 to July week 4 2012.
Appendix 2, verbatim:]
1  exp Perioperative Care/
2  exp Perioperative Period/
3  (peri-operative or perioperative).mp.
4  exp Surgical Procedures, Operative/
5  surgery.fs.
6  (surg* or operat* or procedure*).mp.
7  1 or 2 or 3 or 4 or 5 or 6
8  exp Nutrition Therapy/
9  exp Nutrition Disorders/
10 Nutritional Status/
11 Nutrition Assessment/
12 Cachexia/
13 (weight or underweight or cachexi* or malnutrition).mp.
14 (nutrition* or nutrient* or macronutrient* or micronutrient* or immunonutrition
   or immuno-nutrition).mp.
15 exp Food/
16 (food* or feed* or supplement* or vitamin* or mineral* or protein* or fat*
   or carbohydrate* or calorie* or energy).mp.
17 exp Diet/
18 diet therapy.fs.
19 diet*.mp.
20 exp Fish Oils/
21 exp Amino Acids/
22 (amino acid* or fatty acid* or fish oil* or omega 3 or glutamin* or arginine
   or novel substrate* or nitrogen).mp.
23 exp Feeding Methods/
24 (enteral or parenteral or TPN or naso-gastric or nasogastric or gastrostomy
   or jejunostomy).mp.
25 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21
   or 22 or 23 or 24
26 exp Genital Neoplasms, Female/
27 exp Ovarian Neoplasms/
28 ((gynaecologic* or gynecologic* or ovar*) adj5 (cancer* or tumor* or tumour*
   or malignan* or carcinoma* or adenocarcinoma*)).mp.
29 26 or 27 or 28
30 randomized controlled trial.pt.
31 controlled clinical trial.pt.
32 randomized.ab.
33 placebo.ab.
34 clinical trials as topic.sh.
35 randomly.ab.
36 trial.ti.
37 30 or 31 or 32 or 33 or 34 or 35 or 36
38 7 and 25 and 29 and 37
39 exp animals/ not humans.sh.
40 38 not 39
key: mp = protocol supplementary concept, rare disease supplementary concept, title,
original title, abstract, name of substance word, subject heading word, unique
identifier; pt = publication type; ab = abstract; sh = subject heading;
fs = floating subheading.
(Line 38 is printed as "7 and 25 and 29 and 37~" with a stray tilde.)
```

**Embase**

```
[Embase via Ovid, 1980 to 2012 week 31. Appendix 3, verbatim:]
1  perioperative period/
2  (peri-operative or perioperative).mp.
3  exp surgery/
4  su.fs.
5  (surg* or operat* or procedure*).mp.
6  1 or 2 or 3 or 4 or 5
7  exp diet therapy/
8  exp nutritional disorder/
9  exp nutritional status/
10 nutritional assessment/
11 cachexia/
12 (weight or underweight or cachexi* or malnutrition).mp.
13 (nutrition* or nutrient* or macronutrient* or micronutrient* or immunonutrition
   or immuno-nutrition).mp.
14 exp Food/
15 (food* or feed* or supplement* or vitamin* or mineral* or protein* or fat*
   or carbohydrate* or calorie* or energy).mp.
16 exp diet/
17 diet*.mp.
18 fish oil/
19 exp amino acid/
20 (amino acid* or fatty acid* or fish oil* or omega 3 or glutamin* or arginine
   or novel substrate* or nitrogen).mp.
21 exp food intake/
22 (enteral or parenteral or PN or TPN or naso-gastric or nasogastric or gastrostomy
   or jejunostomy).mp.
23 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20
   or 21 or 22
24 exp female genital tract tumor/
25 exp ovary tumor/
26 ((gynaecologic* or gynecologic* or ovar*) adj5 (cancer* or tumor* or tumour*
   or malignan* or carcinoma* or adenocarcinoma*)).mp.
27 24 or 25 or 26
28 crossover procedure/
29 double-blind procedure/
30 randomized controlled trial/
31 single-blind procedure/
32 random*.mp.
33 factorial*.mp.
34 (crossover* or cross over* or cross-over*).mp.
35 placebo*.mp.
36 (double* adj blind*).mp.
37 (singl* adj blind*).mp.
38 assign*.mp.
39 allocat*.mp.
40 volunteer*.mp.
41 28 or 29 or 30 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39 or 40
42 6 and 23 and 27 and 41
43 (exp Animal/ or Nonhuman/ or exp Animal Experiment/) not Human/
44 42 not 43
```

**Web of Science**

```
Not searched. Databases searched were the Cochrane Gynaecological Cancer Group
Specialised Register, CENTRAL (2012, Issue 7), Medline (1946 to July week 4 2012),
Embase (1980 to 2012 week 31), DARE (to 7 August 2012), AMED (1985 to April 2012),
BNI (1992 to April 2012) and CINAHL. Web of Science was not used.
[CENTRAL/DARE strategy (Appendix 1), verbatim - useful because it is the same
three-block design in a proximity syntax:
#1 MeSH descriptor Perioperative Care explode all trees
#2 MeSH descriptor Perioperative Period explode all trees
#3 peri-operative or perioperative
#4 MeSH descriptor Surgical Procedures, Operative explode all trees
#5 Any MeSH descriptor with qualifier: SU
#6 surg* or operat* or procedure*
#7 (#1 OR #2 OR #3 OR #4 OR #5 OR #6)
#8 MeSH descriptor Nutrition Therapy explode all trees
#9 MeSH descriptor Nutrition Disorders explode all trees
#10 MeSH descriptor Nutritional Status, this term only
#11 MeSH descriptor Nutrition Assessment, this term only
#12 MeSH descriptor Cachexia, this term only
#13 weight or underweight or cachexi* or malnutrition
#14 nutrition* or nutrient* or macronutrient* or micronutrient* or immunonutrition
#15 MeSH descriptor Food explode all trees
#16 food* or feed* or supplement* or vitamin* or mineral* or protein* or fat*
    or carbohydrate* or calorie* or energy
#17 MeSH descriptor Diet explode all trees
#18 Any MeSH descriptor with qualifier: DH
#19 diet*
#20 MeSH descriptor Fish Oils explode all trees
#21 MeSH descriptor Amino Acids explode all trees
#22 amino acid* or fatty acid* or fish oil* or omega 3 or glutamin* or arginine
    or novel substrate* or nitrogen
#23 MeSH descriptor Feeding Methods explode all trees
#24 enteral or parenteral of PN or TPN or naso-gastric or nasogastric or gastrostomy
    or jejunostomy
#25 (#8 OR ... OR #24)
#26 MeSH descriptor Genital Neoplasms, Female explode all trees
#27 MeSH descriptor Ovarian Neoplasms explode all trees
#28 (gynaecologic* or gynecologic* or ovar*) near/5 (cancer* or tumor* or tumour*
    or malignan* or carcinoma* or adenocarcinoma*)
#29 (#26 OR #27 OR #28)
#30 (#7 AND #25 AND #29)
Line #24 is printed with "of PN" where "or PN" is meant.]
```

</details>

<details>
<summary><b>Takaoka T, 2024</b> — Advances in Nutrition</summary>

Taken from: Supplemental Table 2 (Search strategy) in the supplementary material

**PubMed / MEDLINE**

```
[PubMed searched natively, inception to 31 July 2023. Supplemental Table 2, verbatim
(result counts as printed):]
#1  Neoplasms [MeSH]                                    3,857,356
#2  Cancer [TIAB]                                       2,173,946
#3  Tumor [TIAB]                                        1,420,714
#4  #1 OR #2 OR #3                                      4,767,145
#5  Cachexia [MeSH]                                         6,238
#6  Wasting Syndrome [MeSH]                                 1,985
#7  Disease-related malnutrition [TIAB]                       251
#8  #5 OR #6 OR #7                                          8,308
#9  Diagnosis [MeSH]                                    9,374,402
#10 Assessment [TIAB]                                   1,261,169
#11 Screening [TIAB]                                      676,373
#12 #9 OR #10 OR #11                                   10,513,314
#13 #4 AND #8                                               4,381
#14 #13 AND #12                                             1,680
#15 Clinical Study [Publication Type]                   1,138,887
#16 Epidemiologic Studies [MeSH]                        3,152,279
#17 #15 OR #16                                          3,923,924
#18 #14 AND #17                                               439
Note the nutritional-status concept here is narrow - three terms - and there is no
truncation on Cancer/Tumor. Sensitivity was traded for a manageable yield.
```

**Embase**

```
Not searched. Only PubMed and Web of Science were searched, from inception to
31 July 2023, by a single researcher.
```

**Web of Science**

```
[Web of Science searched, inception to 31 July 2023. Supplemental Table 2, verbatim
(result counts as printed):]
#1  TS = Neoplasms                       230,171
#2  TS = Cancer                        3,018,044
#3  TS = Tumor                         2,042,632
#4  #1 OR #2 OR #3                     4,034,303
#5  TS = Cachexia                         12,778
#6  TS = Wasting Syndrome                  6,221
#7  TS = Disease-related malnutrition      4,463
#8  #5 OR #6 OR #7                        22,512
#9  TS = Diagnosis                     1,992,601
#10 TS = Assessment                    2,079,264
#11 TS = Screening                     1,145,410
#12 #9 OR #10 OR #11                   4,803,898
#13 #4 AND #8                             10,115
#14 #13 AND #12                            2,171
#15 TS = Clinical study                2,353,376
#16 TS = Epidemiologic study              58,077
#17 TS = Epidemiological study           142,973
#18 #16 OR #17                           196,384
#19 #15 OR #18                         2,490,979
#20 #14 AND #19                              644
TS = topic search (title, abstract, author keywords, Keywords Plus). Note that the
study-design concept, which is a publication type in PubMed, has to be re-expressed
as free text in Web of Science, and that British and American spellings of
"epidemiologic(al)" must both be entered.
```

</details>

<details>
<summary><b>Lovell AL, 2025</b> — British Journal of Cancer</summary>

Taken from: Supplementary 1 (Proposed search terms prepared for MEDLINE database)

**PubMed / MEDLINE**

```
[MEDLINE (PubMed) searched to 30 September 2024; strategy developed with a library
specialist and set out by PICO element. Supplementary 1, verbatim:]
Population
  Child/ [MeSH], Pediatrics/ [MeSH], Adolescent/ [MeSH], Infant/ [MeSH]
  (child* or pediatric or pediatric or adolescen* or teen* or kids or preteen
  or pre-teen or youth or infan* or "young adult*" or "school age*").mp.
  Neoplasms [MeSH]
  (neoplasm* or cancer or "p?ediatric oncology" or "p?ediatric cancer"
  or "child* cancer").mp.
Intervention
  Drug Therapy/ [MeSH], Antineoplastic Agents/ [MeSH], Alkylating Agents/ [MeSH],
  Antineoplastic Combined Chemotherapy Protocols/ [MeSH]
  (chemotherap* or "drug therapy" or "antineoplastic agent*" or "alkylating agent*"
  or cytotox* or antitumo?r or anti?cancer).mp.
Comparison  [this is where nutritional status sits]
  Malnutrition/ [MeSH], Thinness/ [MeSH], Protein-Energy Malnutrition/ [MeSH],
  Severe Acute Malnutrition/ [MeSH], Sarcopenia/ [MeSH]
  (malnutrition or thinness or "protein-energy malnutrition"
  or "severe-acute malnutrition" or malnourish* or underweight or PEM
  or "protein-calorie malnutrition" or "nutritional deficien*" or undernutrition
  or sarcopeni*).mp.
  Overnutrition/ [MeSH], Overweight/ [MeSH], Obesity/ [MeSH]
  (overnutrition or overweight or obesity or obese or hypernutrition
  or "sarcopenic obesity").mp.
  Nutritional Status/ [MeSH], Body Composition/ [MeSH], Body Mass Index/ [MeSH],
  Body Weight/ [MeSH]
  ("nutrition* status" or "body composition" or "body mass index" or "body weight"
  or BMI).mp.
Outcome
  Pharmacokinetics/ [MeSH], Toxicology/ [MeSH], Metabolism/ [MeSH],
  Pharmacogenetics/ [MeSH]
  (pharmacokinetic* or toxic* or metabolism or pharmacodynamic).mp.
  "Drug-Related Side Effects and Adverse Reactions"/ [MeSH]
  ("drug toxicity" or "drug side effect*" or toxicit*).mp.
  Survival/ [MeSH], Disease-Free Survival/ [MeSH], Survival Rate/ [MeSH],
  Progression-Free Survival/ [MeSH], Survival Analysis/ [MeSH]
  (surviv* or "disease-free surviv*" or "survival rate"
  or "progression-free surviv*" or "survival analysis").mp.
Keyword search: mp = title, book title, abstract, original title, name of substance
word, subject heading word, floating sub-heading word, keyword heading word, organism
supplementary concept word, protocol supplementary concept word, rare disease
supplementary concept word, unique identifier, synonyms, population supplementary
concept word, anatomy supplementary concept word.
Note the strategy mixes PubMed-style [MeSH] tags with Ovid-style .mp. and is titled
"Proposed search terms prepared for MEDLINE database" - it is a term list to be
translated, not a runnable line-numbered strategy.
```

**Embase**

```
Searched, but no Embase-specific string was published. The Methods state that
"Medical Subject Headings, major topics, and multi-purpose terms were developed" and
adapted across databases; only the MEDLINE term list is reproduced
(Supplementary 1).
```

**Web of Science**

```
Searched (Web of Science Core Collection), but no Web of Science-specific string was
published. Databases searched were MEDLINE (PubMed), EMBASE, Web of Science Core
Collection, Scopus, ProQuest Health, Cochrane Trials and Cochrane Reviews, all to
30 September 2024. Only the MEDLINE term list is reproduced.
```

</details>

---

## 06. Health-related quality of life (HRQOL)

**Focus.** How do previously published systematic reviews of cancer treatment build the health-related quality of life concept in their database search strategies?

**Population scope applied.** Cancer type and age left open, per the brief. Two ovarian-specific HRQOL reviews were identified and rejected on the JIF >= 5 threshold - Wilson 2018, "A Systematic Review of Health-Related Quality of Life Reporting in Ovarian Cancer Phase III Clinical Trials", The Oncologist (JIF ~4.8, and the closest miss in this whole exercise), and Kumar 2019, "Quality of life outcomes following surgery for advanced ovarian cancer", Int J Gynecol Cancer (JIF ~4.1). Cramer 2017 is retained partly because it is restricted to women.

**Note.** The three HRQOL blocks span the full range. Mishra names the instruments (QLQ-C30, FACIT, SF-36, HADS, POMS, MSAS and others) as search terms, which is the single most transferable idea in this collection - instrument acronyms retrieve trials whose abstracts never use the phrase "quality of life". Osanto builds a 40-term PRO block that deliberately absorbs anxiety, depression, functional status, fatigue and pain into the HRQOL concept. Cramer does not search the outcome at all.

| Title | 1st author / year | Journal | Impact factor | Purpose of the study | P — Population | I — Intervention / exposure | C — Comparison | O — Outcome | URL |
|---|---|---|---|---|---|---|---|---|---|
| Exercise interventions on health-related quality of life for people with cancer during active treatment | Mishra SI, 2012 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To evaluate the effectiveness of exercise on overall HRQoL and on specific HRQoL domains among adults with cancer during active treatment. Included because its HRQoL block is the most complete in this collection: alongside the expected controlled vocabulary and free text it lists the named measurement instruments, so trials reporting only "FACT-G" or "QLQ-C30" are still retrieved. | Adults with any cancer, during active treatment (surgery, chemotherapy, radiotherapy, hormonal therapy). | Exercise interventions (aerobic, resistance, combination, mind-body including yoga, tai chi, qigong, hydrotherapy). | Usual care, no exercise, or an alternative non-exercise intervention. | Overall HRQoL and HRQoL domains - physical, psychological, social, spiritual well-being, pain, fatigue, sleep, body image, vitality; adverse events. | https://doi.org/10.1002/14651858.CD008465.pub2 |
| Health-related quality of life outcomes in randomized controlled trials in metastatic hormone-sensitive prostate cancer: a systematic review | Osanto S, 2024 | eClinicalMedicine | 9.6 (2023 JIF) | To review how HRQoL was assessed and reported in phase III randomised trials comparing treatment arms in metastatic hormone-sensitive prostate cancer. Included for two reasons: it is one of only two records in this collection with a published Web of Science strategy, and its HRQoL/PRO block is the broadest - it treats anxiety, depression, functional status, fatigue, pain, symptom burden, sexual and social functioning as facets of the same concept, which is exactly the union your review needs across categories 2, 3, 4, 6 and 7. | Patients with metastatic hormone-sensitive prostate cancer (mHSPC). | Systemic treatment arms of phase III RCTs (androgen deprivation therapy alone or in combination with docetaxel, abiraterone, apalutamide, enzalutamide, darolutamide or radiotherapy). | The comparator arm of each trial (usually ADT alone). | Health-related quality of life and patient-reported outcomes - instrument used, domains, timing, compliance, statistical handling, and the direction of any between-arm difference. | https://doi.org/10.1016/j.eclinm.2024.102914 |
| Yoga for improving health-related quality of life, mental health and cancer-related symptoms in women diagnosed with breast cancer | Cramer H, 2017 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To assess the effects of yoga on health-related quality of life, mental health and cancer-related symptoms among women diagnosed with breast cancer, during or after active treatment. Included as the contrast case, and because it is restricted to women: HRQoL is the first-named outcome in the title and the primary outcome of the review, yet no quality-of-life, mental-health or symptom term appears anywhere in any of the six search strategies. | Women with a diagnosis of breast cancer, receiving active treatment or having completed treatment. | Yoga (including asana, pranayama, dhyana, dharana, meditation). | No therapy, or another active intervention (psychosocial/educational, exercise). | Health-related quality of life; mental health (depression, anxiety); cancer-related symptoms (fatigue, sleep disturbance); adverse events. | https://doi.org/10.1002/14651858.CD010802.pub2 |

### Search strategies

<details>
<summary><b>Mishra SI, 2012</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-6 of the review, read in full from PMC7389071

**PubMed / MEDLINE**

```
[MEDLINE searched via PubMed, inception to May 2010 (430 hits) and January 2010 to
November 2011 (190 hits). Appendix 1, verbatim - lines 32-58 are the HRQoL block:]
1-31   [exercise block: exp exercise/; exercise tolerance/; exp exertion/; Pliability/;
       physical fitness/; "Physical Education and Training"/; exp physical endurance/;
       exercise therapy/; exercising.mp.; physical condition$.mp.; stamina.mp.;
       motor activity/; exercise test/; exp Sports/; tai chi.mp. or tai ji/; yoga/;
       muscle stretching exercises/; exp "range of motion, articular"/; pilates.mp.;
       qigong.mp.; chi kung.mp.; resistance training.mp.; mind body therap$.mp.;
       exp complementary therapies/; Bad Ragaz.mp.; Ai Chi.mp.; Halliwick.mp.;
       hippotherapy.mp.; Hydrotherapy/; balance exercise$.mp.; aquatic exercise$.mp.]
32     1 or 2 or 3 or ... or 31
33     "quality of life"/
34     exp health status/
35     "activities of daily living"/
36     life qualit$.mp.
37     exp self concept/
38     health level.mp.
39     level of health.mp.
40     wellness.mp.
41     well being.mp.
42     (activities of daily life or daily living activities).mp.
43     functional ability.mp.
44     good health.mp.
45     healthiness.mp.
46     patient reported outcomes.mp.
47     social adjustment/
48     physical limitations.mp.
49     psychiatric status.mp.
50     pain measurement/
51     functional assessment.mp.
52     fact questionnaire.mp.
53     fact survey.mp.
54     qlc-c30.mp.
55     facit.mp.
56     toi.mp.
57     (flic or sf-36 or ces-d or bdi or sta1 or bfi or hads or lasa or poms or qli
       or rsci or pais or bpi or msas or mos or ptgi or panas).mp.
58     sense of coherence.mp.
59-65  [design filter: randomized.ab.; placebo.ab.; randomly.ab.; trial.ab.;
       randomized controlled trial.pt.; controlled clinical trial.pt.; random$.ab]
66-69  [population: exp neoplasms/; cancer.mp.;
       (neoplasm$ or tumor$ or tumour or malignan$).mp.; active treatment.mp.]
70     [union of lines 33-58 - the HRQoL set]
71     [union of the design lines]
72     [union of the cancer lines]
73     32 and 70 and 71 and 72
74-76  Survivors/ ; survivor.mp. ; 74 or 75   [used to exclude survivorship trials,
       which are covered by the companion review]
Note "qlc-c30" is a transposition of QLQ-C30, and "sta1" of STAI, in the published
appendix. Repair both before reuse.
[Complete unabbreviated strategy, all databases: strategies/06_mishra2012_hrqol.txt]
```

**Embase**

```
[Embase, inception to May 2010 (713 hits) and January 2010 to November 2011 (349 hits).
Appendix 3, verbatim - lines 33-58 are the HRQoL block:]
1-31   [exercise block, Emtree equivalents: exp exercise/; exertion.mp.; pliability/;
       fitness/; (physical education and training).mp.; physical endurance.mp. or
       endurance/; kinesiotherapy/; exercising.mp.; "physical condition$".mp.;
       stamina.mp.; exp motor activity/; exp sports/; exercise test/; tai chi.mp.;
       tai ji.mp.; yoga/; stretching exercise/; "range of motion"/; pilates.mp.;
       qigong.mp.; chi kung.mp.; muscle strength/ or muscle training/ or resistance
       training.mp.; mind body therapy.mp.; alternative medicine/; bad ragaz.mp.;
       ai chi.mp.; halliwick.mp.; hippotherapy.mp.; hydrotherapy/;
       balance exercises.mp.; aquatic exercise/]
32     1 or 2 or ... or 31
33     "quality of life"/
34     exp health status/
35     daily life activity/
36     life qualit$.mp.
37     exp self concept/
38     health level.mp.
39     "level of health".mp.
40     wellbeing/
41     wellness.mp.
42     good health.mp.
43     functional ability.mp.
44     healthiness.mp.
45     "patient reported outcomes".mp.
46     social adaptation/
47     physical limitation$.mp.
48     psychiatric status.mp.
49     pain assessment/
50     functional assessment/
51     questionnaire/ or fact questionnaire.mp.
52     fact survey.mp.
53     health survey/
54     qlc-c30.mp.
55     facit.mp.
56     toi.mp.
57     sense of coherence.mp.
58     (flic or sf-36 or ces-d or bdi or stal or bfi or hads or lasa or poms or qli
       or rsci or pais or bpi or msas or mos or ptgi or panas).mp.
59-64  [design filter]
65     59 or 60 or 61 or 62 or 63 or 64
66     [union of the HRQoL lines]
67-70  exp neoplasm/; cancer.mp.;
       (neoplasm$ or tumor$ or tumour or malignan$).mp.; active treatment
71     (67 or 68 or 69 or 70)
72-74  Survivors/; survivor$.mp.; 72 or 73
75     32 and 65 and 66 and 71
76     75 not 74
(Line 69 is printed as ".mp3" - a typo for .mp.; "stal" in line 58 is STAI.)
[Complete unabbreviated strategy, all databases: strategies/06_mishra2012_hrqol.txt]
```

**Web of Science**

```
Web of Science was used, but for citation searching of key authors rather than with a
subject strategy, so no Web of Science string exists. As reported: "We also searched
citations of key authors through Web of Science and Scopus, and searched PubMed's
related article feature."
Databases searched with a strategy: CENTRAL, PubMed MEDLINE (Appendix 1),
MEDLINE In-Process (Appendix 2), EMBASE (Appendix 3), CINAHL (Appendix 4),
PsycINFO (Appendix 5), and PEDRO, LILACS, SIGLE, SportDiscus, OTSeeker and
Sociological Abstracts (Appendix 6), all from inception to November 2011, with no
language or date restriction. Trial registries (WHO ICTRP, Current Controlled Trials,
CenterWatch, ClinicalTrials.gov), reference lists and expert contact were also used.
[The CINAHL version (Appendix 4) is the same HRQoL set in EBSCOhost syntax and
includes (MH "Functional Status") and (MH "Pain Measurement") as controlled terms.]
[Complete unabbreviated strategy, all databases: strategies/06_mishra2012_hrqol.txt]
```

</details>

<details>
<summary><b>Osanto S, 2024</b> — eClinicalMedicine</summary>

Taken from: Supplementary Table 2 (Search Strategy) in the supplementary appendix

**PubMed / MEDLINE**

```
[PubMed searched natively; restricted to publications from 1 January 2015.
Supplementary Table 2, verbatim - the HRQoL/PRO block reproduced in full, the
population and treatment blocks abbreviated:]
Block 1 (population): ("Metastatic Hormone sensitive Prostate Cancer"[tw] OR
  "mHSPC"[tw] OR "metastatic castration naive prostate cancer"[tw] OR ... [14 phrase
  variants] ... OR (("Prostatic Neoplasms"[mesh] OR "prostate cancer"[tw] OR ...
  [28 prostate-cancer phrase variants] ...) AND ("metastatic"[tw] OR "metasta*"[tw]
  OR "oligometastatic"[tw] OR "oligometasta*"[tw])))
AND
Block 2 (treatment): ("androgen deprivation therapy"[tw] OR "androgen depriv*"[tw]
  OR "androgen block*"[tw] OR "ADT"[tiab] OR "Androgen Antagonists"[Mesh]
  OR "Androgen Antagonists"[Pharmacological Action])
AND
Block 3 (HRQoL / patient-reported outcomes) - verbatim:
  ("Quality of Life"[mesh] OR "Quality of Life"[tw] OR "Life Quality"[tw]
  OR "HR-QoL"[tw] OR "HRQoL"[tw] OR "QoL"[tw] OR "PROs"[tw]
  OR "Patient Reported Outcome Measures"[Mesh] OR "Patient Reported Outcome"[tw]
  OR "Patient Reported Outcomes"[tw] OR "Patient Reported"[tw] OR "Anxiety"[mesh]
  OR "anxiety"[tw] OR "Depression"[mesh] OR "depression"[tw]
  OR "Psychological Distress"[mesh] OR "distress"[tw] OR "emotional"[tw]
  OR "Functional Status"[Mesh] OR "functional status"[tw] OR "health outcomes"[tw]
  OR "health related quality of life"[tw] OR "Health Status"[Mesh]
  OR "health status"[tw] OR "HRQL"[tw] OR "patient outcomes"[tw] OR "PRO"[tw]
  OR "psychological"[tw] OR "psychosocial"[tw] OR "sexual functioning"[tw]
  OR "Sexuality"[Mesh] OR "Sexual Behavior"[Mesh] OR "Social Interaction"[Mesh]
  OR "social functioning"[tw] OR "social wellbeing"[tw] OR "social"[tw]
  OR "Symptom Assessment"[Mesh] OR "symptom assessment"[tw]
  OR "symptom burden"[tw] OR "symptom distress"[tw] OR "Fatigue"[mesh]
  OR "fatigue"[tw] OR "Pain"[mesh] OR "pain"[tw])
AND
Block 4 (design): ("randomized controlled trial"[pt] OR "randomized"[ti]
  OR "randomised"[ti] OR "RCT"[ti] OR "trial"[ti] OR "Clinical Trial, Phase III"[pt]
  OR "phase iii"[tw] OR "phase three"[tw] OR "phase 3"[tw] OR "phaseiii"[tw]
  OR "phasethree"[tw] OR "phase3"[tw])
NOT "review"[pt] AND english[la] AND ("2015/01/01"[PDAT] : "3000/12/31"[PDAT])
NOT (phase II publication types and title terms, unless also phase III)
[Complete unabbreviated strategy, all databases: strategies/06_osanto2024_hrqol-mhspc.txt]
```

**Embase**

```
[Embase (OVID version), same date limits. Supplementary Table 2, verbatim - structure
reproduced, population block abbreviated:]
(("Metastatic Hormone sensitive Prostate Cancer".ti,ab OR "mHSPC".ti,ab OR ...
[same phrase variants] ... OR ((exp *"Prostatic Cancer"/ OR "prostate cancer".ti,ab
OR ... ) ADJ4 ("metastatic".ti,ab OR "metasta*".ti,ab OR "oligometastatic".ti,ab
OR "oligometasta*".ti,ab)))
AND ("androgen deprivation therapy".ti,ab OR "androgen depriv*".ti,ab
OR "androgen block*".ti,ab OR "ADT".ti,ab OR "Androgen deprivation therapy"/
OR exp *"antiandrogen"/)
AND (exp *"Quality of Life"/ OR "Quality of Life".ti,ab OR ... [the same
40-term PRO list, expressed as Emtree explosions plus .ti,ab text words] ...)
AND [phase III / randomised design filter] NOT review NOT meeting abstract,
English, 2015 onwards.
Note the population block uses ADJ4 in Embase where PubMed used a plain AND, so the
Embase run is the more specific of the two.
[Complete unabbreviated strategy, all databases: strategies/06_osanto2024_hrqol-mhspc.txt]
```

**Web of Science**

```
[Web of Science searched. Supplementary Table 2, verbatim - the topic block
reproduced in full, population block abbreviated:]
((TI=("Metastatic Hormone sensitive Prostate Cancer" OR "mHSPC" OR ... [phrase
variants] ... OR (("Prostatic Cancer" OR "prostate cancer" OR ...) AND "metastatic"))
OR AB=(... same phrase variants ... OR (("Prostatic Cancer" OR "prostate cancer"
OR ...) NEAR/5 ("metastatic" OR "metasta*" OR "oligometastatic" OR "oligometasta*"))))
AND (TI=("androgen deprivation therapy" OR "androgen depriv*" OR "androgen block*"
OR "ADT" OR "Androgen deprivation therapy" OR "antiandrogen")
OR AB=("androgen deprivation therapy" OR "androgen depriv*" OR "androgen block*"
OR "ADT" OR "Androgen deprivation therapy" OR "antiandrogen"))
AND TS=("Quality of Life" OR "Quality of Life" OR "Life Quality" OR "HR-QoL"
OR "HRQoL" OR "QoL" OR "PROs" OR "Patient-Reported Outcome"
OR "Patient Reported Outcome" OR "Patient Reported Outcomes" OR "Patient Reported"
OR "Anxiety" OR "anxiety" OR "Depression" OR "depression" OR "Distress Syndrome"
OR "distress" OR "emotional" OR "Functional Status" OR "functional status"
OR "health outcomes" OR "health related quality of life" OR "Health Status"
OR "health status" OR "HRQL" OR "patient outcomes" OR "PRO" OR "psychological"
OR "psychosocial" OR "sexual functioning" OR "Sexuality" OR "Sexual behavior"
OR "Social Interaction" OR "social functioning" OR "social wellbeing" OR "social"
OR "Symptom Assessment" OR "symptom assessment" OR "symptom burden"
OR "symptom distress" OR "Fatigue" OR "fatigue" OR "Pain" OR "pain")
AND TI=("randomized controlled trial" OR "controlled clinical trial" OR "randomized"
OR "randomised" OR "RCT" OR "trial" OR "phase 3 clinical trial" OR "phase iii"
OR "phase three" OR "phase 3" OR "phaseiii" OR "phasethree" OR "phase3")
NOT DT=review AND la=english
AND py=(2015 OR 2016 OR 2017 OR 2018 OR 2019 OR 2020 OR 2021 OR 2022 OR 2023)
NOT dt=(meeting abstract)
NOT (TI=("phase 2 clinical trial" OR "phase ii" OR "phase two" OR "phase 2"
OR "phaseii" OR "phasetwo" OR "phase2") NOT TS=("phase 3 clinical trial" OR ...))
This is the most complete Web of Science template in the collection: note TI=/AB=
used separately where PubMed uses [tw], TS= for the topic block, NEAR/5 replacing
ADJ4, DT= for document type, la= for language and py= for an explicit year list.
Google Scholar and the Cochrane Library were also searched.
[Complete unabbreviated strategy, all databases: strategies/06_osanto2024_hrqol-mhspc.txt]
```

</details>

<details>
<summary><b>Cramer H, 2017</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-6 of the review, read in full from PMC6465041

**PubMed / MEDLINE**

```
[MEDLINE searched via PubMed on 29 January 2016. Appendix 1, verbatim:]
#1  yoga [mh]
#2  yoga* [tiab]
#3  yogic [tiab]
#4  meditation [tiab]
#5  asana* [tiab]
#6  pranayama [tiab]
#7  dharana [tiab]
#8  dhyana [tiab]
#9  #1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8
#10 breast neoplasms [mh]
#11 breast neoplasm* [tiab]
#12 breast cancer [tiab]
#13 breast carcinoma* [tiab]
#14 breast tumor* [tiab]
#15 mamma carcinoma* [tiab]
#16 mammary neoplasm* [tiab]
#17 mammary carcinoma* [tiab]
#18 mammary gland carcinoma* [tiab]
#19 #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18
#20 randomized controlled trial [pt]
#21 controlled clinical trial [pt]
#22 randomized [tiab]
#23 placebo [tiab]
#24 clinical trials as topic [mesh: noexp]
#25 randomly [tiab]
#26 trial [ti]
#27 #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26
#28 Search #7 AND #17 AND #25
#29 Search animals[mh] NOT humans[mh]
#30 Search #26 NOT #27
Three problems in the published appendix, all worth noting before reuse: line #27
unions the population set (#19) with the design terms instead of unioning the design
terms alone; line #28 combines single line numbers (#7 = dharana, #17 = mammary
carcinoma*, #25 = randomly) rather than the three set unions #9, #19 and #27; and
line #30 subtracts #27 from #26 rather than #29 from #28. What was run was almost
certainly #9 AND #19 AND (design union) NOT (animals not humans).
There is no HRQoL, mental-health or symptom block.
```

**Embase**

```
[Embase searched 29 January 2016. Appendix 2 gives two versions.
Embase.com syntax, verbatim:]
#1  random* OR factorial* OR crossover* OR cross NEXT/1 over* OR placebo*
    OR (doubl* AND blind*) OR (singl* AND blind*) OR assign* OR allocat*
    OR volunteer* OR 'crossover procedure'/exp OR 'double blind procedure'/exp
    OR 'randomized controlled trial'/exp OR 'single blind procedure'/exp
#2  'breast neoplasm'
#3  'breast cancer'/exp OR 'breast cancer'
#4  'breast tumour'
#5  'breast tumor'/exp OR 'breast tumor'
#6  'breast carcinoma'/exp OR 'breast carcinoma'
#7  'mamma carcinoma'/exp OR 'mamma carcinoma'
#8  'mammary neoplasm'
#9  'mammary carcinoma'/exp OR 'mammary carcinoma'
#10 'mammary gland carcinoma'
#11 #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10
#12 'breast cancer survivor'
#13 'breast cancer survivors'
#14 #12 OR #13
#15 #11 OR #14
#16 'yoga'/exp OR yoga
#17 yogic
#18 asana
#19 pranayama
#20 dhyana
#21 dharana
#22 'meditation'/exp OR meditation
#23 #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22
#24 #1 AND #11 AND #23
#25 #24 NOT ([animals]/lim NOT [humans]/lim)
#26 #25 AND [embase]/lim
[Embase via OvidSP, verbatim:]
1-19  [Ovid Embase RCT filter: Randomized controlled trial/; Controlled clinical
      study/; Random$.ti,ab.; randomization/; intermethod comparison/; placebo.ti,ab.;
      (compare or compared or comparison).ti.; ((evaluated or evaluate or evaluating
      or assessed or assess) and (compare or compared or comparing or comparison)).ab.;
      (open adj label).ti,ab.; ((double or single or doubly or singly) adj (blind or
      blinded or blindly)).ti,ab.; double blind procedure/; parallel group$1.ti,ab.;
      (crossover or cross over).ti,ab.; ((assign$ or match or matched or allocation)
      adj5 (alternate or group$1 or intervention$1 or patient$1 or subject$1 or
      participant$1)).ti,ab.; (assigned or allocated).ti,ab.; (controlled adj7 (study
      or design or trial)).ti,ab.; (volunteer or volunteers).ti,ab.; human experiment/;
      trial.ti.]
20    or/1-19
21    exp breast/
22    exp breast disease/
23    (21 or 22) and exp neoplasm/
24    exp breast tumor/
25    exp breast cancer/
26    exp breast carcinoma/
27    (breast$ adj5 (neoplas$ or cancer$ or carcin$ or tumo$ or metasta$
      or malig$)).ti,ab.
28    or/21-27
29    exp yoga/
30    (yora or yogic or asana or pranayama or dhyana or dharana or meditation).tw.
31    exp meditation/
32    29 or 30 or 31
33    20 and 28 and 32
34    limit 33 to embase
("yora" in line 30 is a typo for yoga.)
```

**Web of Science**

```
Not searched. Databases searched were the Cochrane Breast Cancer Specialised Register,
MEDLINE via PubMed (Appendix 1), Embase (Appendix 2), CENTRAL 2016 Issue 1
(Appendix 3), the WHO ICTRP portal (Appendix 4), ClinicalTrials.gov (Appendix 5) and
IndMed (Appendix 6), all to 29 January 2016. Web of Science was not used.
[CENTRAL strategy (Appendix 3), verbatim:
#1 MeSH descriptor: [Breast Neoplasms] explode all trees
#2 breast near cancer*
#3 breast near neoplasm*
#4 breast near carcinoma*
#5 breast near tumour*
#6 breast near tumor*
#7 #1 or #2 or #3 or #4 or #5 or #6
#8 MeSH descriptor: [Yoga] explode all trees
#9 MeSH descriptor: [Meditation] explode all trees
#10 yoga or yogic or meditation or asana or pranayama or dharana or dhyana
#11 #8 or #9 or #10
#12 #7 and #11]
```

</details>

---

## 07. Patients' symptoms (fatigue, insomnia, pain, anorexia, dyspnea, cognitive problems, anxiety, nausea, depression, sensory neuropathy, constipation, diarrhea)

**Focus.** How do previously published systematic reviews of cancer treatment build the symptom concept in their database search strategies, given the 12 recommended patient-reported symptoms?

**Population scope applied.** Cancer type and age left open, per the brief.

**Note.** An honest negative finding worth acting on: across everything screened for this exercise, no systematic review in a journal with JIF >= 5 enumerates the 12 symptoms as a search block. Reviews either (a) search a single named symptom, (b) search "symptom(s)" or "patient-reported outcome" as an abstraction, or (c) do not search the outcome at all and pick symptoms up at data extraction - which is what both Reeve and Ream do. If you want a symptom block for an ovarian cancer review, the nearest off-the-shelf material is the PRO block in Osanto 2024 (category 6), which already carries fatigue, pain, anxiety, depression, functional status and symptom burden, and the instrument-name line in Mishra 2012 (category 6), which retrieves via MSAS, MDASI and QLQ-C30 rather than via symptom words.

| Title | 1st author / year | Journal | Impact factor | Purpose of the study | P — Population | I — Intervention / exposure | C — Comparison | O — Outcome | URL |
|---|---|---|---|---|---|---|---|---|---|
| Recommended patient-reported core set of symptoms to measure in adult cancer treatment trials | Reeve BB, 2014 | Journal of the National Cancer Institute | 9.9 (2023 JIF) | To derive, by systematic review plus analysis of six large datasets and multistakeholder consensus, a core set of patient-reported symptoms for adult cancer treatment trials. This is the paper that produced the 12 symptoms in the brief - fatigue, insomnia, pain, anorexia (appetite loss), dyspnea, cognitive problems, anxiety (includes worry), nausea, depression (includes sadness), sensory neuropathy, constipation and diarrhea. Included as the anchor reference for the category, and as a caution: the paper that defines the symptom set retrieved its evidence with a two-term search. | Adults (>= 18 years) with cancer, across diverse cancer populations and treatment modalities. | Anticancer treatment (any modality) in clinical trials measuring a patient-reported outcome. | Not applicable - this is a core-outcome-set derivation, not a comparative review. | Which symptoms should form a core set, judged on prevalence across cancer populations, impact on health outcomes and quality of life, and attribution to disease or to anticancer treatment. | https://doi.org/10.1093/jnci/dju129 |
| Patient-Reported Outcome Measures in Cancer Care: An Updated Systematic Review and Meta-Analysis | Balitsky AK, 2024 | JAMA Network Open | 10.5 (2023 JIF) | To determine whether integrating patient-reported outcome measures into cancer care is associated with patient-related, therapy-related and health-care-utilisation outcomes. Included because it is the best-documented symptom-adjacent strategy at this impact level: an information specialist's line-numbered strategies for five databases, run twice (an original search and a 2022 update), with per-database yields reported. The symptom concept is expressed at one level of abstraction - "patient reported outcome(s)" AND (inventory or instrument* or measure* or self-report*) - rather than by naming symptoms. | Adults (>= 18 years) with active cancer receiving anticancer therapy (survivors excluded). | Administration of a patient-reported outcome measure, with results shared with the patient's health care professional. | Standard care without PROM administration. | Patient-related outcomes (HRQOL, symptom control, patient-clinician communication); therapy-related outcomes (treatment adherence, chemotherapy dose modification, survival); health care utilisation (emergency visits, hospital admissions). | https://doi.org/10.1001/jamanetworkopen.2024.24793 |
| Telephone interventions for symptom management in adults with cancer | Ream E, 2020 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To assess the effectiveness of telephone-delivered interventions for reducing symptoms associated with cancer and its treatment, to determine which symptoms are most responsive, and whether intervention configuration and dose modify the effect. Included because the review's own question is explicitly "which symptoms respond" - it analyses anxiety, depression, fatigue, emotional distress, pain and others as separate outcomes - and yet not one symptom term appears in any of the three search strategies. It is the clearest demonstration in this collection that a symptom-focused review can be built entirely on a population-plus-intervention search. | Adults (>= 18 years) with cancer, during or after treatment. | Telephone-delivered interventions for symptom management, alone or with additional face-to-face, printed or electronic support. | Usual care or another intervention. | Individual symptoms - anxiety, depression, fatigue, emotional distress, pain, nausea and others; symptom clusters; quality of life; adverse events. | https://doi.org/10.1002/14651858.CD007568.pub2 |

### Search strategies

<details>
<summary><b>Reeve BB, 2014</b> — Journal of the National Cancer Institute</summary>

Taken from: Literature Review subsection of the Methods, read from PMC4110472

**PubMed / MEDLINE**

```
[Reported in full in the Literature Review section, verbatim:]
"Search terms included 'multiple symptoms' and 'cancer' and was limited to adults
(aged 18 years or older) and to reports published in English between 2001 and 2011.
This strategy identified 55 publications..."
The review itself is reported as "described elsewhere" - in Reilly CM et al.,
"A literature synthesis of symptom prevalence and severity in persons receiving
active cancer treatment", Support Care Cancer 2013;21:1525-50 - which extended
Kim et al.'s earlier synthesis of studies using the Symptom Distress Scale, the
M.D. Anderson Symptom Inventory and the Memorial Symptom Assessment Scale.
No database name, interface, field tag or line-numbered strategy is given. The 12
symptoms are an output of the review; none of them is an input to the search.
```

**Embase**

```
Not reported. No database is named in the paper; the search is described only by the
two terms above, and the underlying review is cited to Reilly 2013.
```

**Web of Science**

```
Not reported. See above.
```

</details>

<details>
<summary><b>Balitsky AK, 2024</b> — JAMA Network Open</summary>

Taken from: eAppendices (search strategies) in Supplement 1

**PubMed / MEDLINE**

```
[Not searched as PubMed. Ovid MEDLINE and MEDLINE Epub Ahead of Print, In-Process and
other non-indexed citations, 1946 to present; searches to 26 September 2022.
eAppendix in Supplement 1, verbatim (result counts as printed):]
1  exp Neoplasms/ (3489255)
2  (cancer* or neoplasm* or carcinoma* or oncol* or malignan* or tumor* or leukemia*
   or leukaemia* or sarcoma* or lymphoma* or melanoma* or blastoma*
   or myeloma*).mp. (4606954)
3  1 or 2 (4799855)
4  (patient reported outcomes or patient reported outcome or patient based outcome
   or patient reported outcome measure$).mp. (27045)
5  (inventory or instrument* or measure* or self-report*).ti,ab. (3825061)
6  4 and 5 (17872)
7  3 and 6 (3253)
8  Epidemiologic Studies/ (8708)
9  exp Case-Control Studies/ (1189370)
10 exp Cohort Studies/ (2159240)
11 Case control.tw. (134508)
12 (cohort adj (study or studies)).tw. (238711)
13 Cohort analy$.tw. (9174)
14 (Follow up adj (study or studies)).tw. (51361)
15 (observational adj (study or studies)).tw. (123476)
16 Longitudinal.tw. (268228)
17 Retrospective.tw. (597112)
18 Cross sectional.tw. (400545)
19 Cross-sectional studies/ (372470)
20 or/8-19 (3264389)
21 exp animals/ not humans.sh. (4849833)
22 20 not 21 (3196743)
23 7 and 22 (1296)
24 randomized controlled trial.pt. (534665)
25 controlled clinical trial.pt. (94229)
26 randomi?ed.ab. (626711)
27 placebo.ab. (219040)
28 drug therapy.fs. (2336519)
29 randomly.ab. (359969)
30 trial.ab. (556534)
31 groups.ab. (2209788)
32 or/24-31 (5054529)
33 exp animals/ not humans.sh. (4849833)
34 32 not 33 (4396229)
35 7 and 34 (1463)
36 23 or 35 (2191)
37 limit 36 to yr="2012 -Current" (2030)
[Complete unabbreviated strategy, all databases: strategies/07_balitsky2024_proms.txt]
```

**Embase**

```
[Embase via OvidSP, 1974 to 2021 (original search) and 1996 to 23 September 2022
(update). eAppendix in Supplement 1, verbatim (population and PRO blocks; the
observational filter is lines 8-23 and the RCT filter lines 25-44):]
1  exp malignant neoplasm/ (3666710)
2  (cancer* or neoplasm* or carcinoma* or oncol* or malignan* or tumor* or leukemia*
   or leukaemia* or sarcoma* or lymphoma* or melanoma* or blastoma*
   or myeloma*).mp. (6022711)
3  1 or 2 (6089519)
4  (patient reported outcomes or patient reported outcome or patient based outcome
   or patient reported outcome measure$).mp. (49934)
5  (inventory or instrument* or measure* or self-report*).ti,ab. (4948202)
6  4 and 5 (31490)
7  3 and 6 (6768)
8-23  [observational-study filter: clinical study/; case control study/; family study/;
      longitudinal study/; retrospective study/; prospective study/ not randomized
      controlled trials/; cohort analysis/; and .mp. adjacency lines for cohort,
      case control, follow up, observational, epidemiologic$ and cross sectional
      "study or studies"]
24 7 and 23 (2301)
25-44 [Embase RCT filter: randomized controlled trial/; Controlled clinical study/;
      random$.ti,ab.; randomization/; intermethod comparison/; placebo.ti,ab.;
      (compare or compared or comparison).ti.; ((evaluated or evaluate or evaluating
      or assessed or assess) and (compare or compared or comparing or comparison)).ab.;
      (open adj label).ti,ab.; ((double or single or doubly or singly) adj (blind or
      blinded or blindly)).ti,ab.; double blind procedure/; parallel group$1.ti,ab.;
      (crossover or cross over).ti,ab.; ((assign$ or match or matched or allocation)
      adj5 (alternate or group$1 or intervention$1 or patient$1 or subject$1 or
      participant$1)).ti,ab.; (assigned or allocated).ti,ab.; (controlled adj7 (study
      or design or trial)).ti,ab.; (volunteer or volunteers).ti,ab.; human experiment/;
      trial.ti.]
Yields by database for the updated search: MEDLINE, Embase, PsycInfo 605, CENTRAL 3434,
CINAHL 1866; subtotal 13 857, 3554 after limits, 1049 duplicates removed.
[Complete unabbreviated strategy, all databases: strategies/07_balitsky2024_proms.txt]
```

**Web of Science**

```
Not searched. Databases searched were MEDLINE and MEDLINE Epub ahead of print
(OvidSP), Embase (OvidSP), PsycINFO (OvidSP), CENTRAL and CINAHL (EBSCO), from
1 January 2012 to 26 September 2022, with no language or publication-status
restriction. The search from the 2014 predecessor review was re-run first
(eAppendices 1 and 2). Web of Science was not used.
[The CINAHL translation (EBSCOhost) is given in the same appendix and shows the PRO
concept in EBSCO syntax:
S4  (MH "Patient-Reported Outcomes")
S5  TX patient reported outcome
S6  TX patient reported outcomes
S7  TX patient based outcome
S8  TX patient reported outcome measure*
S9  S5 OR S6 OR S7 OR S8
S10 TX inventory or instrument* or measure* or self-report*
S11 S9 AND S10
S12 S4 OR S11
S13 S3 AND S12]
[Complete unabbreviated strategy, all databases: strategies/07_balitsky2024_proms.txt]
```

</details>

<details>
<summary><b>Ream E, 2020</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-3 of the review, read in full from PMC7264015

**PubMed / MEDLINE**

```
[Not searched as PubMed. MEDLINE via Ovid. Appendix 2, verbatim:]
1  exp Neoplasms/
2  (neoplasm* or cancer* or carcinoma* or tumour* or adenocarcinoma* or leukemi*
   or leukaemi* or lymphoma* or tumor* or malignan* or myeloma*).mp.
3  exp Radiotherapy/
4  (radiotherap* or radiation or radiochemotherap* or chemoradi* or chemotherap*).mp.
5  1 or 2 or 3 or 4
6  exp Telemedicine/
7  (telemedicine or (tele adj medicine)).mp.
8  (teleconsultation or (tele adj consultation)).mp.
9  (remote* adj5 consultation*).mp.
10 telephone*.mp.
11 phone*.mp.
12 cellphone*.mp.
13 8 or 6 or 11 or 7 or 10 or 9 or 12
14 "randomized controlled trial".pt.
15 "controlled clinical trial".pt.
16 randomized.ab.
17 randomly.ab.
18 trial.ab.
19 groups.ab.
20 18 or 19 or 16 or 17 or 15 or 14
21 13 and 20 and 5
Note that the population block folds treatment modality (radiotherapy, chemotherapy)
into the cancer concept with OR rather than AND - a useful pattern if you want to
capture treated populations without requiring the treatment to be indexed. There is
no symptom block.
```

**Embase**

```
[Embase via Ovid. Appendix 3, verbatim:]
1  exp Neoplasm/
2  (neoplasm* or cancer* or carcinoma* or tumour* or adenocarcinoma* or leukemi*
   or leukaemi* or lymphoma* or tumor* or malignan* or myeloma*).mp.
3  exp Radiotherapy/
4  (radiotherap* or radiation or radiochemotherap* or chemoradi* or chemotherap*).mp
5  1 or 2 or 3 or 4
6  exp Telemedicine/
7  (telemedicine or (tele adj medicine)).mp.
8  (teleconsultation or (tele adj consultation)).mp.
9  (remote* adj5 consultation*).mp.
10 telephone*.mp.
11 phone*.mp.
12 cellphone*.mp.
13 8 or 6 or 11 or 7 or 10 or 9 or 12
14 exp Controlled Clinical Trial/
15 randomized.ab.
16 randomly.ab.
17 trial.ab.
18 groups.ab.
19 18 or 16 or 17 or 15 or 14
20 19 and 13 and 5
```

**Web of Science**

```
Not searched. Databases searched were CENTRAL, MEDLINE (Ovid), Embase (Ovid),
PsycINFO, CINAHL and British Nursing Index, plus trial registries and reference
lists. Web of Science was not used.
[CENTRAL strategy (Appendix 1), verbatim:
#1 MeSH descriptor Neoplasms explode all trees
#2 neoplasm* or cancer* or carcinoma* or tumour* or adenocarcinoma* or leukemi*
   or leukaemi* or lymphoma* or tumor* or malignan* or myeloma*
#3 MeSH descriptor Radiotherapy explode all trees
#4 radiotherap* or radiation or radiochemotherap* or chemoradi* or chemotherap*
#5 (#1 OR #2 OR #3 OR #4)
#6 MeSH descriptor Telemedicine explode all trees
#7 telemedicine or (tele next medicine)
#8 teleconsultation or (tele next consultation)
#9 telephone*
#10 phone*
#11 cellphone*
#12 remote* near/5 consultation*
#13 (#6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12)
#14 (#5 AND #13)]
```

</details>

---

## 08. Patients' satisfaction

**Focus.** How do previously published systematic reviews of cancer treatment build the patient satisfaction concept in their database search strategies?

**Population scope applied.** Cancer type and age left open, per the brief. The most on-topic review found - Wells 2018, "Effects of patient navigation on satisfaction with cancer care: a systematic review and meta-analysis", Supportive Care in Cancer - was excluded on the JIF >= 5 threshold (JIF ~2.8) and is worth reading alongside these three.

**Note.** Jacobsen 2018 is the only record in the whole collection whose search has a genuine, named outcome block containing patient satisfaction - "patient satisfaction" as free text plus "Patient Satisfaction"[Mesh], sitting in a fourth AND-ed set alongside quality of life, distress, comprehension, adherence and recurrence. If you want a satisfaction block for your review, copy that set. Note also the vocabulary problem: satisfaction, patient experience and patient-reported experience measures are three different literatures with three different index terms, and Shao 2025 shows that searching one does not retrieve the others.

| Title | 1st author / year | Journal | Impact factor | Purpose of the study | P — Population | I — Intervention / exposure | C — Comparison | O — Outcome | URL |
|---|---|---|---|---|---|---|---|---|---|
| Systematic Review of the Impact of Cancer Survivorship Care Plans on Health Outcomes and Health Care Delivery | Jacobsen PB, 2018 | Journal of Clinical Oncology | 42.1 (2023 JIF) | To determine what impact providing a survivorship care plan has on health outcomes and health care delivery for people diagnosed with cancer, with satisfaction with care as one of the health-care-experience outcomes. Included because its fourth search set is an explicit patient-centred outcome block - the clearest published example in this collection of retrieving on satisfaction rather than screening for it. | Individuals diagnosed with cancer. | Survivor or care-provider receipt of a survivorship care plan (SCP). | No receipt of an SCP, an alternative method of receiving an SCP, or no comparison (for non-randomised studies). | Patient-reported health outcomes (e.g. quality of life); health care use; health care costs; health outcomes (e.g. quality-adjusted life years); and health care experience (e.g. satisfaction with care). | https://doi.org/10.1200/JCO.2018.77.7482 |
| Effectiveness and cost-effectiveness of home palliative care services for adults with advanced illness and their caregivers | Gomes B, 2013 | Cochrane Database of Systematic Reviews | 8.4 (2023 JIF, Cochrane Library) | To quantify the effect of home palliative care services on dying at home, and to examine their effect on other patient and caregiver outcomes including symptom control, quality of life, caregiver distress and satisfaction with care, together with resource use, costs and cost-effectiveness. Included as the large-scale contrast: satisfaction with care is named in objective 2, twelve databases were searched, and not one of the strategies contains a satisfaction term. | Adults with advanced illness (the majority of included participants had cancer) and their family caregivers. | Home palliative care services - specialist teams providing palliative care at home. | Usual care, or care without a home palliative care service. | Dying at home (primary); symptom burden and control; quality of life; caregiver distress and grief; satisfaction with care; resource use, costs and cost-effectiveness. | https://doi.org/10.1002/14651858.CD007760.pub2 |
| Factors influencing cancer patients' experiences of care in the USA, United Kingdom and Canada: A systematic review | Alessy SA, 2022 | eClinicalMedicine | 9.6 (2023 JIF) | To identify which patient, clinical and health-system factors are consistently associated with cancer patients' reported experiences of care across three national survey programmes in three countries. Included because it publishes a Web of Science strategy alongside its PubMed strategy, and because it shows the instrument-name route into this literature: rather than searching the concept "satisfaction" or "experience", it searches the named survey instruments (CPES, CAHPS/SEER-CAHPS, AOPSS), which is the same trick Mishra 2012 uses for HRQOL in category 6. | Adults with cancer responding to a national patient-experience survey in the USA, United Kingdom or Canada. | Patient, clinical and health-system characteristics (age, sex, ethnicity, socioeconomic position, cancer type and stage, comorbidity, provider and hospital factors). | Patients with the contrasting characteristic within the same survey. | Reported experience of cancer care, as measured by the National Cancer Patient Experience Survey (CPES), the Consumer Assessment of Healthcare Providers and Systems (CAHPS/SEER-CAHPS) or the Ambulatory Oncology Patient Satisfaction Survey (AOPSS). | https://doi.org/10.1016/j.eclinm.2022.101405 |

### Search strategies

<details>
<summary><b>Jacobsen PB, 2018</b> — Journal of Clinical Oncology</summary>

Taken from: Appendix (PICO Framework and PubMed/MEDLINE Search Strategy) of the article

**PubMed / MEDLINE**

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

**Embase**

```
Not reported. Only a PubMed/MEDLINE strategy is printed. The review states the search
was supplemented by expert input on relevant publications.
```

**Web of Science**

```
Not reported. See above.
```

</details>

<details>
<summary><b>Gomes B, 2013</b> — Cochrane Database of Systematic Reviews</summary>

Taken from: Appendices 1-5 of the review, read in full from PMC4473359

**PubMed / MEDLINE**

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

**Embase**

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

**Web of Science**

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

</details>

<details>
<summary><b>Alessy SA, 2022</b> — eClinicalMedicine</summary>

Taken from: Table 1 (Mesh terms used in PubMed and Web of Science) of the article

**PubMed / MEDLINE**

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

**Embase**

```
Not searched. Only PubMed, Web of Science and Google Scholar were used.
```

**Web of Science**

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

</details>

---

## 09. Annex: reviews excluded by the JIF >= 5 rule

**Focus.** Reviews that were topically closer to ovarian cancer, to gynaecological cancer or to older adults than several records that made the main sheets, and that were rejected only because of the Journal Impact Factor >= 5 threshold. None of these is a quality judgement - they are here so the cost of the threshold is visible and reversible.

**Population scope applied.** Six of the ten are ovarian or gynaecological cancer specific; two are restricted to older adults. The ovarian and geriatric-oncology systematic review literature sits almost entirely in the 2.4-4.8 impact band, so the threshold functions in practice as a trade of population relevance for journal prestige. If you relax it, start here. Impact factors are approximate - see docs/impact_factors.md.

| Title | 1st author / year | Journal | Impact factor | Why relevant | Why excluded | URL |
|---|---|---|---|---|---|---|
| A Systematic Review of Health-Related Quality of Life Reporting in Ovarian Cancer Phase III Clinical Trials | Wilson MK, 2018 | The Oncologist | ~4.8 | The single closest miss in the whole exercise. Ovarian cancer specific, HRQOL specific, and about phase III treatment trials - it maps onto category 6 and onto your review's population simultaneously. Would have replaced a breast or prostate cancer record on the HRQOL sheet. | JIF ~4.8, just below the 5 threshold | https://doi.org/10.1634/theoncologist.2017-0297 |
| Nutritional Interventions to Improve Clinical Outcomes in Ovarian Cancer: A Systematic Review of Randomized Controlled Trials | Rinninella E, 2019 | Nutrients | ~4.8 | Ovarian cancer specific and nutrition specific. Would have given category 5 a second ovarian record alongside Billson 2013, and a more recent one. | JIF ~4.8, just below the 5 threshold | https://doi.org/10.3390/nu11061404 |
| Depression and anxiety in ovarian cancer: a systematic review and meta-analysis of prevalence rates | Watts S, 2015 | BMJ Open | ~2.4 | The only ovarian-cancer-specific depression review found. A prevalence review, so depression is necessarily a search concept rather than a screening criterion - which is exactly the structure category 4 is about. | JIF ~2.4 | https://doi.org/10.1136/bmjopen-2015-007618 |
| Functional recovery in older women undergoing surgery for gynaecological malignancies: A systematic review and meta-analysis | Martin FE, 2020 | Journal of Geriatric Oncology | ~3.0 | Older women, gynaecological cancer, surgical treatment, functional status. On paper this is the single best population-and-outcome match to your review in the entire candidate pool - it fails only on impact factor. | JIF ~3.0 | https://doi.org/10.1016/j.jgo.2020.06.006 |
| Quality of life outcomes following surgery for advanced ovarian cancer: a systematic review and meta-analysis | Kumar S, 2019 | International Journal of Gynecological Cancer | ~4.1 | Ovarian cancer, surgical treatment, HRQOL outcome - the exact intersection of category 1 and category 6. | JIF ~4.1 | https://doi.org/10.1136/ijgc-2018-000125 |
| Ovarian cancer survivors' quality of life: a systematic review | Ahmed-Lecheheb D, 2016 | Journal of Cancer Survivorship | ~3.4 | Ovarian cancer specific HRQOL review covering the survivorship phase, which the records on sheet 6 do not. | JIF ~3.4 | https://doi.org/10.1007/s11764-016-0525-8 |
| A systematic review of patient values, preferences and expectations for the treatment of recurrent ovarian cancer | PEBC's Ovarian Oncology Guidelines Group, 2017 | Gynecologic Oncology | ~4.5 | Ovarian cancer, treatment, and a patient-centred construct (values, preferences, expectations) adjacent to satisfaction. Relevant to categories 1 and 8 together, and to any patient-centred framing of a treatment review. | JIF ~4.5 | https://doi.org/10.1016/j.ygyno.2017.05.039 |
| Psychosocial interventions and quality of life in gynaecological cancer patients: a systematic review | Hersch J, 2009 | Psycho-Oncology | ~3.3 | Gynaecological cancer with HRQOL and psychological outcomes - closer in population to your review than the breast and prostate cancer records that occupy sheet 6. | JIF ~3.3 | https://doi.org/10.1002/pon.1443 |
| Patient-Reported Physical Function Measures in Cancer Clinical Trials | Atkinson TM, 2017 | Epidemiologic Reviews | ~3.4-4.1 | A five-component search built around physical function and PRO measurement properties, in native PubMed syntax. Would have strengthened category 2, though only the measurement-properties component is printed verbatim in the paper. | JIF below 5; sources give ~3.4 (2024) to ~4.1 (2023) | https://doi.org/10.1093/epirev/mxx008 |
| Effects of patient navigation on satisfaction with cancer care: a systematic review and meta-analysis | Wells KJ, 2018 | Supportive Care in Cancer | ~2.8 | The most on-topic satisfaction review found anywhere - satisfaction with cancer care is the outcome, not a secondary endpoint. Directly relevant to category 8. | JIF ~2.8 | https://doi.org/10.1007/s00520-018-4108-2 |

