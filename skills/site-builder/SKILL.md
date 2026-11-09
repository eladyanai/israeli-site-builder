---
name: site-builder
description: Plan, design, build, check or redesign a website with an AI agent, in any language and on any platform, including a landing page, a page inside an existing site, or a "is this ready?" review. Use for "build me a website", "landing page", "redesign", "make the site better", "is this ready to launch", and in Hebrew "תבנה לי אתר", "עמוד נחיתה", "רידיזיין", "תשפר את האתר". Runs a 7-step process with human approval gates and refuses to call work ready without real browser checks. Adds a Hebrew and RTL layer, and Israeli legal notes, when the site needs them.
---

# Site builder

Follow the steps in order and stop at each gate. A fast agent with no gates only makes mistakes faster.

Before anything else, classify the request: new site, redesign, polish, or a page inside an existing site. Then find out which design language is already locked. On an existing site, read 2-3 recent pages first: the theme's colors alone are not its language.

Then note three facts that decide which modules apply: the site's language and direction, the business's country, and the platform.

## The 7 steps

| # | Step | Output | Gate |
|---|---|---|---|
| 1 | Discovery and planning | Brief, audience, sitemap, message bank | Brief approved |
| 2 | Content | Content document, with anything missing marked as missing | Messages approved |
| 3 | Visual design | Brand language, 2-3 styles, locked design kit, then directions inside it | Kit locked, direction chosen |
| 4 | Build | List available components first, build from them, on staging | Approval before any write to a live site |
| 5 | QA | Check report with screenshots | "Ready" only after the report |
| 6 | Marketing and SEO | Launch checklist | Approval to go live |
| 7 | Maintenance | Backups, updates, handover document | - |

## Core: read when needed

| When | Read |
|---|---|
| Starting any step | `references/process.md` |
| Before writing to any site | `references/boundaries.md` |
| Design work, or starting a kit | `references/design-kit.md`, `templates/DESIGN.md` |
| Asking the client for materials | `references/client-materials.md`, `templates/brief.md` |
| Before saying anything is ready | `references/ready-checks.md` |
| Before going live | `references/launch-checklist.md` |

## Modules: load only when they apply

| When | Read |
|---|---|
| The site is in Hebrew, or any right-to-left language | `references/rtl-hebrew.md` |
| The business operates in Israel | `references/israel-requirements.md` |
| Building in WordPress or Elementor | `references/elementor.md` |

Outside Israel, the same legal topics exist (accessibility, privacy and cookies, marketing consent), but this skill holds no notes on them. Say so, and send the client to local sources and a lawyer.

## Scripts

- `scripts/contrast.py '#111223' '#F16A55'` computes contrast. Any site.
- `scripts/bidi_check.py page.html` lists text that may break in RTL. RTL sites only.

## Redesign or polish

Inventory every component first, including galleries, animations and icons. Nothing is removed without approval by name. Motion that worked stays. Take before and after screenshots.

## Report

End every piece of work with what changed, what was checked, and what was not checked.
