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
- **Purpose:** Translates the BA Requirements into native Conga CPQ technical constructs.
- **Functionality:** Reads the BA's requirement and determines the most optimal, standard CPQ architecture to solve it.
  - Maps requirements to standard Conga components (e.g., determining a *Price Matrix* is better than writing an *Apex Pricing Callback*).
  - Identifies which Custom Fields, Metadata, or Salesforce Core Flows are required.
- **Output:** A formal `CPQ_Technical_Design.md` that serves as a rigid blueprint for the Builder tools.

### Task 3: The End-to-End Master Workflow
- **Purpose:** Update the overarching documentation and workflows to connect the entire journey into a seamless pipeline.
- **Flow:** `Business Analyst` (Elicits needs) ➔ `Solutions Architect` (Designs the schema) ➔ `Autonomous Builder` (Deploys the data/code) ➔ `Cart Tester` (Asserts the math) ➔ `Environment Migrator` (Syncs to Prod).
