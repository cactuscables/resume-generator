# Resume Generator

## What This Is
Python script that generates tailored resumes from a single JSON source file. Edit one file, generate multiple targeted versions for different job types. No dependencies beyond Python standard library.

## How It Works
- `resume.json` — Single source of truth for all resume content
- `generate.py` — Reads the JSON, outputs markdown, HTML, and/or plain text
- `output/` — All generated files land here

## Running It

```bash
# Generate everything (all types and formats)
python3 generate.py

# Generate a specific type
python3 generate.py --type devops
python3 generate.py --type project_manager
python3 generate.py --type account_manager

# Specific format only
python3 generate.py --type devops --format html
```

Shell aliases (loaded from .bashrc):
- `resume` — default (Technical PM)
- `resume devops` — DevOps / Automation Engineer
- `resume pm` — Project Manager
- `resume am` — Account Manager / TAM

HTML to PDF: Open `.html` in browser, Ctrl+P, Save as PDF.

## Resume Types

| Type | Focus |
|------|-------|
| `default` / `technical_pm` | Technical Project Manager (balanced) |
| `devops` | Emphasizes automation projects and coding |
| `project_manager` | Emphasizes teams, budgets, stakeholder management |
| `account_manager` | Client-facing TAM/AM angle |

## Editing Resume Content

Edit `resume.json` only. Key sections:
- `basics.summary` — Object with a key per resume type (tailored opening paragraph)
- `skills` — Array of grouped skill categories
- `projects` — Portfolio items (shown for all types except `project_manager`)
- `work` — Job history with bullet points under `highlights`

## Gotchas
- Projects section is intentionally hidden for `project_manager` type
- No pip installs needed — pure Python standard library
- No venv needed
