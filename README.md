# Desider Holdings — SCIEB Programme Dashboard

An interactive PRINCE2 / MSP delivery dashboard for the SCIEB programme. Single
self-contained HTML file — no build step needed to view it, no dependencies, no
tracking, no server.

**Live dashboard:** **https://susman2005.github.io/desider-holdings/**

---

## ⚠️ This is a redacted public copy

Email addresses, financial figures and delivery-partner commercial terms have
been removed. The programme structure, work packages, sub-task breakdown and
status tracking are intact. The unredacted master is held privately and is not
in this repository or its history.

If you are maintaining this: **do not commit the unredacted state file.** Run it
through the redaction step first and keep `data.private.json` out of git — it is
already listed in `.gitignore`.

---

## What it does

- **8 work packages** (WP1–WP8) covering contract, data, pipeline, finance,
  delivery partner, team logistics, the product demo, and governance
- **66 sub-tasks** with per-task owners and tickable progress
- **RAG status** per work package, each with a written reason for the rating —
  status is never carried by colour alone (icon + label on every badge)
- **Original priorities scorecard** tracked against the programme's stated goals
- **Milestone timeline** with days-to-go, overdue flags, and explicit
  "date not set" warnings
- **Filters** by RAG, owner, workstream, open tasks, decisions needed, unowned
- **Decision & update log** you can append to in the browser
- **Export state (JSON)** to hand progress back for the next update cycle
- Light and dark themes, keyboard-accessible, prints cleanly

## Repository layout

```
index.html        the built dashboard — this is what GitHub Pages serves
src/data.json     the state file: work packages, tasks, milestones, log
src/template.html the HTML/CSS/JS shell, with a data injection point
src/build.py      injects data.json into the template → index.html
```

## Updating it

Edit `src/data.json`, then rebuild:

```bash
python3 src/build.py
```

That regenerates `index.html`. Commit both. Alternatively, tick tasks in the
browser, press **Export state (JSON)**, and drop the downloaded file in as the
new `src/data.json`.

Bump `meta.version` and append to the `log` array on each update so the
dashboard carries its own change history.

## Setup — enabling GitHub Pages

1. Push this repository to GitHub (public).
2. Go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**.
4. Set branch to `main` and folder to `/ (root)`. Save.
5. Wait ~60 seconds. The site appears at
   `https://susman2005.github.io/desider-holdings/`.

`.nojekyll` is included so GitHub serves the files as-is rather than running
them through Jekyll.

> **Note:** a GitHub Pages site is crawled and indexed by search engines. That is
> why the content here is redacted. Re-check the redaction before adding
> anything new.

## Design notes

Colour follows a validated palette: a fixed four-step status ramp
(critical / serious / warning / good) kept deliberately separate from any
categorical series colour, so a status badge can never be mistaken for a data
series. Progress meters use a single-hue sequential blue ramp. Every status is
paired with an icon and a text label, so the dashboard remains readable for
colour-blind users, in print, and in forced-colours mode.

No `localStorage` or any browser storage is used — state lives in memory for the
session and is persisted by exporting JSON. That keeps the file portable and
means opening it from a file:// URL, a shared drive, or Pages all behave
identically.

## Provenance

Built from a programme catch-up email of 17 August 2026. Sub-task breakdowns,
RAG ratings, dependency mapping and all dates other than the September travel
window are the project manager's working proposals, not agreed positions —
they are labelled `proposed` in the dashboard and need confirming.

## Licence

© Desider Holdings. All rights reserved. Published for reference; not licensed
for reuse.
