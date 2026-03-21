# Conga CPQ: Bug Fixing Protocol

## Triage
1. **Calculation Errors:** Is the Net Price wrong? Bypass the Apex Callback temporarily to see if the issue is in the declarative data model (Price Matrices, Rules) or the Apex logic (CustomPricingCallback).
2. **UI / Cart Errors:** Is the cart failing to load or timing out? Check the SOQL limits in the callback classes or verify that `Apttus_Config2__SystemProperties__c` has the correct `Max Inline Items` limit set. Check for infinite loops in Constraint Rules.
3. **Constraint Rules Failing:** Ensure the `Apttus_Config2__ConstraintRuleCondition__c` has the "Match in Options" flag set correctly if dealing with deep bundles.

## Resolution Guidelines
- **No Hacks:** Do not use "hacky" custom triggers on `Apttus_Config2__LineItem__c` to bypass CPQ behavior. Always fix the core CPQ configuration or use standard Callbacks.
- **TDD Requirement:** Write a Regression unit test proving the bug exists, apply the fix, and verify the test passes.
