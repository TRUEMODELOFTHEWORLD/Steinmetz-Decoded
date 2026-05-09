# Research Codex Engine

This repository began as **Steinmetz Decoded**, but its architecture is deliberately reusable. A future project can use the same pattern for Tesla, Walter Russell, Eric Dollard, ether history, concave-earth research, sacred geometry, or any other source-heavy subject where credibility depends on strict attribution.

The engine is not a generic blog template. It is a source-grounded research system.

## What The Engine Provides

- Source custody: raw files, public links, manifests, rights notes, checksums, and processing status.
- Structured processing: OCR/text extraction, chapter splits, equation candidates, figure candidates, glossary candidates, quotes, annotations, and crosslinks.
- Scholarly layers: source claims, modern explanations, mathematical reconstruction, historical notes, interpretive readings, speculative connections, and verification queues.
- Reader layers: source-text browser, guided routes, concept pages, visual galleries, equation pages, tools, and public data exports.
- Publication layers: GitHub Pages deployment, citation files, public JSON exports, issue templates, release-readiness pages, and review checklists.

## Fast Start For A New Project

Create a clean starter workspace without Steinmetz content:

```powershell
python pipeline/scripts/bootstrap_new_codex.py `
  --project-title "Tesla Decoded" `
  --project-id tesla-decoded `
  --primary-subject "Nikola Tesla" `
  --output C:\tmp\tesla-decoded
```

The starter project includes the same custody directories, source catalog, claim template, charter, and anti-hallucination rules. Copy the pipeline scripts and site stack from this repository as needed.

## Recommended Fork Strategy

Use one of these approaches:

- **Continue this repository as a multi-collection archive** if the long-term brand is a larger public library.
- **Fork this repository for a new person/topic** if the subject needs its own GitHub Pages site.
- **Run `bootstrap_new_codex.py`** if you want a clean shell without Steinmetz-specific source content.

The best long-term model is a multi-collection codex where pages are organized by both source/person and concept:

```text
sources/
  steinmetz/
  tesla/
  russell/
people/
  charles-proteus-steinmetz/
  nikola-tesla/
concepts/
  ether/
  alternating-current/
  resonance/
  dielectricity/
comparisons/
  steinmetz-vs-tesla/
  mainstream-vs-ether-field/
```

## Non-Negotiable Data Rule

Every claim needs metadata that identifies where it came from and what kind of statement it is:

```json
{
  "person": "Charles Proteus Steinmetz",
  "source_id": "theory-calculation-transient-electric-phenomena-oscillations",
  "location": {
    "chapter": "Chapter 7",
    "page": 42
  },
  "claim_type": "explicit_source_claim",
  "interpretation_layer": "source",
  "confidence": "scan-verified"
}
```

Never let interpretation inherit the authority of the original source. Keep these layers visibly separate:

- `explicit_source_claim`
- `modern_equivalent`
- `mathematical_reconstruction`
- `historical_note`
- `interpretive_reading`
- `speculative_connection`

## Source Intake Flow

1. Add a source manifest before doing analysis.
2. Preserve raw PDFs, scans, OCR, and public links.
3. Extract text and images into `processed/`.
4. Generate candidate catalogs.
5. Promote only scan-checked claims, equations, and figures into canonical pages.
6. Publish reader-facing pages with review labels intact.

Use `.github/ISSUE_TEMPLATE/new-source-intake.yml` when adding a major source.

## Publication Flow

From the repository root:

```powershell
python pipeline/scripts/build_research_indexes.py
python pipeline/scripts/generate_source_text_pages.py
python pipeline/scripts/generate_book_coverage_atlas.py
python pipeline/scripts/generate_chapter_workbench.py
python pipeline/scripts/generate_concept_concordance.py
python pipeline/scripts/generate_theme_evidence_atlas.py
python pipeline/scripts/generate_equation_atlas.py
python pipeline/scripts/generate_visual_topic_galleries.py
python pipeline/scripts/generate_crosslinked_research_surfaces.py
python pipeline/scripts/generate_concept_reader_synthesis.py
python pipeline/scripts/generate_completion_audit.py
python pipeline/scripts/generate_scholarly_exports.py
```

Then verify the public site:

```powershell
cd site
npm install
npm run build
```

## What To Customize First

For a new project, change these first:

- `codex.config.json`
- `PROJECT_CHARTER.md`
- `README.md`
- `sources/source_catalog.json`
- `site/astro.config.mjs`
- `site/src/content/docs/index.mdx`
- top-level concept and source manifests

Keep the review states, claim layers, and source-custody fields even if the visual design changes.

