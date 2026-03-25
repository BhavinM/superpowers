#!/usr/bin/env python3
import argparse
import os

XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<Translations xmlns="http://soap.sforce.com/2006/04/metadata">
    <customApplications>
        <name>Apttus_Config2__ApttusPricingSetup</name>
        <label>{app_label}</label>
    </customApplications>
</Translations>"""

def main():
    parser = argparse.ArgumentParser(description="Multi-Currency & Localization Translation Builder")
    parser.add_argument("--lang", required=True, help="Language code (e.g., fr, de, es)")
    args = parser.parse_args()
    
    base_dir = "force-app/main/default/translations"
    os.makedirs(base_dir, exist_ok=True)
    
    file_path = os.path.join(base_dir, f"{args.lang}.translation-meta.xml")
    with open(file_path, "w") as f:
        f.write(XML_TEMPLATE.format(app_label=f"CPQ Translation ({args.lang})"))
    print(f"✅ Translation Workbench XML Scaffolded at {file_path}")

if __name__ == "__main__":
    main()
