# Final GitHub Handoff

This repository is ready to function as a public Steinmetz research archive and as a reusable source-grounded knowledge-engine template.

## Current Public State

- The live site is configured for GitHub Pages through `.github/workflows/deploy-pages.yml`.
- The Astro/Starlight site builds from `site/`.
- Public data exports live under `site/public/data/`.
- The source corpus, processed data, diagrams, concepts, equations, glossary, patent seed records, and verification queues are all kept in repository-visible folders.
- The project now includes a reusable Research Codex Engine guide and bootstrap script for creating future projects without carrying Steinmetz-specific content.

## Most Important Guarantees

- Source fact, modern explanation, mathematical reconstruction, historical context, interpretation, and speculation are kept as separate layers.
- OCR and extracted diagrams are treated as candidates until scan-reviewed.
- Public pages expose review status instead of hiding uncertainty.
- The system can scale to more Steinmetz works and later to more figures or topics.

## Before Calling Any Future Release Canonical

Run:

```powershell
python pipeline/scripts/generate_completion_audit.py
python pipeline/scripts/generate_scholarly_exports.py
cd site
npm run build
```

Then review:

- `MASTER_PROJECT_TRACKER.md`
- `VERIFICATION_QUEUE.md`
- `site/src/content/docs/roadmap/completion-audit.mdx`
- `site/src/content/docs/roadmap/citation-and-data-export.mdx`
- open GitHub issues for source, equation, diagram, and expert review.

## What Remains Scholarly Work, Not Infrastructure Work

The framework is strong, but a definitive archive always depends on continuing human review:

- scan verification of OCR passages,
- page-accurate citation checking,
- equation-by-equation mathematical review,
- figure crop promotion from extracted candidates,
- edition comparison,
- patent-to-theory interpretation review,
- and expert review by electrical engineers, historians, and source specialists.

This is intentional. The site should never pretend that machine-generated breadth is the same thing as scholarly finality.

## Reuse Path

For a clean new project:

```powershell
python pipeline/scripts/bootstrap_new_codex.py `
  --project-title "New Research Codex" `
  --project-id new-research-codex `
  --primary-subject "Primary Subject" `
  --output C:\tmp\new-research-codex
```

For a larger multi-person archive, keep this repository and add collections while preserving source isolation:

```text
sources/<collection>/<source-id>/
processed/<collection>/<source-id>/
people/<person-id>/
concepts/<concept-id>/
comparisons/<topic-id>/
```

## Maintainer Rhythm

Use this loop:

1. Add or verify sources.
2. Regenerate candidate data.
3. Promote only reviewed material.
4. Rebuild public pages.
5. Run the site build.
6. Commit with a message that names the research layer changed.

That rhythm is what keeps the project both ambitious and trustworthy.

