# israeli-site-builder

> **גרסה מוקדמת.** עוד לא נבדקה על פרויקט אמיתי. אשמח לדיווח על מה שנשבר.
>
> **Early version.** Not yet run on a real project. Reports of what breaks are welcome.

סקיל של [DivineSites](https://divinesites.co.il) ל-Claude Code לבניית אתרים עם סוכן AI: תהליך של 7 שלבים עם נקודות עצירה לאישור אדם, גבולות גזרה ובדיקות בדפדפן אמיתי לפני שאומרים "מוכן". הליבה כללית לכל שפה ופלטפורמה, ויש שכבה לאתר בעברית ולדרישות בישראל.

לא עובדים עם Claude Code? [המדריך](guide/before-you-ask-ai-to-build-a-website.he.md) הוא אותו ידע בקובץ אחד, להדביק או לתת לכל כלי AI לקרוא לפני שמבקשים ממנו לבנות אתר.

A Claude Code skill by [DivineSites](https://divinesites.co.il) for building websites with an AI agent: a 7-step process with human approval gates, clear boundaries, and real-browser checks. The core works for any language and platform, with an extra layer for Hebrew, RTL and Israeli requirements.

Not on Claude Code? [The guide](guide/before-you-ask-ai-to-build-a-website.he.md) (Hebrew) holds the same knowledge in one file to paste into any AI tool before asking it to build a site.

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

Then ask for a site or landing page, or run `/israeli-site-builder:site-builder`.

## Safety

The skill asks before writing to a live site, but you approve what the agent does. Read it before you install it, as with any plugin. It has no hooks and runs nothing on its own. The two scripts run only when called.

## What is inside

- `skills/site-builder/SKILL.md`: the 7-step process and its gates.
- `skills/site-builder/references/`: the core (process, boundaries, design kit, client materials, ready checks, launch checklist) and modules loaded only when they apply (RTL and Hebrew, Israeli requirements, Elementor).
- `guide/`: the same knowledge as one article for any AI tool.
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
