# Research Codex Engine Templates

These templates are for starting a new source-grounded public knowledge archive from the Steinmetz Decoded architecture.

Use them when you want the framework without inheriting Steinmetz-specific content.

## Included Templates

- `codex.config.template.json`: project identity, collection identity, quality rules, and standard layers.
- `source_manifest.template.json`: required custody fields for a book, paper, lecture, patent, archive, or web source.
- `claim_record.template.json`: attribution model for facts, interpretations, and reconstructions.
- `collection_map.template.json`: multi-person or multi-topic collection layout.
- `project_charter.template.md`: public charter for a new codex project.
- `verification_policy.template.md`: review and promotion policy.

## Bootstrap Script

The fastest path is:

```powershell
python pipeline/scripts/bootstrap_new_codex.py `
  --project-title "Tesla Decoded" `
  --project-id tesla-decoded `
  --primary-subject "Nikola Tesla" `
  --output C:\tmp\tesla-decoded
```

That creates a clean starter workspace with source folders, processed-data folders, templates, a charter, and the anti-hallucination rules.

## Reuse Principle

Do not copy only the visual shell. Copy the evidence discipline:

- source custody first,
- candidate extraction second,
- review status always visible,
- interpretation clearly labeled,
- public pages generated from traceable data.

