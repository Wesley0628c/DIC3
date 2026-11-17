# Meal Planning Specification
## Purpose
Provide explainable candidate dishes with explicit stock, date and quantity limitations.

## Requirements
### Requirement: Quantity validation
The system SHALL scale recipe requirements to the target servings and SHALL convert units only within a known physical dimension.
#### Scenario: Incompatible units
- **GIVEN** milk recorded as one pack and a recipe requiring millilitres
- **WHEN** the recipe is evaluated
- **THEN** the requirement is unknown rather than sufficient.
#### Scenario: Known conversion
- **GIVEN** one litre of eligible milk
- **WHEN** a recipe requires five hundred millilitres
- **THEN** the tool reports one thousand millilitres available and the requirement is sufficient.

### Requirement: Preliminary date triage
The system SHALL exclude blocked or review batches from automatic matching, and SHALL never represent eligibility as food safety certification.
#### Scenario: Missing date
- **WHEN** a batch has no recorded label date
- **THEN** it is classified as review with a request to supplement information.
#### Scenario: Passed Use By
- **WHEN** a batch is past its recorded Use By date
- **THEN** it is blocked from automatic recommendation.
#### Scenario: Passed Best Before
- **WHEN** a batch is past its recorded Best Before date
- **THEN** it is marked review and not automatically selected.

### Requirement: Date reminders
The system SHALL distinguish missing dates, passed dates, dates within an inclusive threshold and later dates.
#### Scenario: Threshold boundary
- **WHEN** a batch date is exactly the configured number of days after the reference date
- **THEN** it receives an expiring-soon reminder.

### Requirement: Explicit preferences and evidence
The system SHALL filter recipes containing excluded ingredients and SHALL preserve shortage and unknown flags regardless of ranking mode.
#### Scenario: Expiry first with shortage
- **WHEN** an urgent recipe has insufficient eggs
- **THEN** expiry priority does not change its quantity status to sufficient.
#### Scenario: Excluded ingredient
- **WHEN** the user explicitly excludes eggs
- **THEN** no recipe requiring eggs is returned.
