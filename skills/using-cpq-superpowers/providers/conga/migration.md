# Conga CPQ: Migration Protocol

You are migrating an external or legacy pricing engine into Conga CPQ on Salesforce.

## 1. Data Mapping & Parity
- Extract legacy rules (e.g., from Salesforce CPQ, Excel, or proprietary engines).
- Map legacy products to Conga's `Apttus_Config2__ProductOptionComponent__c` nested standalone/bundle structure.
- Map distinct Product Attributes to `Apttus_Config2__ProductAttributeValue__c`.

## 2. Translating Rules Check
- Legacy "Discount Schedules" -> Conga "Price Matrices".
- Legacy "Product Rules" -> Conga "Constraint Rules" (Condition & Action).
- Legacy "Price Rules" -> Conga "Price Rules" or "Attribute Rules".

## 3. Asset & Order Data (ABO)
- Map legacy Subscriptions/Assets into `Apttus_Config2__AssetLineItem__c`.
- Validate that Asset-Based Ordering (Renewals, Amendments, Cancellations) correctly parses and scales the migrated Asset Line Items.

## 4. Validation
- Run parity testing: Generate an identical cart in the legacy system and Conga CPQ. Verify the net price matches down to the cent.
