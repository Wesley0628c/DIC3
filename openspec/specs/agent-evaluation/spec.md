# Agent and Evaluation Specification
## Purpose
Separate deterministic tool behavior, model orchestration and research evidence.

## Requirements
### Requirement: Read-only model tools
The system SHALL expose only known read-only inventory, knowledge, safety or recipe tools to language models.
#### Scenario: Unknown mutation tool
- **WHEN** a model requests a delete-inventory or arbitrary SQL tool
- **THEN** it is rejected without changing SQLite.

### Requirement: Explicit operating modes
The UI SHALL default to offline operation and SHALL label local keyword routing separately from cloud model inference.
#### Scenario: No API key
- **WHEN** the application starts without credentials
- **THEN** inventory, reminders, recipe quantity checking and local routing remain available.
#### Scenario: Cloud failure
- **WHEN** the selected cloud provider fails
- **THEN** the error is displayed without silently presenting an offline answer as model output.

### Requirement: Evidence limits
The evaluation SHALL use fixed reference dates and SHALL distinguish deterministic checks, source metadata readiness and live tool selection.
#### Scenario: Offline multi-tool case
- **WHEN** a test requires actual cloud model orchestration but the suite is run offline
- **THEN** its status is NOT_RUN rather than PASS.
#### Scenario: Trace selection is correct
- **WHEN** a live response calls all expected tools
- **THEN** only tool selection is automatically scored; factual completion and groundedness remain pending human review.

### Requirement: Proposal traceability
The repository SHALL provide Introduction, Related Work, references, an architecture, flowchart, numbered pseudocode and requirement-to-implementation mapping.
#### Scenario: Review proposal
- **WHEN** a reviewer follows docs/proposal.md
- **THEN** all required chapters and the current validation report are reachable.
