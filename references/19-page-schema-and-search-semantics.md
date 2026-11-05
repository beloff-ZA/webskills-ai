# V3 — Page-Specific Semantic and Structured Data

## Core rule
Use appropriate native semantic HTML tags for the human-facing page and JSON-LD Schema.org structured data only when the page visibly supports the facts. Schema markup is not decoration, a ranking shortcut, or permission to invent rich results. Google's supported rich-result types are a subset of Schema.org. Eligibility never guarantees display.

## Page mapping (select only applicable types)
| Page | Semantic structure | Candidate JSON-LD |
| --- | --- | --- |
| Home | header, nav, main, meaningful H1, footer | WebSite; Organization OR LocalBusiness when accurate and verified |
| About/person | main, article/section, headings, figure | AboutPage, Person when identifying facts are supported |
| Service detail | main, article/section, headings, genuine service details | Service and real provider; optional Offer only with actual terms |
| Contact | main, address for genuine business contact, contact links | ContactPage; relevant Organization/LocalBusiness contact details |
| Business location | address, location/service-area copy, hours only if confirmed | Most specific relevant LocalBusiness subtype supported by facts |
| Product | product page, details, genuine pricing/availability | Product and Offer if policy conditions met |
| Article/blog | article, heading, author/date if known, time datetime | BlogPosting or Article with truthful dates and attribution |
| Breadcrumb-enabled internal page | nav aria-label="Breadcrumb", ordered list and actual links | BreadcrumbList matching visible hierarchy |
| Event | event details, venue, date/time and ticket terms | Event if an actual event exists and matches requirements |
| Video page | video and descriptive supporting content | VideoObject with validated metadata where suitable |
| FAQ/help | actual visible Q&A, semantic headings/details as appropriate | FAQPage only when eligibility/content policy allows; do not assume Google FAQ rich results for ordinary commercial sites |
| Course/training | meaningful syllabus, provider, enrollment details | Course only for genuine eligible courses with complete relevant facts; not every coaching session |
| Search results, filters, utility pages | semantic forms/results, appropriate canonicals | Usually none; consider noindex based on actual SEO strategy |
| Error/404 | honest error content and working links | None; correct HTTP status more important |

## Native HTML tags and microsemantics
- Use `<main>`, `<nav>`, `<article>`, `<section>`, `<header>`, `<footer>`, `<address>`, `<figure>`, `<figcaption>`, `<time datetime>`, `<ol>`, `<ul>`, heading levels and `<a href>` according to meaning; these are not an SEO tag-count checklist.
- Use `<article>` for independently meaningful compositions, not every card.
- `<address>` marks relevant contact information for a person/organization and is not a generic location-text wrapper.
- Links must be genuine crawlable hrefs. Maintain accessible names and keyboard behavior.

## JSON-LD implementation
- Prefer JSON-LD in a `<script type="application/ld+json">` block in the head or body; construct valid JSON, safely serialize and avoid XSS from interpolated user content.
- Define a stable entity identity using `@id` and a canonical `url`; reuse references rather than creating contradictory copies.
- Choose the narrowest accurate types and only properties verified from page, business or trustworthy source.
- Do not add fabricated review, aggregateRating, testimonials, price, location, certification, social profiles, employment claims or opening hours.
- No hidden offers or markup for content absent from the page. Do not tag a coaching service as Course, Product, Event or LocalBusiness without verifying suitability.
- Use absolute canonical URLs for URLs and image fields. Keep logo/image optional if not available.
- For one-page small businesses, often WebSite + truthful Organization/LocalBusiness is enough. A generic Service object may describe real offerings but may not create a special Google rich result.
- Avoid SiteNavigationElement or unsupported schema simply because a generator claims it will produce sitelinks.

## Validation
1. Compare every structured property against visible content and verified facts.
2. Parse JSON-LD syntax and ensure no contradictory entities.
3. Use Google Rich Results Test for supported features and Schema.org validator for general schema semantics.
4. Check Search Console enhancement reports when available.
5. Record unsupported rich-results expectations. Structured data is a signal, not a guarantee.

References:
https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
https://developers.google.com/search/docs/appearance/structured-data/sd-policies
https://developers.google.com/search/docs/appearance/structured-data/search-gallery
https://schema.org/
