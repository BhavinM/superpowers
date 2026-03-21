# Conga CPQ: New Implementation Protocol

You are executing a greenfield implementation for Conga CPQ on Salesforce. Follow this strict protocol to establish a scalable foundation.

## 1. Schema & Data Model
- Identify the core objects: `Apttus_Config2__ProductConfiguration__c`, `Apttus_Config2__LineItem__c`, `Apttus_Config2__AssetLineItem__c`.
- **Constraint:** Do NOT create custom formula fields on the Line Item for pricing calculation. Use Price Rules and Matrices instead.

## 2. Product Catalog Foundation
- Create exact category hierarchies (`Apttus_Config2__ClassificationName__c` and `Apttus_Config2__ClassificationHierarchy__c`).
- Set up Product Groups before creating massive lists of standalone products.
- Configure Product Attribute Groups and Attribute Matrices for guided selling (Questionnaires/Interviews).

## 3. Pricing Engine Setup
- Deploy baseline Price Lists (`Apttus_Config2__PriceList__c`) and Price List Items (`Apttus_Config2__PriceListItem__c`).
- **Rule of Thumb:** Use Price Matrices for multi-dimensional volume discounts, and Price Rules for conditional cross-product discounts.
- Validate Multicurrency and Localization settings in Salesforce before locking the CPQ price books.

## 4. Advanced Features
- **Subscription Management:** Configure Multi-Dimensional Quoting (MDQ) for annual subscription structures.
- **Document Generation:** Scaffold Conga Composer / Conga Quote Generation templates based on the finalized Line Item fields.
- **Approvals:** Outline the `Apttus_Approval__Approval_Request__c` logic based on discounting thresholds (Advanced Approvals).

## 5. Extensibility & Security
- **Callbacks:** If out-of-the-box UI/pricing behavior falls short, generate the standard Conga Callback classes (e.g., `Apttus_Config2.CustomPricingCallback`, `Apttus_Config2.ValidationCallback`).
- **Permissions:** Establish base Conga CPQ permission sets and Role Hierarchies.
- Write comprehensive test classes mapping to specific Product Bundle topologies before committing callbacks.
