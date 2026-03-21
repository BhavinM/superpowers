# Autonomous CPQ Agents Design

## Goal
To give the AI Agent exactly what it needs to autonomously implement Configure, Price, Quote (CPQ) requirements presented in natural language (e.g., "Add a 10% volume discount for Laptops"). The agent needs eyes (discovery), hands (data generation/deployment), and a brain (CPQ rules / scaffolding) to accomplish this without relying on a human using the Salesforce UI.

## Components

### 1. CPQ Discovery Script (`scripts/discovery/cpq_discover.py`)
Since Conga CPQ is highly data-driven, the AI must know the `Id` values of existing Price Lists or Products to map foreign keys properly.
- **Functionality:** Wraps `sf data query` to query and return standard CPQ configuration tables (e.g., `Apttus_Config2__PriceList__c`, `Apttus_Config2__ProductConfiguration__c`) in a simplified JSON structure that the AI can easily parse without token overflow.

### 2. CPQ Data Tree Builder (`scripts/data/cpq_data_builder.py`)
CPQ pricing rules and products are stored as Data, not Code.
- **Functionality:** Accepts a simpler JSON payload from the AI and converts it into a strict **SFDX Data Tree** JSON format. It then automatically runs `sf data tree import` to deploy declarative CPQ data (Price Rules, List Items, Constraint Rules) straight into the Salesforce org.

### 3. Apex Callback Scaffolder (`scripts/code/scaffold_cpq_callback.py`)
When natural language requirements involve procedural logic (e.g., dynamic external pricing integration), the AI needs to write an Apex callback.
- **Functionality:** A CLI tool that the AI executes (`python scaffold_cpq_callback.py --type Pricing --name CustomLaptopPricing`). It instantly generates the `.cls` and `.cls-meta.xml` complete with the mandatory `Apttus_Config2.CustomPricingCallback3` interface methods and basic Unit Test scaffolding, preventing the AI from hallucinating incorrect method signatures.

### 4. End-to-End Orchestration Workflow (`.agents/workflows/cpq-autonomous-implementation.md`)
The glue that ties the LLM to the tools.
- **Functionality:** A strict sequence prompt guiding the AI through parsing requirements, using `cpq_discover.py` to identify required IDs, deciding between declarative (`cpq_data_builder.py`) or programmatic (`scaffold_cpq_callback.py`) routes, and finally deploying.
