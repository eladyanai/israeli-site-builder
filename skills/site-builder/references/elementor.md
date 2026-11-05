# WordPress and Elementor

- Elementor renders from `_elementor_data`. On an Elementor page, editing the regular post content changes nothing visitors see.
- Build from widgets: text, headings, table of contents and FAQ, so the client can edit them. HTML is the exception. Tables are one, because core Elementor has no table widget.
- Check which widgets and plugins exist on this site. Never assume.
- Use the kit's global colors and fonts. Do not invent a palette.
- Scope custom CSS under one unique class. A global selector on one page can break another.
- Repeater rows need unique ids. Without them, the last row's style can override all the others.
- After any write, read the structure back, clear the cache, and look at the public address. Injecting into the DOM skips WordPress filters, so it is not a final check.
- Scripts inside a WordPress content block can be changed on output, for example `&&` becoming entities. Listen for page errors on the public address.
