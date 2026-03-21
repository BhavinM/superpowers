# Conga CPQ: Maintenance & Auditing Protocol

## Routine Maintenance Tasks
1. **Limit Auditing:** Run check on SOQL usage inside `CustomPricingCallback` and `ValidationCallback`. Refactor to Bulkify if approaching SFDC governor limits.
2. **Orphaned Metadata:** Query and delete orphaned `Apttus_Config2__ProductOptionComponent__c` rows where the Parent Product no longer exists.
3. **Permissions Review:** Validate Profile and Permission Set mappings for standard Conga CPQ objects. Ensure sales users have minimal necessary CRUD.
4. **Asset-Based Ordering Cleanup:** Identify stuck "Pending" Asset Line Items that never converted to Active.

## Upgrades
- When a new Conga Base Package is installed, execute the standard Conga post-install scripts.
- Rerun all Apex Unit tests for Callbacks to ensure the new managed package did not introduce breaking changes to the global interfaces.
