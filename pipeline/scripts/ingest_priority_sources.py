#!/usr/bin/env python3
"""Ingest the next priority Steinmetz sources and publish an intake workbench.

This script is intentionally conservative. Internet Archive OCR sources are
seeded into the same candidate pipeline as the existing corpus. DOI, HathiTrust,
archive, and patent records are registered as official acquisition targets, but
they are not promoted as processed until a primary scan or file is in custody.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


BASE_URL = ""
TODAY = date.today().isoformat()


@dataclass(frozen=True)
class InternetArchiveSource:
    source_id: str
    title: str
    year: int
    source_type: str
    internet_archive_id: str
    edition_note: str
    why_it_matters: str
    processing_note: str


IA_SOURCES = [
    InternetArchiveSource(
        source_id="theory-calculation-alternating-current-phenomena-1897",
        title="Theory and Calculation of Alternating Current Phenomena",
        year=1897,
        source_type="book_edition",
        internet_archive_id="theoryandcalcul03steigoog",
        edition_note="First edition; Open Library lists this Internet Archive item for the 1897 W. J. Johnston edition.",
        why_it_matters="Earliest book-form AC symbolic-method source; essential for edition comparison against the later 1916 source already processed.",
        processing_note="OCR-seeded as a separate edition so the archive can compare Steinmetz's original AC presentation against later revisions.",
    ),
    InternetArchiveSource(
        source_id="theory-calculation-alternating-current-phenomena-1900",
        title="Theory and Calculation of Alternating Current Phenomena",
        year=1900,
        source_type="book_edition",
        internet_archive_id="theorycalculatio00steiiala",
        edition_note="Third edition, revised and enlarged; Open Library and Wikimedia Commons point to this Internet Archive item.",
        why_it_matters="Early expanded AC edition; important for tracking the growth of impedance, reactance, transformer, harmonic, and symbolic-method language.",
        processing_note="OCR-seeded as its own source, not merged into the 1916 edition.",
    ),
    InternetArchiveSource(
        source_id="theory-calculation-electric-circuits",
        title="Theory and Calculation of Electric Circuits",
        year=1917,
        source_type="book",
        internet_archive_id="theoryandcalcul06steigoog",
        edition_note="Open Library lists this as a 1917 McGraw-Hill source with Internet Archive identifier theoryandcalcul06steigoog.",
        why_it_matters="Core circuit-theory sequel to Alternating Current Phenomena and companion to Electric Apparatus.",
        processing_note="OCR-seeded as a new core source for circuit equations, network behavior, constants, and applied calculation.",
    ),
    InternetArchiveSource(
        source_id="electric-discharges-waves-impulses-1914",
        title="Elementary Lectures on Electric Discharges, Waves and Impulses, and Other Transients",
        year=1914,
        source_type="lecture_collection_edition",
        internet_archive_id="elementarylectur00stei",
        edition_note="Second edition, revised and enlarged; Open Library lists the 1914 edition with Internet Archive identifier elementarylectur00stei.",
        why_it_matters="Expanded edition of the transient lecture source, with special value for waves, impulses, lightning, and discharge language.",
        processing_note="OCR-seeded separately from the 1911 edition to keep edition differences visible.",
    ),
]


OFFICIAL_INTAKE_RECORDS: list[dict[str, Any]] = [
    {
        "work_id": "law-of-hysteresis-1892",
        "title": "On the Law of Hysteresis",
        "year": 1892,
        "source_type": "journal_article",
        "priority": "critical",
        "status": "registered_primary_article_target",
        "authority_refs": [
            {"type": "doi", "url": "https://doi.org/10.1109/T-AIEE.1892.5570437"}
        ],
        "why_it_matters": "Foundational source for Steinmetz's hysteresis law, magnetic loss, and the later Steinmetz equation.",
        "repo_action": "Acquire a primary scan or publisher PDF, then OCR, page-map, extract equations and hysteresis diagrams, and promote only scan-checked claims.",
    },
    {
        "work_id": "complex-quantities-use-electrical-engineering-1894",
        "title": "Complex Quantities and Their Use in Electrical Engineering",
        "year": 1894,
        "source_type": "conference_paper",
        "priority": "critical",
        "status": "registered_primary_proceedings_target",
        "authority_refs": [
            {
                "type": "publication_note",
                "value": "Proceedings of the International Electrical Congress Held in Chicago, August 21-25, 1893, pp. 33-74."
            },
            {
                "type": "google_books",
                "url": "https://books.google.com/books/about/Proceedings_of_the_International_Electri.html?id=X09AAQAAMAAJ"
            }
        ],
        "why_it_matters": "Flagship source for complex quantities, the symbolic method, and early phasor engineering.",
        "repo_action": "Acquire and verify against the Proceedings scan. Do not use Scribd or forum PDFs as custody copies until they match the primary proceedings.",
    },
    {
        "work_id": "theory-calculation-alternating-current-phenomena-1897",
        "title": "Theory and Calculation of Alternating Current Phenomena",
        "year": 1897,
        "source_type": "book_edition",
        "priority": "critical",
        "status": "ocr_seeded",
        "related_local_source_id": "theory-calculation-alternating-current-phenomena-1897",
        "authority_refs": [
            {"type": "internet_archive", "url": "https://archive.org/details/theoryandcalcul03steigoog"},
            {"type": "open_library", "url": "https://openlibrary.org/books/OL6904963M/Theory_and_calculation_of_alternating_current_phenomena"},
        ],
        "why_it_matters": "Earliest book edition now separated for edition comparison.",
        "repo_action": "Scan-verify OCR chapter starts, compare with 1900 and 1916 editions, then promote symbolic-method deltas.",
    },
    {
        "work_id": "theory-calculation-alternating-current-phenomena-1900",
        "title": "Theory and Calculation of Alternating Current Phenomena",
        "year": 1900,
        "source_type": "book_edition",
        "priority": "critical",
        "status": "ocr_seeded",
        "related_local_source_id": "theory-calculation-alternating-current-phenomena-1900",
        "authority_refs": [
            {"type": "internet_archive", "url": "https://archive.org/details/theorycalculatio00steiiala"},
            {"type": "open_library", "url": "https://openlibrary.org/books/OL7218906M/Theory_and_calculation_of_alternating_current_phenomena"},
        ],
        "why_it_matters": "Early revised edition between the first edition and the later 1916 text.",
        "repo_action": "Use as the first edition-comparison layer for AC terminology and equations.",
    },
    {
        "work_id": "theory-calculation-electric-circuits-1917",
        "title": "Theory and Calculation of Electric Circuits",
        "year": 1917,
        "source_type": "book",
        "priority": "critical",
        "status": "ocr_seeded",
        "related_local_source_id": "theory-calculation-electric-circuits",
        "authority_refs": [
            {"type": "internet_archive", "url": "https://archive.org/details/theoryandcalcul06steigoog"},
            {"type": "open_library", "url": "https://openlibrary.org/books/OL6709519M/Theory_and_calculation_of_electric_circuits"},
        ],
        "why_it_matters": "Distinct core source for circuit equations and calculation, not the same as Electric Apparatus.",
        "repo_action": "Promote circuit equation families after chapter map and equation OCR are reviewed.",
    },
    {
        "work_id": "electric-discharges-waves-impulses-1914",
        "title": "Electric Discharges, Waves and Impulses",
        "year": 1914,
        "source_type": "lecture_collection_edition",
        "priority": "critical",
        "status": "ocr_seeded",
        "related_local_source_id": "electric-discharges-waves-impulses-1914",
        "authority_refs": [
            {"type": "internet_archive", "url": "https://archive.org/details/elementarylectur00stei"},
            {"type": "open_library", "url": "https://openlibrary.org/works/OL16029165W/Elementary_lectures_on_electric_discharges_waves_and_impulses_and_other_transients"},
        ],
        "why_it_matters": "Expanded transient lecture edition; strengthens waves, impulses, and lightning pages.",
        "repo_action": "Compare against the 1911 edition and promote changed or expanded transient passages.",
    },
    {
        "work_id": "mechanical-forces-magnetic-fields-1910",
        "title": "Mechanical Forces in Magnetic Fields",
        "year": 1910,
        "source_type": "journal_article",
        "priority": "critical",
        "status": "registered_primary_article_target",
        "authority_refs": [
            {"type": "doi", "url": "https://doi.org/10.1109/PAIEE.1910.6660496"}
        ],
        "why_it_matters": "High-value source for force, stress, pressure, and tension language in magnetic fields.",
        "repo_action": "Acquire scan/PDF, then build the field-force dossier and keep ether-field readings labeled as interpretation.",
    },
    {
        "work_id": "general-equations-electric-circuit-1908",
        "title": "The General Equations of the Electric Circuit",
        "year": 1908,
        "source_type": "journal_article",
        "priority": "critical",
        "status": "registered_primary_article_target",
        "authority_refs": [
            {"type": "doi", "url": "https://doi.org/10.1109/PAIEE.1908.6742132"}
        ],
        "why_it_matters": "Bridge between symbolic method, differential equations, transients, and general circuit theory.",
        "repo_action": "Acquire the article and link it to Electric Circuits and Transient Electric Phenomena.",
    },
    {
        "work_id": "general-equations-electric-circuit-iii-1919",
        "title": "The General Equations of the Electric Circuit-III",
        "year": 1919,
        "source_type": "journal_article",
        "priority": "critical",
        "status": "registered_primary_article_target",
        "authority_refs": [
            {"type": "doi", "url": "https://doi.org/10.1109/T-AIEE.1919.4765606"}
        ],
        "why_it_matters": "Continuation of Steinmetz's general circuit equation program.",
        "repo_action": "Acquire together with the 1908 paper so the series can be decoded as a sequence.",
    },
    {
        "work_id": "lightning-phenomena-electric-circuits-1907",
        "title": "Lightning Phenomena in Electric Circuits",
        "year": 1907,
        "source_type": "journal_article",
        "priority": "critical",
        "status": "registered_primary_article_target",
        "authority_refs": [
            {"type": "doi", "url": "https://doi.org/10.1109/PAIEE.1907.6742407"}
        ],
        "why_it_matters": "Primary lightning, surge, impulse, and high-voltage transient source.",
        "repo_action": "Acquire scan/PDF and feed the lightning-surges concept page, equation queue, and diagram archive.",
    },
    {
        "work_id": "outline-theory-impulse-currents-1916",
        "title": "Outline of Theory of Impulse Currents",
        "year": 1916,
        "source_type": "journal_article",
        "priority": "critical",
        "status": "registered_primary_article_target",
        "authority_refs": [
            {"type": "doi", "url": "https://doi.org/10.1109/PAIEE.1916.6590573"}
        ],
        "why_it_matters": "Direct source for impulse-current and surge mathematics.",
        "repo_action": "Acquire and decode after the expanded Electric Discharges edition is aligned.",
    },
    {
        "work_id": "cable-charge-and-discharge-1923",
        "title": "Cable Charge and Discharge",
        "year": 1923,
        "source_type": "journal_article",
        "priority": "critical",
        "status": "registered_primary_article_target",
        "authority_refs": [
            {"type": "doi", "url": "https://doi.org/10.1109/T-AIEE.1923.5060899"}
        ],
        "why_it_matters": "Distributed capacity, cable charge/discharge curves, and line-transient behavior.",
        "repo_action": "Acquire and connect to distributed constants, condenser charge, and traveling waves.",
    },
    {
        "work_id": "frequency-conversion-third-class-conductor-arcing-ground-1923",
        "title": "Frequency Conversion by Third Class Conductor and Mechanism of the Arcing Ground and Other Cumulative Surges",
        "year": 1923,
        "source_type": "journal_article",
        "priority": "critical",
        "status": "registered_primary_article_target",
        "authority_refs": [
            {"type": "doi", "url": "https://doi.org/10.1109/T-AIEE.1923.5060887"}
        ],
        "why_it_matters": "Nonlinear discharge, arcing-ground, cumulative-surge, and frequency-conversion source.",
        "repo_action": "Acquire and make this a flagship surge/nonlinear-discharge decoding page.",
    },
    {
        "work_id": "future-of-electricity-1910",
        "title": "The Future of Electricity",
        "year": 1910,
        "source_type": "pamphlet_or_booklet",
        "priority": "high",
        "status": "registered_hathitrust_target",
        "authority_refs": [
            {"type": "online_books_page", "url": "https://onlinebooks.library.upenn.edu/webbin/book/browse?c=x&key=Electrical+engineering+--+Study+and+teaching&type=lcsubc"}
        ],
        "why_it_matters": "Philosophical and forecasting source, useful for Steinmetz's civilizational reading of electricity.",
        "repo_action": "Acquire HathiTrust page images or an equivalent public scan before OCR seeding.",
    },
    {
        "work_id": "systems-electric-transmission-distribution-1900",
        "title": "Systems of Electric Transmission and Distribution",
        "year": 1900,
        "source_type": "pamphlet_or_booklet",
        "priority": "high",
        "status": "registered_hathitrust_google_books_target",
        "authority_refs": [
            {"type": "online_books_page", "url": "https://onlinebooks.library.upenn.edu/webbin/book/lookupid?key=ha010111183"},
            {"type": "google_books", "url": "https://books.google.com/books/about/Systems_of_Electric_Transmission_and_Dis.html?id=ZsMBHL4p_SAC"},
        ],
        "why_it_matters": "Compact source for power transmission, distribution, phase systems, and early AC system selection.",
        "repo_action": "Acquire page images or a text export, then process as a short source with transmission-system tags.",
    },
    {
        "work_id": "steinmetz-electrical-engineering-library-1914",
        "title": "Steinmetz Electrical Engineering Library",
        "year": 1914,
        "source_type": "compiled_volume_or_series",
        "priority": "high",
        "status": "bibliographic_verification_required",
        "authority_refs": [
            {"type": "google_books", "url": "https://books.google.com/books/about/Steinmetz_Electrical_Engineering_Library.html?id=_k9AAQAAMAAJ"},
            {"type": "catalog_trail", "value": "Treat this as a multi-volume library/series until each volume is verified individually."}
        ],
        "why_it_matters": "May bundle important instructional material or compiled lecture content.",
        "repo_action": "Verify the catalog record, contents, authorship/editorial scope, and public-domain status before treating it as a Steinmetz source.",
    },
    {
        "work_id": "charles-proteus-steinmetz-papers-union-college",
        "title": "Charles Proteus Steinmetz Papers - Union College",
        "year": None,
        "source_type": "archival_collection",
        "priority": "high",
        "status": "archival_collection_registered",
        "authority_refs": [
            {"type": "finding_aid", "url": "https://arches.union.edu/do/4d738881-e323-4a1b-8096-f3e51bc11e3e"}
        ],
        "why_it_matters": "Potentially deepest source for writings, GE/publication drafts, notes, ledgers, and correspondence.",
        "repo_action": "Create archival request notes, rights notes, box/folder inventory, and scan intake protocol before public transcription.",
    },
    {
        "work_id": "charles-proteus-steinmetz-collection-carnegie-mellon",
        "title": "Charles Proteus Steinmetz Collection - Carnegie Mellon University Archives",
        "year": None,
        "source_type": "archival_collection",
        "priority": "high",
        "status": "archival_collection_registered",
        "authority_refs": [
            {"type": "finding_aid", "url": "https://findingaids.library.cmu.edu/repositories/2/resources/38"}
        ],
        "why_it_matters": "Letters, photographs, and demonstration objects tied to Steinmetz and Four Lectures on Relativity and Space.",
        "repo_action": "Track as institutional archival material; do not mix letters or object metadata with published technical claims.",
    },
    {
        "work_id": "steinmetz-patents-corpus",
        "title": "Steinmetz Patents Corpus",
        "year": None,
        "source_type": "patent_corpus",
        "priority": "high",
        "status": "seeded_patent_register_exists_expand_to_full_corpus",
        "authority_refs": [
            {"type": "google_patents_query", "url": "https://patents.google.com/?inventor=Charles+Proteus+Steinmetz"},
            {"type": "mit_lemelson", "url": "https://lemelson.mit.edu/resources/charles-steinmetz"},
        ],
        "why_it_matters": "The patent corpus is the practical apparatus counterpart to the books and articles.",
        "repo_action": "Expand the current patent register into a full patent-to-theory bridge with claims, drawings, citations, and concept links.",
    },
]


MASTER_PORTALS = [
    {
        "portal": "Online Books Page: Charles Proteus Steinmetz / source listings",
        "role": "Authority map for HathiTrust and public scan trails.",
        "url": "https://onlinebooks.library.upenn.edu/webbin/book/search?author=Steinmetz%2C+Charles+Proteus",
    },
    {
        "portal": "Open Library author and work pages",
        "role": "Edition checklist, Internet Archive identifiers, and public text/download trails.",
        "url": "https://openlibrary.org/authors/OL164263A/Charles_Proteus_Steinmetz",
    },
    {
        "portal": "Internet Archive",
        "role": "Primary public OCR/PDF source for many public-domain books.",
        "url": "https://archive.org/search?query=creator%3A%22Steinmetz%2C+Charles+Proteus%22",
    },
    {
        "portal": "HathiTrust",
        "role": "Library-grade edition verification and page images where access permits.",
        "url": "https://catalog.hathitrust.org/",
    },
    {
        "portal": "IEEE Xplore / DOI records",
        "role": "Authority trail for AIEE papers; access to PDFs still needs rights/access verification.",
        "url": "https://ieeexplore.ieee.org/",
    },
    {
        "portal": "Union College Steinmetz Papers",
        "role": "Archival source queue for manuscripts, notes, and institutional materials.",
        "url": "https://arches.union.edu/do/4d738881-e323-4a1b-8096-f3e51bc11e3e",
    },
    {
        "portal": "Google Patents",
        "role": "Fast patent discovery portal before full official patent-download normalization.",
        "url": "https://patents.google.com/?inventor=Charles+Proteus+Steinmetz",
    },
]


def load_seed_module(root: Path) -> Any:
    script_path = root / "pipeline" / "scripts" / "seed_source_from_ocr.py"
    spec = importlib.util.spec_from_file_location("seed_source_from_ocr", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not import {script_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["seed_source_from_ocr"] = module
    spec.loader.exec_module(module)
    return module


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def fetch_text(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "SteinmetzDecodedSourceIngest/1.0"},
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_json(url: str) -> dict[str, Any]:
    text = fetch_text(url)
    loaded = json.loads(text)
    return loaded if isinstance(loaded, dict) else {}


def find_ocr_file(metadata: dict[str, Any], archive_id: str) -> str:
    preferred = f"{archive_id}_djvu.txt"
    files = metadata.get("files") or []
    if isinstance(files, list):
        names = [str(file.get("name") or "") for file in files if isinstance(file, dict)]
        if preferred in names:
            return preferred
        for name in names:
            if name.endswith("_djvu.txt"):
                return name
    return preferred


def download_ia_ocr(root: Path, source: InternetArchiveSource, force: bool) -> Path:
    cleaned_dir = root / "processed" / source.source_id / "cleaned_text"
    ocr_path = cleaned_dir / "internet-archive-ocr.txt"
    if ocr_path.exists() and not force:
        return ocr_path
    metadata = fetch_json(f"https://archive.org/metadata/{source.internet_archive_id}")
    ocr_file = find_ocr_file(metadata, source.internet_archive_id)
    ocr_url = f"https://archive.org/download/{source.internet_archive_id}/{ocr_file}"
    text = fetch_text(ocr_url)
    write_text(ocr_path, text)
    metadata_path = root / "sources" / source.source_id / "raw" / "internet_archive_metadata.json"
    write_json(metadata_path, metadata)
    return ocr_path


def seed_processed_source(root: Path, seed_module: Any, source: InternetArchiveSource, ocr_path: Path) -> None:
    source_id = source.source_id
    out_dir = root / "processed" / source_id
    text = seed_module.normalize_ocr(ocr_path.read_text(encoding="utf-8", errors="replace"))
    lines = text.splitlines()
    body_start = seed_module.find_body_start(lines)
    headings = seed_module.extract_headings(lines, body_start)
    body_end = seed_module.find_body_end(lines, headings[-1].line_index if headings else body_start)

    chapter_records: list[dict[str, Any]] = []
    cleaned_dir = out_dir / "cleaned_text"
    for index, heading in enumerate(headings):
        end = headings[index + 1].line_index if index + 1 < len(headings) else body_end
        chapter_lines = lines[heading.line_index:end]
        sequence = index + 1
        chapter_id = seed_module.slug_source_chapter(source_id, heading.kind, sequence)
        chapter_path = cleaned_dir / f"{heading.kind}-{sequence:02d}.md"
        write_text(chapter_path, "\n".join(chapter_lines).strip() + "\n")
        chapter_records.append(
            {
                "id": chapter_id,
                "source_id": source_id,
                "kind": heading.kind,
                "sequence": sequence,
                "number": heading.number,
                "roman": heading.roman,
                "title": heading.title,
                "line_start": heading.line_index + 1,
                "line_end": end,
                "text_path": str(chapter_path.relative_to(root)).replace("\\", "/"),
                "summary": "",
                "concept_tags": [],
                "status": "candidate",
            }
        )

    write_json(out_dir / "chapters.json", chapter_records)
    write_json(out_dir / "figures.json", seed_module.extract_figures(lines, source_id, body_start, body_end))
    write_json(out_dir / "equations.json", seed_module.extract_equation_candidates(lines, source_id, body_start, body_end))
    write_json(out_dir / "concepts.json", seed_module.build_concepts(text, source_id))
    write_json(out_dir / "glossary.json", seed_module.build_glossary(text, source_id))
    write_json(out_dir / "quotes.json", seed_module.extract_quote_candidates(lines, source_id, body_start, body_end))
    write_json(out_dir / "annotations.json", [])
    write_json(out_dir / "crosslinks.json", [])

    report = [
        "# Processing Report",
        "",
        f"Source ID: `{source_id}`",
        f"Source title: {source.title}",
        f"Internet Archive item: `{source.internet_archive_id}`",
        f"OCR input: `{ocr_path.relative_to(root)}`",
        f"Body start line: {body_start + 1}",
        f"Body end line: {body_end}",
        f"Structural headings found: {len(headings)}",
        "",
        "## Status",
        "",
        "All generated records are candidates. OCR, page boundaries, equations, and figure captions require scan verification before canonical use.",
        "",
        "## Source-Specific Note",
        "",
        source.processing_note,
        "",
    ]
    write_text(out_dir / "processing_report.md", "\n".join(report))


def catalog_record(source: InternetArchiveSource) -> dict[str, Any]:
    return {
        "source_id": source.source_id,
        "title": source.title,
        "year": source.year,
        "source_status": "ocr_seeded",
        "processed_status": "Internet Archive OCR downloaded; chapter/lecture candidates and candidate catalogs generated; scan and edition alignment require review",
        "source_type": source.source_type,
        "internet_archive_id": source.internet_archive_id,
        "local_raw_file": None,
        "site_path": f"/sources/{source.source_id}/",
    }


def update_source_catalog(root: Path) -> None:
    catalog_path = root / "sources" / "source_catalog.json"
    catalog = load_json(catalog_path, [])
    if not isinstance(catalog, list):
        catalog = []
    by_id = {str(item.get("source_id")): item for item in catalog if isinstance(item, dict)}
    for source in IA_SOURCES:
        by_id[source.source_id] = catalog_record(source)
    ordered: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in catalog:
        source_id = str(item.get("source_id"))
        if source_id in by_id and source_id not in seen:
            ordered.append(by_id[source_id])
            seen.add(source_id)
    for source in IA_SOURCES:
        if source.source_id not in seen:
            ordered.append(by_id[source.source_id])
            seen.add(source.source_id)
    write_json(catalog_path, ordered)


def write_source_manifest(root: Path, source: InternetArchiveSource) -> None:
    source_dir = root / "sources" / source.source_id
    manifest = {
        "source_id": source.source_id,
        "collection_id": "steinmetz",
        "person_id": "charles-proteus-steinmetz",
        "title": source.title,
        "year": source.year,
        "source_type": source.source_type,
        "source_status": "ocr_seeded",
        "internet_archive_id": source.internet_archive_id,
        "source_url": f"https://archive.org/details/{source.internet_archive_id}",
        "edition_note": source.edition_note,
        "custody": {
            "raw_scan_status": "remote_internet_archive_scan_not_copied",
            "ocr_status": "internet_archive_ocr_preserved",
            "processed_status": "candidate_catalogs_generated",
            "scan_verification": "pending",
        },
        "quality_rules": [
            "OCR text is a navigation and candidate-extraction layer, not a corrected edition.",
            "Exact quotations must be verified against the page image or PDF scan.",
            "Equation, figure, and glossary candidates remain unpromoted until reviewed.",
            "Edition differences must stay visible when comparing this source to related editions.",
        ],
        "why_it_matters": source.why_it_matters,
        "ingested": TODAY,
    }
    write_json(source_dir / "source_manifest.json", manifest)
    raw_readme = f"""# Raw Custody Notes

Source: {source.title}

Internet Archive item: https://archive.org/details/{source.internet_archive_id}

Status: OCR has been preserved under `processed/{source.source_id}/cleaned_text/internet-archive-ocr.txt`. The PDF/page images remain remote custody for now and must be downloaded or checked directly before exact quotation, diagram cropping, or canonical equation promotion.

Edition note: {source.edition_note}
"""
    write_text(source_dir / "raw" / "README.md", raw_readme)


def update_bibliography_manifest(root: Path) -> None:
    path = root / "sources" / "steinmetz_bibliography_manifest.json"
    manifest = load_json(path, {})
    if not isinstance(manifest, dict):
        return
    entries = manifest.setdefault("entries", [])
    if not isinstance(entries, list):
        manifest["entries"] = []
        entries = manifest["entries"]
    by_id = {str(entry.get("work_id")): entry for entry in entries if isinstance(entry, dict)}
    for record in OFFICIAL_INTAKE_RECORDS:
        existing = by_id.get(record["work_id"])
        if existing:
            existing.update(
                {
                    "status": record["status"],
                    "priority": record["priority"],
                    "processing_intent": record["why_it_matters"],
                }
            )
            if record.get("related_local_source_id"):
                existing["related_local_source_id"] = record["related_local_source_id"]
                existing["local_site_path"] = f"/sources/{record['related_local_source_id']}/"
            if record.get("authority_refs"):
                existing["external_refs"] = record["authority_refs"]
        else:
            new_entry = {
                "work_id": record["work_id"],
                "title": record["title"],
                "year": record.get("year"),
                "source_type": record["source_type"],
                "status": record["status"],
                "wikipedia_entry": False,
                "priority": record["priority"],
                "processing_intent": record["why_it_matters"],
                "external_refs": record.get("authority_refs", []),
            }
            if record.get("related_local_source_id"):
                new_entry["related_local_source_id"] = record["related_local_source_id"]
                new_entry["local_site_path"] = f"/sources/{record['related_local_source_id']}/"
            entries.append(new_entry)
            by_id[record["work_id"]] = new_entry
    manifest["updated"] = TODAY
    manifest["next_actions"] = [
        "Finish scan/PDF custody for all newly registered DOI, HathiTrust, archival, and patent targets.",
        "Review the newly OCR-seeded Internet Archive editions for chapter-map accuracy.",
        "Run edition-comparison passes between the 1897, 1900, and 1916 Alternating Current Phenomena editions.",
        "Promote only scan-verified equations, diagrams, quotes, and interpretation layers.",
    ]
    write_json(path, manifest)


def write_official_intake_manifest(root: Path) -> None:
    manifest = {
        "manifest_id": "steinmetz-official-source-expansion",
        "updated": TODAY,
        "purpose": "Priority source expansion register for books, editions, papers, archival collections, and patents requested for the Steinmetz archive.",
        "quality_rule": "A source can be registered as official before it is processed, but it cannot be cited as decoded until source custody, OCR/page mapping, and review state are visible.",
        "records": OFFICIAL_INTAKE_RECORDS,
        "master_portals": MASTER_PORTALS,
        "processing_gates": [
            "Authority trail identified",
            "Public-domain or access status recorded",
            "Raw scan/PDF/OCR stored or remote custody documented",
            "Source manifest created",
            "OCR or embedded text extracted",
            "Chapter/page map created",
            "Equation, figure, concept, glossary, quote, annotation, and crosslink candidates generated",
            "Scan verification workbench created",
            "Canonical public pages promoted only after review",
        ],
    }
    write_json(root / "sources" / "official_source_intake_manifest.json", manifest)
    write_json(root / "processed" / "official_source_intake.json", manifest)
    write_json(root / "site" / "public" / "data" / "official_source_intake.json", manifest)


def md_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("|", "\\|")
        .replace("\n", " ")
    )


def link_for_record(record: dict[str, Any]) -> str:
    local = record.get("related_local_source_id")
    if local:
        return f"[Open source]({BASE_URL}/sources/{local}/)"
    refs = record.get("authority_refs") or []
    for ref in refs:
        if isinstance(ref, dict) and ref.get("url"):
            return f"[Authority]({ref['url']})"
    return "Needs authority file"


def write_official_intake_page(root: Path) -> None:
    rows = []
    for record in OFFICIAL_INTAKE_RECORDS:
        rows.append(
            "| "
            + " | ".join(
                [
                    md_escape(record["title"]),
                    md_escape(record.get("year") or "-"),
                    md_escape(record["source_type"].replace("_", " ")),
                    md_escape(record["priority"]),
                    md_escape(record["status"]),
                    md_escape(record["why_it_matters"]),
                    link_for_record(record),
                ]
            )
            + " |"
        )

    seeded_cards = []
    for source in IA_SOURCES:
        seeded_cards.append(
            f"""<a href="{BASE_URL}/sources/{source.source_id}/">
  <strong>{md_escape(source.title)} ({source.year})</strong>
  <span>{md_escape(source.processing_note)}</span>
</a>"""
        )
    portal_rows = [
        f"| {md_escape(portal['portal'])} | {md_escape(portal['role'])} | [Open]({portal['url']}) |"
        for portal in MASTER_PORTALS
    ]
    page = f"""---
title: Official Source Expansion Workbench
description: Priority intake register for newly added and queued Steinmetz books, papers, archives, and patents.
---

## Source Expansion Status

This page is the control room for the next Steinmetz acquisition wave. Four public Internet Archive sources have been OCR-seeded into the processed corpus. DOI papers, HathiTrust-only items, archival collections, and the full patent corpus are registered here as official targets, but they remain unprocessed until the archive has source custody and verification metadata.

<div class="source-matrix">
{chr(10).join(seeded_cards)}
</div>

## Quality Rule

Registered is not the same as decoded. A source becomes part of the research corpus only after the archive can show authority trail, custody, OCR or text extraction, page/section map, candidate equations, candidate figures, concept/glossary hits, quote candidates, and review state.

## Priority Intake Table

| Source | Year | Type | Priority | Status | Research Value | Link |
| --- | ---: | --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## Master Source Portals

| Portal | Role | Link |
| --- | --- | --- |
{chr(10).join(portal_rows)}

## Next Processing Gates

1. Review newly OCR-seeded chapter maps and correct bad headings.
2. Download or otherwise custody the primary PDFs/scans for the critical DOI papers.
3. Build the AC edition-comparison layer across 1897, 1900, and 1916.
4. Promote only scan-verified equations, diagrams, and quotations into canonical pages.
5. Expand the patent register into a patent-to-theory bridge with drawings and concept links.
"""
    write_text(root / "site" / "src" / "content" / "docs" / "source-library" / "official-source-expansion.mdx", page)


def write_source_overview_pages(root: Path) -> None:
    for source in IA_SOURCES:
        chapters = load_json(root / "processed" / source.source_id / "chapters.json", [])
        equations = load_json(root / "processed" / source.source_id / "equations.json", [])
        figures = load_json(root / "processed" / source.source_id / "figures.json", [])
        quotes = load_json(root / "processed" / source.source_id / "quotes.json", [])
        chapter_count = len(chapters) if isinstance(chapters, list) else 0
        equation_count = len(equations) if isinstance(equations, list) else 0
        figure_count = len(figures) if isinstance(figures, list) else 0
        quote_count = len(quotes) if isinstance(quotes, list) else 0
        page = f"""---
title: {json.dumps(source.title + " (" + str(source.year) + ")")}
description: {json.dumps("OCR-seeded source page for " + source.title + ".")}
---

import SourceRef from '../../../../components/SourceRef.astro';
import SourceAccess from '../../../../components/SourceAccess.astro';

<SourceRef source="{md_escape(source.title)}, {source.year}" location="Internet Archive item: {source.internet_archive_id}" status="candidate OCR" />

<SourceAccess
  title="{md_escape(source.title)}"
  archiveId="{source.internet_archive_id}"
  localPath="sources/{source.source_id}/"
  note="{md_escape(source.edition_note)}"
/>

## Read This Source

<div class="source-matrix">
  <a href="{BASE_URL}/book-coverage/{source.source_id}/">Book coverage atlas<span>Browse all generated sections with concept density and review signals.</span></a>
  <a href="{BASE_URL}/source-texts/{source.source_id}/">Source text index<span>Read the generated OCR-derived section text directly.</span></a>
  <a href="{BASE_URL}/chapter-workbench/{source.source_id}/">Research review<span>Open equation, figure, glossary, quote, and concept candidates section by section.</span></a>
  <a href="https://archive.org/details/{source.internet_archive_id}">Internet Archive scan<span>Verify exact quotations and page images before canonical use.</span></a>
</div>

## Why This Source Was Added

{source.why_it_matters}

## Candidate Processing State

- Source type: `{source.source_type}`
- Internet Archive identifier: `{source.internet_archive_id}`
- Generated section records: {chapter_count}
- Candidate equations: {equation_count}
- Candidate figures: {figure_count}
- Candidate quote hits: {quote_count}
- Review status: OCR-derived candidates, not a corrected critical edition.

## Edition And Custody Note

{source.edition_note}

The PDF/page images remain the verification base. The archive has preserved the Internet Archive OCR and generated candidate catalogs so this source can now participate in search, source-text browsing, concept concordance, theme evidence, and chapter workbench pages.

## Promotion Path

1. Verify title page, edition, and publication metadata.
2. Correct the section map if OCR headings caused false splits.
3. Scan-check equations and diagrams before promotion.
4. Add modern engineering explanations only after source passages are anchored.
5. Keep edition differences visible when comparing related Steinmetz works.
"""
        write_text(root / "site" / "src" / "content" / "docs" / "sources" / source.source_id / "index.mdx", page)


def ingest(root: Path, force: bool, skip_download: bool) -> None:
    seed_module = load_seed_module(root)
    update_source_catalog(root)
    for source in IA_SOURCES:
        write_source_manifest(root, source)
        if skip_download:
            continue
        ocr_path = download_ia_ocr(root, source, force)
        seed_processed_source(root, seed_module, source, ocr_path)
    update_bibliography_manifest(root)
    write_official_intake_manifest(root)
    write_official_intake_page(root)
    if not skip_download:
        write_source_overview_pages(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--force-download", action="store_true")
    parser.add_argument("--skip-download", action="store_true")
    args = parser.parse_args()
    ingest(args.root.resolve(), force=args.force_download, skip_download=args.skip_download)
    print("Ingested priority source expansion records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
