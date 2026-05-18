#!/usr/bin/env python3
"""Add source-grounded reader synthesis blocks to curated concept pages."""

from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import quote


BASE_URL = ""
BEGIN = "{/* BEGIN GENERATED READER SYNTHESIS */}"
END = "{/* END GENERATED READER SYNTHESIS */}"


CONCEPT_READINGS: dict[str, dict[str, str]] = {
    "ether": {
        "source_pattern": "Steinmetz's ether trail is not evenly distributed. The strongest current cluster is in the relativity lectures, where ether is discussed beside the replacement of mechanical ether language by field language; the radiation lectures preserve the older optical-wave setting.",
        "modern": "A modern reader should treat ether passages as historical source language and as evidence of how wave propagation was framed before field theory and relativity settled into present textbook form.",
        "math": "The mathematical bridge is usually indirect: velocity, frequency, wavelength, field energy, and propagation arguments matter more than a single ether equation.",
        "interpretive": "Ether-field readings belong here only as labeled interpretation. Do not attribute Wheeler-style dielectric or counterspatial vocabulary to Steinmetz unless a passage explicitly supports it.",
    },
    "radiation": {
        "source_pattern": "Radiation is a first-principles doorway: Steinmetz begins with energy in transit, then follows frequency, wavelength, spectra, light, heat, ultraviolet, X-rays, and practical illumination.",
        "modern": "Modern engineering reads this as electromagnetic radiation carrying energy and transferring it to matter upon absorption.",
        "math": "The key mathematical spine is velocity, frequency, wavelength, inverse-square distribution, reflection/refraction geometry, and photometric measurement.",
        "interpretive": "Interpretive readings may discuss radiation as field transport, but they must remain separate from the source-level treatment of light and electrical waves.",
    },
    "electric-waves": {
        "source_pattern": "Electric waves connect optical radiation, wireless waves, high-frequency circuit behavior, and transmission-line disturbances.",
        "modern": "Modern readers can map this to electromagnetic waves and distributed-parameter circuit behavior, while keeping Steinmetz's older wave vocabulary visible.",
        "math": "Follow frequency, wavelength, velocity, line constants, reflection, standing waves, and traveling waves.",
        "interpretive": "Field-medium interpretations are useful as comparison layers only after the source distinction between circuit waves, radiation, and line phenomena is clear.",
    },
    "symbolic-method": {
        "source_pattern": "The symbolic method is Steinmetz's engineering translation of alternating quantities into calculable complex form.",
        "modern": "Modern readers know this as phasor and complex impedance analysis, but Steinmetz's presentation keeps the geometric origin close to the algebra.",
        "math": "The core route is rectangular components, the quadrature operator j, impedance, admittance, conductance, susceptance, and phase angle.",
        "interpretive": "Interpretation should not turn symbolic notation into metaphysics. Its first meaning is mathematical economy for AC engineering.",
    },
    "complex-quantities": {
        "source_pattern": "Complex quantities are treated as a general engineering number system, not as decorative notation.",
        "modern": "Modern readers should connect the page to phasors, complex planes, rotating quantities, and sinusoidal steady-state analysis.",
        "math": "Prioritize rectangular/polar conversion, multiplication by j, magnitude, phase, and division of complex quantities.",
        "interpretive": "Any philosophical reading must follow the mathematical layer, because Steinmetz's immediate purpose is calculational power.",
    },
    "hysteresis": {
        "source_pattern": "Hysteresis is both material memory and engineering loss. Steinmetz's importance is that he made magnetic lag calculable enough for apparatus design.",
        "modern": "Modern engineering reads this through B-H loops, core loss, magnetic material behavior, and empirical loss laws.",
        "math": "The Steinmetz hysteresis law, effective resistance, frequency, flux density, and energy per cycle are the core mathematical route.",
        "interpretive": "Ether-field readings may describe lag or memory as field behavior, but the source layer is magnetic material loss and apparatus calculation.",
    },
    "transient-phenomena": {
        "source_pattern": "Transient phenomena are Steinmetz's correction to steady-state habits: electrical systems have temporary terms before permanent behavior is reached.",
        "modern": "Modern readers can map this to time-domain circuit response, natural response, forced response, damping, and distributed-line transients.",
        "math": "Follow exponential terms, oscillatory terms, damping, RLC response, condenser charge/discharge, line reflections, and surge propagation.",
        "interpretive": "Interpretive readings should preserve the engineering fact first: stored electric and magnetic energy must readjust through time.",
    },
    "impedance": {
        "source_pattern": "Impedance gathers resistance and reactance into one calculable AC opposition.",
        "modern": "Modern readers recognize it as complex impedance, but the source path shows why the geometric and physical split mattered.",
        "math": "Use R plus jX, magnitude, phase, voltage/current relation, and power-factor consequences.",
        "interpretive": "Field readings should connect reactance to storage and return, without confusing impedance with a literal material substance.",
    },
    "reactance": {
        "source_pattern": "Reactance is where Steinmetz keeps field storage visible inside circuit calculation.",
        "modern": "Modern engineering treats inductive and capacitive reactance as frequency-dependent quadrature opposition.",
        "math": "Use inductive reactance, condensive/capacitive reactance, phase displacement, impedance triangle, and power-factor relations.",
        "interpretive": "This is a strong field-interpretation bridge, but the source claim remains AC circuit behavior and energy exchange.",
    },
    "admittance": {
        "source_pattern": "Admittance is the reciprocal language that makes parallel AC circuits tractable.",
        "modern": "Modern readers should map it to Y = G + jB, conductance, susceptance, and parallel network calculation.",
        "math": "Focus on reciprocal impedance, conductance, susceptance, and vector addition of branch currents.",
        "interpretive": "Keep the interpretation modest: the page is mostly mathematical method and circuit bookkeeping.",
    },
    "dielectric-loss": {
        "source_pattern": "Dielectric terms lead from capacity and insulation into field stress, loss, and stored electric energy.",
        "modern": "Modern readers can connect this to capacitance, dielectric field, permittivity, loss angle, insulation stress, and displacement current.",
        "math": "Follow capacity, condensive reactance, susceptance, charging current, energy storage, and frequency dependence.",
        "interpretive": "This is a legitimate place to compare dielectric-field language with ether-field vocabulary, provided the comparison is labeled.",
    },
    "distributed-constants": {
        "source_pattern": "Distributed constants move the reader beyond lumped circuits into lines whose resistance, inductance, capacity, and leakage are spread through space.",
        "modern": "Modern readers should connect this to transmission-line theory, propagation velocity, reflections, standing waves, and surge behavior.",
        "math": "Follow line inductance/capacity, velocity, wavelength, attenuation, reflection, and natural period.",
        "interpretive": "Field interpretations are useful here because the line is not merely a component; it is an extended electromagnetic system.",
    },
}

DEFAULT_READING = {
    "source_pattern": "The processed corpus gives this concept a source trail across Steinmetz's books and lectures. Read the source distribution first, because the meaning often changes between radiation, AC calculation, apparatus, and transients.",
    "modern": "Translate the older wording into modern electrical-engineering language only after the source location is visible.",
    "math": "Use the linked equation atlas and source formula maps to decide whether this concept has a mathematical layer, a diagrammatic layer, or mainly a terminology layer.",
    "interpretive": "Interpretive readings are welcome in this archive only when they are labeled and separated from Steinmetz's explicit wording.",
}


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def clean(value: Any, limit: int | None = None) -> str:
    text = "" if value is None else str(value)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        text = text[: limit - 3].rstrip() + "..."
    return text


def esc(value: Any) -> str:
    return html.escape(clean(value), quote=True).replace("{", "&#123;").replace("}", "&#125;")


def md(value: Any) -> str:
    return clean(value).replace("|", "\\|").replace("{", "&#123;").replace("}", "&#125;")


def focused_url(url: Any, query: Any = "") -> str:
    value = clean(url)
    if not value or value == "#":
        return "#"
    base = value.split("#", 1)[0]
    term = clean(query)
    if term:
        separator = "&" if "?" in base else "?"
        base = f"{base}{separator}q={quote(term)}"
    return f"{base}#source-text-reader"


def source_sentence(dossier: dict[str, Any]) -> str:
    sources = dossier.get("sources") or []
    if not sources:
        return "No source concentration has been generated yet."
    top = sources[0]
    return (
        f"The current strongest source route is **{md(top.get('source_title'))}**, "
        f"with **{top.get('occurrence_count', 0)}** candidate hits across "
        f"**{top.get('section_count', 0)}** sections."
    )


def passage_rows(dossier: dict[str, Any]) -> str:
    rows = []
    for section in (dossier.get("priority_sections") or [])[:4]:
        concept = next((clean(item) for item in section.get("concepts", []) if clean(item)), "")
        rows.append(
            "<tr>"
            f"<td><strong>{esc(section.get('section_label'))}</strong><br/><small>{esc(section.get('source_title'))}</small></td>"
            f"<td>{esc(section.get('occurrence_count'))}</td>"
            f"<td>{esc(section.get('location'))}</td>"
            f"<td><a href=\"{esc(focused_url(section.get('source_text_url'), concept))}\">read</a> - <a href=\"{esc(section.get('workbench_url'))}#chapter-local-concept-hits\">research review</a></td>"
            "</tr>"
        )
    if not rows:
        rows.append('<tr><td colspan="4">No generated passage route is available yet.</td></tr>')
    return "\n".join(rows)


def build_block(dossier: dict[str, Any]) -> str:
    slug = str(dossier.get("page_slug") or "")
    reading = {**DEFAULT_READING, **CONCEPT_READINGS.get(slug, {})}
    totals = dossier.get("totals") or {}
    title = dossier.get("page_title") or slug.replace("-", " ").title()
    concept_labels = ", ".join(md(label) for label in dossier.get("concept_labels", [])[:4]) or "tracked concept vocabulary"
    concordance = dossier.get("concordance_links") or []
    concordance_links = " - ".join(f"[{md(item.get('label'))}]({item.get('url')})" for item in concordance) or "No concordance route yet."
    return f"""{BEGIN}

## Reader Synthesis

<div class="concept-synthesis-panel" data-layer="modern">
  <section>
    <h3>What Steinmetz Is Doing Here</h3>
    <p>{esc(reading['source_pattern'])}</p>
    <p>{source_sentence(dossier)}</p>
  </section>
  <section>
    <h3>Modern Translation</h3>
    <p>{esc(reading['modern'])}</p>
    <p>This page currently tracks <strong>{totals.get('occurrences', 0)}</strong> candidate occurrences across <strong>{totals.get('matching_sources', 0)}</strong> sources and <strong>{totals.get('matching_sections', 0)}</strong> sections.</p>
  </section>
  <section>
    <h3>Mathematical And Visual Route</h3>
    <p>{esc(reading['math'])}</p>
    <p>Use the math/visual bridge lower on this page to jump into formula families, source visual maps, and candidate figure leads.</p>
  </section>
  <section>
    <h3>Interpretive Boundary</h3>
    <p>{esc(reading['interpretive'])}</p>
    <p>Layer labels stay active: source claim, modern equivalent, mathematical reconstruction, historical note, and interpretive reading are not interchangeable.</p>
  </section>
</div>

### Fast Reading Path For {md(title)}

<table class="codex-status-table concept-reading-path">
  <thead>
    <tr><th>Passage</th><th>Hits</th><th>Location</th><th>Open</th></tr>
  </thead>
  <tbody>
{passage_rows(dossier)}
  </tbody>
</table>

### Research Position

- **Tracked vocabulary:** {concept_labels}.
- **Concordance:** {concordance_links}.
- **Source discipline:** the table above is for reading and navigation; exact quotation still requires scan verification.
- **Editorial rule:** expand this page by promoting scan-checked passages, equations, and diagrams from the linked workbench pages, not by adding unsourced generalizations.

{END}
"""


def replace_or_insert(existing: str, block: str) -> str:
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), flags=re.DOTALL)
    if pattern.search(existing):
        return pattern.sub(lambda _match: block.strip(), existing).rstrip() + "\n"
    marker = "{/* BEGIN GENERATED CONCEPT DOSSIER */}"
    if marker in existing:
        return existing.replace(marker, block.strip() + "\n\n" + marker, 1)
    return existing.rstrip() + "\n\n" + block.strip() + "\n"


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    data = load_json(root / "processed" / "concept_page_dossiers.json", {})
    dossiers = data.get("dossiers", []) if isinstance(data, dict) else []
    docs_root = root / "site" / "src" / "content" / "docs" / "concepts"
    count = 0
    for dossier in dossiers:
        slug = str(dossier.get("page_slug") or "")
        path = docs_root / f"{slug}.mdx"
        if not slug or not path.exists():
            continue
        existing = path.read_text(encoding="utf-8")
        write_text(path, replace_or_insert(existing, build_block(dossier)))
        count += 1
    payload = {
        "generated_at": date.today().isoformat(),
        "quality_note": "Generated reader synthesis blocks for concept pages from source-grounded dossier data.",
        "page_count": count,
        "pages": [
            {
                "page_slug": dossier.get("page_slug"),
                "page_title": dossier.get("page_title"),
                "totals": dossier.get("totals"),
                "page": f"{BASE_URL}/concepts/{dossier.get('page_slug')}/",
            }
            for dossier in dossiers
        ],
    }
    write_text(
        root / "processed" / "concept_reader_synthesis.json",
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
    )
    write_text(
        root / "site" / "public" / "data" / "concept_reader_synthesis.json",
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
    )
    print(f"Generated reader synthesis for {count} concept pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
