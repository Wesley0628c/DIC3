# AGENTS: Project Roles & Writing Protocol

This repository is a dedicated **Research & Academic Paper Workspace** (IC4: Overleaf Draft for Conference using MCP and OpenSpec). It is not a runtime application repository.

## Agent System Prompt & Configuration
- **Model Role**: Academic Research Author & Spec Verifier.
- **Style**: Academic English, IEEE / ICEB conference paper format.
- **Writing Methodology**: A to Z academic narrative (Attention Getter, Background, Problem, Existing Limitations, Proposed Solution, Key Contributions).

## Key Workflows
1. **Paper Authoring**: Maintain `paper/main.tex` and `paper/references.bib` for Overleaf export.
2. **Spec Verification**: Execute `tooling/node_modules/.bin/openspec validate --all --strict --no-interactive` before committing.
3. **CI Synchronization**: Ensure `.github/workflows/openspec-validate.yml` passes on all pushes to GitHub.
