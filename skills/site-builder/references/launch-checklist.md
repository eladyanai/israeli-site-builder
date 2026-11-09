# Launch checklist

Go through this before and after a site goes live. Each row says who can confirm it. `script` can be checked automatically, `browser` needs a real browser, `human` needs a person. A row you did not check is reported as not checked, never as passed.

## Before launch: content

| Check | How |
|---|---|
| No placeholder copy, lorem ipsum, sample posts or template demo pages | script |
| Site name and tagline are real | script |
| Home page is set and published | script |
| Phone, email, address and social links are correct | human |
| Every testimonial, number and claim has a source | human |
| One voice and form of address across the site. In gendered languages such as Hebrew: plural, feminine, masculine or neutral | human |
| Alt text on images | script |
| Designed 404 page | browser |

## Before launch: function

| Check | How |
|---|---|
| Widths 390, 600, 900, 1440 with no horizontal scroll | browser |
| Hover, touch, and the mobile menu | browser |
| Button text and background colors read from the browser | browser |
| Motion measured as really changing | browser |
| Every form sent for real, and the email reached the client's inbox | human |
| Outgoing mail works through SMTP | browser |
| WhatsApp and phone links open correctly on a phone | human |
| RTL sites: ranges, prices and phone numbers read correctly | script and human |
| Shop only: a real test order, payment, confirmation email and invoice | human |

## Before launch: legal drafts, reviewed by the client's lawyer

The rows below follow Israeli practice (`israel-requirements.md`). Elsewhere, check what the local law asks for: the topics are usually the same.

| Check | How |
|---|---|
| Accessibility statement published, with contact details | script for existence, human for content |
| Privacy policy published | script for existence, human for content |
| Non-essential analytics and marketing wait for consent | browser |
| A form that adds to a mailing list has its own unticked checkbox | browser |

Existence does not prove compliance. Say so in the report.

## Before launch: technical and access

| Check | How |
|---|---|
| Full backup taken, and restore path known | human |
| Security basics: no default admin, plugins from known sources | script and human |
| Platform, theme and plugins updated | script |
| Global colors and fonts set in the theme or kit | script |
| Favicon and share image | script |
| Page titles and descriptions | script |
| Speed: cache on, images optimized | script and browser |
| Client has their own user with the right role | human |
| Domain is in the client's name and renews automatically | human |

## Launch day

| Check | How |
|---|---|
| Client approved going live, in writing | human |
| Moving a live site: list old URLs and prepare 301 redirects | script and human |
| Moving a live site: lower DNS TTL in advance, and note current records | human |
| Mail records (MX, SPF, DKIM) still correct after any DNS change | human |
| "Coming soon" mode off, search engines allowed | script |
| No links or images pointing at the staging address | script |
| SSL valid, http redirects to https | script |
| www and non-www redirect to one address | script |
| robots.txt does not block the site, sitemap responds | script |
| Non-public pages stay hidden from search | script |
| Forms re-tested on the live address | human |

## First week

| Check | How |
|---|---|
| Sitemap submitted to Search Console, errors reviewed | human |
| Analytics receives data, after consent | browser |
| Client has access to analytics and Search Console | human |
| Google Business Profile links to the site | human |
| Old URLs redirect, no 404 spike | script and human |
| Handover document delivered: logins location, backups, what to update and when | human |
| Next maintenance check is scheduled | human |
