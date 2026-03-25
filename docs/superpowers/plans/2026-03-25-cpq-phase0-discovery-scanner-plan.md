# CPQ Phase 0: The Holistic Environmental Scanner Plan

**Goal:** Establish a robust "Phase 0" Discovery Agent that provides the Project Manager and Solutions Architect personas with complete, omniscient context of the given Salesforce CPQ environment BEFORE any designs are formulated or code is written.

---

## Architectural Components

### 1. The Python Scanner (`scripts/discovery/cpq_environment_scanner.py`)
This standalone script executes an exhaustive array of `sf data query` commands to dump the current state of CPQ into a markdown text file. 
- **Relational Data Scanned:** It queries for currently Active Price Lists, Price Rules, Constraints, and Product families.
- **Apex Code Scanned:** It queries the Salesforce `ApexClass` table to discover any existing implementations of the `Apttus_Config2.CustomPricingCallback3`, `ValidationCallback`, or `ProductFilterCallback` interfaces.
- **Metadata Scanned:** It identifies any foundational Custom Fields added to the `Apttus_Config2__LineItem__c` and `Apttus_Proposal__Proposal__c` objects.

### 2. The RAG Output Report (`.agents/reports/CPQ_Discovery_Report.md`)
The Python script formats everything it queried into a beautiful Markdown artifact. 
Because Markdown is natively parsed by Large Language Models, this document serves as perfectly formatted RAG (Retrieval-Augmented Generation) context.
- **Example Output Structure:**
  ```markdown
  ## Active Apex Pricing Callbacks
  - `MarginPricingCallback` (CustomPricingCallback3)
  
  ## Active Price Lists
  - 'Standard Price List' (ID: a0Z...)
  - 'EMEA Enterprise' (ID: a0Z...)
  
  ## Custom Line Item Fields
  - `Discount_Override__c`
  - `Regional_Margin__c`
  ```

### 3. End-to-End Workflow Integration
We must integrate this into our 6-Persona Agency architecture:
1. **The Orchestrator:** Update `.agents/workflows/cpq-e2e-project.md` to add `Phase 0: Environment Scan`. The AI will execute `python scripts/discovery/cpq_environment_scanner.py` before generating Epics.
2. **The Personas:** Update `skills/cpq-solutions-architect/SKILL.md` forcing the AI to silently read `.agents/reports/CPQ_Discovery_Report.md` so its Technical Design Document perfectly matches existing SObject limits and Pricing Callbacks, preventing it from inventing a secondary Pricing Callback when one already exists.
