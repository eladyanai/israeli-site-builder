---
name: site-builder
description: Plan, design, build, check or redesign a Hebrew website for an Israeli business, including a landing page, a page inside an existing site, or a "is this ready?" review. Use for "תבנה לי אתר", "עמוד נחיתה", "רידיזיין", "תשפר את האתר", RTL problems, or a Hebrew WordPress or Elementor site. Runs a 7-step process with human approval gates and refuses to call work ready without real browser checks.
---

# Site builder

Follow the steps in order and stop at each gate. A fast agent with no gates only makes mistakes faster.

Before anything else, classify the request: new site, redesign, polish, or a page inside an existing site. Then find out which design language is already locked. On an existing site, read 2-3 recent pages first: the theme's colors alone are not its language.

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

## Read when needed

| When | Read |
|---|---|
| Starting any step | `references/process.md` |
| Before writing to any site | `references/boundaries.md` |
| Hebrew copy, RTL layout, fonts | `references/rtl-hebrew.md` |
| Design work, or starting a kit | `references/design-kit.md`, `templates/DESIGN.md` |
| Asking the client for materials | `references/client-materials.md`, `templates/brief.md` |
| Building in WordPress or Elementor | `references/elementor.md` |
| Before saying anything is ready | `references/ready-checks.md` |
| Before going live | `references/launch-checklist.md` |
| Accessibility, privacy, cookies, mailing lists | `references/israel-requirements.md` |

## Scripts

- `scripts/contrast.py '#111223' '#F16A55'` computes contrast.
- `scripts/bidi_check.py page.html` lists text that may break in RTL.

## Redesign or polish

Inventory every component first, including galleries, animations and icons. Nothing is removed without approval by name. Motion that worked stays. Take before and after screenshots.

## Report

End every piece of work with what changed, what was checked, and what was not checked.
