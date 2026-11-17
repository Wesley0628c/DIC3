# Context
The local DIC3 tree contains user edits and research summaries. Preserve them. Source reference: Chen-Fanny/Food-Guardian commit e53dfdc, MIT; provenance recorded in THIRD_PARTY.md.

# Goals / Non-Goals
Deliver reviewable course chapters, executable local flows, traceable requirements and fresh test results. Do not fabricate human labels, cloud results or household waste reduction. Multi-household access and full cold-chain reasoning are future work.

# Decisions
1. Reuse reference service boundaries with attribution rather than treating it as original DIC3 code.
2. Default to offline, optional cloud providers explicitly selected. Structured serving controls keep quantities deterministic.
3. Missing label dates become review, addressing an unsafe gap between the original proposal and reference implementation.
4. SQLite IMMEDIATE transactions serialize deductions; optional operation IDs prevent repeated confirmed payloads, and UI provides IDs.
5. Separate dataset fixture checks, static source metadata and cloud tool selection. Retain NOT_RUN status for missing evidence.
6. Keep original bitmap infographic as historical material; current Mermaid diagrams and references are authoritative for this version.

# Alternatives
Full RAG install by default adds embedding downloads and runtime cost; make it optional. Automatic batch deduction from generated recipes requires allocation and confirmation logic not delivered here; keep actual usage confirmation in the inventory UI.

# Risks / Trade-offs
Knowledge fixtures are not validated food-safety rules. Name-based exclusions do not guarantee allergen safety. Same quantities after an intervening edit cannot be detected by quantity-only stale checks. Recipe suggestions share inventory and must be assessed independently.

# Migration Plan
Add schema table idempotently without deleting existing data. Load synthetic batches only on explicit seed command into an empty target database. Existing DIC3 documents remain. Run validation before treating this change as ready.

# Open Questions
Which model and credentials will the user supply for live tests? Where are the original proposal/PPT, local product rules and independently reviewed labels? Track these separately in docs/remaining-work.md.
