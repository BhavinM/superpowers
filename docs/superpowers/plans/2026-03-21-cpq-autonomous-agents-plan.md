# Autonomous CPQ Tools Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement the 4 core standalone assets allowing the AI to autonomously deploy programmatic and declarative CPQ features directly from natural language requirements.

**Architecture:** A Discovery DB script, a JSON Data Builder, an Apex code scaffolder, and a master Markdown agent Workflow.

---

### Task 1: Build CPQ Discovery Tool
**Files:**
- Create: `scripts/discovery/cpq_discover.py`

- [ ] **Step 1:** Write `cpq_discover.py`. It should take arguments like `--object` and `--fields` or predefined flags like `--price-lists`, translating them into `sf data query -q "SELECT Id, Name FROM Apttus_Config2__PriceList__c" --json`.
- [ ] **Step 2:** Ensure it handles exceptions and outputs clean JSON for the LLM to parse.

### Task 2: Build CPQ Data builder
**Files:**
- Create: `scripts/data/cpq_data_builder.py`

- [ ] **Step 1:** Write `cpq_data_builder.py`. It should take an `--input` JSON file provided by the AI and convert it into the strict format expected by `sf data tree import`.
- [ ] **Step 2:** Add an `--execute` flag that directly triggers `sf data tree import --plan <generated-plan.json>` and prints success/failures.

### Task 3: Build Apex Callback Scaffolder
**Files:**
- Create: `scripts/code/scaffold_cpq_callback.py`

- [ ] **Step 1:** Write `scaffold_cpq_callback.py`. It should accept `--type` (e.g., Pricing, Validation, Product) and `--name` (ClassName).
- [ ] **Step 2:** Define templates with the correct `Apttus_Config2` interface boilerplates. Output a well-formatted `.cls` and corresponding API version `.cls-meta.xml` inside `force-app/main/default/classes/`.

### Task 4: Create Orchestration Workflow
**Files:**
- Create: `.agents/workflows/cpq-autonomous-implementation.md`

- [ ] **Step 1:** Write the workflow guiding the agent through the sequence: 
  1. Receive Prompt.
  2. Discovery Phase (`cpq_discover.py`).
  3. Determine Declarative vs Code.
  4. Execution (`cpq_data_builder.py` or `scaffold_cpq_callback.py` followed by `cpq_deploy.py`).

### Task 5: Commit Execution
- [ ] **Step 1:** Run `git add` for all `scripts/` and `.agents/` modifications.
- [ ] **Step 2:** Commit all tools with message: `feat(cpq): add fully autonomous CPQ implementation toolchain`.
