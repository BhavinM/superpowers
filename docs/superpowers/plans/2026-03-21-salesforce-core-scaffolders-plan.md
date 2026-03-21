# Salesforce Core Scaffolding Scripts Plan

**Goal:** Implement Python utilities to output valid Salesforce XML metadata (Flows, Permissions, Custom Meta) so the AI never hallucinates or struggles with XML structural errors when implementing CPQ augmentations.

### Architectures
1. **`sf_meta_scaffolder.py`**: Generates `__mdt` and `.object-meta.xml` headers.
2. **`scaffold_cpq_flow.py`**: Generates `RecordAfterSave` AutoLaunchedFlow XMLs mapping directly to CPQ objects.
3. **`cpq_security_builder.py`**: Builds standard Sales and Admin Permission Sets containing `<objectPermissions>` for the massive list of Conga objects.

### Execution
- We will immediately execute inline based on our Python and XML templates.
- Update `walkthrough.md` and the master workflow afterward.
