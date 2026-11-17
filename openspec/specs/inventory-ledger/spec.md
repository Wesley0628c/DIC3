# Inventory Ledger Specification
## Purpose
Maintain a single household's ingredient batches and confirmed usage events consistently.

## Requirements
### Requirement: Valid batch inputs
The system SHALL accept only finite positive quantities, supported units and ISO calendar dates on inventory creation.
#### Scenario: Reject invalid quantity
- **WHEN** a batch is submitted with NaN, infinity, a boolean, zero or a negative quantity
- **THEN** the operation is rejected without inserting a batch.

### Requirement: Atomic confirmed recording
The system SHALL record consumption or waste only after an explicit UI confirmation, and SHALL update stock and event logs in one transaction.
#### Scenario: User cancels
- **GIVEN** a batch with ten units
- **WHEN** the user closes or cancels the usage dialog
- **THEN** its balance remains ten and no usage event is inserted.
#### Scenario: Concurrent overdraft
- **GIVEN** ten units in a batch
- **WHEN** two requests each attempt to consume seven units
- **THEN** at most one request succeeds and the balance never becomes negative.
#### Scenario: Event write failure
- **WHEN** event insertion fails after a tentative stock update
- **THEN** both the balance update and operation receipt are rolled back.

### Requirement: Idempotent confirmed operation
The system SHALL recognize a repeated operation ID with an identical payload and SHALL reject reuse with a changed payload.
#### Scenario: Repeated confirmation
- **WHEN** the same operation ID and quantity are submitted twice
- **THEN** stock is deducted once and one event is retained.
#### Scenario: Stale quantity
- **WHEN** the current balance differs from the quantity shown for confirmation
- **THEN** the operation is rejected and the user is asked to confirm again.

### Requirement: Recorded event analytics
The system SHALL group recorded consumption and waste by ingredient and unit, without interpreting the ratio as proven waste reduction.
#### Scenario: Different physical units
- **WHEN** logs contain quantities in pieces and grams
- **THEN** the quantities are not summed into a shared physical total.
