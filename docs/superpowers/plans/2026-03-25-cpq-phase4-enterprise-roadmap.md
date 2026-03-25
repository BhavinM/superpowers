# CPQ Superpowers: Phase 4 (Enterprise Governance & Performance)

**Goal:** Establish enterprise-grade "Day 2 Operations" capabilities including performance profiling, rollback safety mechanisms, and Advanced Approvals scaffolding to bulletproof massive CPQ deployments.

---

## Architectural Components

### Task 1: Autonomous Rollback Engine (`scripts/migration/cpq_rollback.py`)
- **Purpose:** Provide an emergency 'Undo' mechanism if a deployed Pricing configuration negatively impacts production quoting speed or margin thresholds.
- **Functionality:** 
  - Before `cpq_env_migrator.py` executes a Delta Migration, it generates a pre-deployment snapshot (JSON states + XML schema) of the impacted CPQ Data.
  - If a failure is detected, the AI (or a human PM) runs `python scripts/migration/cpq_rollback.py --deployment-id <ID>`.
  - The framework issues exact Bulk API Delete and Upsert commands to instantly revert the environment to the last recorded green state.

### Task 2: Apex CPU & Performance Limit Profiler (`scripts/testing/cpq_performance_analyzer.py`)
- **Purpose:** Ensure that complex pricing matrices and custom Apex Callbacks do not breach Salesforce's 10,000ms CPU limits or 101 SOQL limits on 500+ line-item enterprise carts.
- **Functionality:** 
  - Works iteratively alongside the Automated Cart API Tester (`cpq_cart_tester.py`).
  - Instructs the SFDX CLI to pull the resulting Developer Debug Logs.
  - Parses the heap size, SOQL queries consumed, and raw Apex CPU time specifically consumed by `CustomPricingCallback3` operations.
  - The AI halts deployment immediately and warns the Technical Architect if the limits threshold breaches 80% (8,000ms CPU).

### Task 3: Advanced Approvals Scaffolder (`scripts/sfcore/scaffold_cpq_approvals.py`)
- **Purpose:** Automate the highly repetitive, multi-step logic creation required for Conga Advanced Approvals.
- **Functionality:** Given a simple JSON payload (`"Approver": "VP Sales", "Condition": "Discount > 30%"`), this python script scaffolds the complex relational `Apttus_Approval__Approval_Process__c`, `Apttus_Approval__Approval_Rule__c`, and Step records into SFDX Data Tree format for instantly insertable approval matrices.

### Task 4: Technical Debt Analyzer
- **Purpose:** Eradicate poor developer practices from mature CPQ environments.
- **Functionality:** Updates the Phase 0 Discovery Scanner (`cpq_environment_scanner.py`) to actively regex-search for **hardcoded Salesforce IDs** (15 or 18-character strings starting with `01t`, `001`, `a0Z`, etc.) deeply embedded inside Price Rules, Formula Expressions, and active Apex Callbacks.
- **Workflow Integration:** The scanner flags these strings as "Technical Debt". The Solutions Architect persona is forced to read this report and mandate rewriting the bad code using Custom Metadata Types (`__mdt`) during its Design Phase.
