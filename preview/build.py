#!/usr/bin/env python3
"""Render ../kepler/*.md into a single self-contained preview/index.html.

Pure stdlib + the `markdown` package. No server, no network.
Run:  python3 preview/build.py
"""
import html
import json
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit(
        "This needs the `markdown` package. Install it with:\n"
        "    pip3 install --user markdown\n"
        "If that reports an externally-managed environment (Homebrew Python), use:\n"
        "    pip3 install --user --break-system-packages markdown\n"
        "or a venv:\n"
        "    python3 -m venv preview/.venv && preview/.venv/bin/pip install markdown\n"
        "    preview/.venv/bin/python preview/build.py\n"
        "See preview/README.md."
    )

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
PAGES_DIR = REPO / "kepler"
SKIP = {"kepler-New-Page-Template.md"}

MD = markdown.Markdown(
    extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html", "toc"],
    output_format="html5",
)

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
TODO_RE = re.compile(r"<!--\s*TODO\((\w+)\):\s*(.*?)-->", re.S)


def parse(path):
    m = FM_RE.match(path.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"{path.name}: no YAML frontmatter")
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip()
    return fm, m.group(2)


def preprocess(body):
    """TODO comments -> visible blocks; site paths -> preview paths."""
    def todo(m):
        kind, text = m.group(1), " ".join(m.group(2).split())
        return (
            f'\n\n<div class="todo t-{kind}">'
            f'<span class="todo-k">{html.escape(kind)}</span>'
            f'<span class="todo-b">{html.escape(text)}</span></div>\n\n'
        )
    body = TODO_RE.sub(todo, body)
    # WordPress upload paths -> the repo's own images
    body = re.sub(r'(src=")/wp-content/uploads/', r'\1../_images/', body)
    # Internal doc links -> in-page routing
    body = re.sub(r"\]\(/kepler/([a-z0-9\-]+)\)", r"](#\1)", body)
    return body


def slug(name):
    return name[:-3].lower()


def main():
    nav = json.loads((HERE / "nav.json").read_text(encoding="utf-8"))
    on_disk = {p.name for p in PAGES_DIR.glob("*.md")} - SKIP
    in_nav = [f for s in nav["sections"] for f in s["pages"]]

    missing_file = [f for f in in_nav if f not in on_disk]
    missing_nav = sorted(on_disk - set(in_nav))
    dupes = sorted({f for f in in_nav if in_nav.count(f) > 1})
    problems = (
        [f"nav.json lists a page that does not exist: {f}" for f in missing_file]
        + [f"page exists but is not in nav.json: {f}" for f in missing_nav]
        + [f"page listed twice in nav.json: {f}" for f in dupes]
    )
    if problems:
        print("Nav is out of sync with the content:")
        for p in problems:
            print("  -", p)
        sys.exit(1)

    slugs = {slug(f) for f in in_nav}
    nav_html, articles, flat = [], [], []

    for section in nav["sections"]:
        cls = ' class="preview-only"' if section.get("preview_only") else ""
        nav_html.append(f'<div class="nav-sec"{cls}><h3>{html.escape(section["title"])}</h3><ul>')
        for f in section["pages"]:
            fm, body = parse(PAGES_DIR / f)
            s = slug(f)
            flat.append((s, fm.get("title", f)))
            nav_html.append(
                f'<li><a href="#{s}" data-slug="{s}">{html.escape(fm.get("title", f))}</a></li>'
            )

            MD.reset()
            rendered = MD.convert(preprocess(body))

            # dead internal links, checked after rewriting. A target is valid if it
            # is another page's slug or a heading id on this page.
            own_ids = set(re.findall(r'id="([^"]+)"', rendered))
            dead = sorted({h for h in re.findall(r'href="#([a-z0-9\-]+)"', rendered)
                           if h not in slugs and h not in own_ids and not h.startswith("_")})
            words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", rendered)))
            todos = len(TODO_RE.findall(body))

            chips = []
            for k in ("feature", "content_type", "status", "last_verified", "llms_include"):
                if k in fm:
                    bad = ' class="chip bad"' if (
                        (k == "last_verified" and fm[k] != "2026-08")
                        or (k == "status" and fm[k] not in ("GA", "retired"))
                    ) else ' class="chip"'
                    chips.append(f'<span{bad}>{k}: {html.escape(fm[k])}</span>')
            chips.append(f'<span class="chip">{words} words · ~{max(1, round(words/220))} min</span>')
            if todos:
                chips.append(f'<span class="chip warn">{todos} TODO</span>')
            if dead:
                chips.append(f'<span class="chip bad">dead links: {html.escape(", ".join(dead))}</span>')

            articles.append(
                f'<article id="{s}" data-slug="{s}" hidden>'
                f'<div class="meta">{"".join(chips)}</div>'
                f'<p class="desc">{html.escape(fm.get("description", ""))}</p>'
                f"{rendered}</article>"
            )
        nav_html.append("</ul></div>")

    prevnext = {}
    for i, (s, t) in enumerate(flat):
        prevnext[s] = {
            "prev": {"slug": flat[i-1][0], "title": flat[i-1][1]} if i else None,
            "next": {"slug": flat[i+1][0], "title": flat[i+1][1]} if i < len(flat)-1 else None,
        }

    out = (HERE / "template.html").read_text(encoding="utf-8")
    out = out.replace("%%SITE%%", html.escape(nav["site"]))
    out = out.replace("%%NAV%%", "\n".join(nav_html))
    out = out.replace("%%ARTICLES%%", "\n".join(articles))
    out = out.replace("%%PREVNEXT%%", json.dumps(prevnext))
    out = out.replace("%%FIRST%%", flat[0][0])
    (HERE / "index.html").write_text(out, encoding="utf-8")

    print(f"Built preview/index.html — {len(flat)} pages, {len(nav['sections'])} sections.")
    print(f"Open it:  open {HERE / 'index.html'}")


if __name__ == "__main__":
    main()
