# CPQ Superpowers: Phase 2 Enhancements Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Elevate the autonomous CPQ toolchain from "Implementation & Building" to "Testing, Sandbox Migration, and Validation", addressing the most complex bottlenecks in enterprise CPQ rollouts.

---

### Conceptual Overview
Phase 1 gave the AI the ability to discover data, write code/config, and deploy. Phase 2 gives the AI the ability to test those changes autonomously, migrate them across environments, and validate document templates.

---

### Task 1: Comprehensive Environment Migration Engine (`scripts/migration/cpq_env_migrator.py`)
Moving full CPQ architectures across Salesforce Sandboxes requires capturing the full tapestry of CPQ Data intertwined with Salesforce Core Metadata.
- **Goal:** A comprehensive Python migration engine supporting **Full, Selective, and Delta (Incremental)** migrations:
  1. **Metadata Sync Phase:** Autonomously targets and synchronizes standard Salesforce architecture tied to the CPQ deployment. This includes deploying Custom Objects, Custom Fields, Custom Metadata Types (`__mdt`), Custom Settings, CPQ Object Page Layouts, CPQ User Permission Sets & Roles, Email Templates (for quotes), and CPQ-related Flows.
  2. **Data Sync Phase:** Utilizes the SF Bulk API to export the massive `Apttus_Config2` relational data trees and sequentially upsert them into the Target Org. This includes automatically migrating Product Hierarchies, Field Expressions, Constraint Rules, Attribute Rules, Pricing Rules, Price Matrices, and Incentives while dynamically resolving foreign key relationships.
  3. **Delta & Selective Tracking Mode:** Instead of a monolithic full-database sync every time, the engine supports targeted deployment triggers. It accepts explicitly listed record IDs (`--records "Id1,Id2"`) for focused bug fixes, or differential timestamp queries (`--since "2026-03-01T00:00:00Z"`) to migrate only configurations modified in the current sprint.
- **AI Integration:** The AI can use this to say, "Perform a Delta migration of any Price Rules or Constraint Rules modified in the last 24 hours from Sandbox UAT, and sync their related Custom Fields to Production."

### Task 2: Automated Cart API Tester (`scripts/testing/cpq_cart_tester.py`)
Testing CPQ pricing rules manually by clicking through the UI takes engineers hours. 
- **Goal:** A Python Testing Framework that sequentially triggers the standard **Conga CPQ REST APIs** (or `Apttus_CPQApi` global methods via SFDX Apex invocation) to mathematically prove the AI's newly deployed pricing configurations actually work.
- **Supported API Sequence:**
  1. **Create Cart API:** (`Apttus_CPQApi.CPQ.CreateCartRequestDO`) - Spins up a headless cart for a Test Proposal.
  2. **Add Products API:** (`Apttus_CPQApi.CPQ.AddMultiProductRequestDO`) - Supports inserting Standalone products and deeply nested Bundles with Options.
  3. **Update Price API:** (`Apttus_CPQApi.CPQ.UpdatePriceRequestDO`) - Forces the execution of Price Rules, Constraint Rules, Matrices, and CustomPricingCallbacks.
  4. **Finalize Cart API:** (`Apttus_CPQApi.CPQ.FinalizeCartRequestDO`) - Synchronizes the pricing totals back to the Quote object.
- **AI Validation:** The AI can instruct the tool: "Invoke `cpq_cart_tester.py`, create a cart for Proposal P-001, add Laptop Product ID, run UpdatePrice, and assert that the final NetPrice strictly equals $900.00."

### Task 3: Conga Composer Template Validator (`scripts/validation/conga_template_analyzer.py`)
Deploying `.docx` quote templates that contain invalid or misspelled merge fields (e.g., `{{Apttus_Proposal__Proposal__c.NonExistentField__c}}`) causes painful runtime errors when generating PDFs.
- **Goal:** A script that parses binary `.docx` files locally, extracts all `{{ }}` merge tags, queries the Salesforce org's SObject schema, and warns the AI of any invalid fields BEFORE deploying the template to Salesforce.

### Task 4: Multi-Currency & Localization Builder (`scripts/sfcore/cpq_translation_builder.py`)
- **Goal:** A script that automatically maps and generates valid `Translation Workbench` XML files and standard CPQ Label overrides, drastically accelerating global, multi-currency CPQ deployments.
