#!/usr/bin/env python3
"""
Resume Generator - Generate tailored resumes from JSON source

Usage:
    python generate.py                      # Generate default resume
    python generate.py --type devops        # Generate DevOps-focused resume
    python generate.py --type project_manager
    python generate.py --format markdown    # Output as markdown
    python generate.py --format html        # Output as HTML
    python generate.py --format txt         # Output as plain text
"""

import json
import argparse
from datetime import datetime
from pathlib import Path


def load_resume(path: str = "resume.json") -> dict:
    """Load resume data from JSON file"""
    with open(path, 'r') as f:
        return json.load(f)


def get_summary(resume: dict, resume_type: str = "default") -> str:
    """Get appropriate summary based on resume type"""
    summaries = resume['basics'].get('summary', {})
    if isinstance(summaries, str):
        return summaries
    return summaries.get(resume_type, summaries.get('default', ''))


def format_date(date_str: str) -> str:
    """Format date string for display"""
    if not date_str:
        return "Present"
    try:
        if len(date_str) == 4:  # Just year
            return date_str
        dt = datetime.strptime(date_str[:7], "%Y-%m")
        return dt.strftime("%Y")
    except:
        return date_str


def format_date_range(start: str, end: str) -> str:
    """Format date range for work experience"""
    start_fmt = format_date(start)
    end_fmt = format_date(end) if end else "Present"
    return f"{start_fmt} - {end_fmt}"


def generate_markdown(resume: dict, resume_type: str = "default") -> str:
    """Generate markdown formatted resume"""
    b = resume['basics']

    lines = []

    # Header
    lines.append(f"# {b['name']}")
    lines.append("")

    # Contact line
    contact = []
    if b.get('location'):
        contact.append(f"{b['location']['city']}, {b['location']['region']}")
    for profile in b.get('profiles', []):
        if profile['network'] == 'LinkedIn':
            contact.append(profile['url'].replace('https://', ''))
    if b.get('phone'):
        contact.append(b['phone'])
    if b.get('email'):
        contact.append(b['email'])

    lines.append(" | ".join(contact))
    lines.append("")

    # Summary
    lines.append("## PROFESSIONAL SUMMARY")
    lines.append("")
    lines.append(get_summary(resume, resume_type))
    lines.append("")

    # Skills
    lines.append("## SKILLS")
    lines.append("")
    for skill_group in resume.get('skills', []):
        keywords = ", ".join(skill_group['keywords'])
        lines.append(f"**{skill_group['name']}:** {keywords}")
        lines.append("")

    # Projects (if targeting technical roles)
    if resume.get('projects') and resume_type in ['default', 'devops', 'technical_pm']:
        lines.append("## PROJECTS")
        lines.append("")
        for project in resume['projects']:
            year = project.get('startDate', '')
            url = project.get('url', '')
            lines.append(f"### {project['name']} | {project.get('description', '')}  [{year}]")
            lines.append("")
            for highlight in project.get('highlights', []):
                lines.append(f"- {highlight}")
            if url:
                lines.append(f"- GitHub: {url}")
            lines.append("")

    # Work Experience
    lines.append("## PROFESSIONAL EXPERIENCE")
    lines.append("")
    for job in resume.get('work', []):
        date_range = format_date_range(job.get('startDate', ''), job.get('endDate', ''))
        lines.append(f"### {job['name']} | {job['position']}  [{date_range}]")
        lines.append(f"*{job.get('location', '')}*")
        lines.append("")
        for highlight in job.get('highlights', []):
            lines.append(f"- {highlight}")
        lines.append("")

    # Education
    lines.append("## EDUCATION")
    lines.append("")
    for edu in resume.get('education', []):
        lines.append(f"**{edu['institution']}**")
        lines.append(f"{edu['studyType']} in {edu['area']} | {edu.get('endDate', '')}")
        lines.append("")

    return "\n".join(lines)


def generate_plain_text(resume: dict, resume_type: str = "default") -> str:
    """Generate plain text resume (good for ATS)"""
    b = resume['basics']

    lines = []

    # Header
    lines.append(b['name'].upper())
    lines.append("=" * len(b['name']))

    # Contact
    contact = []
    if b.get('location'):
        contact.append(f"{b['location']['city']}, {b['location']['region']}")
    for profile in b.get('profiles', []):
        if profile['network'] == 'LinkedIn':
            contact.append(profile['url'].replace('https://', ''))
    if b.get('phone'):
        contact.append(b['phone'])
    if b.get('email'):
        contact.append(b['email'])
    lines.append(" | ".join(contact))
    lines.append("")

    # Summary
    lines.append("PROFESSIONAL SUMMARY")
    lines.append("-" * 20)
    lines.append(get_summary(resume, resume_type))
    lines.append("")

    # Skills
    lines.append("SKILLS")
    lines.append("-" * 20)
    for skill_group in resume.get('skills', []):
        keywords = ", ".join(skill_group['keywords'])
        lines.append(f"{skill_group['name']}: {keywords}")
    lines.append("")

    # Projects
    if resume.get('projects') and resume_type in ['default', 'devops', 'technical_pm']:
        lines.append("PROJECTS")
        lines.append("-" * 20)
        for project in resume['projects']:
            year = project.get('startDate', '')
            lines.append(f"{project['name']} | {project.get('description', '')} [{year}]")
            for highlight in project.get('highlights', []):
                lines.append(f"  * {highlight}")
            if project.get('url'):
                lines.append(f"  * GitHub: {project['url']}")
            lines.append("")

    # Work
    lines.append("PROFESSIONAL EXPERIENCE")
    lines.append("-" * 20)
    for job in resume.get('work', []):
        date_range = format_date_range(job.get('startDate', ''), job.get('endDate', ''))
        lines.append(f"{job['name']} | {job['position']} [{date_range}]")
        lines.append(f"{job.get('location', '')}")
        for highlight in job.get('highlights', []):
            lines.append(f"  * {highlight}")
        lines.append("")

    # Education
    lines.append("EDUCATION")
    lines.append("-" * 20)
    for edu in resume.get('education', []):
        lines.append(f"{edu['institution']}")
        lines.append(f"{edu['studyType']} in {edu['area']} | {edu.get('endDate', '')}")

    return "\n".join(lines)


def generate_html(resume: dict, resume_type: str = "default") -> str:
    """Generate HTML resume (can be converted to PDF)"""
    b = resume['basics']

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{b['name']} - Resume</title>
    <style>
        body {{
            font-family: 'Georgia', serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            line-height: 1.5;
            color: #333;
        }}
        h1 {{
            margin-bottom: 5px;
            font-size: 28px;
        }}
        .contact {{
            color: #666;
            margin-bottom: 20px;
        }}
        h2 {{
            border-bottom: 2px solid #333;
            padding-bottom: 5px;
            margin-top: 25px;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        h3 {{
            margin-bottom: 5px;
            font-size: 16px;
        }}
        .job-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }}
        .date {{
            color: #666;
            font-style: italic;
        }}
        .location {{
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
        }}
        ul {{
            margin-top: 5px;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 5px;
        }}
        .skills-group {{
            margin-bottom: 8px;
        }}
        .skills-group strong {{
            font-weight: bold;
        }}
        .project-link {{
            color: #0066cc;
            font-size: 14px;
        }}
        @media print {{
            body {{
                margin: 0;
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <h1>{b['name']}</h1>
    <div class="contact">
"""

    contact_parts = []
    if b.get('location'):
        contact_parts.append(f"{b['location']['city']}, {b['location']['region']}")
    for profile in b.get('profiles', []):
        if profile['network'] == 'LinkedIn':
            contact_parts.append(f'<a href="{profile["url"]}">{profile["url"].replace("https://", "")}</a>')
    if b.get('phone'):
        contact_parts.append(b['phone'])
    if b.get('email'):
        contact_parts.append(f'<a href="mailto:{b["email"]}">{b["email"]}</a>')

    html += " | ".join(contact_parts)
    html += """
    </div>

    <h2>Professional Summary</h2>
    <p>""" + get_summary(resume, resume_type) + """</p>

    <h2>Skills</h2>
"""

    for skill_group in resume.get('skills', []):
        keywords = ", ".join(skill_group['keywords'])
        html += f'    <div class="skills-group"><strong>{skill_group["name"]}:</strong> {keywords}</div>\n'

    # Projects
    if resume.get('projects') and resume_type in ['default', 'devops', 'technical_pm']:
        html += "\n    <h2>Projects</h2>\n"
        for project in resume['projects']:
            year = project.get('startDate', '')
            html += f"""
    <div class="job-header">
        <h3>{project['name']} | {project.get('description', '')}</h3>
        <span class="date">{year}</span>
    </div>
    <ul>
"""
            for highlight in project.get('highlights', []):
                html += f"        <li>{highlight}</li>\n"
            if project.get('url'):
                html += f'        <li class="project-link">GitHub: <a href="{project["url"]}">{project["url"]}</a></li>\n'
            html += "    </ul>\n"

    # Work Experience
    html += "\n    <h2>Professional Experience</h2>\n"
    for job in resume.get('work', []):
        date_range = format_date_range(job.get('startDate', ''), job.get('endDate', ''))
        html += f"""
    <div class="job-header">
        <h3>{job['name']} | {job['position']}</h3>
        <span class="date">{date_range}</span>
    </div>
    <div class="location">{job.get('location', '')}</div>
    <ul>
"""
        for highlight in job.get('highlights', []):
            html += f"        <li>{highlight}</li>\n"
        html += "    </ul>\n"

    # Education
    html += "\n    <h2>Education</h2>\n"
    for edu in resume.get('education', []):
        html += f"""
    <p><strong>{edu['institution']}</strong><br>
    {edu['studyType']} in {edu['area']} | {edu.get('endDate', '')}</p>
"""

    html += """
</body>
</html>
"""
    return html


def main():
    parser = argparse.ArgumentParser(description="Generate tailored resumes from JSON")
    parser.add_argument("--type", "-t",
                       choices=["default", "devops", "project_manager", "technical_pm"],
                       default="default",
                       help="Resume type/focus")
    parser.add_argument("--format", "-f",
                       choices=["markdown", "html", "txt", "all"],
                       default="all",
                       help="Output format")
    parser.add_argument("--output", "-o",
                       help="Output filename (without extension)")
    parser.add_argument("--source", "-s",
                       default="resume.json",
                       help="Source JSON file")

    args = parser.parse_args()

    # Load resume
    resume = load_resume(args.source)

    # Determine output filename
    base_name = args.output or f"DustinWilliams_Resume_{args.type}"

    # Generate outputs
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    formats_to_generate = ['markdown', 'html', 'txt'] if args.format == 'all' else [args.format]

    for fmt in formats_to_generate:
        if fmt == 'markdown':
            content = generate_markdown(resume, args.type)
            ext = 'md'
        elif fmt == 'html':
            content = generate_html(resume, args.type)
            ext = 'html'
        elif fmt == 'txt':
            content = generate_plain_text(resume, args.type)
            ext = 'txt'

        output_path = output_dir / f"{base_name}.{ext}"
        with open(output_path, 'w') as f:
            f.write(content)
        print(f"Generated: {output_path}")

    print(f"\nResume type: {args.type}")
    print("To convert HTML to PDF, open the HTML file in a browser and print to PDF")


if __name__ == "__main__":
    main()
