# V3 — Metadata, Canonicals, Robots and Discovery

## Rule
Every indexable route gets purposeful, unique metadata matching its visible content. Implement in delivered HTML head (static, SSR, pre-rendered, or search-engine-compatible rendering). SPA-only client-side head updates are not a substitute for checking rendered/crawled output.

## Required by page
- Descriptive, concise unique `<title>`, reflecting page topic and optionally brand.
- Unique factual `<meta name="description" content="...">` summarising user value. There is no mandatory character limit; target useful clarity rather than a magic 155–160 count. Google may generate its own snippet.
- `<link rel="canonical" href="https://example.com/preferred-path/">` absolute URL for the preferred page version. Canonicals are signals, not guaranteed commands. Coordinate with redirects, navigation, sitemap, hreflang and protocol/host preferences.
- `<html lang="...">` matching the visible page's language.
- Indexing instructions only as required: omit robots meta for ordinary index/follow defaults, use `noindex` for pages that must be excluded and that crawlers can access. Do not block a noindex page in robots.txt and expect noindex to be seen.
- Social previews: `og:type`, `og:title`, `og:description`, `og:url`, `og:image` with public absolute image URL when an actual preview image is provided; Twitter/X card metadata where appropriate. Never generate an unverified image URL.
- For multilingual sites, include validated reciprocal hreflang alternate links and x-default where suitable. Do not add hreflang to monolingual sites.
- Use robots.txt for crawl guidance, not secrecy or guaranteed deindexing. Produce a canonical-domain sitemap.xml listing only intended indexable canonical URLs, with accurate optional lastmod (actual meaningful modification). Submit to Search Console/Bing Webmaster Tools when access and permission exist.
- Ensure working status codes: 200 for valid pages, redirects for moved URLs, genuine 404/410 for missing pages, no soft 404 placeholder routes.
- Prevent staging, test and development deployments from being indexed. Ensure production is not inadvertently noindexed.
- Avoid obsolete meta keywords, unsupported ranking claims, meta revisit-after and title/description duplication across route templates.

## Framework integration
Provide a reusable SEO configuration per route (title, description, canonical path, robots policy, social asset, schema objects) rather than hardcoding a single global title. Document how the framework outputs metadata in the final HTML. Keep social images and favicons under developer/client asset ownership.

## Quality gate
Inspect real HTML responses for multiple routes; verify canonical URL and robots directives; check share previews; crawl internal links; validate sitemap and robots output; test redirects/404s; check mobile and JS rendering. Only report tests actually executed.

Official guidance:
https://developers.google.com/search/docs/appearance/title-link
https://developers.google.com/search/docs/appearance/snippet
https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
