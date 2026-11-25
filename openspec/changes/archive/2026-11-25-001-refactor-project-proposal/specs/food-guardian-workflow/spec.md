## ADDED Requirements
### Requirement: Inventory context
The proposed system SHALL retrieve ingredient batches with quantities, units, label dates, opening state and storage information before making actionable recommendations.
#### Scenario: Missing storage information
- **WHEN** information required by an applicable storage rule is absent
- **THEN** the system requests clarification and does not invent missing values.

### Requirement: Quantity and constraints
The proposed system SHALL scale recipe requirements to the requested servings, preserve unknown unit conversions and respect explicit exclusions.
#### Scenario: Unconvertible stock
- **WHEN** a recipe requires grams but the batch only records an unspecified pack
- **THEN** the quantity remains unknown and is not described as sufficient.
#### Scenario: Ingredient shortage
- **WHEN** available eligible quantity is less than the requirement
- **THEN** the output shows the shortage and does not label the dish immediately executable.
#### Scenario: Explicit exclusion
- **WHEN** the user excludes an ingredient
- **THEN** a recipe requiring that ingredient is not recommended as executable.

### Requirement: Explainable date priority
The proposed system SHALL distinguish date reminders from storage-rule checks and SHALL reveal the grounds for priority.
#### Scenario: Near-date batch
- **WHEN** an ingredient is close to its recorded date
- **THEN** priority is shown as a management reminder rather than a guarantee of food safety.

### Requirement: Confirmed updates
The proposed system SHALL update inventory only after explicit confirmation of actual usage, with a consistent transaction and operation identifier.
#### Scenario: Cancellation
- **WHEN** the user cancels the confirmation
- **THEN** stock and usage records remain unchanged.
#### Scenario: Repeated confirmation
- **WHEN** the same confirmed operation identifier is received again
- **THEN** the same operation does not deduct stock twice.
#### Scenario: Failed update
- **WHEN** inventory or event writing fails
- **THEN** the transaction is rolled back and the user is asked to confirm again.

### Requirement: Planned evaluation
The proposal SHALL specify comparable baselines, fixed conditions and explicit metric denominators.
#### Scenario: Compare methods
- **WHEN** the tool-based workflow is evaluated against an inventory-conditioned model
- **THEN** both methods use the same inventory snapshot, rules and reference date.
