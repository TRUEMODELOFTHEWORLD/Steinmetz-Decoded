# Processing Pipeline

The pipeline turns raw Steinmetz source material into reviewable data.

It is intentionally transparent: every machine-produced output should be inspectable, reproducible, and marked with a review status.

## Reusable Codex Bootstrap

To start a new source-grounded project from the same architecture without Steinmetz-specific content:

```powershell
python pipeline/scripts/bootstrap_new_codex.py `
  --project-title "Tesla Decoded" `
  --project-id tesla-decoded `
  --primary-subject "Nikola Tesla" `
  --output C:\tmp\tesla-decoded
```

The bootstrap creates custody folders, a source catalog, claim templates, a project charter, and a verification policy. It is intentionally small so future projects can adopt the evidence model before choosing their final web design.

## Stages

1. **Custody**
   - Copy or link raw PDFs, scans, OCR, and metadata into `sources/<source-id>/`.
   - Record checksums and external source URLs.

2. **OCR and Text Cleaning**
   - Preserve raw OCR.
   - Create normalized text without deleting uncertain readings.
   - Mark OCR defects instead of silently fixing technical terms.

3. **Structural Split**
   - Split by book, lecture, chapter, section, and page when possible.
   - Preserve page mapping separately from cleaned prose.

4. **Candidate Extraction**
   - Equations
   - Figures
   - Concepts
   - Glossary terms
   - Quotes and hidden gems
   - Crosslinks

5. **Review and Promotion**
   - Candidates remain in `processed/`.
   - Reviewed explanatory work moves to canonical Markdown pages.

## First Script

```powershell
python pipeline/scripts/seed_source_from_ocr.py `
  --source-id radiation-light-and-illumination `
  --ocr processed/radiation-light-and-illumination/cleaned_text/internet-archive-ocr.txt
```

The script uses only the Python standard library. It creates lecture splits and candidate JSON catalogs from the Internet Archive OCR seed.

## Cross-Source Research Indexes

After sources have candidate catalogs, rebuild the corpus-wide indexes:

```powershell
python pipeline/scripts/build_research_indexes.py
```

This writes:

- `processed/research_index.json`
- `processed/equation_index.json`
- `processed/figure_index.json`
- `processed/glossary_index.json`
- `processed/concept_index.json`
- `processed/quote_index.json`
- `processed/evidence_ledger.json`
- `processed/chapter_atlas.json`
- `processed/source_processing_status.md`

These indexes are inventory and review tools. They count candidates, promoted original scan crops, glossary terms, concept seeds, quote candidates, and next actions. They do not promote OCR output to canonical truth.

To generate the project completion audit:

```powershell
python pipeline/scripts/generate_completion_audit.py
```

This writes `processed/completion_audit.json` and `site/src/content/docs/roadmap/completion-audit.mdx`. The audit measures infrastructure readiness for canonical review; it is not a scholarly certification.

To generate public citation and data exports:

```powershell
python pipeline/scripts/generate_world_class_artifacts.py
python pipeline/scripts/generate_publication_readiness.py
python pipeline/scripts/generate_verification_workbench.py
python pipeline/scripts/generate_claim_attribution_ledger.py
python pipeline/scripts/generate_scholarly_exports.py
```

The first command writes notation, diagram provenance, schema-reference, and expert-review-packet ledgers plus their public roadmap pages. The second writes release, accessibility, edition-comparison, and patent bridge controls. The third writes equation, figure, patent, and canonical verification workbench queues with source links and OCR snippets. The fourth writes a claim attribution ledger that classifies source facts, OCR candidates, modern translations, diagrams, patents, and interpretation layers. The fifth command writes `CITATION.cff`, `processed/citation_index.json`, `processed/citation_index.csl.json`, `processed/citation_index.bib`, `site/public/data/manifest.json`, public copies of the core JSON indexes and ledgers, and `site/src/content/docs/roadmap/citation-and-data-export.mdx`. These exports are reusable research aids; they preserve review-state data and do not certify candidate material as canonical.

## Public Corpus Pages

After chapter splits and indexes exist, generate the public source-text browser, book coverage atlas, chapter workbench, and concept concordance:

```powershell
python pipeline/scripts/generate_source_text_pages.py
python pipeline/scripts/generate_book_coverage_atlas.py
python pipeline/scripts/generate_chapter_workbench.py
python pipeline/scripts/generate_concept_concordance.py
```

The source-text browser exposes the current processed text for every chapter, lecture, section, or report division. The book coverage atlas adds a source-by-source map above those reader pages, with every processed section, top themes, concept density, glossary density, and candidate equation/figure/quote counts. The chapter workbench joins each section to theme snippets, concept/glossary hits, equation candidates, figure candidates, quote candidates, source links, and promotion checklists. The concept concordance scans the same corpus for curated Steinmetz terminology and links each hit back to source text and workbench pages. These layers are candidate research aids, not corrected editions.

## PDF Image Extraction

For original Steinmetz diagrams, use the PyMuPDF-based extraction tool:

```powershell
python -m pip install -r pipeline/requirements.txt

python pipeline/scripts/extract_pdf_images.py `
  --source-id radiation-light-and-illumination `
  --pdf sources/radiation-light-and-illumination/raw/radiation-light-and-illumination-1909-ia-scan.pdf `
  --mode pages `
  --pages 1-20 `
  --dpi 220
```

Generated full-page renders and embedded image dumps are review candidates, not canonical diagrams. Curated figure crops should be promoted into:

```text
diagrams/original/<source-id>/figures/
```

with exact source-page metadata and a matching diagram analysis page.

To crop a verified region from a rendered page:

```powershell
python pipeline/scripts/crop_image_region.py `
  --source-id radiation-light-and-illumination `
  --figure-id rli-fig-14-spectrum-of-radiation `
  --source-image processed/radiation-light-and-illumination/image_extraction/page_renders/pdf-page-0038-220dpi.png `
  --source-location "Radiation, Light and Illumination, printed page 18, Fig. 14" `
  --box 120,620,1010,930 `
  --out diagrams/original/radiation-light-and-illumination/figures/fig-14-spectrum-of-radiation.png
```

## Review Standard

Machine output is useful but not authoritative. Quotations, formulas, and figure descriptions must be checked against the scan before being treated as canonical.
