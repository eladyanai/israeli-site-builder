# Design kit

The kit is a decision file the agent reads before every screen. Start from `../templates/DESIGN.md`. Never leave a value empty: an empty value invites invention.

## Must contain
- **Color:** name by role, exact value, why, computed contrast (`../scripts/contrast.py`), and a rule for text on each color.
- **Typography:** family, weight, size and line height per role, checked on real copy in the site's language. Hebrew: see `rtl-hebrew.md`.
- **Components:** button and form in every state: hover, focus, disabled, error, success.
- **Spacing and depth:** a fixed scale for spacing, radius and shadow.
- **Voice:** real samples and a say / do not say list. No lorem ipsum.
- **Images and motion:** style, what to avoid, duration, and behavior with reduced motion.
- **Direction:** on a right-to-left site, what flips and what does not (`rtl-hebrew.md`).
- **Lock history:** what was approved, when, and what it replaced.

## Existing site
Read 2-3 recent pages of the same type. Theme colors alone are not the language: backgrounds, fonts, buttons, radii and shadows on real pages are.

## Avoid generic AI design
A colored bar on one side of a card, gradient text, a card inside a card, identical spacing everywhere, an oversized heading, a small pill above the heading, and copy that sounds like a slogan. Look at the screenshot for these before saying ready.

## Check the kit itself
Compare the kit against the live site. A kit that states the wrong font is worse than no kit.
