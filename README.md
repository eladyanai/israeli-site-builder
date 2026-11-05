# israeli-site-builder

> **גרסה מוקדמת.** עוד לא נבדקה על פרויקט אמיתי. אשמח לדיווח על מה שנשבר.
>
> **Early version.** Not yet run on a real project. Reports of what breaks are welcome.

סקיל של [DivineSites](https://divinesites.co.il) ל-Claude Code לבוני אתרים ישראלים: תהליך של 7 שלבים עם נקודות עצירה לאישור אדם, גבולות גזרה ובדיקות בדפדפן אמיתי לפני שאומרים "מוכן".

A Claude Code skill by [DivineSites](https://divinesites.co.il) for people building Hebrew websites in Israel: a 7-step process with human approval gates, clear boundaries, and real-browser checks.

Background article (Hebrew): https://divinesites.co.il/blog/website-design/claude-code-skill-israeli-websites/

## Install

In Claude Code, version 2.1.275 or later:

```
/plugin install israeli-site-builder --marketplace eladyanai/israeli-site-builder
```

Older versions:

```
/plugin marketplace add eladyanai/israeli-site-builder
/plugin install israeli-site-builder@israeli-site-builder
```

Without the plugin system: [download the release](https://github.com/eladyanai/israeli-site-builder/releases/latest) and copy `skills/site-builder` to `~/.claude/skills/`.

Then ask for a Hebrew site or landing page, or run `/israeli-site-builder:site-builder`.

## Safety

The skill asks before writing to a live site, but you approve what the agent does. Read it before you install it, as with any plugin. It has no hooks and runs nothing on its own. The two scripts run only when called.

## What is inside

- `skills/site-builder/SKILL.md`: the 7-step process and its gates.
- `skills/site-builder/references/`: process detail, boundaries, RTL and Hebrew, design kit, Elementor, ready checks, launch checklist, Israeli requirements, client materials.
- `skills/site-builder/templates/`: brief and `DESIGN.md`.
- `skills/site-builder/scripts/`: contrast and RTL checks.
- `evals/`: test requests.

Not yet here: the client board module, and a run on a real project.

## Not legal advice

This skill does not promise compliance with accessibility, privacy or marketing law.

## Credits

The structure of the `DESIGN.md` template draws on [VoltAgent/awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design), and the signs of generic AI design draw on [PyModel/designer-skill](https://github.com/PyModel/designer-skill). Both are MIT licensed.

## License

MIT. See [LICENSE](LICENSE).
