#!/usr/bin/env python3
"""Static syntax check for the search strategies that cannot be executed.

Usage: python3 scripts/lint_strategies.py [--write]
       --write  regenerate draft/lint.md

The PubMed draft is executed by scripts/test_draft.py and scripts/recall_test.py. The Ovid
MEDLINE, Embase and Web of Science translations cannot be run without platform access, so
this catches the classes of error that do not need execution to detect:

  * unbalanced parentheses or quotation marks
  * curly quotation marks, which no platform parses as phrase delimiters
  * truncation inside a controlled-vocabulary heading  (exp neoplas*/ , 'neoplas*'/exp)
    - this is a real published error, present in Soong 2025's Embase strategy
  * line-number ranges (or/1-9) that reference lines the file does not contain
  * set references (#12, 4 and 21) that point at non-existent sets
  * field codes that do not exist on the stated platform
  * Web of Science tags used without '='

It reports problems, not style. A clean run does not mean a strategy is good; it means it
will parse.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OVID_FIELDS = {"mp", "ti", "ab", "tw", "kf", "kw", "pt", "sh", "fs", "af", "hw", "id",
               "ti,ab", "ti,ab,kf", "ti,ab,kw", "ab,ti", "ti,ab,kw.", "nm", "rn", "so"}
WOS_TAGS = {"TS", "TI", "AB", "AU", "DT", "LA", "PY", "SO", "AK", "KP", "ALL"}


def logical_statements(text, kind):
    """Return [(first_lineno, joined_statement)].

    The strategy files wrap long lines for readability, so a single search statement can
    span several physical lines. Checking balance per physical line produces nothing but
    false positives; statements have to be rejoined first. A new statement starts at an
    Ovid line number, or at a Web of Science field tag / boolean operator.
    """
    starts_new = (re.compile(r"^\s*\d+\s") if kind == "ovid"
                  else re.compile(r"^\s*(?:[A-Z]{2,3}\s*=|(?:NOT|AND)\s+[A-Z]{2,3}\s*=)"))
    out = []
    for raw in text.split("\n"):
        n = len(out)  # placeholder, replaced below
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        out.append(raw)
    # re-walk with real line numbers, joining continuations
    stmts, cur, cur_no = [], None, None
    for n, raw in enumerate(text.split("\n"), 1):
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        if cur is None or starts_new.match(raw):
            if cur is not None:
                stmts.append((cur_no, cur))
            cur, cur_no = s, n
        else:
            cur += " " + s
    if cur is not None:
        stmts.append((cur_no, cur))
    return stmts


def check_balance(lineno, s, problems, fname):
    if s.count("(") != s.count(")"):
        problems.append((fname, lineno, "unbalanced parentheses", s.strip()[:88]))
    if s.count('"') % 2:
        problems.append((fname, lineno, "odd number of double quotes", s.strip()[:88]))
    if s.count("'") % 2:
        problems.append((fname, lineno, "odd number of single quotes", s.strip()[:88]))
    for ch, name in (("“", "left curly double quote"), ("”", "right curly double quote"),
                     ("‘", "left curly single quote"), ("’", "right curly single quote")):
        if ch in s:
            problems.append((fname, lineno, f"{name} will not parse as a phrase delimiter",
                             s.strip()[:88]))


def lint_ovid(path, fname, agnostic_only=False):
    """Ovid MEDLINE / Embase: numbered lines, or/N-M ranges, .fs./.mp. field codes.

    agnostic_only=True runs just the checks that hold on any platform (curly quotes,
    truncation inside a controlled-vocabulary heading). Used for strategies/, whose files
    are transcriptions that often mix PubMed, Ovid and Web of Science syntax in one
    document, so Ovid line-number and field-code rules do not apply.
    """
    problems = []
    code = logical_statements(open(path).read(), "ovid")
    numbers = set()
    for n, s in code:
        m = re.match(r"\s*(\d+)\s", s)
        if m:
            numbers.add(int(m.group(1)))
    for n, s in code:
        if not agnostic_only:
            check_balance(n, s, problems, fname)
        else:
            # Only flag prose-vs-syntax issues on lines that actually look like a search
            # statement; these transcriptions also contain headings and narrative.
            looks_like_search = re.search(
                r"(\.mp\.|\.ti|\.ab|\.tw|\bexp \b|/\s|\[|\bTI \b|\bAB \b|TS=|\bMH \b|\bor/|"
                r"\bOR\b|\bAND\b|\badj\d|\bnear/)", s)
            if looks_like_search:
                for ch, name in (("\u201c", "left curly double quote"),
                                 ("\u201d", "right curly double quote")):
                    if ch in s:
                        problems.append((fname, n,
                                         f"{name} will not parse as a phrase delimiter",
                                         s.strip()[:88]))
        # truncation inside a subject heading
        for m in re.finditer(r"exp\s+[A-Za-z][^/\n]*\*[^/\n]*/", s):
            problems.append((fname, n, "truncation inside an exploded subject heading "
                             "- platforms reject this", m.group(0)[:70]))
        for m in re.finditer(r"'[^']*\*[^']*'\s*/\s*exp", s):
            problems.append((fname, n, "truncation inside an Emtree explosion "
                             "- Embase rejects this", m.group(0)[:70]))
        if agnostic_only:
            continue
        # or/N-M ranges must reference lines that exist
        for m in re.finditer(r"\bor/(\d+)-(\d+)", s):
            a, b = int(m.group(1)), int(m.group(2))
            missing = [x for x in range(a, b + 1) if x not in numbers]
            if missing:
                problems.append((fname, n, f"or/{a}-{b} references line(s) not present: "
                                 f"{missing[:8]}", s.strip()[:88]))
        # bare "N and M" set references
        for m in re.finditer(r"^\s*\d+\s+(\d+)\s+and\s+(\d+)", s):
            for g in m.groups():
                if int(g) not in numbers:
                    problems.append((fname, n, f"references set {g}, which is not defined",
                                     s.strip()[:88]))
        # field codes
        for m in re.finditer(r"\.([a-z,]{2,12})\.", s):
            f = m.group(1)
            if f not in OVID_FIELDS:
                problems.append((fname, n, f"unrecognised Ovid field code .{f}.",
                                 s.strip()[:88]))
    return problems


def lint_wos(path, fname):
    problems = []
    code = logical_statements(open(path).read(), "wos")
    for n, s in code:
        check_balance(n, s, problems, fname)
        for m in re.finditer(r"\b([A-Z]{2,3})\s*=", s):
            if m.group(1) not in WOS_TAGS:
                problems.append((fname, n, f"unrecognised Web of Science tag {m.group(1)}=",
                                 s.strip()[:88]))
        for m in re.finditer(r"\b(TS|TI|AB|DT|LA|PY)\b(?!\s*=)", s):
            if not re.search(rf"{m.group(1)}\s*=", s):
                problems.append((fname, n, f"{m.group(1)} used without '='", s.strip()[:88]))
        for m in re.finditer(r"\bNEAR\b(?!/\d)", s):
            problems.append((fname, n, "NEAR without /n - Web of Science needs NEAR/n",
                             s.strip()[:88]))
    return problems


def main():
    targets = [("draft/ovid_medline.txt", lint_ovid),
               ("draft/embase_ovid.txt", lint_ovid),
               ("draft/web_of_science.txt", lint_wos)]
    all_problems = []
    for rel, fn in targets:
        p = os.path.join(ROOT, rel)
        probs = fn(p, rel)
        all_problems += probs
        print(f"{rel}: {len(probs)} problem(s)")
        for _, n, why, snippet in probs:
            print(f"   line {n}: {why}\n      {snippet}")

    # also lint the published strategies transcribed into strategies/, read-only report
    print("\n--- published strategies in strategies/ (errors here are the AUTHORS', "
          "preserved deliberately) ---")
    pub = []
    sd = os.path.join(ROOT, "strategies")
    for fn in sorted(os.listdir(sd)):
        if not fn.endswith(".txt"):
            continue
        probs = lint_ovid(os.path.join(sd, fn), "strategies/" + fn, agnostic_only=True)
        pub += probs
        print(f"strategies/{fn}: {len(probs)} flagged")

    if "--write" in sys.argv:
        out = os.path.join(ROOT, "draft", "lint.md")
        L = ["# Static syntax check of the untested translations", "",
             "Generated by `python3 scripts/lint_strategies.py --write`.", "",
             "The PubMed draft is executed (`draft/counts.md`, `draft/recall.md`). The Ovid,",
             "Embase and Web of Science translations cannot be run without platform access,",
             "so they get a static check instead: balanced parentheses and quotes, curly",
             "quotes, truncation inside controlled-vocabulary headings, line-number ranges",
             "that reference missing lines, and field codes that do not exist on the stated",
             "platform.", "",
             "**A clean result means the strategy will parse. It does not mean it is good.**", ""]
        if all_problems:
            L += ["## Problems found in the drafted translations", "",
                  "| File | Line | Problem | Text |", "|---|---:|---|---|"]
            for f, n, why, snip in all_problems:
                safe = snip.replace("|", r"\|")
                L.append(f"| `{f}` | {n} | {why} | `{safe}` |")
        else:
            L += ["## Problems found in the drafted translations", "",
                  "None. All three translations pass every check above.", ""]
        L += ["", "## The published strategies in `strategies/`", "",
              "These are transcriptions of other people's published work. Anything flagged",
              "below is **their** error, preserved deliberately — see `strategies/README.md`.",
              "It is listed here so you know what you are inheriting if you reuse a block.", ""]
        if pub:
            L += ["| File | Line | Problem | Text |", "|---|---:|---|---|"]
            for f, n, why, snip in pub:
                safe = snip.replace("|", r"\|")
                L.append(f"| `{f}` | {n} | {why} | `{safe}` |")
        else:
            L.append("Nothing flagged.")
        open(out, "w").write("\n".join(L) + "\n")
        print("\nwrote draft/lint.md")


if __name__ == "__main__":
    main()
