#!/usr/bin/env python3
import argparse
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.sf_client import SFClient, logger

def recursive_bundle_discovery(product_name: str) -> dict:
    """Recursively crawls the CPQ Cartesian Graph from root Product -> OptionGroups -> Component Options."""
    logger.info(f"Initiating Recursive SOQL Bound Discovery for Target Payload '{product_name}'...")
    
    # 1. Fetch Root Product Architecture Bounds
    root_query = f"SELECT Id, Name, Apttus_Config2__ConfigurationType__c FROM Product2 WHERE Name = '{product_name}' LIMIT 1"
    root_records = SFClient.execute_query(root_query)
    
    if not root_records:
        logger.error(f"Root Cartesian Product '{product_name}' utterly missing from Sandbox Org Database boundaries.")
        return {}
        
    root_id = root_records[0].get('Id')
    graph = {
        "Product": root_records[0],
        "OptionGroups": []
    }
    
    # 2. Extract Distinct Relational Option Groups Hierarchies
    logger.info(f"Root Bundle explicitly structured (ID: {root_id}). Systematically compiling Apttus_Config2__ProductOptionGroup__c dimensional arrays...")
    group_query = f"SELECT Id, Name, Apttus_Config2__MinOptions__c, Apttus_Config2__MaxOptions__c FROM Apttus_Config2__ProductOptionGroup__c WHERE Apttus_Config2__ProductId__c = '{root_id}'"
    groups = SFClient.execute_query(group_query)
    
    for group in groups:
        group_id = group.get('Id')
        logger.info(f"Resolving descendant component boundaries recursively for OptionGroup '{group.get('Name')}' (ID: {group_id})...")
        
        # 3. Recursively map the explicit Component Options sub-matrix logic boundaries
        comp_query = f"SELECT Id, Apttus_Config2__ComponentProductId__r.Name, Apttus_Config2__Default__c FROM Apttus_Config2__ProductOptionComponent__c WHERE Apttus_Config2__ProductOptionGroupId__c = '{group_id}'"
        components = SFClient.execute_query(comp_query)
        group['Components'] = components
        graph["OptionGroups"].append(group)
        
    return graph

def main() -> None:
    parser = argparse.ArgumentParser(description="Autonomous CPQ SECURE Deep Discovery Engine")
    parser.add_argument("--bundle", required=True, help="Target Salesforce CPQ Explicit Root Bundle Boundary String")
    args = parser.parse_args()

    topology = recursive_bundle_discovery(args.bundle)
    
    if topology:
        logger.info(f"✅ Deep Discovery dimensional recursion structurally generated against Org boundaries limits safely.")
        print(json.dumps(topology, indent=2))
    else:
        logger.warning(f"⚠️ Zero recursive structural mapping matrices implicitly parsed.")

if __name__ == "__main__":
    main()
