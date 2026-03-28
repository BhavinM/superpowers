#!/usr/bin/env python3
import argparse
import sys
import os
import json

# Ensure Core logging module is universally accessible within hierarchy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.sf_client import SFClient, logger

def main() -> None:
    parser = argparse.ArgumentParser(description="Autonomous CPQ SECURE Data Discovery Script")
    parser.add_argument("--query", required=True, help="SFDX SOQL Dynamic Query parameter")
    args = parser.parse_args()

    logger.info(f"Initiating Autonomy Discovery Engine Query...")
    
    # Delegated explicitly to the safe, centralized CLI wrapper (Neutralizes Injection Vectors)
    records = SFClient.execute_query(args.query)
    
    if records:
        logger.info(f"✅ Discovered {len(records)} active structural schema records.")
        # Natively pipe raw JSON output so LLM Agent workflows can iteratively parse responses downstream
        print(json.dumps(records, indent=2))
    else:
        logger.warning(f"⚠️ Zero matching configuration records isolated recursively.")

if __name__ == "__main__":
    main()
