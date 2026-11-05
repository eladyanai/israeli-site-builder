# Before saying "ready"

| Check | How |
|---|---|
| Widths 390, 600, 900, 1440 | Screenshot each, no horizontal scroll |
| Interaction | Hover, touch on mobile, open the menu |
| Button colors | Read text and background colors from the browser |
| Motion | Measure that the effect really changes with scroll or time |
| Forms | Send for real and confirm the email arrived |
| Text direction | Ranges, prices and phone numbers, by eye and by script |
| Not checked | Write it down. Video transparency on iPhone needs a real phone |

## Text direction

Wrap a number range in `<bdi>`, without the currency or percent sign. Spaces around a dash split it into two runs that swap places, and a sign before a number can jump to the other side and change the meaning without anyone noticing.
