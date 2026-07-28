#!/usr/bin/env python3
"""Re-run the candidate-finding searches that populated the workbook.

Usage:
  python3 scripts/find_candidates.py                 # list the built-in outcome concepts
  python3 scripts/find_candidates.py hrqol           # run one
  python3 scripts/find_candidates.py --all           # run all of them
  python3 scripts/find_candidates.py --terms "malnutrition[ti] OR cachexia[ti]"

Why this exists: docs/methods.md describes how candidate reviews were found and gives
example queries, but no verbatim log of every search was kept during the work. Rather than
reconstruct one after the fact — which would be a guess dressed as a record — this script
makes the search *reproducible going forward*. Point it at a new outcome concept and it
runs the same pattern used for the eight categories: outcome concept AND cancer AND
systematic-review filter, restricted to journals above the impact threshold.

It prints PMID, year, journal, first author and title, plus whether a PMC copy exists,
because retrievability of the strategy was the second selection criterion.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

EUT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UA = {"User-Agent": "sunami-lab-review/1.0 (mailto:chenyangsu87@gmail.com)"}

# Journals used in the workbook plus the near-threshold ones checked and rejected.
HIGH_IF_JOURNALS = (
    '"Cochrane Database Syst Rev"[ta] OR "J Clin Oncol"[ta] OR "Lancet Oncol"[ta] '
    'OR "Ann Oncol"[ta] OR "JAMA Oncol"[ta] OR "Cancer Treat Rev"[ta] '
    'OR "Crit Rev Oncol Hematol"[ta] OR "JAMA Netw Open"[ta] OR "Eur J Cancer"[ta] '
    'OR "Br J Cancer"[ta] OR "J Natl Cancer Inst"[ta] OR "Int J Nurs Stud"[ta] '
    'OR "EClinicalMedicine"[ta] OR "Cancer"[ta] OR "ESMO Open"[ta] OR "Age Ageing"[ta] '
    'OR "Ageing Res Rev"[ta] OR "J Cachexia Sarcopenia Muscle"[ta] OR "Haematologica"[ta] '
    'OR "Adv Nutr"[ta] OR "Clin Nutr"[ta] OR "Nutr Rev"[ta] OR "Am J Clin Nutr"[ta] '
    'OR "J Med Internet Res"[ta] OR "Psychol Med"[ta] OR "Lancet Psychiatry"[ta] '
    'OR "JAMA Psychiatry"[ta] OR "Neurosci Biobehav Rev"[ta] OR "BMJ"[ta] '
    'OR "J Clin Epidemiol"[ta] OR "Lancet Healthy Longev"[ta] OR "Int J Surg"[ta]'
)
SR_FILTER = ('systematic review[ti] OR meta-analys*[ti] OR scoping review[ti] '
             'OR systematic review[pt] OR meta-analysis[pt]')
CANCER = ('cancer[ti] OR oncolog*[ti] OR neoplas*[ti] OR chemotherapy[ti] '
          'OR malignan*[ti] OR tumour[ti] OR tumor[ti]')

CONCEPTS = {
    "treatment_ovarian": 'ovarian[ti] AND (treatment[ti] OR therapy[ti] OR management[ti])',
    "functional": ('"functional status"[tiab] OR "physical function*"[tiab] '
                   'OR "activities of daily living"[tiab] OR "functional decline"[tiab] '
                   'OR "physical performance"[tiab] OR disability[ti]'),
    "cognition": 'cognitive[ti] OR cognition[ti] OR neurocognitive[ti] OR chemobrain[tiab]',
    "depression": 'depression[ti] OR depressive[ti] OR distress[ti]',
    "nutrition": ('malnutrition[ti] OR "nutritional status"[ti] OR cachexia[ti] '
                  'OR "nutritional support"[ti] OR "weight loss"[ti] OR sarcopenia[ti]'),
    "hrqol": '"quality of life"[ti] OR HRQOL[ti] OR "patient-reported outcome*"[ti]',
    "symptoms": ('"symptom burden"[ti] OR "symptom cluster*"[ti] OR symptoms[ti] '
                 'OR "symptom management"[ti] OR "patient-reported outcome*"[ti]'),
    "satisfaction": ('"patient satisfaction"[ti] OR satisfaction[ti] '
                     'OR "patient experience*"[ti]'),
}


def get(url):
    for attempt in range(4):
        try:
            return json.loads(urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=90).read())
        except Exception:
            if attempt == 3:
                raise
            time.sleep(3 * (attempt + 1))


def run(concept_query, label, retmax=30):
    term = (f"({concept_query}) AND ({CANCER}) AND ({SR_FILTER}) "
            f"AND ({HIGH_IF_JOURNALS})")
    d = get(f"{EUT}/esearch.fcgi?db=pubmed&retmode=json&retmax={retmax}"
            f"&term={urllib.parse.quote(term)}")["esearchresult"]
    ids = d.get("idlist", [])
    print(f"\n### {label}   hits={d.get('count')}   showing {len(ids)}")
    if not ids:
        return
    time.sleep(0.4)
    r = get(f"{EUT}/esummary.fcgi?db=pubmed&retmode=json&id={','.join(ids)}")["result"]
    for p in r.get("uids", []):
        rec = r[p]
        pmc = next((i["value"] for i in rec.get("articleids", [])
                    if i.get("idtype") == "pmc"), "")
        au = (rec.get("authors") or [{}])[0].get("name", "")
        print(f"  {p}  {(rec.get('pubdate') or '')[:4]}  "
              f"{'PMC' if pmc else '   '}  "
              f"{(rec.get('fulljournalname') or '')[:30]:30s}  {au[:18]:18s}  "
              f"{rec.get('title','')[:88]}")
    time.sleep(0.4)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        print("Built-in concepts:", ", ".join(CONCEPTS))
        return
    if args[0] == "--terms":
        run(" ".join(args[1:]), "custom")
    elif args[0] == "--all":
        for k, v in CONCEPTS.items():
            run(v, k)
    else:
        for a in args:
            if a not in CONCEPTS:
                print(f"unknown concept '{a}'. Known: {', '.join(CONCEPTS)}")
                continue
            run(CONCEPTS[a], a)


if __name__ == "__main__":
    main()
