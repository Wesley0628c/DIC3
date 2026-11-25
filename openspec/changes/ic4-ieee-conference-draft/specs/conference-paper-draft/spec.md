## ADDED Requirements
### Requirement: IEEE conference format
The paper draft SHALL provide a LaTeX document using the standard IEEEtran conference class with title, abstract, index terms, six core sections, and BibTeX citations.
#### Scenario: Inspect LaTeX structure
- **WHEN** the reviewer checks `paper/main.tex` and `paper/references.bib`
- **THEN** the document compiles in standard IEEEtran mode and resolves all citations.

### Requirement: Academic evidence boundary
The paper draft SHALL strictly distinguish proposed architectures and planned evaluations from empirically proven findings.
#### Scenario: Check claim boundaries
- **WHEN** the reviewer reads the abstract, contributions, and experimental design sections
- **THEN** experimental evaluations and waste reduction effects are designated as proposed/planned rather than completed achievements.

### Requirement: Algorithm and workflow formalization
The paper draft SHALL formalize the Food Guardian decision workflow and Algorithm 1 within standard LaTeX algorithmic formatting.
#### Scenario: Inspect Algorithm 1
- **WHEN** the reviewer reviews Section III of the paper
- **THEN** Algorithm 1 details input, output, and numbered execution lines corresponding to project specifications.

### Requirement: Overleaf export packaging
The submission SHALL provide an automated mechanism and archive for importing into Overleaf with zero manual configuration.
#### Scenario: Overleaf archive readiness
- **WHEN** the export archive is inspected
- **THEN** all necessary LaTeX sources, bibliographies, and assets are present.

### Requirement: GitHub Actions CI automation
The repository SHALL maintain an automated GitHub Actions workflow for validating OpenSpec specifications on push and pull requests.
#### Scenario: CI execution
- **WHEN** commits are pushed to the GitHub repository
- **THEN** GitHub Actions runs strict OpenSpec validation successfully.
