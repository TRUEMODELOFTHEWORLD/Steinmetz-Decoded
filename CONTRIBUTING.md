# Contributing

This project welcomes careful source work, mathematical reconstruction, historical notes, glossary work, diagram cleanup, and disciplined interpretive comparison.

## Ground Rules

- Cite source text, page number, chapter, or scan image wherever possible.
- Mark OCR uncertainty with `Needs verification`.
- Preserve Steinmetz's original notation before adding modern notation.
- Keep speculative or ether-field readings under an explicit `Interpretive Reading` heading.
- Do not merge mainstream and nonstandard claims into a single unlabelled explanation.
- Prefer small, traceable changes over sweeping rewrites.

## Page Pattern

For concept, equation, diagram, and hidden-gem pages, use this order:

1. Source Anchor
2. Steinmetz Original
3. Modern Equivalent
4. Mathematical Reconstruction
5. Plain-English Explanation
6. Historical Context
7. Tesla-Era Comparison
8. Ether-Field Interpretive Reading
9. Verification Notes

## Promotion Checklist

Before an extraction becomes canonical:

- The source title, edition, and page are identified.
- OCR has been checked against the scan for quoted passages.
- Equations preserve original notation and include modern translation.
- Interpretive material is clearly labeled.
- Related concepts, equations, figures, and glossary terms are cross-linked.

## Review Workflow

Use the GitHub issue templates for source verification, equation review, and diagram review. They exist so review work is structured enough to become canonical later.

Use the new source-intake issue template before adding a major book, paper, lecture, patent, archive collection, or correspondence file. A source should enter the repository through custody first, then extraction, then review, then public synthesis.

Promotion states:

- `candidate`: found by OCR, script, or first-pass reading.
- `source-located`: tied to chapter, page, line, figure, or equation location.
- `scan-verified`: checked against a scan or trusted edition.
- `mathematically-reviewed`: notation, units, variables, and derivation checked.
- `canonical`: stable public explanation with source anchors and crosslinks.

## Citation And Data

The project publishes citation and data exports under `site/public/data/`. Do not remove review-state fields from generated JSON. They are part of the anti-hallucination system.

Use the notation ledger, diagram provenance ledger, schema reference, and expert review packets before promoting a large change. They show which records are source-located, scan-derived, reconstructed, or still awaiting review.

Use the release-level, accessibility, edition-comparison, and patent bridge pages before calling a milestone public-ready. They make the difference between broad coverage and reviewed publication explicit.

When adding a new source, update source custody first:

- source ID
- title
- author/editor when known
- year and edition when known
- raw file or public archive link
- processing status
- public site path
- checksum if a local artifact is stored

## Reusing The Engine

If you are cloning this repository to build a different public knowledge archive, start with `RESEARCH_CODEX_ENGINE.md` and `templates/research-codex-engine/`. The preferred clean-start path is:

```powershell
python pipeline/scripts/bootstrap_new_codex.py `
  --project-title "New Research Codex" `
  --project-id new-research-codex `
  --primary-subject "Primary Subject" `
  --output C:\tmp\new-research-codex
```

The subject may change. The evidence rules should not.
