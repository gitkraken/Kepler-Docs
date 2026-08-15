# Local docs preview

Renders the pages in `../kepler/` into a single self-contained HTML file with a
left nav, so you can read the docs as a site before they go into WordPress.

## Requirements

`python3` and the `markdown` package. Nothing else — no server, no npm, no
build step. `index.html` is self-contained, so you can send it to someone and
it works.

macOS ships `python3`, but **`markdown` is not installed by default.** If
`build.py` exits with `This needs the markdown package`, install it:

```
pip3 install --user markdown
```

On a Homebrew Python you may get `error: externally-managed-environment`
(PEP 668). Either of these works instead:

```
pip3 install --user --break-system-packages markdown
```

```
python3 -m venv preview/.venv && preview/.venv/bin/pip install markdown
# then build with:  preview/.venv/bin/python preview/build.py
```

The venv option keeps it out of your system Python. `preview/.venv/` is
gitignored.

## Use it

```
python3 preview/build.py
open preview/index.html
```

Re-run `build.py` after editing any markdown and reload the page.

## The nav

`nav.json` is the proposed left-nav structure for the help center. The real nav
is built in WordPress, not in this repo, so this file is the only place it's
written down. Edit it and re-run the build.

`build.py` fails loudly if a page exists in `kepler/` but is missing from
`nav.json`, or if `nav.json` names a page that doesn't exist — so the nav can't
drift out of sync with the content silently.

## What the preview shows that the real site won't

- **TODO annotations.** Inline `<!-- TODO(verify) -->` and `<!-- TODO(screenshot) -->`
  comments render as visible callouts. Toggle them off to read the page as a
  reader would.
- **A frontmatter strip** under each title, so stale `last_verified` stamps and
  wrong `status` values are obvious.
- **Length metrics** per page — word count and read time.

## What it deliberately doesn't do

It isn't pixel-matched to the help center theme. It's for checking structure,
flow, length, link integrity, and table rendering — not final visual design.
