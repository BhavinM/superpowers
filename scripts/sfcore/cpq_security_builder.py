#!/usr/bin/env python3
import argparse
import os

PERM_SET_XML_START = """<?xml version="1.0" encoding="UTF-8"?>
<PermissionSet xmlns="http://soap.sforce.com/2006/04/metadata">
    <description>CPQ Access for {persona}</description>
    <hasActivationRequired>false</hasActivationRequired>
    <label>CPQ {persona}</label>"""

PERM_SET_XML_END = """
</PermissionSet>"""

CPQ_OBJECTS = [
    "Apttus_Config2__ProductConfiguration__c",
    "Apttus_Config2__LineItem__c",
    "Apttus_Config2__PriceList__c",
    "Apttus_Config2__PriceListItem__c",
    "Apttus_Config2__AssetLineItem__c",
    "Apttus_Proposal__Proposal__c",
    "Apttus_Proposal__Proposal_Line_Item__c"
]

def generate_obj_perms(objects, allow_edit=False):
    lines = []
    for obj in objects:
        lines.append(f"""    <objectPermissions>
        <allowCreate>{"true" if allow_edit else "false"}</allowCreate>
        <allowDelete>false</allowDelete>
        <allowEdit>{"true" if allow_edit else "false"}</allowEdit>
        <allowRead>true</allowRead>
        <modifyAllRecords>{"true" if obj == "Apttus_Proposal__Proposal__c" else "false"}</modifyAllRecords>
        <object>{obj}</object>
        <viewAllRecords>false</viewAllRecords>
    </objectPermissions>""")
    return "\n".join(lines)

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"✅ Created Permission Set XML: {path}")

def main():
    parser = argparse.ArgumentParser(description="Generate CPQ Permission Sets to avoid XML hallucination")
    parser.add_argument("--persona", type=str, required=True, choices=["SalesRep", "CPQAdmin"], help="Target user persona")
    args = parser.parse_args()

    xml_content = PERM_SET_XML_START.format(persona=args.persona)
    
    if args.persona == "SalesRep":
        xml_content += "\n" + generate_obj_perms(CPQ_OBJECTS, allow_edit=True)
    elif args.persona == "CPQAdmin":
        xml_content += "\n" + generate_obj_perms(CPQ_OBJECTS, allow_edit=True)
        
    xml_content += PERM_SET_XML_END
    
    file_name = f"CPQ_{args.persona}.permissionset-meta.xml"
    file_path = os.path.join("force-app/main/default/permissionsets", file_name)
    create_file(file_path, xml_content)

if __name__ == "__main__":
    main()
