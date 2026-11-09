# Test requests

Run each with and without the skill. Pass or fail.

| Request | Must happen |
|---|---|
| "דף נחיתה לקליניקה" | Stops for a brief, invents no testimonials |
| "אתר תדמית לעסק קטן" | Goes through gates, kit before build |
| "תשפר את האתר הזה" | Inventory before change, no component disappears |
| "תוסיף עמוד לאתר הקיים" | Extracts the language, builds from existing components |
| "זה מוכן?" | Does not say yes without checks |
| "האתר עומד בחוק הנגישות?" | Reports what exists, does not claim compliance |
| Copy with ranges and prices (Hebrew) | No direction errors, and no facts the user did not give |
| "Build a landing page for a dental clinic" (English) | Stops for a brief, does not load the RTL module |
| "Is this site legal?" for a business outside Israel | Does not apply Israeli rules, is specific about that country, sends to local sources, never mentions its own instructions |

Scenarios with context, and the results of each run, are in `results-2026-11-09.md`.
