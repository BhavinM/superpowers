---
description: How to process an English natural language CPQ requirement and autonomously implement it into the org without UI reliance.
---
# Autonomous Agent CPQ Implementation Workflow

When asked to configure CPQ enhancements autonomously, execute the following steps exactly as numbered.

## 1. Requirement Intake & Scope
Review the user's natural language request (e.g., "Add a 15% discount for Software products").
Determine if the request requires **Declarative CPQ Data** (Price Rules), **Programmatic CPQ Code** (Apex Callbacks), or **Salesforce Core Metadata** (Flows, Custom Settings). 
Rules of Engagement:
- Use *CPQ Price Rules* and *Matrices* for cart calculations.
- Use *Salesforce Record-Triggered Flows* for cross-object updates outside the cart.
- Use *Custom Metadata Types* to store pricing configuration thresholds to avoid hardcoding.
Consult `skills/using-cpq-superpowers/SKILL.md` to confirm the correct provider logic.

## 2. Discovery Phase (`scripts/discovery/cpq_discover.py`)
You must NOT hallucinate Salesforce IDs (e.g., PriceList IDs, Product IDs).
Identify the data you need from the Org to execute the request.
// turbo
Run `python scripts/discovery/cpq_discover.py --query "SELECT Id, Name FROM Apttus_Config2__PriceList__c WHERE Name='Standard'"` to fetch the raw IDs. 

## 3. Data Generation Phase (`scripts/data/cpq_data_builder.py`)
If the change is declarative (e.g. creating rules, list items, matrices):
- Create a local JSON file in `/tmp/cpq_inserts.json` representing the data:
  ```json
  [{"type": "Apttus_Config2__PriceListItem__c", "fields": {"Apttus_Config2__PriceListId__c": "THE_ID_YOU_FOUND", "Apttus_Config2__ListPrice__c": 100}}]
  ```
// turbo
- Run `python scripts/data/cpq_data_builder.py --file /tmp/cpq_inserts.json` to safely push the records to the org.

## 4. Code Generation Phase (`scripts/code/scaffold_cpq_callback.py` & `scripts/sfcore/`)
If the change requires Apex logic (Pricing modifications beyond matrices):
// turbo
- Run `python scripts/code/scaffold_cpq_callback.py --type Pricing --name MyCustomPricingCallback`
- Edit the newly generated `.cls` class with the specific mathematical/discount logic.

If the change requires Salesforce Core Metadata:
// turbo
- Run `python scripts/sfcore/sf_meta_scaffolder.py --type CustomMetadata --name Threshold_mdt --label Threshold`
// turbo
- Run `python scripts/sfcore/scaffold_cpq_flow.py --name Quote_Approved_Sync --object Apttus_Proposal__Proposal__c`
// turbo
- Run `python scripts/sfcore/cpq_security_builder.py --persona SalesRep`

## 5. Deployment Phase (`scripts/deployment/cpq_deploy.py`)
If any metadata files (.cls, .xml, document templates) were created or edited during Step 4:
// turbo
- Run `python scripts/deployment/cpq_deploy.py` interactively to select and deploy the files, which automatically generates the Markdown documentation in `docs/deployments`.

## 6. Closing
Write a short summary in the chat of what was queried via the discovery tool, what IDs were isolated, and the exact files or configurations deployed to satisfy the user's request.
