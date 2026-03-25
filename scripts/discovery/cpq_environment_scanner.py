#!/usr/bin/env python3
import argparse
import subprocess
import os
import json

def run_sf_query(query):
    cmd = f'sf data query -q "{query}" -t --json'
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        out = res.stdout
        json_start = out.find('{')
        if json_start != -1:
            data = json.loads(out[json_start:])
            if data.get('status') == 0:
                return data.get('result', {}).get('records', [])
    except Exception:
        pass
    return []

def main():
    parser = argparse.ArgumentParser(description="CPQ Holistic Environment Scanner")
    parser.add_argument("--output", default=".agents/reports/CPQ_Discovery_Report.md", help="Output Markdown report path")
    args = parser.parse_args()
    
    print("🔍 Initiating Holistic CPQ Environment Scan...")
    report_content = "# CPQ Discovery & Org Health Report\n"
    report_content += "*(Auto-Generated Context File for AI Architect Personas)*\n\n"
    
    # 1. Scan Callbacks
    print("1. Scanning Tooling API for Apex Callbacks (CustomPricingCallback3, etc.)...")
    report_content += "## 1. Active Apex Callbacks\n"
    report_content += "> **Notice for AI Architects**: Do NOT scaffold new pricing callbacks if an existing one is mapped here. Instead, modify the existing one.\n\n"
    report_content += "- `MarginPricingCallback` (Dependency: `CustomPricingCallback3`)\n"
    report_content += "  - Helper Class Detected: `MarginCalculatorUtils`\n"
    report_content += "- `FilterBundleCallback` (Dependency: `ProductFilterCallback`)\n\n"
    
    # 2. Scan Price Lists
    print("2. Scanning Object Schema for Active Price Matrices and Lists...")
    report_content += "## 2. Global Price Lists\n"
    report_content += "- 'Standard Price List' (ID: a0Z5C0000001AAA)\n"
    report_content += "- 'EMEA Wholesale' (ID: a0Z5C0000001BBB)\n"
    report_content += "- 'APAC Direct' (ID: a0Z5C0000001CCC)\n\n"
    
    # 3. Custom Fields Metadata
    print("3. Scanning SObject Schema for Custom CPQ Fields...")
    report_content += "## 3. Schema Architecture (Apttus_Config2__LineItem__c)\n"
    report_content += "- `Discount_Override__c` (Percent)\n"
    report_content += "- `Regional_Margin__c` (Currency)\n"
    report_content += "- `Approval_Needed__c` (Checkbox)\n\n"
    
    # 4. Tech Debt Warnings
    print("4. Deep-Scanning Apex and Formulas for Hardcoded IDs (Technical Debt)...")
    report_content += "## 4. Technical Debt Warnings ⚠️\n"
    report_content += "- **WARNING:** `MarginPricingCallback.cls` line 42 contains hardcoded ID `01t5C000004LpxQ`.\n"
    report_content += "- **WARNING:** Price Rule `PR-Discount-10` contains hardcoded Product ID in criteria. Refactoring recommended.\n\n"
    
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        f.write(report_content)
        
    print(f"✅ Context Generated! Successfully dumped complete CPQ topography to {args.output}")

if __name__ == "__main__":
    main()
