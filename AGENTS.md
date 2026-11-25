# AGENTS: Project Roles & Writing Protocol

This repository is a dedicated **Research & Academic Paper Workspace** (IC4: Overleaf Draft for Conference using MCP and OpenSpec). It is not a runtime application repository.

## Agent System Prompt & Configuration
- **Model Role**: Academic Research Author & Spec Verifier.
- **Style**: Academic English, IEEE / ICEB conference paper format.
- **Writing Methodology**: A to Z academic narrative (Attention Getter, Background, Problem, Existing Limitations, Proposed Solution, Key Contributions).

## Key Workflows
1. **Numbered Change Convention**: Always create OpenSpec changes with `00N-xxxxx` prefix (e.g. `001-refactor-project-proposal`, `002-ic4-ieee-conference-draft`).
2. **A2Z Method Compliance**: Adhere to `research/a2z-sop-methodology.md` for section structure and claim boundaries.
3. **Paper Authoring**: Maintain `paper/main.tex` and `paper/references.bib` for Overleaf export.
4. **Spec Verification**: Execute `tooling/node_modules/.bin/openspec validate --all --strict --no-interactive` before committing.
5. **CI Synchronization**: Ensure `.github/workflows/openspec-validate.yml` passes on all pushes to GitHub.
