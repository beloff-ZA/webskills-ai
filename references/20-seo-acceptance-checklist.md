# V3 — SEO Acceptance Gate

Use as part of the existing V2 validation and creative-director protocol. SEO is an independent audit dimension; it must not excuse derivative visuals, poor readability or fabricated claims.

## Pass/fail
- [ ] Page has one clear intent and a unique reason to exist.
- [ ] First meaningful viewport explains the real service/topic and next action.
- [ ] Unique, accurate title and description exist for each indexable route.
- [ ] Heading tree, landmarks, link text, images and content are semantic and accessible.
- [ ] No unnatural keyword repetition, generic filler or automatically spun location pages.
- [ ] Core copy, links and page-specific metadata are present in crawled/rendered HTML.
- [ ] Canonical URL, robots directives, redirects and status codes agree.
- [ ] Sitemap includes only actual intended indexable canonicals; robots.txt does not conflict.
- [ ] Social metadata references actual public images where supplied.
- [ ] Page-specific JSON-LD, if any, matches verified on-page facts and appropriate schema types.
- [ ] No fake ratings, FAQ rich result promises, invented business details or unsupported course/product markup.
- [ ] Mobile readability, speed, keyboard access and visual design reviewed alongside SEO.
- [ ] Tests performed and remaining unknowns clearly reported.

## Severity
- Blocker: incorrect noindex, canonical to wrong domain, fabricated schema facts, inaccessible core content, misleading page claims.
- Major: duplicated titles/descriptions sitewide, broken navigation/crawl paths, invalid page schema, soft 404.
- Minor: underdescriptive alt text, missing optional social image, incomplete helpful supporting context.

## Score separately
Provide 0–4 scores for Content usefulness, Natural language, Metadata, Crawl/indexing, Semantics, Structured-data accuracy and Verification. Mark untested as 'Not tested'; never invent a pass. Do not collapse SEO quality into a ranking prediction.

## Deliverable
For every page or page class, report the intended title, meta description, canonical, robots directive, heading outline, candidate schema type (or 'none'), and outstanding business facts. For implemented projects show the source files changed and tools/tests run.
