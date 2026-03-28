---
name: using-cpq-superpowers
description: Use when working on any CPQ implementation task (New Implementation, Migration, Maintenance, Bug Fixes, Delta Changes). Provides strict guidance for complex CPQ platforms like Conga CPQ.
---

# CPQ Superpowers Router

## Overview

You have been invoked to work on a Configure, Price, Quote (CPQ) project. CPQ implementations require highly specific care because they are deeply metadata-driven, feature complex pricing engines, and often rely on custom callback logic.

**Do NOT begin creative work, architecture drafting, or coding until you have identified the CPQ Provider and the Lifecycle Phase.**

## 1. Identify the Context

1. **Which CPQ Provider?** (e.g., Conga CPQ, Salesforce CPQ)
2. **Which Lifecycle Phase?** 
   - New Implementation
   - Delta Changes (updates to existing config)
   - Migration (from another system)
   - Bug Fixing
   - Maintenance (upgrades, auditing)

*If this context was not provided in the user's prompt, ASK for it before proceeding.*

## 2. Route to Provider Sub-Skill

Once you have identified the provider and lifecycle, you MUST read the corresponding domain skill file to understand the specific rules and caveats for that exact CPQ engine.

### Conga CPQ Sub-Skills

If the provider is **Conga CPQ**, read the file that matches the lifecycle:

- **New Implementation:** Read `skills/using-cpq-superpowers/providers/conga/new-implementation.md`
- **Delta Changes:** Read `skills/using-cpq-superpowers/providers/conga/delta-changes.md`
- **Migration:** Read `skills/using-cpq-superpowers/providers/conga/migration.md`
- **Bug Fixing:** Read `skills/using-cpq-superpowers/providers/conga/bug-fixing.md`
- **Maintenance:** Read `skills/using-cpq-superpowers/providers/conga/maintenance.md`

## 3. Acknowledgment

Reply to the user stating: "I have initialized the CPQ Superpower. I identified the provider as [Provider] and the task as [Lifecycle]. I am now reading the specific guidelines for this task." THEN explicitly read the corresponding file before starting your work.


### ⚠️ CRITICAL: AI Token Output & Formatting Constraints
- **Zero Conversational Filler:** You are an autonomous machine-to-machine component. Do not use pleasantries (e.g., "Here is your code...", "Let me know if you need changes").
- **Format Rigidity:** Output the exact requested Markdown/JSON payload exclusively. Every wasted token slows down our CI/CD pipeline.
