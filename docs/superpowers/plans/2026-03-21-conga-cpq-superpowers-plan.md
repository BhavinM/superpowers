# Customize CPQ Superpowers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a suite of specific CPQ superpower skills that route tasks appropriately and provide targeted instructions for Conga CPQ implementation lifecycles.

**Architecture:** A Router skill (`using-cpq-superpowers`) determines the provider and lifecycle, then directs the agent to provider-specific markdown skills (e.g., `providers/conga/migration.md`) which contain rules for core CPQ domains (Catalog, Pricing, Callbacks, etc.).

**Tech Stack:** Markdown (Prompt Engineering for Agent Skills)

---

### Task 1: Initialize Core Router Skill

**Files:**
- Create: `skills/using-cpq-superpowers/SKILL.md`

- [ ] **Step 1: Write the Core Router Skill**
Write the main `using-cpq-superpowers` skill that acts as the entry point. It should:
1. Identify if the user is working on Conga CPQ or another provider.
2. Identify the lifecycle (Migration, New Implementation, Delta, Bug Fix, Maintenance).
3. Instruct the agent to read the appropriate provider file (e.g., `skills/using-cpq-superpowers/providers/conga/migration.md`) before doing any creative work.

- [ ] **Step 2: Commit**
Run: `git add skills/using-cpq-superpowers/SKILL.md`
Run: `git commit -m "feat(cpq): add core using-cpq-superpowers router skill"`
Expected: commit succeeds.

### Task 2: Create Conga CPQ Base Sub-Skills

**Files:**
- Create: `skills/using-cpq-superpowers/providers/conga/new-implementation.md`
- Create: `skills/using-cpq-superpowers/providers/conga/delta-changes.md`
- Create: `skills/using-cpq-superpowers/providers/conga/migration.md`
- Create: `skills/using-cpq-superpowers/providers/conga/bug-fixing.md`
- Create: `skills/using-cpq-superpowers/providers/conga/maintenance.md`

- [ ] **Step 1: Write New Implementation rules**
Create `new-implementation.md` with guidelines covering: Schema, Product Catalog, Pricing Setup, Callbacks, Security/Permissions, Document Generation, and Approvals from scratch.

- [ ] **Step 2: Write Delta Changes rules**
Create `delta-changes.md` with rules for modifying existing Product/Pricing Rules, constraint rules, attributes, and matrices safely without breaking existing configuration.

- [ ] **Step 3: Write Migration rules**
Create `migration.md` with a checklist for extracting rules from legacy CPQ, mapping data, and validating parity.

- [ ] **Step 4: Write Bug Fixing and Maintenance rules**
Create `bug-fixing.md` and `maintenance.md` for troubleshooting callbacks, auditing limits, and asset-based ordering (renewals/amendments) issues.

- [ ] **Step 5: Verify Directory Structure**
Run: `ls -la skills/using-cpq-superpowers/providers/conga`
Expected: lists the 5 new markdown files created.

- [ ] **Step 6: Commit**
Run: `git add skills/using-cpq-superpowers/providers/conga/`
Run: `git commit -m "feat(conga): create conga cpq lifecycle sub-skills"`
Expected: commit succeeds.
