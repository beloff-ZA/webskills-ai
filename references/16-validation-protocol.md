# Design validation: test, don't congratulate yourself
For meaningful UI work, test with available tools and report untested areas.

## Visual and viewport matrix
Check narrow (320/390 CSS px), tablet (768/1024), desktop (1440/1920), native-scale large (2560/3840) and ultrawide (3440) when feasible. Test landscape, zoom/reflow (200%, and WCAG 400% reflow context where applicable), long content and empty/error states. Test DPR 1x/2x and image crop/clarity; note CSS viewport versus physical pixels. Verify keyboard, touch targets, focus, colour contrast, light/dark/true-black variants where supported, reduced motion and no horizontal overflow. Do not claim to physically test OLED or HDR without suitable equipment.

## Commerce tasks
Try finding a product, filtering, selecting a variant, viewing delivery/returns and progressing through cart/checkout in a safe test environment. Do not place a live order unless explicitly authorised.

## Static quality
Run project lint/types/tests/build when available. Run browser accessibility/performance tools if available. Distinguish screenshots, automated checks and actual device tests.

## Self audit
Read [anti-AI audit](15-anti-ai-pattern-audit.md). Inspect template-pattern clusters and source similarity. The included script `scripts/design_audit.py` performs *text-based warnings only* for an input file; it cannot assess visual plagiarism. A report must contain: tests run, observed problems, changes made, tests not run, originality concerns requiring human judgment.