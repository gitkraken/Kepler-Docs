#!/usr/bin/env python3
"""Regenerate llms.txt and llms-full.txt from kepler/*.md.

Both files used to be hand-written, which is why they went stale. This derives
them from the pages themselves. Section grouping comes from preview/nav.json —
the one place the docs IA is written down, since the real help-center nav lives
in WordPress.

Run:  python3 scripts/build-llms.py
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PAGES = REPO / "kepler"
SKIP = {"kepler-New-Page-Template.md"}
FULL_FIELDS = ["product", "feature", "content_type", "audience", "plan_required",
               "status", "last_verified"]
FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)

BLURB = ("Kepler is GitKraken's Agentic Development Environment (ADE) — it pulls every "
         "issue and pull request assigned to you into one place, then hands any of it to "
         "the coding agent you already use (Claude Code, Codex, Copilot, Cursor, Auggie, "
         "or OpenCode) with the context already attached.")


def parse(path):
    m = FM_RE.match(path.read_text(encoding="utf-8"))
    if not m:
        sys.exit(f"{path.name}: no YAML frontmatter")
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km:
            val = km.group(2).strip()
            # A value that needed YAML quoting (a description containing ": ",
            # say) keeps its quotes through this regex parser; strip them so
            # they do not reach llms.txt.
            if len(val) > 1 and val[0] == val[-1] and val[0] in ('"', "'"):
                val = val[1:-1]
            fm[km.group(1)] = val
    return fm, m.group(2)


def clean(body):
    body = re.sub(r"<!--.*?-->\n?", "", body, flags=re.S)
    body = re.sub(r"<figure>.*?</figure>\n?", "", body, flags=re.S)
    body = re.sub(r"^<kbd>.*?</kbd>\n+", "", body)
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def write(path, text):
    """LF on every platform, so regenerating on Windows is not a whole-file diff."""
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def main():
    nav = json.loads((REPO / "preview" / "nav.json").read_text(encoding="utf-8"))
    listed = [f for s in nav["sections"] for f in s["pages"]]
    on_disk = {p.name for p in PAGES.glob("*.md")} - SKIP
    if missing := sorted(on_disk - set(listed)):
        sys.exit(f"Not in preview/nav.json, so it would be silently dropped: {missing}")

    included, excluded, out, full = [], [], [], []
    for section in nav["sections"]:
        rows = []
        for f in section["pages"]:
            fm, body = parse(PAGES / f)
            if fm.get("llms_include") != "true":
                excluded.append(f)
                continue
            rows.append((f, fm, body))
            included.append(f)
        if rows:
            out.append(f"## {section['title']}\n")
            for f, fm, _ in rows:
                out.append(f"- [{fm['title']}](https://help.gitkraken.com/kepler/"
                           f"{f[:-3].lower()}/): {fm['description']}")
            out.append("")
            for f, fm, body in rows:
                full.append("---")
                full.append(f"# {fm['title']}")
                full.append(f"URL: https://help.gitkraken.com/kepler/{f[:-3].lower()}/")
                full += [f"{k}: {fm[k]}" for k in FULL_FIELDS if k in fm]
                full += ["", clean(body), ""]

    excluded += sorted(SKIP)
    head = ["# Kepler", "", f"> {BLURB}", "",
            f"Scope: {len(included)} pages included. "
            f"Excluded: {len(excluded)} — {', '.join(sorted(excluded))}.", ""]
    write(REPO / "llms.txt", "\n".join(head + out).rstrip() + "\n")

    stamp = date.today().isoformat()
    fhead = ["# Kepler Documentation — llms-full.txt", f"Generated: {stamp}",
             f"Pages: {len(included)}", "Source: https://help.gitkraken.com/kepler/", ""]
    write(REPO / "llms-full.txt", "\n".join(fhead + full).rstrip() + "\n")

    print(f"llms.txt: {len(included)} pages. llms-full.txt: "
          f"{(REPO / 'llms-full.txt').stat().st_size} bytes.")
    print(f"Excluded: {', '.join(sorted(excluded))}")


if __name__ == "__main__":
    main()
