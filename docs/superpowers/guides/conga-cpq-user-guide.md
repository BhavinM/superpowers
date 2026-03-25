# Autonomous Conga CPQ: Step-by-Step User Guide

Welcome to the Autonomous Conga CPQ Implementer! This guide explains how to leverage your AI Agent and the underlying Python toolchain to automatically build, configure, and deploy Conga CPQ tasks natively in Salesforce using simple natural language.

---

## The Core Concept

Instead of clicking through dozens of Salesforce screens to configure Price Lists, Constraint Rules, or writing Apex Callbacks from scratch, you provide a plain English requirement to this AI Agent. The AI will autonomously:
1. **Query** your Salesforce org to find the right Data IDs (`cpq_discover.py`).
2. **Generate** the configuration or code (`cpq_data_builder.py` / `scaffold_cpq_callback.py`).
3. **Deploy** the changes back to Salesforce (`cpq_deploy.py`).

---

## How to Trigger the Agent

To activate the autonomous behavior, you can simply tell the AI in the chat:
> *"Run the `/cpq-autonomous-implementation` workflow to [insert your requirement here]"*

Or, reference the skills directly:
> *"Use the CPQ superpowers to [insert your requirement here]"*

### Step-by-Step Execution Flow

#### Step 1: Write a Clear Prompt
Provide a clear requirement. To help the AI apply the correct safety rules, always specify whether you are doing a **New Implementation**, a **Migration**, a **Delta Change**, or a **Bug Fix**.

**Example Prompt:**
> "Run the /cpq-autonomous-implementation workflow. This is a Delta Change. I need you to create a 15% volume discount for all 'Software' products belonging to the 'Standard' Price List."

#### Step 2: The AI Reaches into Salesforce (Discovery)
The AI realizes it needs the actual `Id` for the 'Standard' Price List. It will autonomously run a background script against your environment:
```bash
python scripts/discovery/cpq_discover.py --query "SELECT Id FROM Apttus_Config2__PriceList__c WHERE Name='Standard'"
```
*You don't have to do anything here. The AI does this on its own.*

#### Step 3: The AI Generates the Solution
Depending on your request, the AI takes one of three paths:

**Path A: Declarative Changes (Pricing, Attributes, Rules)**
If you just asked for a Price Rule, the AI creates a JSON payload and runs the Data Builder:
```bash
python scripts/data/cpq_data_builder.py --file /tmp/cpq_inserts.json
```
*Result:* The Price Rule is created directly in the org via bulk data API.

**Path B: Code Changes (Apex Callbacks)**
If you asked for something highly complex (e.g., *"Calculate margin based on an external API"*), the AI scaffolds an Apex class:
```bash
python scripts/code/scaffold_cpq_callback.py --type Pricing --name MarginPricingCallback
```
*Result:* The AI generates perfectly formatted Code without hallucinating interfaces, and then injects your requested logic inside.

**Path C: Salesforce Core Extensions (Flows, Permissions)**
If you asked for process automation (e.g., *"Give the SalesRep persona access to CPQ"*):
```bash
python scripts/sfcore/cpq_security_builder.py --persona SalesRep
```
*Result:* A comprehensive Permission Set XML covering all 80+ standard Conga objects is generated automatically.

#### Step 4: Deployment & Auto-Documentation
If the AI generated Code or Salesforce Metadata (Paths B & C), it will run the deployer:
```bash
python scripts/deployment/cpq_deploy.py
```
The deployer pushes the code to Salesforce and generates a clean Markdown status report in `docs/deployments/` so your team has a historic log of exactly what the AI changed!

---

## 3 Real-World Examples

### Example 1: Creating a Price Rule (Declarative)
**Your Prompt:**
> "Use the CPQ superpowers for a Delta Change. I need a new Price Rule that gives a 10% discount to the 'Premium Support' product when the Cart total exceeds $50,000. Look up the Price List 'Enterprise' to attach it."

**What the AI does:**
1. Queries Salesforce for the 'Enterprise' Price List ID and 'Premium Support' Product ID.
2. Generates the `Apttus_Config2__PriceRule__c` and `Apttus_Config2__PriceRuleEntry__c` JSON records.
3. Automatically pushes the records directly to your Salesforce environment.

### Example 2: Scaffolding a Pricing Callback (Code)
**Your Prompt:**
> "Run /cpq-autonomous-implementation. We're doing a New Implementation. I need an Apex CustomPricingCallback that sets the Line Item's Net Price to $0 if a custom Checkbox 'Is_Free_Trial__c' on the cart header is checked."

**What the AI does:**
1. Runs the Scaffolder: `python scripts/code/scaffold_cpq_callback.py --type Pricing --name FreeTrialPricingCallback`.
2. Edits the `afterPricingLineItem` method in the generated `FreeTrialPricingCallback.cls` to inject the `$0` assignment logic.
3. Deploys the Apex Class to Salesforce and writes the Markdown Deployment Log.

### Example 3: Salesforce Metadata & Flow Integration
**Your Prompt:**
> "Use the CPQ tools for a Delta Change. Generate a SalesRep permission set for CPQ. Also, I need a Salesforce Flow that triggers when a Conga Quote (`Apttus_Proposal__Proposal__c`) is Accepted, syncing the Close Date to the Opportunity."

**What the AI does:**
1. Runs `python scripts/sfcore/cpq_security_builder.py --persona SalesRep`.
2. Runs `python scripts/sfcore/scaffold_cpq_flow.py --name Quote_Accepted_Sync --object Apttus_Proposal__Proposal__c`.
3. The AI opens the generated Flow XML and injects the Opportunity Date sync logic.
4. Deploys both the Flow and the Permission Set using the deployment script.

---

## Phase 2 Capabilities: Migration, Testing, & Validation
Beyond day-to-day implementation, the CPQ toolchain includes dedicated operations for Sandbox Lifecycle Management:

### 1. The Environment Migration Engine
You can instruct the AI to migrate CPQ configurations across Sandboxes without needing 3rd-party deployment tools. The engine performs a two-stage Metadata (`__c`, `__mdt`, Layouts, Permissions) and Data (`Apttus_Config2` relational trees) sync.
**Prompt Example:**
> "Run the CPQ Migration Engine in Delta Mode. Sync all Custom Fields and Price Rules modified since '2026-03-01' from Sandbox UAT to Production."

### 2. Autonomous Cart API Tester
The AI can mathematically prove its new pricing code works by silently spinning up an Apex Cart in the background.
**Prompt Example:**
> "Use the CPQ Cart Tester. Create a cart for Proposal P-001, add Laptop Product ID 12345, run the UpdatePrice API, and assert that the NetPrice is $900.00."

### 3. Conga Template Validator
Before deploying a `.docx` quote template, the AI can parse the inner XML to ensure no merge-fields will crash the generation engine.
**Prompt Example:**
> "Run the Conga Template Analyzer on `templates/Enterprise_Quote.docx` and verify all SObject bindings are valid against the schema."

---

## Value Proposition Summary

**1. Faster Implementations (Zero-Touch Config)**
Instead of a human manually clicking through 40 screens to build a nested Product Bundle and 5 Constraint Rules, the AI generates the unified JSON and pushes it via the `cpq_data_builder.py` simultaneously.

**2. Safer Migrations (Schema + Data Parity)**
CPQ Migrations fail because a custom field added to `Apttus_Config2__LineItem__c` wasn't migrated before the Data. The `cpq_env_migrator.py` automatically pulls the Salesforce Schema Metadata, deploys it to the target, and *then* upserts the relational CPQ Data trees natively.

**3. Bug-Free Day-to-Day Maintenance (Scaffolding & Testing)**
When fixing bugs or writing new Pricing logic, the AI never hallucinates Apex methods. It uses `scaffold_cpq_callback.py` to get the perfect boilerplate, writes the fix, and uses `cpq_cart_tester.py` to run standard `Apttus_CPQApi` methods to assert the math works before pushing to production.

---

## Tips for Best Results
- **Name your records:** If you want the AI to attach rules to existing products or price lists, mention their exact names (e.g., "The 'Hardware' category" or "The 'EMEA' Price List") so the AI's Discovery script can query them accurately.
- **State the Lifecycle Phase:** Always tell the AI if you are doing a `New Implementation`, `Migration`, `Bug Fix`, or `Delta Change`. This dictates which overarching safety rules the AI applies.
