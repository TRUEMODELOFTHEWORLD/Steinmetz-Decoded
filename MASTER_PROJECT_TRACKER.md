# Master Project Tracker

This tracker converts the original project charter into a working control file. It is the source of truth for what the archive is trying to become, what has already been built, what is only seeded, and what still needs careful research.

The guiding rule is speed with labels: publish useful candidate layers quickly, but never hide uncertainty. A statement must trace to a Steinmetz source, a modern reference, a mathematical derivation, or an explicitly marked interpretive reading.

## Status Legend

| Status | Meaning |
| --- | --- |
| Done | Implemented and usable in the repo or public site. |
| Started | Structure exists and first examples are public, but the work is not complete. |
| Repeating | Must be applied to every source, concept, equation, diagram, and interpretive note. |
| Pending | Not yet meaningfully implemented. |
| Needs Verification | Candidate material exists but requires scan, citation, OCR, or mathematical review. |
| Future Scope | Important, but intentionally held until the Steinmetz foundation is stronger. |

## Current Snapshot

| Area | Current State |
| --- | --- |
| Public site | Astro/Starlight documentation site with GitHub Pages deployment workflow. |
| Live URL | https://truemodeloftheworld.github.io/Charles-Proteus-Steinmetz-Texts-AI-Decoded/ |
| Seeded Steinmetz records | Fifteen source records in `sources/source_catalog.json`. |
| Expanded bibliography intake | `sources/steinmetz_bibliography_manifest.json` maps the current Wikipedia works list into seeded, planned, and verification-needed records. |
| Corpus completion matrix | `processed/steinmetz_corpus_completion_matrix.json` and public corpus-completion pages now join the bibliography intake, official expansion manifest, source catalog, processed counts, and patent register into one authority layer: 49 bibliography/source-frontier records, 15 seeded source records, and 14 critical frontier works. |
| Patent intake | `sources/steinmetz_patents/patent_register.json` seeds the Wikipedia-listed patent examples and marks the full 200-plus patent catalog as an authority-pass milestone. |
| First canonical source | `Radiation, Light and Illumination` by Charles Proteus Steinmetz. |
| Public pages | Source library, source dashboard, concepts, equations, diagrams, comparisons, glossary, hidden gems, research questions, roadmap, and tools. |
| Original scan crops | Fifteen promoted crops: five from `Radiation, Light and Illumination`, four from `Alternating Current Phenomena`, and six from `Transient Electric Phenomena and Oscillations`, with manifests and checksums. |
| Modern visual aids | Twenty public SVG reading aids now exist, including new generated guides for rotating magnetic fields, distributed line constants, surge reflection, dielectric/magnetic storage, admittance, harmonics, hysteresis loss, synchronizing reactors, field-energy boundaries, and engineering number planes. |
| Reader UX layer | Sidebar Reader Mode now provides source-only filtering, page-local ask/search, translation shortcuts, diagram lightbox viewing, readable source/code blocks, mobile-first responsive hardening, a direct Start Reading entry, a redesigned source-library hub, and card-based routes that join book coverage, source text, diagrams, formulas, tools, and verification layers for non-specialist and specialist entry. |
| Source research reader | Generated source-text pages now mount an enhanced reader with readable/transcript/dense modes, in-reader search, match highlighting, match navigation, font controls, copy links, and incoming concept-query focus. |
| Original-source access | Source pages now expose Archive.org scan links, OCR links, and inline scan readers where stable archive IDs exist. |
| Source text browser | Generated public reader pages now expose 394 processed chapters, lectures, sections, and report divisions under `site/src/content/docs/source-texts/`. |
| Book coverage atlas | Generated book-level coverage pages now expose all 15 seeded sources under `site/src/content/docs/book-coverage/`, with every processed section linked to source text and chapter workbench pages, plus source study-guide panels for first reads, math, visuals, and field-language trails. |
| Source research dashboards | Generated dashboards now enrich all 15 curated `/sources/...` overview pages, tying each source to source text, book coverage, chapter workbench, visual maps, formula maps, theme evidence, concept trails, terminology signals, and verification focus. |
| Chapter workbench | Generated research maps now expose 394 processed sections under `site/src/content/docs/chapter-workbench/`, joining source links, theme snippets, concept/glossary hits, equation candidates, figure candidates, quote candidates, modern prompts, interpretive boundaries, and promotion checklists. |
| Passage atlas and research map | Generated discovery pages now rank 150 balanced candidate passages from 5,427 source-derived candidates across 15 sources and nine themes, with a reader-facing research map, study curriculum, and renewed hidden-gems page. |
| Concept concordance | Generated concept-trace pages now expose 77 curated terms and concepts under `site/src/content/docs/concept-concordance/`, linking every hit back to source text and chapter workbench pages. |
| Concept page dossiers | Generated source-grounded dossiers now enrich 22 curated concept pages, including Ether, with corpus counts, source distribution, aliases, priority passages, concordance links, and next editorial actions. |
| Theme evidence atlas | Generated source-grounded theme pages now expose nine charter-critical evidence routes under `site/src/content/docs/theme-evidence/`, covering ether/field language, magnetism/hysteresis, dielectricity/capacity, impedance/reactance, AC symbolic method, transients/surges, waves/radiation, energy/power, and apparatus. |
| Figure candidate atlas | Generated visual-routing pages now separate 15 promoted original scan crops from 504 OCR/PDF-text figure references, with source-text and workbench links for figure verification. |
| Equation atlas | Generated math-routing pages now expose 3,845 equation/formula candidates from 15 sources, including 2,528 reviewable relation candidates and 1,330 strong formula candidates grouped by mathematical family. |
| Crosslinked research surfaces | Generated source visual maps, source formula maps, and concept evidence bridges now connect diagrams, formulas, concepts, source text, and workbench pages across all 15 processed sources and 22 curated concept pages. |
| Visual topic galleries | Generated eight topic-level visual galleries now connect modern guide diagrams, figure candidates, source maps, formula leads, and workbench links for radiation, AC symbolic geometry, transients, hysteresis, dielectric-field energy, power systems, ether/field language, and illumination. |
| Guided reading routes | `processed/reading_routes.json` and `site/src/content/docs/reading-routes/` now provide nine purpose-built pathways through the corpus: first-hour reading, source-only reading, AC symbolic method, transients, field language, mathematics, visuals, apparatus, and patents. |
| Deep-decoding promotion queue | `processed/deep_decoding_promotion_queue.json` and a public roadmap page now rank all 394 processed sections for the next curated long-form decoding passes, with global and source-balanced queues. |
| Completion audit | `processed/completion_audit.json` and a public completion-audit page now measure source-by-source readiness for canonical review. |
| World-class criteria | Public expert finishing criteria now define what the archive must do before it can honestly call itself definitive. |
| Scholarly exports | `CITATION.cff`, `processed/citation_index.json`, CSL JSON, BibTeX, public `/data/` exports, and a data manifest now publish reusable research data with review-state labels intact. |
| Review governance | Editorial policy, canonical review workflow, contribution rules, and GitHub issue templates now guide source, equation, and diagram promotion. |
| World-class ledgers | `processed/notation_ledger.json`, `processed/diagram_provenance_ledger.json`, `processed/schema_reference.json`, and `processed/expert_review_packets.json` now route notation, diagram, data, patent, concept, and interpretive-boundary review. |
| Publication readiness | `processed/release_readiness.json`, `processed/accessibility_audit.json`, `processed/edition_comparison_index.json`, and `processed/patent_theory_bridge.json` now track release levels, accessibility, edition collation, and patent-to-theory work. |
| Canonical verification workbench | `processed/canonical_verification_workbench.json`, equation/figure/patent verification queues, and four public roadmap pages now turn priority candidates into scan-check work cards. |
| Claim attribution ledger | `processed/claim_attribution_ledger.json` now classifies 4,890 facts, OCR candidates, equations, modern translations, figures, patents, and future interpretive layers by source and claim type. |
| Research Codex Engine | `pipeline/scripts/bootstrap_new_codex.py`, reusable templates, and public engine documentation now let a future project clone the architecture without inheriting Steinmetz-specific content. |
| Evidence ledger | `processed/evidence_ledger.json` now indexes 4,855 traceability records across sources, concepts, glossary terms, equations, figures, quotes, and promoted scan crops. |
| Chapter atlas | `processed/chapter_atlas.json` now maps 394 chapter, lecture, section, and report-section records to OCR/PDF-text theme counts for research routing. |
| New deep-decoding pages | Public pages now include General Lectures on high-frequency surges, Elementary Lectures on the electric field, Engineering Mathematics on general number, AC Phenomena on impedance/reactance and admittance, Theoretical Elements on fields of force and hysteresis/effective resistance, Electric Apparatus on the hysteresis motor, Transient Phenomena on transient terms and standing/traveling waves, Relativity and Space on the gravitational field, America and the New Epoch on industrial government as historical context, and Commonwealth Edison on reactors and synchronism; the highest-impact thin entries now include source-text, workbench, formula, visual, and verification routes. |
| Research indexes | Generated JSON indexes for sources, concepts, equations, figures, glossary terms, and quotes under `processed/`. |
| Verification control | `VERIFICATION_QUEUE.md` tracks the next scan-check and promotion work. |

## Original Goal Matrix

| Original Goal | Status | Notes |
| --- | --- | --- |
| Build a GitHub repo and public knowledge base | Done | Repo structure, Pages workflow, and public site are in place. |
| Preserve raw sources, OCR, scans, metadata, and checksums | Started | First source and multi-source records exist. More checksum and custody work is needed source by source. |
| Process the first Steinmetz book as canonical example | Started | `Radiation, Light and Illumination` has OCR, chapter candidates, full generated lecture text pages, diagrams, first deep lecture page, figures, concepts, and equations. |
| Scale to multiple Steinmetz books | Started | Fifteen source records are now seeded, including earlier AC editions, Electric Circuits, and the 1914 Electric Discharges edition; all processed sections have generated public text-reader pages. |
| Account for more notable Steinmetz works | Started | The corpus completion matrix now tracks 49 records and identifies 14 critical frontier works still requiring acquisition or explicit public deferral before completion language is honest. |
| Include patents in detail | Started | A seeded patent register covers the Wikipedia-listed examples with Google Patents links, technical digests, diagram targets, and completion rules; full 200-plus catalog remains pending authority verification. |
| Extract every major concept | Started | Public concept encyclopedia exists; generated concept concordance now traces 77 concepts across all processed sections; 22 curated concept pages now carry source-grounded dossiers for deeper reading and promotion; scan-grounded promotion continues. |
| Extract equations and derivations | Started | Equation candidates, public math pages, first twelve-equation canon, candidate Steinmetz hysteresis-law page, generated equation atlas, and source formula maps now expose the broader formula layer; scan verification and worked examples continue. |
| Extract diagrams and figures | Started | RLI, AC Chapter V, and transient crops exist; 504 figure references, source visual maps, eight visual topic galleries, and 20 modern SVG reading aids now make the visual layer visible while crop verification continues. |
| Build glossary of forgotten electrical language | Started | Glossary index plus source-located pages for condensive reactance, wattless component, imaginary unit `j`, electrostatic capacity, counter e.m.f., and effective resistance. |
| Compare Steinmetz with modern EE | Started | Radiation and AC symbolic method comparisons exist. Needs broader equation-by-equation comparison. |
| Compare Steinmetz with Tesla-era science | Started | Introductory Tesla-era comparison and transient page exist. Needs Tesla source anchoring before stronger claims. |
| Include Ken Wheeler-style ether-field readings | Started | Reading guide and concept sections exist. Must remain visibly interpretive. |
| Build hidden gems index | Started | Hidden Gems now draws from the generated passage atlas and exposes candidate gems across the corpus; exact quote cards still require scan verification. |
| Build research questions section | Started | Section exists and should evolve after each source pass. |
| Build interactive tools | Started | Frequency/wavelength, AC waveform/harmonics, impedance, phasor/symbolic-form, power-factor, hysteresis-loss, transient RLC condenser-discharge, and lightning/surge traveling-wave tools exist. |
| Build repeatable data pipeline | Started | OCR seeding, image extraction, crop tooling, and index generation exist. |
| Build evidence ledger, chapter atlas, and chapter workbench | Done | `processed/evidence_ledger.json`, `processed/chapter_atlas.json`, `processed/chapter_workbench.json`, and public explanatory/generated pages are live. |
| Build concept concordance | Done as generated research layer | `processed/concept_concordance.json` and public concept-trace pages are live as candidate source-location aids. |
| Build completion audit and final scholarly gates | Started | `processed/completion_audit.json`, public completion audit, and world-class completion criteria are live. |
| Avoid hallucination | Repeating | Labels and verification queue are active. This must be enforced forever. |

## Expert Additions Beyond The Original Charter

These are new workstreams added after the foundation was built. They define what must happen for the archive to become world-class rather than merely large.

| Added Workstream | Status | Why It Matters |
| --- | --- | --- |
| Critical-edition editorial policy | Started | OCR correction, uncertain readings, page breaks, spelling variants, and math transcription now have a public rule page. |
| Citation/export system | Started | Researchers can export BibTeX, CSL JSON, stable source IDs, recommended citations, and public JSON data. |
| Canonical review workflow | Started | Candidate -> source-located -> scan-verified -> mathematically reviewed -> context reviewed -> canonical is public and tied to issue templates. |
| Guided reading routes | Started | Generated routes make the corpus browsable by purpose without replacing source-text, workbench, or verification layers. |
| Corpus completion authority layer | Started | Generated completion matrix prevents the archive from confusing processed breadth with complete Steinmetz coverage; critical unprocessed works now remain public frontier items. |
| Deep-decoding promotion queue | Started | Generated promotion queue turns broad corpus coverage into prioritized editorial targets for richer curated source pages. |
| Concept page depth dossiers | Started | Generated dossier sections prevent promoted concept pages from remaining thin placeholders while keeping OCR evidence visibly provisional. |
| Mathematical errata and notation ledger | Started | The first generated notation ledger maps source and modern symbols across the canonical equation seed set. |
| Diagram provenance ledger | Started | The generated provenance ledger maps promoted original crops and early redraws; the separate recreated visual index now tracks the newest generated guide diagrams. |
| Visual discovery galleries | Started | Topic-level visual galleries now make diagrams, figure candidates, formula leads, source maps, and verification paths discoverable together rather than as isolated pages. |
| Edition comparison layer | Started | A generated edition-collation queue now identifies source edition review work. |
| Patent-to-theory bridge | Started | A generated patent bridge links seeded patents to concepts, diagram targets, and theory-review actions. |
| Accessibility and reading-quality audit | Started | Generated structural audit covers alt text, tables, iframes, and manual review gates. |
| Mobile readiness audit | Started | Generated structural mobile audit tracks responsive CSS gates, source-text readers, table-heavy pages, scan embeds, visual panels, tools, and manual viewport review rules. |
| Research API and data export | Started | Public data manifest, reusable JSON exports, citation index, CSL JSON, and BibTeX now generate. |
| Canonical verification workbench | Started | Equation OCR snippets, original crop cards, and patent authority-review cards now route scan-check work item by item. |
| Claim attribution and source isolation | Started | A generated ledger now keeps source custody, Steinmetz wording, math candidates, modern translations, diagrams, patents, and interpretation layers separate for future multi-author expansion. |
| Contributor governance | Started | Contribution rules and source/equation/diagram review templates are now present. |
| Independent expert review packets | Started | Six generated packets route source custody/OCR, equation notation, diagram provenance, concepts/glossary, patents, and interpretive-boundary review. |
| Definitive release levels | Started | Named release levels now distinguish foundation, source coverage, scan verification, equation canon, diagram canon, patent authority, and definitive release. |
| Reusable Research Codex Engine | Started | Bootstrap script, templates, and public documentation define how to reuse the architecture for Tesla, ether history, or other research domains without mixing claims across subjects. |

## Extraction Requirements From The Original Charter

| Requirement | Status | Next Promotion Step |
| --- | --- | --- |
| 1. Every major concept Steinmetz explains | Started | Expand source-by-source concept index and promote pages only after source locations are recorded. |
| 2. Every important equation and derivation | Started | First twelve-equation canon is published as source-located candidate data and pages; generated equation atlas now routes 3,845 formula candidates into review families; next step is scan verification and worked examples. |
| 3. Every diagram, figure, circuit, waveform, and geometric representation | Started | Use the figure candidate atlas to route 504 OCR/PDF-text figure references into source-text, workbench, crop, and verification passes; use the recreated visual index as a labeled modern guide layer. |
| 4. Every important definition of electrical terms | Started | Add exact Steinmetz wording to concept and glossary pages. |
| 5. Every unusual, obsolete, or nonmodern scientific term | Started | Promote `electrostatic capacity`, `counter-electromotive force`, and `effective resistance`. |
| 6. Statements on ether, fields, magnetism, dielectricity, hysteresis, reactance, impedance, transients, AC, complex quantities, symbolic methods, and waves | Done as generated evidence layer, repeating for verification | `processed/theme_evidence_atlas.json` and public theme pages gather source-located hits and snippets; next step is scan verification and promotion of the strongest passages. |
| 7. Where Steinmetz differs from modern textbook language | Started | Continue comparison pages, especially for symbolic method, reactance, admittance, and transients. |
| 8. Where Steinmetz anticipates, clarifies, or conflicts with modern EE | Started | Tie claims to exact quotes and modern formulas. |
| 9. Connections to Tesla-era electrical science | Started | Gather Tesla source passages before making stronger comparative pages. |
| 10. Connections to Ken Wheeler interpretations | Started | Keep as labeled interpretive readings with fact/interpretation/speculation separated. |
| 11. Hidden gems | Started | Convert priority quotes into scan-verified entries with research questions. |

## Layer Requirements

Each mature concept, equation, diagram, or comparison page should include these layers:

| Layer | Status | Rule |
| --- | --- | --- |
| Steinmetz original wording and meaning | Started | Quote sparingly and cite exact source location. |
| Modern electrical engineering interpretation | Started | Use modern terms only after preserving Steinmetz's framing. |
| Mathematical breakdown | Started | Preserve original notation before translating it. |
| Plain-English explanation | Started | Clarify without flattening the technical content. |
| Historical context | Started | Mark as historical note and source later. |
| Ether-field interpretive reading | Started | Label as interpretation, not historical proof. |
| Tesla-era comparison | Started | Label overlap, divergence, and open questions. |
| Current status of the concept | Started | Say whether it is still used, renamed, absorbed, or obsolete. |

## Repository Architecture Tracker

| Directory | Status | Role |
| --- | --- | --- |
| `sources/` | Done, expanding | Raw source texts, public-domain records, scans, OCR custody, manifests. |
| `sources/steinmetz_patents/` | Started | Patent register, authority workflow, and future raw patent custody folders. |
| `processed/` | Done, expanding | Cleaned OCR, chapter candidates, JSON indexes, figure/equation/glossary candidates, generated annotations, and crosslink indexes. |
| `analysis/` | Started | Deep commentary by book, chapter, concept, equation, and diagram. |
| `concepts/` | Started | Repo-native encyclopedia source material. |
| `math/` | Started | Equation catalogs, canonical equation set, derivations, notation translations, worked examples. |
| `diagrams/` | Started | Original crops, manifests, public copies, modern redraws. |
| `comparisons/` | Started | Mainstream, Steinmetz, Tesla-era, and ether-field comparison notes. |
| `glossary/` | Started | Historical terminology and modern equivalents. |
| `hidden-gems/` | Started | Overlooked statements and follow-up questions. |
| `research-questions/` | Started | Living research agenda. |
| `pipeline/` | Started | Repeatable processing scripts and extraction workflow. |
| `templates/` | Started | Page templates for future promotions. |
| `site/` | Done, expanding | Public website and interactive tools. |

## Website Section Tracker

| Section From Charter | Status | Current Location |
| --- | --- | --- |
| 1. Home | Done | `site/src/content/docs/index.mdx`, with `site/src/content/docs/start-reading.mdx` as a guided reader entry |
| 2. Who Was Steinmetz? | Done | `site/src/content/docs/who-was-steinmetz.mdx` |
| 3. Why Steinmetz Matters | Done | `site/src/content/docs/why-steinmetz-matters.mdx` |
| 4. Source Library | Done, expanding | `site/src/content/docs/source-library/index.mdx`, source pages with source-access readers, generated book coverage pages, generated source-text browser pages, generated chapter workbench pages, and generated concept concordance pages |
| 4a. Expanded Bibliography Intake | Started | `site/src/content/docs/source-library/bibliography-intake.mdx` |
| 4b. Steinmetz Patent Register | Started | `site/src/content/docs/sources/steinmetz-patents/index.mdx` |
| 4c. Source Text Browser | Started | `site/src/content/docs/source-texts/` generated from processed chapter records |
| 4d. Book Coverage Atlas | Started | `site/src/content/docs/book-coverage/` generated from processed workbench records, with one index and one source-level coverage page per seeded source, now including source study guides |
| 4e. Chapter Research Workbench | Started | `site/src/content/docs/chapter-workbench/` generated from processed chapter, concept, glossary, equation, figure, and quote records |
| 4f. Concept Concordance | Started | `site/src/content/docs/concept-concordance/` generated from processed text sections and curated concept vocabulary |
| 4f-1. Concept Page Dossiers | Started | `site/src/content/docs/concepts/` curated pages now include generated source-grounded dossier sections, with `site/src/content/docs/concepts/dossier-index.mdx` as the coverage index |
| 4f-2. Theme Evidence Atlas | Started | `site/src/content/docs/theme-evidence/` generated from processed text sections and charter-critical theme vocabulary |
| 4f-3. Guided Reading Routes | Started | `site/src/content/docs/reading-routes/` generated from book coverage metadata to give newcomers, engineers, field-language readers, diagram readers, and patent researchers clean entry paths |
| 4f-4. Deep-Decoding Promotion Queue | Started | `site/src/content/docs/roadmap/deep-decoding-promotion-queue.mdx` and `processed/deep_decoding_promotion_queue.json` rank the next sections to convert from generated coverage into curated long-form pages |
| 8a. Figure Candidate Atlas | Started | `site/src/content/docs/diagrams/figure-candidate-atlas.mdx` generated from figure candidates and promoted scan crops |
| 8b. Source Visual Maps | Started | `site/src/content/docs/diagrams/source-visuals/` generated for all 15 processed sources, linking promoted crops, figure candidates, modern guide diagrams, source text, workbench, and formula maps |
| 7a. Source Formula Maps | Started | `site/src/content/docs/mathematics/source-formula-maps/` generated for all 15 processed sources, linking formula families, top candidates, source text, workbench, and visual maps |
| 4g. Completion Audit | Started | `site/src/content/docs/roadmap/completion-audit.mdx` generated from source readiness gates |
| 4h. Citation And Data Export | Started | `site/src/content/docs/roadmap/citation-and-data-export.mdx`, `CITATION.cff`, public `/data/` exports, BibTeX, and CSL JSON generated |
| 4i. Editorial Policy And Review Workflow | Started | `site/src/content/docs/roadmap/editorial-policy.mdx`, `site/src/content/docs/roadmap/canonical-review-workflow.mdx`, contribution rules, and GitHub issue templates |
| 4j. Notation, Provenance, Schema, And Review Packets | Started | `site/src/content/docs/roadmap/notation-ledger.mdx`, `diagram-provenance-ledger.mdx`, `schema-reference.mdx`, and `expert-review-packets.mdx` generated |
| 4k. Canonical Verification Workbench | Started | `site/src/content/docs/roadmap/canonical-verification-workbench.mdx`, `equation-verification-queue.mdx`, `figure-verification-queue.mdx`, and `patent-verification-queue.mdx` generated |
| 4l. Claim Attribution Ledger | Started | `site/src/content/docs/roadmap/claim-attribution-ledger.mdx` and `processed/claim_attribution_ledger.json` generated |
| 5. Book-by-Book Deep Decoding | Started | RLI, AC, transient, engineering math, Theoretical Elements, Electric Apparatus, General Lectures, Relativity and Space, Commonwealth Edison, historical-context pages, and generated book coverage pages |
| 6. Concept Encyclopedia | Started | `site/src/content/docs/concepts/` |
| 7. Mathematics of Steinmetz | Started | `site/src/content/docs/mathematics/` plus generated `mathematics/equation-atlas/` family pages and generated source formula maps |
| 8. Diagram Archive | Started | `site/src/content/docs/diagrams/` with global lightbox viewing, figure candidate atlas, recreated visual index, original crop pages, and generated source visual maps |
| 9. Steinmetz vs Modern EE | Started | `site/src/content/docs/comparisons/` |
| 10. Steinmetz and Tesla-Era Electrical Science | Started | `site/src/content/docs/comparisons/tesla-era-electrical-science.mdx` |
| 11. Steinmetz and Ken Wheeler-Style Field Interpretation | Started | `site/src/content/docs/comparisons/ether-field-reading-guide.mdx` |
| 12. Hidden Gems Index | Started | `site/src/content/docs/hidden-gems.mdx` |
| 13. Glossary of Forgotten Electrical Language | Started | `site/src/content/docs/glossary/` |
| 14. Research Questions | Started | `site/src/content/docs/research-questions.mdx` |
| 15. Interactive Tools | Started | `site/src/content/docs/tools/index.mdx`, including wave relation, AC waveform/harmonics, impedance, phasor/symbolic form, power factor, hysteresis loss, transient RLC response, and lightning/surge traveling waves. |
| Reader filtering and multilingual access | Started | Sidebar source-only filter, page-local ask/search, Google Translate shortcuts, lightbox diagram viewer, and readable source/code transcript blocks. |
| Mobile readiness audit | Started | `site/src/content/docs/roadmap/mobile-readiness-audit.mdx` and `processed/mobile_readiness_audit.json` track responsive CSS gates and high-risk generated page families for phone review. |
| 16. Data Pipeline | Started | `pipeline/` and `processed/source_processing_status.md` |

## Data Pipeline Tracker

| Pipeline Function | Status | Current Implementation |
| --- | --- | --- |
| Ingest PDFs or text files | Started | Local source folders and `sources/source_catalog.json`. |
| Run OCR if needed | Pending | External OCR workflow still needs standardization. |
| Split by book/chapter/page | Started | `seed_source_from_ocr.py`, `extract_pdf_text.py`, and source-specific parsers for `Theoretical Elements`, `America and the New Epoch`, and `Commonwealth Edison`. |
| Extract equations | Started | Candidate extraction in generated indexes. |
| Extract figures | Started | PyMuPDF image extraction and crop tooling. |
| Create metadata | Started | Source catalog plus crop manifests. |
| Generate concept tags | Started | Research index builder. |
| Generate summaries | Started | Public source and chapter pages, mostly curated. |
| Generate public source text readers | Started | `generate_source_text_pages.py` builds 394 public source-text section pages from processed chapter records. |
| Generate book coverage atlas pages | Started | `generate_book_coverage_atlas.py` builds 15 source-level book-coverage pages plus an index and `processed/book_coverage_atlas.json`, including generated source study-guide panels and route links. |
| Generate source research dashboards | Started | `generate_source_research_dashboards.py` appends dashboard front doors to all 15 curated source overview pages and writes `processed/source_research_dashboards.json`. |
| Generate chapter workbench pages | Started | `generate_chapter_workbench.py` builds 394 public workbench section pages plus indexes and `processed/chapter_workbench.json`. |
| Generate concept concordance pages | Started | `generate_concept_concordance.py` builds 78 public concept-concordance pages plus `processed/concept_concordance.json`. |
| Generate concept page dossiers | Started | `generate_concept_page_dossiers.py` appends source-grounded dossier sections to 22 curated concept pages and writes `processed/concept_page_dossiers.json`. |
| Generate theme evidence atlas pages | Started | `generate_theme_evidence_atlas.py` builds 10 public theme-evidence pages plus `processed/theme_evidence_atlas.json`. |
| Generate figure candidate atlas pages | Started | `generate_figure_candidate_atlas.py` builds a public figure atlas plus `processed/figure_candidate_atlas.json`, routing promoted crops and OCR/PDF-text candidates back to source pages. |
| Generate equation atlas pages | Started | `generate_equation_atlas.py` builds `processed/equation_atlas.json`, public data export, and source-routed formula family pages. |
| Generate recreated visual guides | Started | `generate_recreated_visuals.py` builds `processed/recreated_visual_index.json`, public SVG assets, and a recreated visual index page. |
| Generate crosslinked research surfaces | Started | `generate_crosslinked_research_surfaces.py` builds source visual maps, source formula maps, concept math/visual bridges, and `processed/crosslinked_research_surfaces.json`. |
| Generate guided reading route pages | Started | `generate_reading_routes.py` builds `processed/reading_routes.json` and the public `reading-routes/` page from source coverage, workbench links, and candidate density. |
| Generate deep-decoding promotion queue | Started | `generate_deep_decoding_queue.py` builds `processed/deep_decoding_promotion_queue.json` and a public roadmap page ranking the next source sections for curated promotion. |
| Generate completion audit | Started | `generate_completion_audit.py` builds `processed/completion_audit.json` and the public completion audit page. |
| Generate scholarly exports | Started | `generate_scholarly_exports.py` builds `CITATION.cff`, citation JSON, CSL JSON, BibTeX, public `/data/` exports, a data manifest, and the public citation/export page. |
| Generate world-class scholarly ledgers | Started | `generate_world_class_artifacts.py` builds notation, diagram provenance, schema reference, and expert review packet JSON plus public roadmap pages. |
| Generate publication readiness controls | Started | `generate_publication_readiness.py` builds release readiness, accessibility audit, edition comparison, and patent bridge JSON plus public roadmap pages. |
| Generate mobile readiness audit | Started | `generate_mobile_readiness_audit.py` builds `processed/mobile_readiness_audit.json` and a public roadmap page, then exposes the JSON through public data exports. |
| Generate canonical verification queues | Started | `generate_verification_workbench.py` builds equation OCR-snippet queues, original-figure crop review cards, patent authority-review cards, and public roadmap pages. |
| Generate claim attribution ledger | Started | `generate_claim_attribution_ledger.py` classifies evidence, canonical equations, modern translations, diagrams, and patents by claim type and interpretation layer. |
| Generate glossary candidates | Started | `processed/glossary_index.json`. |
| Generate equation candidates | Started | `processed/equation_index.json`. |
| Generate diagram candidates | Started | `processed/figure_index.json`. |
| Store outputs as JSON and Markdown | Started | `processed/` plus site MDX pages. |
| Preserve source page references | Started | Active rule; many candidates still need page verification. |

## Required Data Files

| Data File | Status |
| --- | --- |
| `source_manifest.json` | Started through source catalog and per-source manifests. |
| `book_metadata.json` | Started in source records, needs per-book promotion. |
| `chapters.json` | Started in processed source outputs. |
| `equations.json` | Started through `processed/equation_index.json`. |
| `canonical_equations.json` | Started with the first twelve source-located equation records. |
| `equation_atlas.json` | Started as the generated source-routed formula family atlas across all processed equation candidates. |
| `figures.json` | Started through `processed/figure_index.json` and crop manifests. |
| `concepts.json` | Started through `processed/concept_index.json`. |
| `glossary.json` | Started through `processed/glossary_index.json`. |
| `quotes.json` | Started through `processed/quote_index.json`. |
| `annotations.json` | Started through per-source files and generated `processed/annotations_index.json`. |
| `crosslinks.json` | Started through per-source files and generated `processed/crosslinks_index.json`. |
| `evidence_ledger.json` | Done as the archive-wide traceability layer for source claims, candidates, and promoted assets. |
| `chapter_atlas.json` | Done as the archive-wide OCR/PDF-text theme routing map for chapters, lectures, sections, and report divisions. |
| `book_coverage_atlas.json` | Started as the generated source-by-source coverage map with section links, theme totals, concept density, glossary density, candidate counts, and source study-guide routes. |
| `source_research_dashboards.json` | Started as the generated source overview dashboard layer connecting curated source pages to reading, workbench, formula, visual, theme, concept, and verification routes. |
| `chapter_workbench.json` | Done as the archive-wide generated workbench index joining section text, theme routing, term hits, equations, figures, quotes, links, and promotion status. |
| `concept_concordance.json` | Done as the archive-wide generated concept-trace index across processed source text. |
| `concept_page_dossiers.json` | Started as the curated concept-page enrichment layer built from concordance evidence. |
| `theme_evidence_atlas.json` | Done as the archive-wide generated evidence router for charter-critical themes across processed source text. |
| `figure_candidate_atlas.json` | Started as the archive-wide visual routing layer for promoted original crops and OCR/PDF-text figure references. |
| `recreated_visual_index.json` | Started as the generated index of modern source-keyed guide diagrams. |
| `crosslinked_research_surfaces.json` | Started as the generated bridge joining concepts, formulas, figures, source visual maps, and source formula maps. |
| `reading_routes.json` | Started as the archive-wide guided study route layer across all processed sections. |
| `deep_decoding_promotion_queue.json` | Started as the archive-wide editorial queue for converting source coverage into mature deep-decoding pages. |
| `completion_audit.json` | Started as the source-by-source readiness audit for canonical review. |
| `citation_index.json` | Started as the archive-wide citation record set for project and source records. |
| `citation_index.csl.json` | Started as the CSL JSON export for citation managers. |
| `citation_index.bib` | Started as the BibTeX export for citation managers. |
| `notation_ledger.json` | Started as the source/modern symbol review ledger for the first canonical equation set. |
| `diagram_provenance_ledger.json` | Started as the provenance ledger for original crops and modern redraws. |
| `schema_reference.json` | Started as the descriptive schema reference for processed and public exports. |
| `expert_review_packets.json` | Started as the routed expert-review bundle index. |
| `release_readiness.json` | Started as the named publication release-level map. |
| `accessibility_audit.json` | Started as the structural accessibility scan and manual gate list. |
| `mobile_readiness_audit.json` | Started as the structural mobile-readiness gate list and generated-page review queue. |
| `edition_comparison_index.json` | Started as the edition-collation queue for seeded sources. |
| `patent_theory_bridge.json` | Started as the patent-to-concept and patent-to-theory bridge. |
| `canonical_verification_workbench.json` | Started as the queue index for equation, figure, and patent verification work. |
| `equation_verification_queue.json` | Started as the scan-check queue for canonical equation candidates, including OCR snippets and source/workbench links. |
| `figure_verification_queue.json` | Started as the scan-crop review queue for original Steinmetz figures. |
| `patent_verification_queue.json` | Started as the authority PDF, claim, drawing, and theory-bridge queue for seeded patents. |
| `claim_attribution_ledger.json` | Started as the source-isolation ledger for facts, candidates, translations, diagrams, patents, and interpretive boundaries. |
| `site/public/data/manifest.json` | Started as the public data export manifest. |
| generated `source-texts/` pages | Started with 394 text-section pages plus source indexes, marked candidate and pagefind-disabled. |
| generated `book-coverage/` pages | Started with one corpus index and 15 source-level coverage maps. |
| generated `chapter-workbench/` pages | Started with 394 section workbench pages plus source indexes and a corpus index. |
| generated `concept-concordance/` pages | Started with 77 concept pages plus a corpus index. |
| generated concept dossier sections | Started with 22 enriched curated concept pages plus a concept dossier index. |
| generated `reading-routes/` page | Started with nine purpose-built study paths across the processed corpus. |
| generated completion audit page | Started with source-by-source readiness gates and next actions. |
| `steinmetz_bibliography_manifest.json` | Started with Wikipedia-derived works intake and source-processing status. |
| `patent_register.json` | Started with Wikipedia-listed patent examples and Google Patents authority links. |

## Near-Term Milestone Sequence

| Milestone | Work Items | Definition Of Done |
| --- | --- | --- |
| M1. Public trust hardening | Master tracker, public tracker, verification queue, Pages, build checks. | A new contributor can see exactly what exists and what remains candidate. |
| M2. RLI scan-verified anchor | Verify spectrum table, Figs. 14, 15, 18, 19, and page references. | RLI first-source pages can be marked reviewed where applicable. |
| M3. AC symbolic canon | Verify `j`, rectangular components, `Z = r + jx`, reactance, admittance, conductance, susceptance, and power factor. | AC symbolic method section now has a first canonical equation set and Chapter V crops; scan verification remains. |
| M4. Transient canon | Verify permanent/transient terms, RLC oscillation, critical resistance, decrement, and surge figures. | Transient theory has canonical equation, diagram, and interactive response pages. |
| M5. Diagram expansion | Extract and publish original AC and transient figures with manifests. | Started with AC Chapter V and first transient condenser/decrement figures; source-keyed redraw sheets added; next step is surge, line, hysteresis, and apparatus figures. |
| M6. Glossary expansion | Promote key older terms with source usage and modern equivalents. | Started with source-located pages for electrostatic capacity, counter e.m.f., and effective resistance; concept pages now cover conductance, susceptance, and dielectric loss. |
| M7. Pipeline refinement | Improve parsers, page maps, OCR cleanup, annotation, crosslink, evidence, and chapter-atlas JSON. | Aggregate annotation, crosslink, evidence ledger, and chapter atlas now generate; Theoretical Elements, America, and Commonwealth Edison now have source-specific parsers; next step is scan verification and page-map refinement. |
| M7A. Public text coverage | Generate public reader pages for every processed chapter and section. | Generated 410 source-text pages, including 394 processed text-section pages and 16 index pages. |
| M7B. Book coverage atlas | Generate source-level coverage maps so every seeded book has a non-shell representation. | Generated 16 book-coverage pages, including one corpus index and 15 source maps, source study-guide panels, and `processed/book_coverage_atlas.json`. |
| M7C. Chapter research coverage | Generate a source-linked research map for every processed chapter and section. | Generated 410 chapter-workbench pages, including 394 section maps and 16 index pages, backed by `processed/chapter_workbench.json`. |
| M7D. Concept trace coverage | Generate cross-source concept concordance pages from the full processed text corpus. | Generated 78 concept-concordance pages, including 77 concept pages and a corpus index, backed by `processed/concept_concordance.json`. |
| M7E. Completion audit coverage | Generate source-by-source readiness gates and final scholarly criteria. | Generated `processed/completion_audit.json`, public completion audit, and world-class criteria page. |
| M7F. Scholarly export and review governance | Generate citation/data exports and public review rules. | Generated `CITATION.cff`, citation index, BibTeX, CSL JSON, public data manifest, editorial policy, canonical review workflow, and GitHub review templates. |
| M7G. Critical scholarly ledgers | Generate notation, diagram provenance, schema, and expert review packet controls. | Generated four processed ledgers and four public roadmap pages for review routing. |
| M7H. Publication readiness controls | Generate release, accessibility, edition, and patent bridge controls. | Generated four processed readiness indexes and four public roadmap pages. |
| M7I. Canonical verification workbench | Generate scan-check queues for equations, figures, and patents. | Generated four processed queue indexes and four public roadmap pages with source links and OCR snippets. |
| M7J. Claim attribution ledger | Generate source-isolation and interpretation-layer controls. | Generated a 4,890-record attribution ledger and public roadmap page. |
| M7K. Figure candidate atlas | Generate a visual-routing map for all promoted scan crops and remaining figure candidates. | Public figure atlas separates original crop assets from OCR/PDF-text candidates and links each candidate back to source text and workbench pages. |
| M7L. Guided reading routes | Generate purpose-built reader pathways so the corpus is explorable without becoming shallow. | Public route page now exposes nine generated pathways backed by `processed/reading_routes.json` and linked from home, sidebar, Start Reading, Source Library, and data exports. |
| M7M. Mobile publication hardening | Treat phone reading as a publication gate for source text, tables, diagrams, tools, and navigation. | Global responsive CSS is in place; `processed/mobile_readiness_audit.json` and a public roadmap page now track CSS gates, page-risk patterns, and required manual viewports. |
| M7N. Deep-decoding promotion queue | Turn broad generated coverage into prioritized curated writing work. | All 394 processed sections are ranked globally and by source-balanced priority; the public queue defines required deep-page layers and links every candidate to source text and workbench pages. |
| M7O. Concept page depth | Prevent curated concept pages from feeling like shells by attaching source-grounded dossier sections to each promoted concept. | Twenty-two concept pages now carry corpus counts, source distribution, priority passages, aliases, concordance links, and editorial action lists, backed by `processed/concept_page_dossiers.json`. |
| M7P. Passage discovery atlas | Surface source-dense passages for readers and editors without treating OCR snippets as verified quotes. | Generated 150 balanced public passage candidates from 5,427 source-derived candidates, plus theme pages, a research map, a study curriculum, a rebuilt hidden-gems page, and public data export. |
| M7Q. Equation atlas and formula routing | Make the full mathematical candidate layer visible without promoting OCR formulas as verified. | Generated 3,845 equation/formula candidates, 2,528 reviewable relation candidates, and 1,330 strong formula candidates across source-routed family pages and public data export. |
| M7R. Recreated visual breadth | Expand visual reading aids beyond the first-wave diagrams while keeping them separate from original figures. | Generated 10 additional source-keyed SVG guide diagrams and a recreated visual index, bringing the public modern SVG guide layer to 20 diagrams. |
| M7S. Crosslinked math/visual surfaces | Stop treating diagrams, formulas, concepts, and source pages as isolated showcases. | Generated source visual maps and source formula maps for all 15 processed sources, plus math/visual evidence bridges on 22 curated concept pages. |
| M7T. Source overview dashboards | Prevent curated source pages from being thin doors beside richer generated layers. | Added generated dashboards to all 15 curated source overview pages, plus a source-dashboard index and public data export. |
| M7U. Visual topic galleries | Treat diagrams as a site-wide discovery system rather than one archive page. | Registered all 20 modern guide diagrams in the generated visual index, regenerated source/concept visual surfaces, and added eight theme galleries with figure and formula leads. |
| M8. Expanded Steinmetz source intake | Add notable works and patents to control files, public pages, and verification queue. | Wikipedia bibliography and patent examples are now tracked; next step is acquisition and source-by-source processing. |
| M9. Future multi-author architecture | Prepare separate source domains for Tesla, Dollard, Walter Russell, and others. | Wider scope can be added without blending fact, comparison, and interpretation. |

## Multi-Author Future Scope

The current archive should remain Steinmetz-first. The site architecture should eventually support other research domains such as Nikola Tesla, Eric Dollard, Walter Russell, and related figures, but only after the source model is strong enough to keep each author's claims separate.

Future rule: never merge an author's position into Steinmetz's. Use comparison pages, explicit citations, and labeled interpretive sections.

The future architecture is now tracked publicly at `site/src/content/docs/roadmap/future-codex-architecture.mdx`. It is intentionally downstream of the Steinmetz-first milestone.

## Operating Rules

- Keep raw source custody visible before commentary.
- Keep original notation before modern translation.
- Keep diagrams tied to source page, crop manifest, and checksum where possible.
- Keep source fact, modern explanation, mathematical reconstruction, historical note, interpretive reading, speculative connection, and needs-verification labels visible.
- Do not promote OCR-derived claims to reviewed status without scan verification.
- Do not use Tesla, Wheeler, Dollard, or ether-field language as proof of Steinmetz's intent unless Steinmetz explicitly says it.
- Do not erase alternative interpretations; label them.
- Do not write shallow summary pages when a structured source page is needed.

## Update Log

| Commit | Contribution |
| --- | --- |
| `8747b5b` | Built the first Steinmetz Decoded research archive foundation. |
| `2aa209a` | Added PDF image extraction pipeline and first scan figure crop. |
| `58497a0` | Configured GitHub Pages deployment. |
| `d7d7866` | Added research index pipeline and original Steinmetz figure crops. |
| `90d0ed6` | Expanded AC and transient research codex pages. |
| `1e77f25` | Added master project tracker and power factor tool. |
| `26cff7e` | Added original AC symbolic method figure set. |
| `ee7c982` | Added original transient figure set. |
| `fa62a7d` | Promoted source-located glossary terms. |
| `d87468b` | Generated annotation and crosslink indexes. |
| `4f023b9` | Added first canonical equation set. |
| `a7bc0fe` | Added transient RLC explorer. |
| `d6078ef` | Added source-keyed diagram redraw sheets. |
| `5173d6e` | Added phasor symbolic form explorer. |
| `b7c70a7` | Added hysteresis loss explorer and Steinmetz-law candidate page. |
| `131b7b9` | Added AC waveform harmonics explorer and wave-shape concept page. |
| `b3f8d41` | Added lightning surge traveling-wave explorer and surge concept page. |
| `6330cc6` | Added expanded Steinmetz bibliography intake, seeded patent register, and future codex architecture page. |
| `2d678d1` | Seeded four additional Steinmetz OCR sources and added public source entry pages. |
| `646e3a2` | Added source reader UX, original-source access, reader filters, translation shortcuts, and diagram lightbox. |
| `5ad0fa6` | Added source-specific parsers for Theoretical Elements and America, expanded the chapter atlas, and published new deep-decoding pages. |
| `f920f7d` | Extracted Commonwealth Edison PDF text, generated page-map and report-section catalogs, added reactor/synchronism pages, and updated indexes. |
| `5532083` | Added the generated source-text browser for all processed chapters, lectures, sections, and report divisions. |
| `98d531d` | Added the generated chapter research workbench for all processed sections. |
| `d5c69f6` | Added the generated concept concordance across the processed Steinmetz corpus. |
| `feb0145` | Added the generated completion audit and world-class finishing criteria. |
| `62967cd` | Added scholarly citation/data exports, editorial policy, canonical review workflow, and issue templates. |
| `69ed6ec` | Added notation, diagram provenance, schema reference, and expert review packet ledgers. |
| `7935569` | Added publication readiness, accessibility, edition comparison, and patent-to-theory bridge controls. |
| `4906c5d` | Added the canonical verification workbench, equation review queues, figure review queues, and patent authority-review queues. |
| `e8c79bd` | Added the claim attribution ledger and source-isolation data model for facts, candidates, translations, diagrams, patents, and interpretive boundaries. |
| `f87c901` | Added the generated book coverage atlas and upgraded the Steinmetz profile and browsing UX. |
| `2ddab91` | Fixed source-reader UX and browsing paths with improved reader controls, source access, and navigation. |
| `59b1978` | Added the generated theme evidence atlas across charter-critical Steinmetz themes. |
| `d00189e` | Strengthened generated source-text and snippet readability so source manuscripts, workbench excerpts, concordance snippets, and theme evidence excerpts expand instead of trapping text in scroll boxes. |
| `1ebcddf` | Added generated figure candidate atlas so promoted scan crops and OCR/PDF-text figure references are visible, linked, and reviewable source by source. |
| `acca450` | Added generated guided reading routes so readers can enter the processed corpus by purpose while staying linked to source text, workbench pages, verification routes, and public data exports. |
| `c88cbc3` | Added generated source study guides to every book coverage page, giving each source first-read, math, visual, and field-language routes from existing metadata. |
| `3fb4a60` | Added site-wide mobile responsive hardening for grids, cards, tables, source readers, code blocks, fixed controls, and visual panels. |
| `4afac0c` | Added the generated mobile readiness audit, public data export, and tracker controls for phone/tablet publication review. |
| `eeb9284` | Added the generated deep-decoding promotion queue, public roadmap page, and public data export for source-balanced curated-page promotion. |
| `pending` | Added generated passage atlas, research map, study curriculum, and hidden-gems discovery layer across the 15-source corpus. |
| `pending` | Added generated equation atlas, formula-family pages, recreated visual index, and 10 new source-keyed guide diagrams. |
| `pending` | Added generated visual topic galleries and corrected recreated-visual indexing so all 20 modern guide diagrams propagate into source maps and concept bridges. |

## Next Work Queue

1. Verify RLI page anchors and promote the first reviewed source claims.
2. Complete second-pass review of original AC Chapter V figure crops and refine the symbolic-method redraw sheet.
3. Complete second-pass review of original transient figure crops and refine the condenser-response redraw sheet.
4. Scan-verify the first 12 canonical equations and expand each with exact page anchors and additional worked examples.
5. Use the generated equation atlas to promote the first source-balanced batch of formula pages beyond the seed canon, beginning with transients, impedance/admittance, engineering mathematics, distributed constants, and apparatus formulas.
6. Use the generated recreated visual index and visual topic galleries to attach visual guide diagrams to the most relevant concept, equation, chapter workbench, and source guide pages.
7. Scan-verify glossary term pages for `electrostatic capacity`, `counter-electromotive force`, and `effective resistance`, then promote dielectric and hysteresis terms.
8. Refine generated annotation and crosslink indexes with page maps, confidence levels, and curated canonical links.
9. Add advanced interactive tools: multi-section surge lattice diagram, vector phasor animation, and source-specific worked calculators.
10. Scan-verify the Commonwealth Edison report, crop Appendix Figure 1, and promote corrected synchronizing-power equations.
11. Use the generated reading routes, book coverage atlas, source-text browser, chapter workbench, and concept concordance to promote the next batch of chapter-by-chapter deep readings without losing full-text coverage.
12. Use the deep-decoding promotion queue to promote the next source-balanced batch of curated pages, beginning with high-value math, transient, field-language, and apparatus sections.
13. Use the passage atlas to promote the first source-balanced batch of scan-verified hidden gems, beginning with field/ether boundaries, symbolic AC, transients, and dielectric-field passages.
14. Acquire and process high-priority bibliography intake sources: `On the Law of Hysteresis`, `Complex Quantities and Their Use in Electrical Engineering`, `The General Equations of the Electric Circuit`, `Mechanical Forces in Magnetic Fields`, and first-edition variants where available.
15. Complete the Steinmetz patent authority pass, download patent PDFs/drawings, and create one verified patent page per patent.
16. Use the new citation/data exports, scholarly ledgers, and review templates to prepare external expert review packets.
17. Use the generated figure candidate atlas to crop the highest-value unpromoted figures from AC, RLI, Elementary Lectures, General Lectures, Electric Apparatus, Engineering Mathematics, and Relativity and Space.
18. Use the mobile readiness audit to manually inspect the highest-risk generated pages at 360px, 430px, 768px, and desktop widths before each publication push.
19. Add the remaining world-class apparatus: formal JSON schemas, deeper accessibility testing, completed edition collation, verified patent dossiers, and named release publication notes.
