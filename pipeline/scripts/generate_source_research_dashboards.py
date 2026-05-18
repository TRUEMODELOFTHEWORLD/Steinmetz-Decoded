#!/usr/bin/env python3
"""Append source-level research dashboards to every curated source page.

The generated source-text browser, book coverage atlas, chapter workbench,
visual maps, and formula maps already expose a large amount of material. This
script makes the curated /sources/<source>/ pages behave like useful front
doors instead of thin summaries by attaching a dashboard for every processed
source.

All dashboards are routing and evidence-management layers. They do not promote
OCR/PDF text into canonical quotation or convert candidate equations and figures
into verified claims.
"""

from __future__ import annotations

import html
import json
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


BASE_URL = ""
BEGIN_DASHBOARD = "{/* BEGIN GENERATED SOURCE RESEARCH DASHBOARD */}"
END_DASHBOARD = "{/* END GENERATED SOURCE RESEARCH DASHBOARD */}"

THEME_LABELS = {
    "alternating-current": "Alternating current",
    "complex-quantities": "Complex quantities",
    "dielectricity": "Dielectricity / capacity",
    "ether": "Ether references",
    "fields": "Field language",
    "hysteresis": "Hysteresis",
    "impedance-reactance": "Impedance / reactance",
    "lightning-surges": "Lightning / surges",
    "magnetism": "Magnetism",
    "radiation-light": "Radiation / light",
    "transients": "Transients / damping",
    "waves-lines": "Waves / transmission lines",
}

THEME_ROUTES = {
    "alternating-current": "alternating-current-and-symbolic-method",
    "complex-quantities": "alternating-current-and-symbolic-method",
    "dielectricity": "dielectricity-capacity-and-displacement",
    "ether": "ether-field-language",
    "fields": "ether-field-language",
    "hysteresis": "magnetism-and-hysteresis",
    "impedance-reactance": "reactance-impedance-and-admittance",
    "lightning-surges": "transients-oscillations-and-surges",
    "magnetism": "magnetism-and-hysteresis",
    "radiation-light": "waves-lines-and-radiation",
    "transients": "transients-oscillations-and-surges",
    "waves-lines": "waves-lines-and-radiation",
    "energy-power": "energy-power-and-work",
    "apparatus-systems": "machines-apparatus-and-systems",
}


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


def esc(value: Any) -> str:
    text = html.escape("" if value is None else str(value), quote=True)
    return (
        text.replace("\\", "&#92;")
        .replace("*", "&#42;")
        .replace("_", "&#95;")
        .replace("`", "&#96;")
        .replace("{", "&#123;")
        .replace("}", "&#125;")
        .replace("$", "&#36;")
    )


def site_url(path: str | None) -> str:
    if not path:
        return ""
    if path.startswith("http"):
        return path
    if path.startswith(BASE_URL):
        return path
    if path.startswith("/"):
        return f"{BASE_URL}{path}"
    return f"{BASE_URL}/{path}"


def format_number(value: Any) -> str:
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return "0"


def theme_label(theme_id: str) -> str:
    return THEME_LABELS.get(theme_id, theme_id.replace("-", " ").title())


def theme_route(theme_id: str, fallback: str) -> str:
    route = THEME_ROUTES.get(theme_id)
    if route:
        return site_url(f"/theme-evidence/{route}/")
    return fallback


def strip_existing_dashboard(text: str) -> str:
    if BEGIN_DASHBOARD not in text:
        return text.rstrip() + "\n"
    before, rest = text.split(BEGIN_DASHBOARD, 1)
    if END_DASHBOARD not in rest:
        return before.rstrip() + "\n"
    _, after = rest.split(END_DASHBOARD, 1)
    return (before.rstrip() + "\n\n" + after.strip()).rstrip() + "\n"


def source_lookup(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item.get("source_id")): item for item in data.get("sources", []) if item.get("source_id")}


def records_by_source(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    for record in data.get("records", []):
        source_id = str(record.get("source_id") or "")
        if source_id:
            out.setdefault(source_id, []).append(record)
    return out


def count_record_features(record: dict[str, Any]) -> tuple[int, int, int]:
    return (
        len(record.get("equations") or []),
        len(record.get("figures") or []),
        len(record.get("quotes") or []),
    )


def section_score(record: dict[str, Any]) -> int:
    equations, figures, quotes = count_record_features(record)
    concepts = len(record.get("concept_hits") or [])
    glossary = len(record.get("glossary_hits") or [])
    words = int(record.get("word_count") or 0)
    return equations * 150 + figures * 120 + quotes * 90 + concepts * 35 + glossary * 25 + words // 120


def top_sections(records: list[dict[str, Any]], limit: int = 8) -> list[dict[str, Any]]:
    return sorted(records, key=section_score, reverse=True)[:limit]


def section_label(record: dict[str, Any]) -> str:
    return str(record.get("label") or record.get("title") or record.get("id") or "Untitled section")


def section_links(source_id: str, record: dict[str, Any]) -> dict[str, str]:
    slug = record.get("slug") or ""
    return {
        "source": site_url(f"/source-texts/{source_id}/{slug}/"),
        "workbench": site_url(f"/chapter-workbench/{source_id}/{slug}/"),
    }


def concept_rows(records: list[dict[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    counts: Counter[str] = Counter()
    labels: dict[str, str] = {}
    for record in records:
        for hit in record.get("concept_hits") or []:
            concept_id = str(hit.get("id") or "")
            if not concept_id:
                continue
            counts[concept_id] += int(hit.get("count") or 0)
            labels[concept_id] = str(hit.get("label") or concept_id)
    return [
        {
            "id": concept_id,
            "label": labels.get(concept_id, concept_id),
            "count": count,
            "link": site_url(f"/concept-concordance/{concept_id}/"),
        }
        for concept_id, count in counts.most_common(limit)
    ]


def glossary_rows(records: list[dict[str, Any]], limit: int = 8) -> list[dict[str, Any]]:
    counts: Counter[str] = Counter()
    labels: dict[str, str] = {}
    for record in records:
        for hit in record.get("glossary_hits") or []:
            term_id = str(hit.get("id") or hit.get("term") or hit.get("label") or "")
            if not term_id:
                continue
            counts[term_id] += int(hit.get("count") or 0)
            labels[term_id] = str(hit.get("label") or hit.get("term") or term_id)
    return [
        {
            "id": term_id,
            "label": labels.get(term_id, term_id),
            "count": count,
        }
        for term_id, count in counts.most_common(limit)
    ]


def theme_rows(source: dict[str, Any], records: list[dict[str, Any]], limit: int = 8) -> list[dict[str, Any]]:
    if source.get("theme_totals"):
        return [
            {
                "id": str(item.get("id") or ""),
                "label": str(item.get("label") or theme_label(str(item.get("id") or ""))),
                "count": int(item.get("count") or 0),
            }
            for item in source.get("theme_totals", [])[:limit]
        ]

    counts: Counter[str] = Counter()
    for record in records:
        for theme_id, count in (record.get("theme_counts") or {}).items():
            counts[str(theme_id)] += int(count or 0)
    return [
        {"id": theme_id, "label": theme_label(theme_id), "count": count}
        for theme_id, count in counts.most_common(limit)
    ]


def source_claim(source: dict[str, Any], themes: list[dict[str, Any]]) -> str:
    title = source.get("title") or "This source"
    top = ", ".join(item["label"] for item in themes[:3])
    sections = format_number(source.get("section_count"))
    words = format_number(source.get("word_total"))
    if top:
        return (
            f"{title} currently contributes {sections} processed sections and "
            f"{words} candidate OCR/PDF-text words to the archive. Its strongest "
            f"tracked evidence clusters are {top}."
        )
    return (
        f"{title} currently contributes {sections} processed sections and "
        f"{words} candidate OCR/PDF-text words to the archive."
    )


def dashboard_markdown(
    source: dict[str, Any],
    records: list[dict[str, Any]],
    crosslinked: dict[str, Any] | None,
) -> tuple[str, dict[str, Any]]:
    source_id = str(source["source_id"])
    links = source.get("links") or {}
    xlinks = (crosslinked or {}).get("links") or {}
    themes = theme_rows(source, records)
    concepts = concept_rows(records)
    glossary = glossary_rows(records)
    priority = top_sections(records)

    formula_count = (
        (crosslinked or {}).get("formula_candidates")
        if crosslinked
        else source.get("equation_candidate_count")
    )
    figure_count = (
        (crosslinked or {}).get("figure_candidates")
        if crosslinked
        else source.get("figure_candidate_count")
    )
    promoted_crops = (crosslinked or {}).get("promoted_crops", 0)
    modern_guides = (crosslinked or {}).get("modern_visual_guides", 0)

    overview = {
        "source_id": source_id,
        "title": source.get("title"),
        "year": source.get("year"),
        "sections": source.get("section_count"),
        "words": source.get("word_total"),
        "equation_candidates": source.get("equation_candidate_count"),
        "formula_candidates": formula_count,
        "figure_candidates": figure_count,
        "promoted_crops": promoted_crops,
        "modern_visual_guides": modern_guides,
        "quote_candidates": source.get("quote_candidate_count"),
        "themes": themes,
        "concepts": concepts,
        "glossary": glossary,
        "priority_sections": [
            {
                "id": record.get("id"),
                "label": section_label(record),
                "word_count": record.get("word_count"),
                "equations": count_record_features(record)[0],
                "figures": count_record_features(record)[1],
                "quotes": count_record_features(record)[2],
                "links": section_links(source_id, record),
            }
            for record in priority
        ],
        "links": {
            "coverage": links.get("coverage") or site_url(f"/book-coverage/{source_id}/"),
            "source_text": links.get("source_text_index") or xlinks.get("source_text") or site_url(f"/source-texts/{source_id}/"),
            "workbench": links.get("chapter_workbench_index") or xlinks.get("workbench") or site_url(f"/chapter-workbench/{source_id}/"),
            "visual_map": xlinks.get("visual_map") or site_url(f"/diagrams/source-visuals/{source_id}/"),
            "formula_map": xlinks.get("formula_map") or site_url(f"/mathematics/source-formula-maps/{source_id}/"),
            "archive": (links.get("archive") or ""),
        },
    }

    mode_cards = [
        ("Read", overview["links"]["source_text"], "Open the processed source text first, before commentary."),
        ("Study", overview["links"]["coverage"], "Use the book coverage map for section-by-section orientation."),
        ("Analyze", overview["links"]["workbench"], "Open the chapter workbench for concepts, equations, figures, and glossary hits."),
        ("Visuals", overview["links"]["visual_map"], "Review figure candidates, promoted crops, and modern guide diagrams."),
        ("Math", overview["links"]["formula_map"], "Review source-routed formula candidates and equation families."),
    ]
    if overview["links"]["archive"]:
        mode_cards.append(("Verify", overview["links"]["archive"], "Open the external scan or custody link for page-image checking."))

    lines: list[str] = [
        "",
        BEGIN_DASHBOARD,
        "",
        "## Source Research Dashboard",
        "",
        '<div class="source-text-warning" data-layer="source">',
        "  <strong>Generated source dashboard:</strong> this section joins the source overview to the book coverage atlas, source text reader, chapter workbench, visual maps, and formula maps. Counts are candidate research aids until scan verification promotes them.",
        "</div>",
        "",
        '<div class="codex-signal">',
        f"  <div><strong>{format_number(source.get('section_count'))}</strong><p>processed sections</p></div>",
        f"  <div><strong>{format_number(source.get('word_total'))}</strong><p>candidate words</p></div>",
        f"  <div><strong>{format_number(formula_count)}</strong><p>formula candidates</p></div>",
        f"  <div><strong>{format_number(figure_count)}</strong><p>figure candidates</p></div>",
        f"  <div><strong>{format_number(promoted_crops)}</strong><p>promoted crops</p></div>",
        "</div>",
        "",
        "### Choose Your Door",
        "",
        '<div class="source-matrix source-dashboard-doors">',
    ]

    for label, href, description in mode_cards:
        if not href:
            continue
        lines.append(
            f'  <a href="{esc(href)}">{esc(label)}<span>{esc(description)}</span></a>'
        )

    lines.extend(
        [
            "</div>",
            "",
            "### What This Source Currently Gives The Archive",
            "",
            source_claim(source, themes),
            "",
            "This is a routing judgment based on processed metadata, not a final historical claim. The strongest next move for any exact quotation, equation, or diagram is still to open the source scan and check the page image.",
            "",
            "### Dominant Evidence Themes",
            "",
            '<table class="codex-status-table source-dashboard-table">',
            "  <thead><tr><th>Theme</th><th>Candidate Hits</th><th>Evidence Route</th></tr></thead>",
            "  <tbody>",
        ]
    )
    for theme in themes[:8]:
        theme_id = theme.get("id") or ""
        route = theme_route(str(theme_id), overview["links"]["workbench"])
        lines.append(
            f'    <tr><td>{esc(theme.get("label"))}</td><td>{format_number(theme.get("count"))}</td><td><a href="{esc(route)}">Open theme evidence</a></td></tr>'
        )
    lines.extend(["  </tbody>", "</table>", ""])

    lines.extend(
        [
            "### Best First Sections To Read",
            "",
            '<div class="route-section-list compact-route-list">',
        ]
    )
    for record in priority:
        equations, figures, quotes = count_record_features(record)
        route_links = section_links(source_id, record)
        concepts_text = ", ".join(
            str(hit.get("label") or hit.get("id"))
            for hit in (record.get("concept_hits") or [])[:4]
            if hit.get("label") or hit.get("id")
        ) or "No current concept hits"
        themes_text = ", ".join(theme_label(str(item)) for item in (record.get("top_themes") or [])[:3]) or "No current theme tags"
        lines.extend(
            [
                '  <article class="route-section-card source-dashboard-section">',
                "    <div>",
                f"      <h3>{esc(section_label(record))}</h3>",
                f"      <p>{esc(record.get('location') or 'location pending')} - {format_number(record.get('word_count'))} words</p>",
                "    </div>",
                "    <div>",
                "      <strong>Signals</strong>",
                f"      <p>{esc(themes_text)}</p>",
                f"      <small>{esc(concepts_text)}</small>",
                "    </div>",
                "    <div>",
                "      <strong>Candidate material</strong>",
                f"      <p>{format_number(equations)} equations - {format_number(figures)} figures - {format_number(quotes)} quotes</p>",
                "    </div>",
                '    <nav aria-label="Open source dashboard section routes">',
                f'      <a href="{esc(route_links["source"])}">Read source</a>',
                f'      <a href="{esc(route_links["workbench"])}">Research review</a>',
                "    </nav>",
                "  </article>",
            ]
        )
    lines.extend(["</div>", ""])

    if concepts:
        lines.extend(
            [
                "### Concepts To Follow From This Source",
                "",
                '<div class="source-dashboard-pills">',
            ]
        )
        for concept in concepts[:10]:
            lines.append(
                f'  <a href="{esc(concept["link"])}">{esc(concept["label"])}<span>{format_number(concept["count"])} hits</span></a>'
            )
        lines.extend(["</div>", ""])

    if glossary:
        lines.extend(
            [
                "### Terminology Signals",
                "",
                '<table class="codex-status-table source-dashboard-table">',
                "  <thead><tr><th>Term</th><th>Candidate Hits</th><th>Use</th></tr></thead>",
                "  <tbody>",
            ]
        )
        for term in glossary[:8]:
            lines.append(
                f'    <tr><td>{esc(term["label"])}</td><td>{format_number(term["count"])}</td><td>Review in workbench before promoting to glossary.</td></tr>'
            )
        lines.extend(["  </tbody>", "</table>", ""])

    lines.extend(
        [
            "### Verification Focus",
            "",
            '<div class="research-passages">',
            '  <section data-layer="source">',
            "    <h3>Source custody</h3>",
            "    <p>Verify title page, edition, page images, and OCR line boundaries before final quotation.</p>",
            "  </section>",
            '  <section data-layer="modern">',
            "    <h3>Mathematics</h3>",
            "    <p>Use the formula map to locate equations, then correct OCR symbols and preserve Steinmetz notation before modern translation.</p>",
            "  </section>",
            '  <section data-layer="interpretive">',
            "    <h3>Interpretation boundary</h3>",
            "    <p>Modern engineering and ether-field readings belong after source anchoring, with labels kept visible.</p>",
            "  </section>",
            "</div>",
            "",
            END_DASHBOARD,
            "",
        ]
    )

    return "\n".join(lines), overview


def build_index_page(dashboards: list[dict[str, Any]]) -> str:
    cards = []
    for item in dashboards:
        cards.append(
            f'<a href="{esc(site_url(f"/sources/{item["source_id"]}/"))}">{esc(item["title"])}'
            f'<span>{esc(item.get("year") or "")} - {format_number(item.get("sections"))} sections - '
            f'{format_number(item.get("formula_candidates"))} formulas - {format_number(item.get("figure_candidates"))} figures</span></a>'
        )
    return "\n".join(
        [
            "---",
            'title: Source Research Dashboards',
            'description: Front-door dashboards for every processed Steinmetz source.',
            "---",
            "",
            "{/* Generated by pipeline/scripts/generate_source_research_dashboards.py. Do not edit by hand. */}",
            "",
            "The source dashboards connect each curated source overview to the actual material behind it: source text, book coverage, chapter workbench, visual maps, formula maps, and verification routes. Use this page when a source overview feels too small for the amount of processed evidence behind it.",
            "",
            '<div class="source-text-warning" data-layer="source">',
            "  <strong>Candidate layer:</strong> these dashboards expose processed evidence and review routes. They do not certify OCR text, equations, figures, or page locations as final.",
            "</div>",
            "",
            '<div class="source-matrix evidence-source-grid">',
            *cards,
            "</div>",
            "",
        ]
    )


def main() -> None:
    root = Path.cwd()
    book_atlas = load_json(root / "processed/book_coverage_atlas.json", {})
    workbench = load_json(root / "processed/chapter_workbench.json", {})
    crosslinked = load_json(root / "processed/crosslinked_research_surfaces.json", {})

    sources = source_lookup(book_atlas)
    records = records_by_source(workbench)
    cross_sources = source_lookup(crosslinked)

    dashboards: list[dict[str, Any]] = []
    for source_id, source in sources.items():
        source_page = root / "site/src/content/docs/sources" / source_id / "index.mdx"
        if not source_page.exists():
            continue
        dashboard, overview = dashboard_markdown(source, records.get(source_id, []), cross_sources.get(source_id))
        original = source_page.read_text(encoding="utf-8")
        updated = strip_existing_dashboard(original).rstrip() + "\n\n" + dashboard
        write_text(source_page, updated)
        dashboards.append(overview)

    dashboards.sort(key=lambda item: (str(item.get("title") or ""), int(item.get("year") or 0)))
    output = {
        "generated_at": date.today().isoformat(),
        "quality_note": "Source research dashboards are generated routing layers over candidate OCR/PDF evidence.",
        "source_count": len(dashboards),
        "sources": dashboards,
    }
    write_json(root / "processed/source_research_dashboards.json", output)
    write_json(root / "site/public/data/source_research_dashboards.json", output)
    write_text(root / "site/src/content/docs/source-library/source-research-dashboards.mdx", build_index_page(dashboards))
    print(f"Generated source research dashboards for {len(dashboards)} sources.")


if __name__ == "__main__":
    main()
