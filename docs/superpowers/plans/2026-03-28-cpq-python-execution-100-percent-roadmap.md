# CPQ Superpowers: The 100% Python Execution Roadmap

**Goal:** Transform the foundational "Golden Skeleton" of the AI CPQ Agency into a true, 100% mathematically executable Production Engine by building the intensive Python business logic required for deep data ETL, SOQL traversal, and Anonymous Apex execution integrations.

---

## Phase 1: Deep Discovery & Dependency Graphing (40% ➔ 100%)
*Target Focus:* `scripts/discovery/cpq_environment_scanner.py`

**The Implementation Protocol:**
1. **Recursive SOQL Pollers:** Write Python execution arrays that query a root Product grouping, then dynamically loop to recursively query its massive `Apttus_Config2__ProductOptionGroup__c` and nested `Apttus_Config2__ProductOptionComponent__c` hierarchies natively without breaching API transaction limits.
2. **Metadata API Hooks:** Utilize the standard `sf project retrieve` operations and Python `xml.etree.ElementTree` parsing to extract and securely map active specific Validation Rules and Custom Field overrides native on the `Apttus_Config2__LineItem__c` object.
3. **Graphing Output:** Output the relational matrices into an actionable, flattened `.json` array structuring the precise topology of the organization's pricing metrics.

## Phase 2: The Data Builder Translation Engine (10% ➔ 100%)
*Target Focus:* `scripts/data/cpq_data_builder.py`

**The Implementation Protocol:**
1. **LLM payload Parser:** Write robust regex/JSON extraction models that flawlessly ingest the `CPQ_TDD.md` spec outputs natively from the Copilot outputs.
2. **Pre-Flight ID Resolution:** Write sub-routines invoking `sf_client.py` that dynamically look up the explicit Salesforce Foreign Key IDs of the `PriceListId__c` and `ProductId__c` referencing string names (e.g., "Enterprise SaaS") provided by the LLM.
3. **Bulk API Trees:** Translate the newly resolved relationship paths into absolute `sfdx data tree` JSON configurations. Orchestrate the CLI `tree import` bulk commands, explicitly capturing and logging index mapping failures.

## Phase 3: The Cart Math Assertions (15% ➔ 100%)
*Target Focus:* `scripts/testing/cpq_cart_tester.py` & `cpq_performance_analyzer.py`

**The Implementation Protocol:**
1. **Anonymous Apex Virtualization:** Build a native Python templating orchestrator that dynamically compiles the `Apttus_CPQApi.CPQ.AddMultiProductRequestDO` execution string blocks leveraging the parameters fed by the QA Architect.
2. **SFDX Compute Hooks:** Execute the generated Apex files securely (`sf apex run -f cart_simulation.apex`).
3. **Trace Profile Extraction:** Fetch the subsequent payload `debug_log` string matrices natively. Instantiate complex Regex algorithms mapping block-level `Apex CPU Time: X/10000ms` boundaries.
4. **Boolean Assertion Logic:** Embed strict Python `unittest` boolean assertions computing the differential comparing the SOQL resultant `Apttus_Config2__NetPrice__c` explicitly against the BRD specification outputs.

## Phase 4: Delta Migration & Bulk ETL Seed (20% ➔ 100%)
*Target Focus:* `scripts/migration/cpq_env_migrator.py`

**The Implementation Protocol:**
1. **The Recursive Seed Engine (`--seed`)**: Utilize Salesforce Bulk API configurations to natively query 10,000+ relational Cartesian CPQ records downward targeting the Production root.
2. **Foreign Key Scrambling Matrix:** Ingest the colossal JSON graph structure, dynamically stripping all distinct 18-Character IDs native to Production. 
3. **Progressive Sequencing:** Re-configure the matrices natively into the target Dev/UAT sandbox systematically targeting hierarchical precedence (Products ➔ PriceLists ➔ Options/Constraints ➔ Matrices ➔ Rules) ensuring pristine database referential integrity arrays.
