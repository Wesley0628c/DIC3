# Why
IC4 requires drafting an IEEE two-column conference paper based on the Food Guardian project proposal, managing specifications with OpenSpec, and providing seamless deployment to Overleaf and GitHub.

# What Changes
- Create an IEEEtran-compliant LaTeX conference draft in `paper/main.tex` and `paper/references.bib`.
- Formalize system architecture, flowchart, and Algorithm 1 into academic conference figures, tables, and algorithmic environments.
- Define the `conference-paper-draft` capability in OpenSpec to ensure strict compliance with academic standards and evidence boundaries.
- Set up a GitHub Actions workflow (`.github/workflows/openspec-validate.yml`) for automated strict OpenSpec validation upon every push/PR.
- Provide a ready-to-import Overleaf bundle (`paper/ieee-food-guardian-overleaf.zip`).

# Capabilities
## New Capabilities
- conference-paper-draft: IEEE conference draft structure, Overleaf packaging, and GitHub CI workflow.

## Modified Capabilities
None.

# Impact
Adds academic paper sources under `paper/`, GitHub Actions workflow under `.github/workflows/`, and new OpenSpec tracking. Does not alter underlying DIC3 proposal documentation.
