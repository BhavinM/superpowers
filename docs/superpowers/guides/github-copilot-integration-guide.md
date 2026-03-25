# Autonomous Conga CPQ: GitHub Copilot Integration Guide

The CPQ Superpowers framework (Markdown architecture + Python executing limits) is entirely LLM-Agnostic. While natively built for terminal CLI agents, you can seamlessly embed this Virtual Agency directly into **GitHub Copilot Chat** using 3 massive tiers of automation:

---

## Option 1: The Fast Path (Copilot Custom Instructions)
GitHub Copilot natively searches your workspace for a `.github/copilot-instructions.md` file and silently adopts its entire logic as a hidden "System Prompt". 

We have placed an overarching `copilot-instructions.md` directly into this repo.
**How to use:**
1. Open up GitHub Copilot Chat in your IDE.
2. Ask a generic CPQ question: *"Build me a layered tier margin block."*
3. Copilot will automatically ingest our hidden `.github` master prompt, assume the identity of the **CPQ Project Manager / Business Analyst**, interrogate you on Price Waterfall restrictions, and format its response exactly to match our `CPQ_TDD.md` specification!

---

## Option 2: The Explicit Path (`#file` Context Directing)
If you do not want Copilot strictly assuming the CPQ UI Persona globally, you can explicitly prompt it using localized context referencing when orchestrating complex deployments.

1. **The Architecture Idea:**
   - Command in chat: *"Read `#file cpq-solutions-architect/SKILL.md` and `#file CPQ_BRD.md`. Write me the functional Tech Specs restricting this problem to standard Conga limits without Apex."*
2. **The JSON/Data Generation (Copilot Edits):**
   - Open Copilot Edits (`Cmd+I` in VS Code).
   - Command: *"Read `#file CPQ_TDD.md`. Generate the strict payload file `price_rule.json` holding the Option constraint matrices."*
   - Copilot produces mathematically accurate JSON immediately based on our frameworks.
3. **Execution Routing:**
   - Because Copilot does not run terminal scripts inherently, you must manually open your terminal and fire `python scripts/data/cpq_data_builder.py --file price_rule.json` to push Copilot's output up into Salesforce.

---

## Option 3: The Ultimate Path (VS Code `@conga` Participant)
Because GitHub Copilot prevents raw AI from arbitrarily executing Python scripts (for infosec reasons), the final bridge is explicitly building a lightweight target VS Code Custom Chat Participant (`@conga`).

**How the Extension Architecture functions:**
1. You type `@conga Migrate this complex Software Tiering into my Dev Box`.
2. The Custom VSC Extension captures your prompt and pings the Copilot LLM backend, using our E2E master workflows to formulate the JSON mappings and Discovery schemas.
3. Instead of forcing you to use the terminal, the VSC extension directly leverages the `vscode.window.createTerminal().sendText()` API mechanism to immediately fire our local python hooks: 
   - `python scripts/discovery/cpq_discover.py`
   - `python scripts/testing/cpq_performance_analyzer.py`
   - `python scripts/migration/cpq_env_migrator.py`

This enables Copilot to perform the 100% "Hands-Free Execution" traditionally restricted to terminal AI bots!
