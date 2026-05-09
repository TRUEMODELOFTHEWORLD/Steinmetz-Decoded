# Steinmetz Decoded

LIVE WEBSITE : https://truemodeloftheworld.github.io/Charles-Proteus-Steinmetz-Texts-AI-Decoded/

An open-source research archive and public knowledge base for the writings of Charles Proteus Steinmetz.

This project is designed to become a rigorous, source-grounded, mathematically faithful, historically careful, and conceptually deep archive of Steinmetz's books, lectures, papers, diagrams, terminology, equations, and electrical worldview.

The project is not a summary site. It is a research system.

## Mission

For every processed source, the archive aims to preserve and explain:

- Steinmetz's original wording, notation, definitions, diagrams, and page references.
- Modern electrical engineering equivalents and mathematical translations.
- Historical context from early twentieth-century electrical science.
- Tesla-era parallels and differences, when the evidence supports them.
- Clearly labeled ether-field or Ken Wheeler-style interpretive readings, separated from historical claims.
- Hidden gems: statements that are technically rich, forgotten, philosophically important, or unusually clear.

Every claim should be traceable to a source text, a derivation, a modern reference, or an explicitly labeled interpretation.

## Repository Map

```text
sources/       Raw PDFs, scans, source manifests, custody notes, and source metadata.
processed/     Cleaned OCR, chapter splits, extracted candidate JSON, page maps, and processing reports.
analysis/      Book, chapter, concept, equation, and diagram commentary.
concepts/      Cross-source concept encyclopedia pages.
math/          Equation catalogs, derivations, notation translations, and worked examples.
diagrams/      Original, cleaned, recreated, and annotated diagrams.
comparisons/   Steinmetz vs modern EE, Tesla-era science, and labeled ether-field readings.
glossary/      Historical, obsolete, and modernized electrical terminology.
hidden-gems/   Important overlooked passages and research notes.
research-questions/
               Living research agenda and unresolved questions.
pipeline/      Repeatable ingestion, extraction, schema, and quality-control tooling.
site/          Astro/Starlight public documentation website.
```

## First Canonical Source

The first source is:

**Charles Proteus Steinmetz, _Radiation, Light and Illumination: A Series of Engineering Lectures Delivered at Union College_**, McGraw-Hill, 1909, compiled and edited by Joseph LeRoy Hayden.

The local raw source files are stored in:

```text
sources/radiation-light-and-illumination/raw/
```

The first processed OCR seed is stored in:

```text
processed/radiation-light-and-illumination/cleaned_text/internet-archive-ocr.txt
```

## Seeded Source Corpus

The first expansion pass has also copied local PDFs and, where available, downloaded public OCR seeds for:

- _Elementary Lectures on Electric Discharges, Waves and Impulses, and Other Transients_
- _Engineering Mathematics_
- _Theory and Calculation of Alternating Current Phenomena_
- _Theory and Calculation of Transient Electric Phenomena and Oscillations_
- _Theoretical Elements of Electrical Engineering_
- _Investigation of Some Trouble in the Generating System of the Commonwealth Edison Co._

See `sources/source_catalog.json` for the current processing corpus, `sources/steinmetz_bibliography_manifest.json` for the expanded Wikipedia-derived works intake, and `sources/steinmetz_patents/patent_register.json` for the seeded patent register.

## Quality Labels

Use these labels throughout the project:

- **Steinmetz explicitly states**: directly supported by source text.
- **Modern equivalent**: translation into current electrical engineering language.
- **Mathematical reconstruction**: a derivation or notation translation reconstructed from source and math.
- **Historical note**: contextual material requiring a source.
- **Interpretive reading**: ether-field, Ken Wheeler-style, Dollard-style, or other nonstandard reading.
- **Speculative connection**: possible but unproven connection.
- **Needs verification**: claim, page map, OCR, citation, diagram, or derivation still awaiting review.

## Website

The public site skeleton lives in `site/` and uses Astro + Starlight. It supports MDX long-form pages, sidebar navigation, search, KaTeX math, citations, callouts, and interactive explainer components.

Current site features include:

- A friendly Start Reading entry page with routes for newcomers, source-first researchers, engineering students, visual readers, and verification reviewers.
- A redesigned reader-gateway layer that connects the home page, Start Reading, Source Library, book coverage, visual topic galleries, equation atlas, and verification queues so casual readers and technical researchers can enter the same corpus without hunting through unrelated indexes.
- Expanded source-library pages for the first seeded Steinmetz corpus.
- Generated source research dashboards on every curated source overview, so `/sources/...` pages now route directly into source text, book coverage, workbench, visual maps, formula maps, theme evidence, concept trails, and verification focus.
- A generated source-text browser exposing every processed chapter, lecture, section, and report division as public reader pages.
- A generated research reader system with readable/transcript/dense modes, in-reader search, match highlighting, font controls, source-asset links, and concept links that open source passages with the searched term preloaded.
- A generated book coverage atlas that summarizes every processed source, counts candidate equations, figures, quotes, concepts, and glossary hits, and links each book section into the source reader and workbench.
- A generated Steinmetz corpus completion matrix that records all 49 current bibliography and source-frontier records, including the 14 critical works that still require acquisition or explicit public deferral before the archive can claim definitive completion.
- A generated chapter research workbench that maps every processed section to source links, theme snippets, glossary hits, equation candidates, figure candidates, quote candidates, and promotion checklists.
- A generated concept concordance that traces 77 core terms and concepts across all 394 processed text sections, with source-text and workbench links for every hit.
- A generated theme evidence atlas that gathers source-located OCR/PDF-text passages for ether, fields, magnetism, dielectricity, hysteresis, reactance, impedance, transients, symbolic method, wave phenomena, radiation, energy, and apparatus.
- A generated passage atlas, research map, study curriculum, and hidden-gems discovery layer that surface source-dense passages while keeping OCR verification warnings visible.
- A generated equation atlas that routes 3,845 equation/formula candidates from 15 sources into mathematical families while preserving OCR verification warnings.
- Generated source visual maps and source formula maps that connect every processed source to its diagrams, formula candidates, source text, workbench pages, and concept routes.
- Generated math/visual evidence bridges on curated concept pages so pages like Ether, radiation, symbolic method, hysteresis, transients, reactance, and admittance no longer stand apart from the broader formula and diagram layers.
- Generated visual topic galleries that let readers enter by theme while still seeing source maps, workbench links, figure candidates, formulas, and verification boundaries.
- Expanded curated deep-decoding pages for the electric field, general number, transient terms, high-frequency surges, impedance/reactance, admittance, hysteresis/effective resistance, hysteresis motor, standing/traveling waves, and first mathematical equation pages, with source-text, workbench, formula, visual, and verification routes.
- A generated completion audit that measures source-by-source readiness for canonical review and keeps the path to a definitive archive explicit.
- Public citation and data exports, including `CITATION.cff`, BibTeX, CSL JSON, a public data manifest, and reusable copies of the core processed indexes.
- A critical-edition editorial policy, canonical review workflow, and GitHub issue templates for source verification, equation review, and diagram review.
- Generated notation, diagram provenance, schema reference, and expert review packet ledgers that turn broad coverage into reviewable scholarly work.
- Generated release-level, accessibility-audit, edition-comparison, and patent-to-theory bridge controls for publication readiness.
- A generated canonical verification workbench that turns the first equation canon, promoted original crops, and seeded patents into source-linked scan-check queues.
- Recreated research-guide diagrams for radiation, transients, symbolic AC geometry, hysteresis, field propagation, illumination, rotating magnetic fields, distributed line constants, surge reflection, field storage, admittance, harmonics, synchronizing reactors, field-energy boundaries, and engineering number planes.
- A station-section/reactor reading aid for the Commonwealth Edison report.
- Interactive frequency/wavelength, AC waveform/harmonics, impedance/reactance, phasor/symbolic-form, power-factor, hysteresis-loss, transient RLC response, and lightning/surge traveling-wave tools.
- Site-wide readable source/code blocks that wrap long OCR passages instead of trapping them in horizontal or vertical scroll panes.
- Quality labels that separate source claims, modern interpretation, mathematical reconstruction, and speculative readings.
- A reusable Research Codex Engine scaffold for future source-grounded projects that should reuse the architecture without inheriting Steinmetz-specific content.

To run it after dependencies are installed:

```powershell
cd site
npm run dev
```

To verify a production build:

```powershell
cd site
npm run build
```

## GitHub Pages

The repository includes `.github/workflows/deploy-pages.yml`, which builds the Astro/Starlight site from `site/` and deploys it with GitHub Actions.

On GitHub, enable Pages once:

1. Open repository **Settings**.
2. Go to **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Push to `main` or run the workflow manually from the **Actions** tab.

The default Pages URL is:

```text
https://truemodeloftheworld.github.io/Charles-Proteus-Steinmetz-Texts-AI-Decoded/
```

## Processing Pipeline

The first standard-library pipeline script seeds source-level catalogs:

```powershell
python pipeline/scripts/seed_source_from_ocr.py `
  --source-id radiation-light-and-illumination `
  --ocr processed/radiation-light-and-illumination/cleaned_text/internet-archive-ocr.txt
```

It creates chapter splits and candidate catalogs while preserving the raw OCR. Human review is still required before promoting candidates to canonical analysis.

The corpus-wide research index builder is:

```powershell
python pipeline/scripts/build_research_indexes.py
```

It writes dashboard data for sources, concepts, equations, figures, glossary terms, quote candidates, annotations, and crosslinks into `processed/`, including `processed/source_processing_status.md`.

For PDFs with embedded text, the page-preserving extraction step is:

```powershell
python pipeline/scripts/extract_pdf_text.py `
  --source-id commonwealth-edison-generating-system-trouble `
  --pdf sources/commonwealth-edison-generating-system-trouble/raw/commonwealth-edison-generating-system-trouble-local.pdf
```

The source-specific Commonwealth Edison parser is:

```powershell
python pipeline/scripts/seed_commonwealth_edison_report.py
```

The public source-text browser generator is:

```powershell
python pipeline/scripts/generate_source_text_pages.py
```

It generates `site/src/content/docs/source-texts/`, including one index page, per-source indexes, and reader pages for all processed chapters, lectures, sections, and report divisions.

The book coverage atlas generator is:

```powershell
python pipeline/scripts/generate_book_coverage_atlas.py
```

It generates `site/src/content/docs/book-coverage/` and `processed/book_coverage_atlas.json`, adding book-level coverage maps above the individual source-text pages. Each book page lists every processed section, top themes, top concepts, glossary density, candidate equation/figure/quote counts, and links into the source text and chapter workbench.

The chapter research workbench generator is:

```powershell
python pipeline/scripts/generate_chapter_workbench.py
```

It generates `site/src/content/docs/chapter-workbench/` and `processed/chapter_workbench.json`, joining each processed section to source text links, theme routing, concept/glossary hits, candidate equations, candidate figures, candidate quote passages, modern reading prompts, and explicitly labeled interpretive boundaries.

The public concept concordance generator is:

```powershell
python pipeline/scripts/generate_concept_concordance.py
```

It generates `site/src/content/docs/concept-concordance/` and `processed/concept_concordance.json`, scanning every processed section for curated Steinmetz electrical, mathematical, field-language, historical, and Tesla-era overlap terms. Concordance hits are source-location aids, not final definitions.

The corpus completion matrix generator is:

```powershell
python pipeline/scripts/generate_corpus_completion_matrix.py
```

It joins the bibliography intake, official source-expansion manifest, source catalog, processed counts, and patent register into `processed/steinmetz_corpus_completion_matrix.json` and public pages under `site/src/content/docs/source-library/corpus-completion/`.

To create a clean starter project from this architecture without Steinmetz content:

```powershell
python pipeline/scripts/bootstrap_new_codex.py `
  --project-title "Tesla Decoded" `
  --primary-subject "Nikola Tesla" `
  --output .\tesla-decoded
```

The public theme evidence atlas generator is:

```powershell
python pipeline/scripts/generate_theme_evidence_atlas.py
```

It generates `site/src/content/docs/theme-evidence/` and `processed/theme_evidence_atlas.json`, collecting source-located evidence routes for charter-critical themes such as ether and field language, magnetism and hysteresis, dielectricity and capacity, impedance and reactance, symbolic AC method, transients and surges, waves and radiation, energy, and apparatus.

The completion audit generator is:

```powershell
python pipeline/scripts/generate_completion_audit.py
```

It generates `site/src/content/docs/roadmap/completion-audit.mdx` and `processed/completion_audit.json`, measuring source custody, section splits, public readers, workbench coverage, concepts, equations, figures, glossary terms, quote candidates, original scan crops, and curated source pages.

The scholarly apparatus generators are:

```powershell
python pipeline/scripts/generate_equation_atlas.py
python pipeline/scripts/generate_recreated_visuals.py
python pipeline/scripts/generate_crosslinked_research_surfaces.py
python pipeline/scripts/generate_visual_topic_galleries.py
python pipeline/scripts/generate_source_research_dashboards.py
python pipeline/scripts/generate_world_class_artifacts.py
python pipeline/scripts/generate_publication_readiness.py
python pipeline/scripts/generate_verification_workbench.py
python pipeline/scripts/generate_claim_attribution_ledger.py
python pipeline/scripts/generate_scholarly_exports.py
```

The first five commands generate the public equation atlas, recreated visual index, source visual maps, source formula maps, concept math/visual evidence bridges, visual topic galleries, and source research dashboards. The world-class command generates `processed/notation_ledger.json`, `processed/diagram_provenance_ledger.json`, `processed/schema_reference.json`, `processed/expert_review_packets.json`, and their public roadmap pages. The publication-readiness command adds release, accessibility, edition, and patent bridge controls. The verification command generates source-linked canonical verification queues for equations, figures, and patents. The claim-attribution command classifies evidence, equations, translations, figures, and patents by claim layer. The export command publishes the current processed indexes and scholarly ledgers under `site/public/data/`.

It generates `CITATION.cff`, `processed/citation_index.json`, `processed/citation_index.csl.json`, `processed/citation_index.bib`, public data exports under `site/public/data/`, and the public citation/data export page. These exports preserve review-state fields so candidate records are not confused with verified claims.

## Current Processing Milestone

The archive now includes:

- Fifteen source records in `sources/source_catalog.json`.
- An expanded Steinmetz bibliography intake manifest for additional books, lecture collections, pamphlets, and papers.
- Eight additional Internet Archive OCR seeds beyond the initial local-PDF corpus, including _General Lectures on Electrical Engineering_, _America and the New Epoch_, _Theory and Calculation of Electric Apparatus_, _Four Lectures on Relativity and Space_, earlier _Alternating Current Phenomena_ editions, _Theory and Calculation of Electric Circuits_, and the 1914 _Electric Discharges_ edition.
- A seeded Steinmetz patent register for the Wikipedia-listed examples, with the full 200-plus patent catalog marked as an authority-pass milestone.
- Cross-source JSON indexes under `processed/`.
- Generated annotation and crosslink indexes for review-state notes and navigation between sources, concepts, terms, equations, and figures.
- A first twelve-equation canon in `processed/canonical_equations.json`, with public pages for the new equation spine.
- A generated equation atlas in `processed/equation_atlas.json`, with public formula-family pages for 3,845 equation/formula candidates, 2,528 reviewable relation candidates, and 1,330 strong formula candidates.
- A generated crosslinked research-surface layer in `processed/crosslinked_research_surfaces.json`, with source visual maps and source formula maps for all 15 processed sources plus concept evidence bridges on 22 curated concept pages.
- A generated source research dashboard layer in `processed/source_research_dashboards.json`, with every curated source overview enriched as a reader/research front door.
- A source-located candidate page for the Steinmetz hysteresis law and its 1.6-power loss relation.
- A generated source-processing dashboard.
- A PDF text extraction and page-map pass for the Commonwealth Edison report, with 5 report sections, 220 equation candidates, 12 concept candidates, 12 glossary candidates, and a deep page on reactors and synchronism.
- A generated source-text browser with 394 public text-section pages across the processed corpus.
- A generated book coverage atlas for all 15 seeded sources, covering 394 processed sections and 1,050,685 processed words with direct source-reader and workbench links.
- A generated chapter workbench with 394 section-level research maps across the processed corpus.
- A generated concept concordance with 77 concept pages tracing hits across all 394 processed sections.
- A generated passage atlas with 150 balanced public passage candidates selected from 5,427 OCR/PDF-text candidates, plus a research map, study curriculum, theme passage pages, and rebuilt hidden-gems discovery page.
- A generated completion audit for all 15 seeded sources, plus public world-class finishing criteria.
- A generated citation and public data export system for source records, processed indexes, CSL JSON, BibTeX, and a site data manifest.
- Public editorial and canonical-review rules, plus GitHub review issue templates for source, equation, and diagram work.
- A generated notation ledger, diagram provenance ledger, schema reference, and expert review packet system for the next canonical-review phase.
- A generated release readiness map, accessibility audit, edition comparison queue, and patent-to-theory bridge.
- A generated canonical verification workbench with equation OCR snippets, original figure crop review cards, and patent authority-review cards.
- A generated claim attribution ledger that keeps source facts, OCR candidates, modern translations, diagrams, patents, and future interpretive layers separated.
- Fifteen original scan-derived crops: five from _Radiation, Light and Illumination_, four from _Alternating Current Phenomena_, and six from _Transient Electric Phenomena and Oscillations_, with crop manifests and checksums.
- A generated figure candidate atlas with 504 OCR/PDF-text figure references routed back to source text and workbench pages.
- Twenty public modern SVG reading aids, including 10 newly generated source-keyed guide diagrams for rotating fields, distributed line constants, impulse surge reflection, field storage, admittance, harmonics, hysteresis loss, synchronizing reactors, field-energy boundaries, and engineering number planes.
- Public site pages for the dashboard, source library, diagram archive, concepts, equations, comparisons, and interactive tools.
- A second public layer for symbolic AC method, impedance, reactance, admittance, transient terms, standing/traveling waves, RLC oscillation, and source-located historical glossary terms.
- A practical verification queue in `VERIFICATION_QUEUE.md`.

The full requirement and milestone map is maintained in `MASTER_PROJECT_TRACKER.md`, with a public mirror at:

```text
https://truemodeloftheworld.github.io/Charles-Proteus-Steinmetz-Texts-AI-Decoded/project-tracker/
```

## Current Live-Ready Site Surface

The public site currently builds more than one thousand pages, including:

- Source overviews for the seeded Steinmetz corpus.
- Source research dashboards for all 15 processed sources, joining each curated overview to reading, study, analysis, math, visual, theme, concept, and verification routes.
- Full generated text-reader coverage for 394 processed chapters, lectures, sections, and report divisions.
- Generated research workbench pages for 394 processed sections, connecting each chapter to source text, concepts, glossary terms, equations, figures, quotes, and promotion steps.
- Generated concept-concordance pages for 77 terms and concepts, each linked back to source text and chapter workbench pages.
- Generated passage-atlas and research-map pages for source-grounded discovery across the 15-source corpus.
- Generated equation-atlas pages for formula discovery across the 15-source corpus, grouped by symbolic AC, impedance/admittance, transients, waves/radiation, magnetism/hysteresis, power/energy, engineering mathematics, and apparatus systems.
- Generated source visual maps and source formula maps for all 15 processed sources, so a reader can browse one book's diagrams, formulas, source text, and workbench pages without bouncing through unrelated indexes.
- A generated completion-audit page and world-class criteria page for the final expert review path.
- Deep source pages for _Radiation, Light and Illumination_, _Alternating Current Phenomena_, _Transient Electric Phenomena_, and _Engineering Mathematics_.
- Concept pages for radiation, electric waves, lightning and surges, ether, illumination, transients, symbolic method, harmonics and wave shape, hysteresis, impedance, reactance, admittance, power factor, distributed constants, oscillation and damping, inductance/capacity, power-limiting reactors, and synchronizing power.
- Equation pages for wavelength/frequency, symbolic operator `j`, reactance forms, impedance/reactance, admittance, power/effective resistance, capacity susceptance, transient terms, RLC oscillation, condenser decrement, and Commonwealth Edison synchronizing power.
- Glossary pages for condensive reactance, wattless component, imaginary unit `j`, electrostatic capacity, counter e.m.f., and effective resistance.
- Comparison pages for modern EE, AC symbolic method, Tesla-era science, Tesla-era transients, and ether-field interpretation.
- Interactive tools for frequency/wavelength, AC waveform/harmonics, impedance/reactance, phasor/symbolic form, power factor, hysteresis loss, transient RLC condenser-discharge response, and lightning/surge traveling waves.
- Original scan-crop pages for RLI visual anchors and AC Chapter V symbolic-method figures, with a modern symbolic-method redraw sheet.
- Original scan-crop page for transient starting current, condenser charge, oscillation, and decrement figures, with a modern condenser-response redraw sheet.
- A recreated visual index with modern guide diagrams tied to source families and concept routes.
- Concept pages with generated math/visual evidence bridges that link concept reading directly into formula families, source formula maps, source visual maps, and figure candidates.
