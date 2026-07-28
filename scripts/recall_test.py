#!/usr/bin/env python3
"""Relative-recall test: does the drafted strategy actually retrieve studies it must find?

Usage: python3 scripts/recall_test.py [--write]
       --write  regenerate draft/recall.md

Sizing a strategy (scripts/test_draft.py) says whether it is screenable. This says whether
it is sensitive. Each known item in data/recall_known_items.yml is a real study that a
review of ovarian cancer treatment and patient-centred outcomes in older adults must not
miss. Every block, and the recommended primary search, is intersected with the known-item
UIDs in a single query, so a miss is exact rather than inferred.

First the titles of all known items are re-fetched from PubMed and compared with the
recorded titles, so a mistyped PMID cannot silently pass as a retrieval failure.
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def stamp():
    """UTC date of this run, so a quoted count can always be dated."""
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
EUT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UA = {"User-Agent": "sunami-lab-review/1.0 (mailto:chenyangsu87@gmail.com)"}


def post(endpoint, params):
    data = urllib.parse.urlencode(params).encode()
    for attempt in range(5):
        try:
            return json.loads(urllib.request.urlopen(
                urllib.request.Request(f"{EUT}/{endpoint}", data=data, headers=UA),
                timeout=120).read())
        except Exception:
            if attempt == 4:
                raise
            time.sleep(3 * (attempt + 1))


def flat(q):
    return " ".join(q.split())


def main():
    items = yaml.safe_load(open(os.path.join(ROOT, "data", "recall_known_items.yml")))["items"]
    d = yaml.safe_load(open(os.path.join(ROOT, "draft", "blocks_pubmed.yml")))
    blocks = d["blocks"]
    pmids = [str(i["pmid"]) for i in items]
    by_pmid = {str(i["pmid"]): i for i in items}

    # --- step 1: confirm every PMID is the paper we think it is -----------------------
    def norm(s):
        """Lowercase, collapse every non-alphanumeric run to one space. Applied to BOTH
        sides so hyphenation and punctuation differences cannot cause a false mismatch."""
        return " ".join("".join(ch if ch.isalnum() else " " for ch in (s or "").lower()).split())

    r = post("esummary.fcgi", {"db": "pubmed", "retmode": "json", "id": ",".join(pmids)})["result"]
    bad = []
    for p in pmids:
        rec = r.get(p)
        if not rec or "error" in rec:
            bad.append((p, "PMID does not resolve"))
            continue
        live, mine = norm(rec.get("title", "")), norm(by_pmid[p]["title"])
        # the recorded title may be abbreviated, so require a solid shared prefix either way
        if not (mine[:45] in live or live[:45] in mine):
            bad.append((p, f"title mismatch: PubMed says '{rec.get('title','')[:70]}'"))
    print(f"known items: {len(pmids)}   PMID/title check: "
          f"{'ALL OK' if not bad else str(len(bad)) + ' PROBLEM(S)'}")
    for p, why in bad:
        print(f"   {p}: {why}")
    if bad:
        sys.exit("Fix the known-item list before trusting the recall numbers.")
    time.sleep(0.5)

    uid_set = " OR ".join(f"{p}[uid]" for p in pmids)

    def retrieved(term):
        res = post("esearch.fcgi", {"db": "pubmed", "retmode": "json", "retmax": "200",
                                    "term": f"({term}) AND ({uid_set})"})["esearchresult"]
        time.sleep(0.5)
        return set(res.get("idlist", []))

    # --- step 2: each block on its own -------------------------------------------------
    print("\n=== each block against the known items ===")
    hits = {}
    for k, b in blocks.items():
        got = retrieved(flat(b["query"]))
        hits[k] = got
        print(f"  {len(got):>2}/{len(pmids)}  {k:<16} {b['label']}")

    # --- step 3: the combinations that matter ------------------------------------------
    P, I = flat(blocks["P_ovarian"]["query"]), flat(blocks["I_treatment"]["query"])
    A = flat(blocks["A_older"]["query"])
    OUT = " OR ".join(f"({flat(blocks[k]['query'])})" for k in blocks if k.startswith("O"))

    combos = {
        "P": f"({P})",
        "P AND I": f"({P}) AND ({I})",
        "P AND anyOutcome (no treatment block)": f"({P}) AND ({OUT})",
        "P AND I AND anyOutcome": f"({P}) AND ({I}) AND ({OUT})",
        "P AND I AND age AND anyOutcome": f"({P}) AND ({I}) AND ({A}) AND ({OUT})",
    }
    print("\n=== combinations against the known items ===")
    cres = {}
    for name, term in combos.items():
        got = retrieved(term)
        cres[name] = got
        miss = [p for p in pmids if p not in got]
        print(f"  {len(got):>2}/{len(pmids)} ({100*len(got)/len(pmids):5.1f}%)  {name}")
        for p in miss:
            it = by_pmid[p]
            print(f"        MISS {p}  {it['title'][:78]}")

    if "--write" in sys.argv:
        out = os.path.join(ROOT, "draft", "recall.md")
        L = ["# Relative-recall test of the drafted strategy", "",
             f"_Run {stamp()}._", "",
             "Generated by `python3 scripts/recall_test.py --write`.", "",
             f"**{len(pmids)} known items** — real studies that a review of ovarian cancer "
             "treatment and patient-centred outcomes in older adults must not miss. Sources "
             "and the reason each is eligible are in `data/recall_known_items.yml`. Every "
             "PMID and title is re-verified against PubMed before the test runs.", "",
             "## Recall of the candidate searches", "",
             "| Search | Known items retrieved | Recall |", "|---|---|---:|"]
        for name in combos:
            n = len(cres[name])
            L.append(f"| {name} | {n}/{len(pmids)} | {100*n/len(pmids):.0f}% |")
        L += ["", "## Misses", ""]
        any_miss = False
        for name in combos:
            miss = [p for p in pmids if p not in cres[name]]
            if not miss:
                L.append(f"**{name}** — no misses.")
                L.append("")
                continue
            any_miss = True
            L += [f"**{name}** — {len(miss)} missed:", ""]
            for p in miss:
                it = by_pmid[p]
                blocks_hit = [k for k in blocks if p in hits[k]]
                L.append(f"- `{p}` {it['title']} *({it['journal']}, {it['year']})* — "
                         f"matched blocks: {', '.join(blocks_hit) or 'none'}")
            L.append("")
        if not any_miss:
            L.append("No misses in any candidate search.")
            L.append("")
        L += ["## Each block on its own", "",
              "How many of the known items each block retrieves in isolation. A low number "
              "is not necessarily bad — an outcome block is meant to be selective — but a "
              "block that retrieves none of the items in its own domain is broken.", "",
              "| Block | Known items | Concept |", "|---|---:|---|"]
        for k, b in blocks.items():
            L.append(f"| `{k}` | {len(hits[k])}/{len(pmids)} | {b['label']} |")
        L += ["", "## Per-domain check", "",
              "| Domain | Items | Retrieved by its own outcome block |", "|---|---:|---:|"]
        dom_block = {"functional": "O1_functional", "cognition": "O2_cognition",
                     "depression": "O3_depression", "nutrition": "O4_nutrition",
                     "hrqol": "O5_hrqol", "symptoms": "O6_symptoms",
                     "satisfaction": "O7_satisfaction"}
        doms = {}
        for it in items:
            doms.setdefault(it.get("domain", "other"), []).append(str(it["pmid"]))
        for dom, ps in sorted(doms.items()):
            bk = dom_block.get(dom)
            if not bk:
                L.append(f"| {dom} | {len(ps)} | n/a |")
            else:
                n = sum(1 for p in ps if p in hits[bk])
                L.append(f"| {dom} | {len(ps)} | {n}/{len(ps)} (`{bk}`) |")
        open(out, "w").write("\n".join(L) + "\n")
        print("\nwrote draft/recall.md")


if __name__ == "__main__":
    main()
