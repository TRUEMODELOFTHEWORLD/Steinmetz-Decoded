#!/usr/bin/env python3
"""Bootstrap a new Research Codex project from this repo's architecture.

The script is intentionally small and dependency-free. It creates a clean
starter workspace with the same source isolation principles as Steinmetz
Decoded, but without any Steinmetz content. Users can then copy or adapt the
pipeline scripts and site stack they need.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any


SAFE_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = re.sub(r"-+", "-", lowered).strip("-")
    return lowered or "research-codex"


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def assert_safe_output(output: Path, force: bool) -> None:
    if output.exists():
        if not output.is_dir():
            raise SystemExit(f"Output path exists and is not a directory: {output}")
        if any(output.iterdir()) and not force:
            raise SystemExit(
                f"Output directory is not empty: {output}\n"
                "Use --force only if you intentionally want starter files merged into it."
            )


def build_config(args: argparse.Namespace) -> dict[str, Any]:
    project_id = args.project_id or slugify(args.project_title)
    if not SAFE_ID.match(project_id):
        raise SystemExit("Project ID must be lowercase letters, numbers, and hyphens.")
    collection_id = args.collection_id or project_id
    return {
        "schema": "research-codex-engine-0.1",
        "generated_at": date.today().isoformat(),
        "project_id": project_id,
        "project_title": args.project_title,
        "collection_id": collection_id,
        "primary_subject": args.primary_subject,
        "purpose": args.purpose,
        "quality_rules": [
            "Every factual claim must point to a source, derivation, reference, or labeled interpretation.",
            "Keep original source wording separate from modern explanation and speculative synthesis.",
            "Do not mark OCR-derived content as reviewed until a scan or authoritative text has been checked.",
            "Preserve source, page, section, edition, and confidence metadata whenever possible.",
        ],
        "standard_layers": [
            "source custody",
            "clean text",
            "page or section map",
            "concept extraction",
            "equation extraction",
            "figure extraction",
            "glossary candidates",
            "quote candidates",
            "modern explanation",
            "historical context",
            "interpretive reading",
            "verification queue",
        ],
    }


def scaffold(output: Path, config: dict[str, Any]) -> None:
    directories = [
        "sources/raw",
        "sources/manifests",
        "processed",
        "analysis",
        "concepts",
        "math",
        "diagrams/original",
        "diagrams/recreated",
        "comparisons",
        "glossary",
        "hidden-gems",
        "research-questions",
        "pipeline/scripts",
        "pipeline/schemas",
        "site/content",
        "site/public/data",
        "templates",
    ]
    for relative in directories:
        (output / relative).mkdir(parents=True, exist_ok=True)

    write_json(output / "codex.config.json", config)
    write_json(output / "sources" / "source_catalog.json", [])
    write_json(
        output / "sources" / "manifests" / "source_manifest.template.json",
        {
            "source_id": "example-source-id",
            "collection_id": config["collection_id"],
            "title": "Example Source Title",
            "creator": config["primary_subject"],
            "year": None,
            "edition": None,
            "source_type": "book | paper | lecture | patent | archive | web",
            "authority_refs": [],
            "raw_files": [],
            "rights_status": "unknown",
            "processing_status": "raw",
            "quality_notes": [],
        },
    )
    write_json(
        output / "processed" / "claim-template.json",
        {
            "claim_id": "example-claim",
            "person": config["primary_subject"],
            "source_id": "example-source-id",
            "location": {"chapter": None, "page": None, "section": None},
            "claim_type": "explicit_source_claim",
            "interpretation_layer": "source",
            "confidence": "needs-verification",
            "text": "",
        },
    )
    write_json(
        output / "templates" / "collection_map.template.json",
        {
            "schema": "research-codex-engine.collection-map-0.1",
            "project_id": config["project_id"],
            "collections": [
                {
                    "collection_id": config["collection_id"],
                    "type": "person | topic | tradition | archive",
                    "title": config["primary_subject"],
                    "scope": "Books, lectures, papers, patents, correspondence, diagrams, and later commentary.",
                    "source_root": f"sources/{config['collection_id']}",
                    "processed_root": f"processed/{config['collection_id']}",
                    "public_path": f"/people/{config['collection_id']}/",
                }
            ],
            "global_indexes": [
                "concepts",
                "comparisons",
                "glossary",
                "math",
                "diagrams",
                "hidden-gems",
                "research-questions",
            ],
            "attribution_policy": (
                "Every cross-collection synthesis must preserve person, source, "
                "location, layer, and confidence metadata."
            ),
        },
    )
    write_text(
        output / "templates" / "verification_policy.md",
        """# Verification Policy

## Review States

- `raw`: source has been identified but not processed.
- `ocr`: text came from OCR or machine extraction.
- `candidate`: a machine or first-pass human extraction.
- `source-located`: tied to a source, section, page, figure, or equation.
- `scan-verified`: checked against a scan or trusted edition.
- `mathematically-reviewed`: formulas, variables, notation, and units reviewed.
- `canonical`: stable public explanation with source anchors and crosslinks.

## Promotion Rules

- A quotation must be checked against the scan before becoming canonical.
- A formula must preserve original notation before modern translation.
- A diagram must keep original source-page metadata.
- A modern explanation must not be presented as the author's own statement.
- An interpretive reading must never be allowed to erase source uncertainty.
""",
    )
    write_text(
        output / "README.md",
        f"""# {config['project_title']}

This starter project was created with the Research Codex Engine scaffold.

## First Steps

1. Add raw sources under `sources/raw/`.
2. Create one manifest per source under `sources/manifests/`.
3. Add records to `sources/source_catalog.json`.
4. Run or adapt the pipeline scripts from the Steinmetz Decoded project.
5. Publish generated pages only with visible source custody and confidence labels.

## Non-Negotiable Rule

Do not mix source fact, modern explanation, and interpretation. Each layer must stay visibly labeled.

## Review Before Publication

Use `templates/verification_policy.md` before promoting any extracted passage, formula, image, or concept to a canonical page.
""",
    )
    write_text(
        output / "PROJECT_CHARTER.md",
        f"""# {config['project_title']} Charter

Primary subject: {config['primary_subject']}

Purpose: {config['purpose']}

## Layers

- Source text and custody.
- Structured data and page maps.
- Concepts, equations, diagrams, glossary, quotes, and hidden gems.
- Modern explanation and historical context.
- Labeled interpretation and open questions.
- Verification queues and release levels.
""",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a clean Research Codex starter project.")
    parser.add_argument("--project-title", required=True, help="Human-readable title, e.g. Tesla Decoded.")
    parser.add_argument("--project-id", help="Stable lowercase slug. Defaults to a slug of the title.")
    parser.add_argument("--collection-id", help="Primary collection slug. Defaults to project id.")
    parser.add_argument("--primary-subject", required=True, help="Main person, topic, or tradition.")
    parser.add_argument("--purpose", default="A source-grounded public research codex.")
    parser.add_argument("--output", type=Path, required=True, help="Output directory for the starter project.")
    parser.add_argument("--force", action="store_true", help="Allow writing into a non-empty output directory.")
    args = parser.parse_args()

    output = args.output.resolve()
    assert_safe_output(output, args.force)
    config = build_config(args)
    scaffold(output, config)
    print(f"Created Research Codex starter at {output}")


if __name__ == "__main__":
    main()
