# CPQ Superpowers: Phase 2 Enhancements Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Elevate the autonomous CPQ toolchain from "Implementation & Building" to "Testing, Sandbox Migration, and Validation", addressing the most complex bottlenecks in enterprise CPQ rollouts.

---

### Conceptual Overview
Phase 1 gave the AI the ability to discover data, write code/config, and deploy. Phase 2 gives the AI the ability to test those changes autonomously, migrate them across environments, and validate document templates.

---

### Task 1: Environment Migration Engine (`scripts/migration/cpq_env_migrator.py`)
Moving full CPQ architectures across Salesforce Sandboxes usually requires expensive 3rd-party tools because it involves both massive relational Data and scattered Custom Metadata.
- **Goal:** A comprehensive 2-stage Python migration engine:
  1. **Metadata Sync Phase:** Autonomously retrieves Custom Objects and Custom Fields (especially custom fields newly added directly to core Conga objects like `Apttus_Config2__LineItem__c` or standard objects like `Opportunity`) from the Source Org and deploys them to the Target Org to ensure schema parity.
  2. **Data Sync Phase:** Utilizes the SF Bulk API to export `Apttus_Config2` relational data trees and upserts them sequentially into the Target Org, automatically resolving foreign key relationships (like Product Options to Product).
- **AI Integration:** The AI can use this to say, "Migrate the Laptop Pricing Product Catalog and all its custom attribute fields from Sandbox UAT to Production."

### Task 2: Automated Cart API Tester (`scripts/testing/cpq_cart_tester.py`)
Testing CPQ pricing rules manually by clicking through the UI takes engineers hours. 
- **Goal:** A tool that the AI can use to instantly verify if its newly created Price Rules actually work. The script creates a test Proposal, spins up a Cart via the Conga CPQ API, adds specific products, calculates pricing, and validates if the `NetPrice` matches the expected outcome.

### Task 3: Conga Composer Template Validator (`scripts/validation/conga_template_analyzer.py`)
Deploying `.docx` quote templates that contain invalid or misspelled merge fields (e.g., `{{Apttus_Proposal__Proposal__c.NonExistentField__c}}`) causes painful runtime errors when generating PDFs.
- **Goal:** A script that parses binary `.docx` files locally, extracts all `{{ }}` merge tags, queries the Salesforce org's SObject schema, and warns the AI of any invalid fields BEFORE deploying the template to Salesforce.

### Task 4: Multi-Currency & Localization Builder (`scripts/sfcore/cpq_translation_builder.py`)
- **Goal:** A script that automatically maps and generates valid `Translation Workbench` XML files and standard CPQ Label overrides, drastically accelerating global, multi-currency CPQ deployments.
