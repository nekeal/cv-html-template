# CV Template

A simple and customizable CV template generator that renders HTML and PDF versions of your resume from context files.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) for Python package management
- [just](https://github.com/casey/just) for running commands
- Google Chrome (for PDF generation)

### Using as a GitHub Template

This repository is set up as a GitHub template. To use it:

1. Click the **"Use this template"** button on the repository page
2. Create a new repository with your desired name
3. Clone your new repository locally
4. Edit `src/cv/common_context.py` and `src/cv/context.py` with your information
5. Run `just html` to generate your CV

## Usage

### Editing Your CV Content

The CV content is stored in Python context files:

1. **Common Context**: Edit `src/cv/common_context.py` to modify personal details that remain consistent across all versions:
   - Name, title, contact information
   - Summary/profile
   - Education
   - Certificates
   - Languages

2. **Specific Context**: Edit `src/cv/context.py` (default) or create company-specific context files to customize:
   - Work experience
   - Skills
   - Other experiences/projects

### Available Commands

This project uses `just` as a command runner. Here are the available commands:

```bash
# Create a new company-specific context file
just new company_name

# Render HTML and PDF for a specific company
just render company_name

# Commit changes for a specific company application
just commit company_name

# Generate HTML using the default context
just html

# Generate PDF using the default context
just pdf

# Format code with ruff
just autoformat
```

### Workflow for Job Applications

1. Create a new company-specific context file:
   ```bash
   just new acme_corp
   ```

2. Edit the newly created context file in `YYYY/acme_corp/context.py` to tailor your CV for the company.

3. Render the CV for the specific company:
   ```bash
   just render acme_corp
   ```

4. Commit your changes:
   ```bash
   just commit acme_corp
   ```

### Customizing HTML Template

The HTML template is located at `templates/basic/cv_template.html.j2`. You can modify this file to change the layout and styling of your CV.

## Utilities

The project includes utility functions like `b()` for bolding text in `src/cv/utils.py`. You can add more utility functions as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
