# Context
IC4 builds on DIC3 by converting the refactored project proposal into an IEEE conference paper draft for Overleaf and establishing spec validation on GitHub.

# Goals / Non-Goals
## Goals
- Provide a complete, self-contained LaTeX IEEE conference paper draft.
- Maintain honest research claims (planned evaluation vs. measured findings).
- Provide export scripts and zip packages for instant Overleaf compilation.
- Implement GitHub Actions for automated OpenSpec strict validation.

## Non-Goals
- Falsifying or reporting unmeasured physical experiments.
- Submitting directly to conference submission portals (drafting and staging only).

# Decisions
- Place all LaTeX paper materials in `paper/` to maintain clean repository separation.
- Use standard IEEEtran conference format (`\documentclass[conference]{IEEEtran}`).
- Maintain citations in standard BibTeX (`references.bib`) referencing official sources (R1–R7, T1, S1).
- Package the paper bundle as a zip archive for Overleaf users without requiring local LaTeX installations.
- Use GitHub Actions with Node 22.x to run strict OpenSpec validation.

# Workflow
OpenSpec Change Proposal → LaTeX & BibTeX Paper Draft → Local Strict Validation → GitHub Actions CI Configuration → Overleaf Bundle Export.

# Verification
1. `openspec validate --all --strict --no-interactive` exits with code 0.
2. `paper/main.tex` and `paper/references.bib` are syntax-checked and free of unresolved cross-references.
3. Zip package can be unpacked and directly imported into Overleaf.
