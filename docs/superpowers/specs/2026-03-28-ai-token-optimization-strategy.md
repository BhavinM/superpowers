# Autonomous CPQ Agency: AI Token & Context Window Optimization Strategy

## Context Vulnerability Overview
As our 6-Persona AI engine scales linearly across 60+ Conga SObjects, deep Cartesian bundle graphs, and massive APEX execution logs, we face severe risks of **Context Window Bloat**. Passing raw metadata and concatenated histories to LLMs (like GPT-4, Claude, or GitHub Copilot) will result in expensive token burns, hallucination spikes, and "Lost in the Middle" contextual amnesia.

This document identifies the 4 primary token vulnerabilities within our orchestrated pipeline and dictates concrete remediation strategies.

---

## Scenario 1: The Cascading "Chain of Thought" Redundancy 
**The Risk:** In the `cpq-e2e-project` loop, we have 6 sequential personas (`PM -> BA -> SA -> TA -> QA -> Builder`). If the Orchestrator indiscriminately appends Phase 1 (`BRD.md`), Phase 2 (`FSD.md`), and Phase 3 (`TDD.md`) into the Builder's context window context, the Builder LLM receives thousands of irrelevant tokens concerning abstract business requirements.

**The Optimization Strategy: Strict Context Slicing**
- **Artifact Isolation:** The `Builder` persona should **only** ingest the `TDD.md` (Technical Specs) and the `SFDX Data Schema`. It does *not* need the overarching business stories.
- **Implementation:** Explicitly flush the orchestrator's chat history array upon transitioning architectural boundaries, feeding only the *immediately preceding* markdown artifact as the "Source of Truth" context.

## Scenario 2: Massive Recursive SFDX Discovery JSON Dumps
**The Risk:** The `cpq_discover.py` recursive crawler transforms Conga CPQ bundles (Products -> Option Groups -> Components) into Python JSON dictionaries. A single Enterprise Server bundle with 50 option groups and 200 components yields a massive 5,000-line relational JSON structure. Subjecting the `cpq-solutions-architect` to this raw payload consumes ~20,000 tokens per execution.

**The Optimization Strategy: Schema Pruning & Field Striping**
- **Null Value Pruning:** Natively drop all JSON keys with `null` or empty string values before dumping.
- **Audit Field Exclusion:** Actively delete default Salesforce system fields (`CreatedDate`, `CreatedById`, `LastModifiedDate`, `SystemModstamp`) from the Python dictionary.
- **Key Aliasing:** Minify verbose SObject fields dynamically (ex: `Apttus_Config2__ConfigurationType__c` mapped down to `ConfigType`).

## Scenario 3: Salesforce Debug Log Execution Trace Ingestion
**The Risk:** `cpq_cart_tester.py` virtualizes Anonymous Apex testing math natively. Standard CPQ computation `.log` files natively generate 5MB-10MB strings containing millions of tokens of internal `METHOD_ENTRY` and `DB_SOQL` matrices. Passing this raw Salesforce Native log to the `QA Architect` LLM will instantly breach any 128k/200k Context limit.

**The Optimization Strategy: Regex-Governed Log Distillation**
- **Token Shielding:** As currently implemented structurally, our engine explicitly utilizes Python regex `line_item_matches = re.findall(r'CART...NET_PRICE...', log)` to extract only the 5 explicit lines of calculation boundaries. We must mandate that the LLM is **never** granted access to the raw `.apex` log files visually, limiting token usage to < 200 tokens per validation suite.

## Scenario 4: "Mega-Prompt" Copilot Skills Overloading
**The Risk:** Passing the entire 60-SObject CPQ mappings directory as a global Knowledge Context base during a basic `cpq-business-analyst` elicitation phase burns tokens needlessly querying technical architectures the BA doesn't need.

**The Optimization Strategy: Dynamic Semantic RAG Injection**
- **Skill Chunking:** The `.agents/skills` repository should be partitioned. Only load the `conga-cpq-technical-architect` Skill Markdown arrays when specifically invoking `$Phase 4`.

---
## Review Execution
Would you like to authorize the implementation of the **JSON Schema Pruning (Scenario 2)** and **Context Slicing (Scenario 1)** protocols deeply into our Python orchestrators?
