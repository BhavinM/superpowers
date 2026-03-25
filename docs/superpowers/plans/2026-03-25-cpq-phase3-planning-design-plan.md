# CPQ Superpowers: Phase 3 (Planning & Design) Roadmap

**Goal:** Establish specialized AI Skills to handle the crucial "front-end" of the CPQ implementation lifecycle. CPQ projects often fail because generic requirements miss critical pricing math, constraints, or bundling limitations.

---

### Task 1: The CPQ Business Analyst Skill (`skills/cpq-business-analyst/SKILL.md`)
- **Purpose:** Teaches the AI how to act as a senior CPQ Business Analyst to prevent "garbage in, garbage out" implementations.
- **Functionality:** Instead of blindly accepting generic prompts like "Add a 10% discount", the Agent will cross-examine the user with a strict questionnaire framework depending on the request type:
  - **For Product/Bundling Requests:** "Are there min/max option limits?", "Do we need inclusion/exclusion Constraint Rules?"
  - **For Pricing Requests:** "Is this applied to the Base Price, Net Price, or Customer Price?", "Does this impact the Price Waterfall?", "Is it tier-based, volume-based, or term-based?"
  - **For Quoting Requests:** "Will this require updates to the Word Document Template?", "Are Advanced Approvals triggered?"
- **Output:** A highly detailed `.agents/requirements/Req_CPQ_001.md` document that leaves no ambiguity.

### Task 2: The CPQ Solutions Architect Skill (`skills/cpq-solutions-architect/SKILL.md`)
- **Purpose:** Translates BA Requirements into a functional CPQ Solution Design.
- **Functionality:** Determines the most optimal, standard CPQ architecture (e.g., "Solve this using a Price Matrix, not an Apex Callback").
- **Output:** A formal Solution Design Spec (FSD).

### Task 3: The CPQ Technical Architect Skill (`skills/cpq-technical-architect/SKILL.md`)
- **Purpose:** Converts the high-level Solution Design into a rigid, low-level Technical Design Document (TDD). 
- **Functionality:** Defines exact API names, field types, required SOQL structure, and JSON data tree schema. This is the exact blueprint handed directly to the Implementation Engine.
- **Output:** A formal Technical Design Spec (TDD) holding all schema mappings.

### Task 4: The CPQ QA/Test Architect Skill (`skills/cpq-qa-architect/SKILL.md`)
- **Purpose:** Translates the BA requirements into mathematically precise Test Cases for the automated pipeline.
- **Functionality:** Designs exact positive/negative execution scenarios (e.g., "Add Laptop ID 123 with Option X; Assert Net Price = $900"). Supplies the precise parameters needed to fuel `cpq_cart_tester.py` without humans having to invent the test data.
- **Output:** A Master Test Plan document mapping use cases to expected CPQ Cart math.

### Task 5: The End-to-End Master Workflow
- **Purpose:** Update the overarching documentation and workflows to connect the entire journey into a seamless pipeline.
- **Flow:** `Business Analyst` (Elicits Needs) ➔ `Solutions Architect` (Functional approach) ➔ `Technical Architect` (Low-level specs) ➔ `QA Architect` (Test Plans) ➔ `Autonomous Builder` (Deploys data/code) ➔ `Cart Tester` (Validates math) ➔ `Environment Migrator` (Syncs to Prod).
