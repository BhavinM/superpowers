#!/usr/bin/env python3
import argparse
import os

TEMPLATES = {
    "Pricing": {
        "cls": """global class {name} implements Apttus_Config2.CustomPricingCallback3 {{
    global void start(Apttus_Config2.ProductConfiguration cart) {{}}
    global void setMode(Apttus_Config2.CustomPricingCallback3.PricingMode mode) {{}}
    global void onPriceItemSet(Apttus_Config2__LineItem__c item, Apttus_Config2__PriceListItem__c priceListItem) {{}}
    global void beforePricing(Apttus_Config2.ProductConfiguration cart) {{}}
    global void beforePricingLineItem(Apttus_Config2.ProductConfiguration cart, Apttus_Config2.LineItem item) {{}}
    global void afterPricingLineItem(Apttus_Config2.ProductConfiguration cart, Apttus_Config2.LineItem item) {{}}
    global void afterPricing(Apttus_Config2.ProductConfiguration cart) {{}}
    global void finish() {{}}
}}""",
        "test": """@isTest
private class {name}Test {{
    @isTest static void testPricing() {{
        {name} callback = new {name}();
        System.assertNotEquals(null, callback);
    }}
}}"""
    },
    "Validation": {
        "cls": """global class {name} implements Apttus_Config2.CustomValidationCallback2 {{
    global Apttus_Config2.CustomClass.ValidationResult validateCart(Apttus_Config2.ProductConfiguration cart) {{
        return new Apttus_Config2.CustomClass.ValidationResult(true);
    }}
    global Apttus_Config2.CustomClass.ValidationResult validateAssetItems(Apttus_Config2.ProductConfiguration cart, List<Apttus_Config2__AssetLineItem__c> assets) {{
        return new Apttus_Config2.CustomClass.ValidationResult(true);
    }}
}}""",
        "test": """@isTest
private class {name}Test {{
    @isTest static void testValidation() {{
        {name} callback = new {name}();
        System.assertNotEquals(null, callback);
    }}
}}"""
    }
}

XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>60.0</apiVersion>
    <status>Active</status>
</ApexClass>"""

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"✅ Created {path}")

def main():
    parser = argparse.ArgumentParser(description="Scaffold CPQ Apex Callbacks and Tests instantly to avoid boilerplate hallucination.")
    parser.add_argument("--type", type=str, required=True, choices=["Pricing", "Validation"], help="The standard CPQ Callback Interface to implement")
    parser.add_argument("--name", type=str, required=True, help="The apex Class Name")
    args = parser.parse_args()

    base_dir = "force-app/main/default/classes"
    
    # Class
    cls_path = os.path.join(base_dir, f"{args.name}.cls")
    cls_meta = cls_path + "-meta.xml"
    create_file(cls_path, TEMPLATES[args.type]["cls"].format(name=args.name))
    create_file(cls_meta, XML_TEMPLATE)
    
    # Test Class
    test_path = os.path.join(base_dir, f"{args.name}Test.cls")
    test_meta = test_path + "-meta.xml"
    create_file(test_path, TEMPLATES[args.type]["test"].format(name=args.name))
    create_file(test_meta, XML_TEMPLATE)

if __name__ == "__main__":
    main()
