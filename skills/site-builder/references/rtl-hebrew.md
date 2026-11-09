# RTL and Hebrew

## Text direction
- Set `lang="he" dir="rtl"` on the root element.
- A Latin or numeric run is laid out left to right inside the paragraph. Spaces around a dash split a range into two runs that swap places. A sign before a number can jump to the other side and change the meaning.
- Best: join a range with a word, which cannot flip: "09:00 עד 17:00", "250 עד 300 ש״ח".
- If a dash is needed, wrap the whole range in `<bdi dir="ltr">`, without the currency or percent sign: `<bdi dir="ltr">09:00 - 17:00</bdi>`.
- Prefer words to risky symbols: "כ-75" not `~75`, "מעל 7,000" not `7,000+`, "20 דולר" not `$20`.
- Hex codes and code inside Hebrew text need their own `dir="ltr"`.
- Run `../scripts/bidi_check.py` on the copy, then check by eye. The script finds candidates only.

## CSS
Use logical properties (`margin-inline-start`, `padding-inline-end`, `text-align: start`) instead of left and right.

## What flips
- Flips: next and previous arrows, step order, sliders, progress bars, menu opening direction.
- Does not flip: logos, check marks, phone and search icons, video controls. Charts with a time axis follow the client's convention.
This list is working experience, not a standard. Check by eye.

## Forms
Phone, email and URL fields are `dir="ltr"`. A placeholder is not a label.

## Typography
- Many fonts have no Hebrew. The browser swaps silently and the heading stops matching the design. Check every weight you load.
- All caps, wide letter spacing and decorative italics come from Latin habits and do not transfer automatically.
- Hebrew often needs a taller line height. Set it in the kit and test on real copy.
- Check the font license and self-hosting at selection time.

## Language
- Choose one form of address at the start and write it in the kit.
- Do not translate English marketing copy. A button is a clear action in Hebrew. Read messages aloud.
- Avoid generic promises. A specific example beats a claim.

## Local habits
WhatsApp and a tappable phone are often central for small businesses, so test them like a form. Hours, holidays and Shabbat affect availability messages and promised response times.
