#!/usr/bin/env python3
import argparse
import os

CMDT_XML = """<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <deploymentStatus>Deployed</deploymentStatus>
    <description>Stores CPQ thresholds and integration settings</description>
    <label>{label}</label>
    <pluralLabel>{label}s</pluralLabel>
    <visibility>Public</visibility>
</CustomObject>"""

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"✅ Created {path}")

def main():
    parser = argparse.ArgumentParser(description="Scaffold Salesforce Core Metadata (Custom Metadata Types, Settings)")
    parser.add_argument("--type", type=str, required=True, choices=["CustomMetadata", "CustomSetting"], help="Type of metadata to generate")
    parser.add_argument("--name", type=str, required=True, help="API Name of the metadata (e.g. CPQ_Setting__mdt)")
    parser.add_argument("--label", type=str, required=True, help="Label of the metadata")
    args = parser.parse_args()

    if args.type == "CustomMetadata":
        if not args.name.endswith("__mdt"):
            args.name += "__mdt"
        
        obj_dir = f"force-app/main/default/objects/{args.name}"
        obj_path = os.path.join(obj_dir, f"{args.name}.object-meta.xml")
        create_file(obj_path, CMDT_XML.format(label=args.label))
    # Extendible to CustomSettings or Fields later

if __name__ == "__main__":
    main()
