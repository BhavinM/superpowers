# [PATTERN EXAMPLE] SaaS Tiered Subscription Bundle

## 1. Product Context
The `Enterprise SaaS License` is a parent Product Bundle.
- Requires precisely 1 `Implementation Package` Option (Min 1, Max 1).
- Cannot be sold concurrently with `Legacy Premise Software` (Constraint Rule: Exclusion).

## 2. Pricing Context
Tiered mathematical discounting applies ONLY to the Base Price (Waterfall).
- Quantity 0-100: Standard List Price
- Quantity 101-500: 15% Discount on marginal units.
- Term-Based: Subscription term length fundamentally multiplies the overall Final Net Price.

## 3. Tech Architecture (SObject)
- Create `Apttus_Config2__PriceMatrix__c` associated to the product.
- DO NOT use `CustomPricingCallback3` because Standard Tiered Matrices support volume scale discounts implicitly.

## 4. Quoting & Output Context
Requires Vice President Approval if Net Price drops below a 40% overarching margin.
