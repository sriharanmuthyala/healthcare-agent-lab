# Healthcare Agent Lab

Research-linked opportunity explorer, prototype selection workflow and fictional inbox demo. Prepared for Natasha and collaborator, 9 October 2026.

## What works today

- Search and filter 75 source-linked workflows in Healthcare (44) and Other healthcare (31).
- Adjust six ranking weights and view the top five.
- Compare up to three opportunities and download implementation briefs.
- Run a deterministic inbox classification and reply-drafting demo using fictional FAQ rules.
- Run a Python workflow to validate provenance, rank candidates and export briefs.

This is a curated research snapshot with a working selection engine. It does not yet autonomously ingest Google Drive, discover new candidates with an LLM, call a live AI model, send messages or integrate with patient systems. Analyst scores are judgements about prototype suitability, not measured ROI. The browser demo is rules-based and is not validated medical triage.

## Run locally

Python 3 standard library only:

```sh
python3 discovery.py --output generated
python3 -m unittest test_discovery.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000 . Search a subset with `python3 discovery.py --query appointment`. Supply custom weights with `--weights weights.json` using the six keys in `dist/catalogue.json`.

## GitHub

Upload this folder into a separate repository, such as healthcare-agent-lab. The included GitHub Actions workflow publishes `dist/` to GitHub Pages when Pages uses GitHub Actions and the workflow has the required repository permissions. Do not copy the Sites-specific `.openai/hosting.json` into a GitHub Pages repository.

Original reports remain in Google Drive. This package contains source links and paraphrased candidate briefs, not copies of the PDFs. Source links may require your collaborator's own Drive access. The private hosted explorer also requires access separately. No collaborator invitations have been sent.

## Discovery-agent next stage

Use `prompts/discover.md` as the extraction and validation contract. Implement authorised Drive ingestion in a secure backend, then model-assisted candidate extraction with source identifiers and locators. Validate proposed objects before adding them to the catalogue. Treat source documents as untrusted evidence. Keep model credentials and confidential source material out of browser bundles and public repositories.

The initial scope is Australian provider workflows. US payer and life-sciences examples remain in the catalogue with explicit local-fit labels. Potential benefits are hypotheses until measured in a pilot. The documentation prototype requires qualified clinical review.

## Initial shortlist

Provider inbox (97), document intake and matching (95), protocol/policy search (95), call quality review (93) and appointment coordination (90). Ties use alphabetical title ordering. Rankings change with weights.

## Files

- `dist/index.html`, `dist/styles.css`, `dist/app.js`: redesigned buildless browser application.
- `dist/logic.js`: ranking, filtering and fictional inbox logic.
- `tests/logic.test.js`: browser logic checks.
- `dist/catalogue.json`: source metadata, candidate definitions and scores.
- `discovery.py`: ranking, validation and brief export.
- `test_discovery.py`: checks for shortlist, ranking controls and missing evidence.
- `prompts/discover.md`: model-assisted research specification.
- `.github/workflows/pages.yml`: optional GitHub Pages publishing.


## Expanded coverage
168 source entries map to 75 workflows: 115 supplied Google healthcare entries, 52 Microsoft Healthcare entries and one supplementary MEDITECH excerpt. Original research workflows remain. The Source map tab and dist/source-mapping.csv preserve every entry-to-workflow mapping. Company examples are distinct from workflow counts. Conventional AI and infrastructure examples do not imply deployed generative agents. Prototype rankings are analyst estimates and customer productivity metrics are not reused as ROI.

## Navigation and design
Healthcare contains human patient services, clinical workflows and provider operations. Other healthcare contains animal health, life sciences, wellness and shared supporting capabilities. Each retains its detailed area and sector. The redesigned explorer uses a sidebar, five featured picks, searchable workflow cards and a dialog for detailed evidence. Source mapping, comparison, adjustable weights and brief downloads remain available.

The Pages workflow runs the Python and JavaScript tests before publishing dist. Enable Settings → Pages → GitHub Actions in the destination repository. The deployment URL should be taken from the successful workflow, not assumed before publication.
