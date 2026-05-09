#!/usr/bin/env python3
"""Enrich public concept pages with source-grounded dossiers.

The concept concordance already knows where terms appear in the processed
corpus. This script promotes that evidence into the human-facing concept pages
without pretending candidate OCR is final. It appends or replaces a generated
section in each curated page so the pages become useful entry points instead of
thin placeholders.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any


BASE_URL = "/Charles-Proteus-Steinmetz-Texts-AI-Decoded"
OLD_BEGIN = "<!-- BEGIN GENERATED CONCEPT DOSSIER -->"
OLD_END = "<!-- END GENERATED CONCEPT DOSSIER -->"
BEGIN = "{/* BEGIN GENERATED CONCEPT DOSSIER */}"
END = "{/* END GENERATED CONCEPT DOSSIER */}"


PAGE_CONCEPTS: dict[str, list[str]] = {
    "admittance": ["admittance"],
    "complex-quantities": ["complex-quantities"],
    "conductance": ["conductance"],
    "dielectric-loss": ["dielectricity", "dielectric-field", "dielectric-constant"],
    "distributed-constants": ["distributed-constants", "wave-propagation"],
    "electric-waves": ["electric-waves", "wave-propagation", "electrical-radiation"],
    "ether": ["ether"],
    "harmonics-wave-shape": ["frequency", "alternating-current", "wave-length"],
    "hysteresis": ["hysteresis", "magnetism"],
    "illumination": ["illumination", "light", "photometry", "light-flux-density"],
    "impedance": ["impedance"],
    "inductance-capacity": ["inductance", "electrostatic-capacity", "energy-storage-fields"],
    "lightning-surges": ["lightning-surges", "protective-reactance"],
    "oscillation-damping": ["oscillation", "damping", "resonance"],
    "power-factor": ["power-factor"],
    "power-limiting-reactors": ["power-limiting-reactor", "protective-reactance"],
    "radiation": ["radiation", "light", "electrical-radiation"],
    "reactance": ["reactance"],
    "susceptance": ["susceptance"],
    "symbolic-method": ["symbolic-method", "complex-quantities"],
    "synchronizing-power": ["synchronizing-power", "synchronism"],
    "transient-phenomena": ["transient-phenomena", "field-collapse"],
}


PAGE_GUIDANCE: dict[str, str] = {
    "ether": "Read this concept as a historical-language and field-theory boundary page. The current corpus places most ether hits in Steinmetz's relativity lectures, where ether is treated alongside the rise of Faraday-Maxwell field language; the earlier radiation source uses it in the wave-theory-of-light setting. That distribution matters.",
    "radiation": "Read this concept as the bridge from physics to illumination engineering: Steinmetz treats radiation as energy in transit before later lectures convert that physical idea into measurement, lamps, flux, distribution, and visual response.",
    "electric-waves": "Read this concept as a connector between optical radiation, wireless or high-frequency waves, and transmission-line behavior. Keep wavelength, frequency, velocity, and source context visible.",
    "hysteresis": "Read this concept as both material physics and engineering loss accounting. The archive should preserve Steinmetz's magnetic vocabulary before translating it into modern loss models.",
    "symbolic-method": "Read this concept as a mathematical language page: the important work is not only the formulas, but Steinmetz's translation between rotating vectors, rectangular components, and symbolic calculation.",
    "transient-phenomena": "Read this concept as a time-domain correction to steady-state circuit thinking. The strongest pages should show where Steinmetz separates permanent terms from transient terms and then follows the stored energy.",
    "inductance-capacity": "Read this concept as an energy-storage pair. The archive should keep magnetic-flux and dielectric-flux language visible before reducing everything to modern lumped L and C notation.",
    "power-limiting-reactors": "Read this concept as a practical power-system stability and protection page. The theory matters because Steinmetz is dealing with station behavior, synchronism, short-circuit current, and recovery.",
    "synchronizing-power": "Read this concept through the Commonwealth Edison report and related AC-machine language. It belongs to stability, phase relation, station sections, and real apparatus, not only abstract phasors.",
}


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def clean_text(value: Any, limit: int | None = None) -> str:
    text = "" if value is None else str(value)
    replacements = {
        "\u00a0": " ",
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\ufeff": "",
        "\u00e2\u20ac\u201d": "-",
        "\u00e2\u20ac\u201c": "-",
        "\u00e2\u20ac\u02dc": "'",
        "\u00e2\u20ac\u2122": "'",
        "\u00e2\u20ac\u0153": '"',
        "\u00e2\u20ac\ufffd": '"',
        "\u00c2\u00b7": "-",
        "\u00c2": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: limit - 3].rstrip() + "..."
    return text


def md_escape(value: Any) -> str:
    return (
        clean_text(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("{", "&#123;")
        .replace("}", "&#125;")
        .replace("|", "\\|")
    )


def read_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", text, flags=re.MULTILINE)
    if match:
        return clean_text(match.group(1))
    return path.stem.replace("-", " ").title()


def concept_index(root: Path) -> dict[str, dict[str, Any]]:
    data = load_json(root / "processed" / "concept_concordance.json", {})
    concepts = data.get("concepts", []) if isinstance(data, dict) else []
    return {str(concept.get("id")): concept for concept in concepts if concept.get("id")}


def source_link(source_id: str) -> str:
    return f"{BASE_URL}/source-texts/{source_id}/"


def concordance_link(concept_id: str) -> str:
    return f"{BASE_URL}/concept-concordance/{concept_id}/"


def aggregate_sources(concepts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    totals: dict[str, dict[str, Any]] = {}
    for concept in concepts:
        for source in concept.get("source_totals", []):
            source_id = str(source.get("source_id"))
            if source_id not in totals:
                totals[source_id] = {
                    "source_id": source_id,
                    "source_title": source.get("source_title"),
                    "occurrence_count": 0,
                    "section_count": 0,
                    "concepts": [],
                }
            totals[source_id]["occurrence_count"] += int(source.get("occurrence_count") or 0)
            totals[source_id]["section_count"] += int(source.get("section_count") or 0)
            totals[source_id]["concepts"].append(concept.get("label"))
    return sorted(totals.values(), key=lambda item: (-item["occurrence_count"], str(item["source_title"])))


def aggregate_sections(concepts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sections: dict[str, dict[str, Any]] = {}
    for concept in concepts:
        label = concept.get("label")
        for hit in concept.get("section_hits", []):
            section_id = str(hit.get("section_id"))
            if section_id not in sections:
                sections[section_id] = {
                    "section_id": section_id,
                    "source_id": hit.get("source_id"),
                    "source_title": hit.get("source_title"),
                    "year": hit.get("year"),
                    "section_label": hit.get("section_label"),
                    "location": hit.get("location"),
                    "status": hit.get("status"),
                    "occurrence_count": 0,
                    "concepts": [],
                    "source_text_url": hit.get("source_text_url"),
                    "workbench_url": hit.get("workbench_url"),
                    "snippets": [],
                }
            sections[section_id]["occurrence_count"] += int(hit.get("occurrence_count") or 0)
            sections[section_id]["concepts"].append(label)
            for snippet in hit.get("snippets", [])[:2]:
                cleaned = clean_text(snippet, 360)
                if cleaned and cleaned not in sections[section_id]["snippets"]:
                    sections[section_id]["snippets"].append(cleaned)
    return sorted(sections.values(), key=lambda item: (-item["occurrence_count"], str(item["source_title"]), str(item["section_label"])))


def build_dossier(root: Path, page_slug: str, concept_ids: list[str], page_title: str, index: dict[str, dict[str, Any]]) -> dict[str, Any]:
    concepts = [index[concept_id] for concept_id in concept_ids if concept_id in index]
    sources = aggregate_sources(concepts)
    sections = aggregate_sections(concepts)
    aliases = []
    for concept in concepts:
        for alias in concept.get("aliases", []):
            alias = clean_text(alias)
            if alias and alias not in aliases:
                aliases.append(alias)
    return {
        "page_slug": page_slug,
        "page_title": page_title,
        "concept_ids": [concept.get("id") for concept in concepts],
        "concept_labels": [concept.get("label") for concept in concepts],
        "generated_at": date.today().isoformat(),
        "quality_note": "Generated concept-page dossier. Counts, snippets, and passages are OCR/PDF-text aids and require scan verification before exact quotation.",
        "guidance": PAGE_GUIDANCE.get(page_slug, "Read this concept page through the linked source passages first. Use the dossier to locate Steinmetz's wording, then add modern, mathematical, historical, and interpretive layers only with labels."),
        "totals": {
            "occurrences": sum(int(concept.get("total_occurrences") or 0) for concept in concepts),
            "matching_sections": len(sections),
            "matching_sources": len(sources),
            "aliases": len(aliases),
        },
        "aliases": aliases,
        "sources": sources,
        "priority_sections": sections[:10],
        "concordance_links": [
            {
                "concept_id": concept.get("id"),
                "label": concept.get("label"),
                "url": concordance_link(str(concept.get("id"))),
            }
            for concept in concepts
        ],
    }


def focused_url(url: Any, anchor: str) -> str:
    value = clean_text(url)
    if not value or value == "#":
        return "#"
    base = value.split("#", 1)[0]
    return f"{base}#{anchor}"


def source_distribution_cards(sources: list[dict[str, Any]]) -> str:
    cards = []
    for source in sources[:8]:
        title = md_escape(source.get("source_title"))
        url = source_link(str(source.get("source_id")))
        concepts = ", ".join(sorted(set(clean_text(item) for item in source.get("concepts", []) if item)))
        cards.append(
            f"""<a className=\"evidence-source-card\" href=\"{url}\">
  <strong>{title}</strong>
  <span>{source.get('occurrence_count', 0)} candidate hits across {source.get('section_count', 0)} sections.</span>
  <small>{md_escape(concepts)}</small>
</a>"""
        )
    if not cards:
        cards.append(
            """<div className=\"evidence-source-card\">
  <strong>No concordance data yet.</strong>
  <span>Add aliases and rerun the concordance.</span>
</div>"""
        )
    return f"""<div className=\"evidence-source-grid\">
{chr(10).join(cards)}
</div>"""


def text_code_block(value: str) -> str:
    text = clean_text(value, 360).replace("```", "'''")
    return f"```text\n{text}\n```"


def priority_section_blocks(sections: list[dict[str, Any]]) -> str:
    blocks = []
    for section in sections[:6]:
        concepts = ", ".join(sorted(set(clean_text(item) for item in section.get("concepts", []) if item)))
        source_url = focused_url(section.get("source_text_url"), "source-text")
        workbench_url = focused_url(section.get("workbench_url"), "chapter-local-concept-hits")
        excerpt_url = focused_url(section.get("workbench_url"), "source-located-theme-snippets")
        snippets = section.get("snippets", [])[:2]
        snippet_blocks = "\n\n".join(text_code_block(snippet) for snippet in snippets)
        blocks.append(
            f"""<details className=\"layered-reading\" data-layer=\"source\">
<summary>{md_escape(section.get('section_label'))} - {section.get('occurrence_count', 0)} candidate hits</summary>

**Source:** {md_escape(section.get('source_title'))} ({md_escape(section.get('year'))})

**Location:** {md_escape(section.get('location'))} - **Tracked concepts:** {md_escape(concepts)}

<div className=\"focused-route-links\">
  <a href=\"{source_url}\">Read manuscript text</a>
  <a href=\"{workbench_url}\">Open concept hits</a>
  <a href=\"{excerpt_url}\">Open source snippets</a>
</div>

{snippet_blocks}

</details>"""
        )
    if not blocks:
        return "<p>No priority passages are available yet. Add aliases to the concept concordance and rerun the generator.</p>"
    return "\n\n".join(blocks)


def concordance_links(links: list[dict[str, Any]]) -> str:
    if not links:
        return "No concordance link is available yet."
    return " - ".join(f"[{md_escape(link['label'])}]({link['url']})" for link in links)


def build_markdown(dossier: dict[str, Any]) -> str:
    totals = dossier["totals"]
    aliases = ", ".join(f"`{md_escape(alias)}`" for alias in dossier["aliases"][:18]) or "No aliases tracked yet."
    source_cards = source_distribution_cards(dossier["sources"])
    passage_blocks = priority_section_blocks(dossier["priority_sections"])
    top_source = dossier["sources"][0] if dossier["sources"] else None
    top_source_sentence = (
        f"The strongest current source concentration is **{md_escape(top_source.get('source_title'))}** with {top_source.get('occurrence_count', 0)} candidate hits across {top_source.get('section_count', 0)} sections."
        if top_source
        else "No source concentration has been identified yet."
    )
    return f"""{BEGIN}

## Source-Grounded Dossier

<div class=\"source-text-warning\" data-layer=\"source\">
  <strong>Generated evidence layer:</strong> this dossier is built from the processed concept concordance. Counts and snippets are OCR/PDF-text aids, not final quotations. Verify against scans before making exact claims.
</div>

<div class=\"codex-signal\">
  <div><strong>{totals['occurrences']}</strong><p>Candidate occurrences tracked for this page.</p></div>
  <div><strong>{totals['matching_sources']}</strong><p>Sources with at least one hit.</p></div>
  <div><strong>{totals['matching_sections']}</strong><p>Sections, lectures, chapters, or report divisions to review.</p></div>
</div>

### What The Current Corpus Shows

{dossier['guidance']}

{top_source_sentence}

The dossier is meant to turn a concept page into a research workbench: begin with Steinmetz's source wording, then add modern interpretation, mathematical reconstruction, historical context, and any ether-field reading as separate layers.

### Terms And Aliases Tracked

{aliases}

### Concordance Records

{concordance_links(dossier['concordance_links'])}

### Source Distribution

{source_cards}

### Priority Passages To Read

{passage_blocks}

### Reading Layers To Build Out

| Layer | What to add next |
| --- | --- |
| Steinmetz wording | Pull exact source passages only after scan verification; keep OCR text labeled until then. |
| Modern engineering reading | Translate the source usage into present electrical-engineering or physics language without erasing the older vocabulary. |
| Mathematical layer | Link equations, variables, diagrams, and worked examples when the concept has formula candidates. |
| Historical layer | Identify whether the term is still used, renamed, absorbed into modern theory, or historically obsolete. |
| Ether-field interpretation | Keep interpretive readings separate from Steinmetz's explicit claim and from modern physics. |
| Open questions | Record places where the concordance suggests a lead but the scan or edition has not yet been checked. |

### Next Editorial Actions

1. Open the highest-priority source-text passages above and verify the wording against scans.
2. Promote exact definitions, equations, diagrams, and hidden-gem passages into this page with source references.
3. Add related concept links, equation pages, and diagram pages once the evidence is scan checked.
4. Keep speculative or Wheeler-style readings in explicitly labeled interpretation blocks.

{END}
"""


def replace_section(existing: str, generated: str) -> str:
    begin_pattern = f"(?:{re.escape(BEGIN)}|{re.escape(OLD_BEGIN)})"
    end_pattern = f"(?:{re.escape(END)}|{re.escape(OLD_END)})"
    pattern = re.compile(begin_pattern + r".*?" + end_pattern, flags=re.DOTALL)
    if pattern.search(existing):
        return pattern.sub(lambda _match: generated.strip(), existing).rstrip() + "\n"
    return existing.rstrip() + "\n\n" + generated.strip() + "\n"


def build_index_page(root: Path, dossiers: list[dict[str, Any]]) -> str:
    rows = []
    for dossier in sorted(dossiers, key=lambda item: (-item["totals"]["occurrences"], item["page_title"])):
        rows.append(
            f"| [{md_escape(dossier['page_title'])}]({BASE_URL}/concepts/{dossier['page_slug']}/) | {dossier['totals']['occurrences']} | {dossier['totals']['matching_sources']} | {dossier['totals']['matching_sections']} | {', '.join(md_escape(label) for label in dossier['concept_labels'][:4])} |"
        )
    return f"""---
title: Concept Dossier Index
description: Generated source-grounded dossier coverage for public concept pages.
---

{{/* Generated by pipeline/scripts/generate_concept_page_dossiers.py. Do not edit by hand. */}}

## Concept Dossier Index

This generated index shows which curated concept pages now carry source-grounded dossier sections. The dossiers are not final scholarship; they are evidence maps that point readers to Steinmetz source text, workbench pages, and scan-verification tasks.

| Concept Page | Candidate Hits | Sources | Sections | Concordance Concepts |
| --- | ---: | ---: | ---: | --- |
{chr(10).join(rows)}

## Use Rule

Use these dossiers to find source passages. Do not treat OCR snippets as exact quotation until the relevant scan or edition has been checked.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Append generated source-grounded dossiers to public concept pages.")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    index = concept_index(root)
    docs_dir = root / "site" / "src" / "content" / "docs" / "concepts"
    dossiers = []

    for page_slug, concept_ids in PAGE_CONCEPTS.items():
        path = docs_dir / f"{page_slug}.mdx"
        if not path.exists():
            continue
        title = read_title(path)
        dossier = build_dossier(root, page_slug, concept_ids, title, index)
        if not dossier["concept_ids"]:
            continue
        existing = path.read_text(encoding="utf-8")
        generated = build_markdown(dossier)
        write_text(path, replace_section(existing, generated))
        dossiers.append(dossier)

    write_json(root / "processed" / "concept_page_dossiers.json", {
        "generated_at": date.today().isoformat(),
        "quality_note": "Generated concept-page dossier data. Counts and snippets are OCR/PDF-text aids and require scan verification.",
        "dossier_count": len(dossiers),
        "dossiers": dossiers,
    })
    write_text(docs_dir / "dossier-index.mdx", build_index_page(root, dossiers))


if __name__ == "__main__":
    main()
