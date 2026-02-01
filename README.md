# Resume Generator

Generate tailored resumes from a single JSON source file. One master file, multiple output formats, easy customization per job type.

## Why This Exists

- **Single source of truth** - All resume data in one JSON file
- **Easy tailoring** - Different summaries for different job types
- **Multiple formats** - Generate Markdown, HTML, and plain text
- **Version control** - Track changes in Git
- **ATS-friendly** - Plain text output maps well to application fields

## Quick Start

```bash
# Generate all formats with default settings
python generate.py

# Generate DevOps-focused resume
python generate.py --type devops

# Generate Project Manager version
python generate.py --type project_manager

# Generate only HTML
python generate.py --format html

# Generate with custom output name
python generate.py --type devops --output MyResume_DevOps
```

## Output

Generated files go to the `output/` folder:
- `*.md` - Markdown (good for GitHub, can convert to many formats)
- `*.html` - HTML (open in browser, print to PDF)
- `*.txt` - Plain text (copy/paste into job applications)

## Converting HTML to PDF

1. Open the `.html` file in Chrome/Safari/Firefox
2. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows)
3. Select "Save as PDF"
4. Adjust margins if needed

## Resume Types

| Type | Focus |
|------|-------|
| `default` | Technical Project Manager (balanced) |
| `technical_pm` | Same as default, emphasizes technical + leadership |
| `devops` | Emphasizes coding projects, automation, technical skills |
| `project_manager` | Emphasizes team leadership, budgets, stakeholder management |

## Customizing

Edit `resume.json` to update your information:

- **basics.summary** - Different summaries for each resume type
- **skills** - Grouped by category
- **projects** - Your portfolio projects
- **work** - Work experience with highlights
- **education** - Degrees and certifications

## File Structure

```
resume-generator/
├── resume.json      # Your master resume data
├── generate.py      # Generator script
├── README.md        # This file
└── output/          # Generated resumes
    ├── *.md
    ├── *.html
    └── *.txt
```

## Future Enhancements

- [ ] PDF generation without browser (weasyprint or similar)
- [ ] Auto-fill job application forms
- [ ] Keyword matching against job descriptions
- [ ] Cover letter generator
