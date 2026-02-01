# Quick Reference

## Commands (from anywhere in Terminal)

```bash
resume           # Technical PM (default)
resume devops    # DevOps / Automation Engineer
resume pm        # Project Manager
resume am        # Account Manager / TAM
```

## What Happens

1. Generates HTML resume
2. Opens in browser
3. Press `Cmd+P` → Save as PDF
4. Upload PDF to job application

## Which Version to Use

| Job Posting Says | Use This |
|------------------|----------|
| Technical Project Manager, Solutions Engineer, Implementation Manager | `resume` |
| DevOps, SysAdmin, Platform Engineer, Automation | `resume devops` |
| Project Manager, Program Manager | `resume pm` |
| Account Manager, Customer Success, Technical Account Manager | `resume am` |

## Manual Generation (if aliases aren't loaded)

```bash
cd ~/Projects/resume-generator
python3 generate.py --type default
python3 generate.py --type devops
python3 generate.py --type project_manager
python3 generate.py --type account_manager
```

## Output Location

Generated files: `~/Projects/resume-generator/output/`

## Edit Your Resume Data

Edit `resume.json` to update your info, then regenerate.
