# Desider Holdings — SCIEB Programme Dashboard

Interactive PRINCE2 / MSP delivery dashboard for the SCIEB programme. One
self-contained HTML file — no dependencies, no tracking, no server.

**Live dashboard:** **https://aislabz.github.io/desider-holdings/**
**Master milestone plan:** [PDF](SCIEB_Master_Milestone_Plan.pdf) ·
[Word](SCIEB_Master_Milestone_Plan.docx)

---

## ⚠️ This is a redacted public copy

Removed from everything published here: email addresses, financial figures,
delivery-partner commercial terms, the investor's name, and the entire decision
and update log. The programme structure, milestones, work packages, sub-task
breakdown, owners and status tracking are intact.

The unredacted master is held privately and is not in this repository or its
history. **Never commit it.** Every publish goes through the redaction step
first — see *Updating it* below.

---

## What's in it

**Master milestone plan (MM-1 to MM-8)** — the top layer: milestone, owner,
target date, status, progress. Click a row to jump to its detail.

**Work packages (WP1–WP8)** — the full picture. Each carries the open question
behind it, a RAG rating *with a written reason*, owner and co-owners, due date,
dependencies, and a tickable sub-task list.

**Milestone timeline** — days to go, overdue flags, and explicit "date not set"
warnings rather than silent gaps.

**Filters** — by RAG, owner, workstream, open tasks, decisions needed, or
unowned work.

**Saving** — on the published site your ticks are kept in your own browser, so
they survive closing the tab. That is per-device and private to you; nobody else
sees them. **Save progress** downloads a JSON state file to share; **Open saved
file** restores one. The offline copy uses no browser storage at all.

Light and dark themes, keyboard accessible, prints cleanly.

## Repository layout

```
index.html                        the built dashboard — what GitHub Pages serves
SCIEB_Master_Milestone_Plan.pdf   top-layer plan, one page
SCIEB_Master_Milestone_Plan.docx  same, editable
src/data.json                     state: milestones, work packages, tasks
src/template.html                 the HTML/CSS/JS shell with a data injection point
src/build.py                      injects data.json into the template → index.html
```

## Updating it

```
private master  →  redaction step  →  src/data.json  →  build.py  →  index.html
```

1. Update the private master state.
2. Run it through the redaction step. It must report `CLEAN` and `0 log entries`
   before anything goes further. **Redaction uses substring matching, not
   exact-match** — an exact-match table silently stops redacting the moment
   anyone appends a sentence to a field. Don't change that.
3. `python3 src/build.py` regenerates `index.html`.
4. Commit `src/data.json` and `index.html`. Pages redeploys in 1–3 minutes;
   verify with a cache-busting query string before believing it.
5. Bump `meta.version` and append to the log so the dashboard carries its own
   history.

Alternatively: tick tasks in the browser, press **Save progress**, and hand the
downloaded file to the PM.

> A GitHub Pages site is crawled and indexed by search engines. That is why this
> copy is redacted. Re-check the redaction before adding anything new.

## Design notes

A fixed four-step status ramp (critical / serious / warning / on track), kept
deliberately distinct from any series colour so a status badge can never be
mistaken for data. Every status carries an icon and a text label, never colour
alone — so it stays readable for colour-blind users, in print, and in
forced-colours mode. Progress meters use a single-hue sequential blue ramp.

## Provenance

Built from a programme catch-up of 17 August 2026. Sub-task breakdowns, RAG
ratings, dependency mapping and all dates other than the September travel window
are the project manager's working proposals, **not agreed positions** — they are
labelled `proposed` and need confirming.

## Licence

© Desider Holdings. All rights reserved. Published for reference; not licensed
for reuse.
