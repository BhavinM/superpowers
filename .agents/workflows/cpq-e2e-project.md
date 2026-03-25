---
description: The ultimate End-to-End Orchestrator. Trigger this with a basic business requirement to unleash the entire 6-Persona AI CPQ Agency (PM ➔ BA ➔ SA ➔ TA ➔ QA ➔ Builder ➔ Migrator).
---

# End-to-End Virtual CPQ Agency Workflow

When asked to run an end-to-end CPQ implementation, execute the following steps precisely in chronological order.

## Phase 0: Discovery & Context Gathering
1. **[Holistic Scanner]** // turbo-all
   Run `python scripts/discovery/cpq_environment_scanner.py` to rigorously map the current org's CPQ metadata, dependencies, and rules. 
   This automatically generates `.agents/reports/CPQ_Discovery_Report.md`. Provide this exact file path to the Architects when assigning them tasks.

## Phase 1: Agile Setup & Business Elicitation
1. **[Project Manager]** Read the user's initial prompt. Establish the high-level Epic in your notes.
2. **[Business Analyst]** Call the `using-cpq-business-analyst` skill to interrogate the user. Ask the probing questions regarding Bundling, Pricing Waterfalls, and Output Documents. DO NOT PROCEED until answered.
3. Write the resulting answers into `/docs/specs/CPQ_BRD.md`.

## Phase 2: Functional & Technical Architecture
1. **[Solutions Architect]** Pass the `CPQ_BRD.md` to the `using-cpq-solutions-architect` skill. Determine if this should be solved via declarative matrices or Apex Callbacks. Write `/docs/specs/CPQ_FSD.md`.
2. **[Technical Architect]** Pass the FSD to the `using-cpq-technical-architect` skill to convert it into exact JSON payloads, SOQL Discovery queries, and Salesforce API names. Write `/docs/specs/CPQ_TDD.md`.
3. **[QA Test Architect]** Pass the BRD and TDD to the `using-cpq-qa-architect` skill to write mathematically precise testing arrays (Inputs -> Outputs). Write `/docs/specs/CPQ_TestPlan.md`.

## Phase 3: Autonomous Implementation & Testing
1. **[Autonomous Builder]** Call the `/cpq-autonomous-implementation` workflow. Execute `scaffold_cpq_approvals.py` for approval logic or `cpq_data_builder.py` for pricing rules, using the exact blueprints dictated by the Technical Architect's TDD.
2. **[Cart API Tester]** // turbo-all
   Use the parameters defined in `CPQ_TestPlan.md` to run `python scripts/testing/cpq_cart_tester.py`. Assure the AI that the mathematical output strictly matches business expectations.

## Phase 4: Governance & Performance Limits Analysis
1. **[Performance Profiler]** // turbo-all
   Extract the generating Debug Log ID from the tester's test-run. Execute `python scripts/testing/cpq_performance_analyzer.py --log_id <ID>` to assert that the `CustomPricingCallback` Apex loops did not violate Salesforce 10,000ms CPU or SOQL 101 limits.
2. If limits are breached, fail the task and force the Technical Architect to refactor the pricing logic.

## Phase 5: Production Release
1. **[Migration Engine]** // turbo-all
   Mandate a local pre-deployment backup via the `cpq_rollback.py` protocols.
   Run `python scripts/migration/cpq_env_migrator.py --mode delta` to push the perfectly verified Schema Metadata and Relational Data to the Target Sandbox.
2. Report total success back to the Agile Project Manager!
