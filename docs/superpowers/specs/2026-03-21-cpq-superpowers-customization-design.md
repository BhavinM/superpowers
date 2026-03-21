# CPQ Superpowers Customization Design (Conga Focus)

## Goal
Establish a structured, extensible process (via superpowers skills) for CPQ implementations (New, Delta, Migration, Bug Fix, Maintenance). The system will initially support Conga CPQ on Salesforce, with the architecture built to easily accommodate future CPQ engines (e.g., Salesforce CPQ) without breaking existing workflows.

## Architecture: Router + Domain Hybrid Model

The architecture decouples the routing logic from the highly specialized CPQ implementation instructions.

### 1. Core Router Skill (`skills/using-cpq-superpowers/SKILL.md`)
Acts as the single entry point gateway for any CPQ-related task.
- **Responsibility:** Determine the CPQ Provider (e.g., Conga) and the Lifecycle Phase (e.g., Migration).
- **Behavior:** If context is missing, it interrogates the user. Once context is clear, it permanently routes the agent to read the corresponding subdomain skill explicitly before any creative or implementation work begins.

### 2. Provider Subdirectories (`skills/using-cpq-superpowers/providers/conga/`)
Contains highly focused sub-skills for specific lifecycle tasks to provide rigid instructions for the agent.
- `migration.md`: Instructions for migrating from other CPQs (auditing current rules, mapping attributes, ensuring parity).
- `new-implementation.md`: greenfield project setup, core metadata structuring.
- `delta-changes.md`: Safely updating existing configurations (e.g., adding a new product line or tweaking a price rule).
- `maintenance.md`: Upgrading packages, auditing limits, or refactoring.
- `bug-fixing.md`: Troubleshooting CPQ specific issues (e.g., cart pricing calculation errors, callback failures).

## Data Flow / User Experience

1. **User Request:** "Help me migrate old pricing rules to Conga CPQ."
2. **Skill Activation:** The agent loads the active skills and invokes `using-cpq-superpowers`.
3. **Routing:** The Router explicitly notes the context: `Provider=Conga`, `Lifecycle=Migration`.
4. **Delegation:** The agent reads `skills/using-cpq-superpowers/providers/conga/migration.md`.
5. **Execution:** The agent strictly follows the migration process (e.g., auditing, mapping, generating Apex callback classes, validation) before invoking `writing-plans`.

## Verification & Extensibility

**Testing the Design:** We will verify this by building a test request for a Conga Migration, ensuring the router correctly hands off to the migration document, and the migration document provides the necessary CPQ caveats.

**Extensibility:** Adding a new provider (e.g., Salesforce CPQ) requires ZERO changes to Conga skills. It simply requires creating the `providers/sfcpq/` directory and adding a minimal routing rule to `SKILL.md`.
