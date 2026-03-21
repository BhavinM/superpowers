#!/usr/bin/env python3
import argparse
import os

FLOW_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Flow xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>60.0</apiVersion>
    <environments>Default</environments>
    <interviewLabel>{name} {{!$Flow.CurrentDateTime}}</interviewLabel>
    <label>{name}</label>
    <processMetadataValues>
        <name>BuilderType</name>
        <value>
            <stringValue>LightningFlowBuilder</stringValue>
        </value>
    </processMetadataValues>
    <processType>AutoLaunchedFlow</processType>
    <start>
        <locationX>50</locationX>
        <locationY>0</locationY>
        <connector>
            <!-- AI: ADD YOUR FLOW LOGIC / RECORD UPDATES HERE -->
        </connector>
        <object>{sobject}</object>
        <recordTriggerType>CreateAndUpdate</recordTriggerType>
        <triggerType>RecordAfterSave</triggerType>
    </start>
    <status>Draft</status>
</Flow>"""

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"✅ Created Flow XML: {path}")

def main():
    parser = argparse.ArgumentParser(description="Scaffold Salesforce Record-Triggered Flows for CPQ Objects")
    parser.add_argument("--name", type=str, required=True, help="API Name of the Flow (e.g. Quote_Accepted_Sync)")
    parser.add_argument("--object", type=str, required=True, help="SObject API Name (e.g. Apttus_Proposal__Proposal__c)")
    args = parser.parse_args()

    flow_path = os.path.join("force-app/main/default/flows", f"{args.name}.flow-meta.xml")
    create_file(flow_path, FLOW_XML.format(name=args.name, sobject=args.object))

if __name__ == "__main__":
    main()
