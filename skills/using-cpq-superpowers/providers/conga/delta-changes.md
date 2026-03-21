# Conga CPQ: Delta Changes Protocol

You are modifying an existing Conga CPQ implementation. The primary risk is breaking existing active quotes or nested product bundle rules.

## Prior to Any Changes
1. **Scope the Impact:** Run a dependency check on the Product (`Apttus_Config2__Product2Id__c`) before deleting or modifying an Option Group.
2. **Review Active Rules:** Check `Apttus_Config2__PriceRule__c` and `Apttus_Config2__ConstraintRule__c` to see if the target product is bound by legacy conditions.

## Safe Update Procedures
- **Adding a Product:** Create the product, associate it to appropriate Price Lists, and add to the Category structure. Create an Inclusion/Exclusion Constraint Rule if necessary.
- **Updating Pricing:** Do NOT delete old Price List Items. Set their `Expiration Date` to past, and create a NEW Price List Item with `Effective Date` as today.
- **Modifying Attributes:** Adding fields to Attribute Groups must be synced to the Attribute Matrix. Validate constraint rules dependent on these attributes.
- **Modifying Callbacks:** If augmenting the `CustomPricingCallback`, ensure backward compatibility by isolating the new logic in a dedicated helper class and conditionally triggering it based on a custom setting or line item flag.
