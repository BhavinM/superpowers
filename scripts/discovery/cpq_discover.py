#!/usr/bin/env python3
import argparse
import subprocess
import json

def run_query(query):
    cmd = f'sf data query -q "{query}" --json'
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        # Parse output safely skipping any warnings SF CLI might throw before JSON
        out = result.stdout
        json_start = out.find('{')
        if json_start != -1:
            data = json.loads(out[json_start:])
            if data.get('status') == 0:
                # Return simplified records
                return json.dumps(data.get('result', {}).get('records', []), indent=2)
            else:
                return f"Error: {data.get('message')}"
        return f"Unknown error or non-JSON output. Stderr: {result.stderr}"
    except Exception as e:
        return f"Execution error: {e}"

def main():
    parser = argparse.ArgumentParser(description="Autonomously query CPQ data context")
    parser.add_argument("--query", type=str, required=True, help="SOQL query to execute (e.g. \"SELECT Id, Name FROM Apttus_Config2__PriceList__c\")")
    args = parser.parse_args()
    
    print(run_query(args.query))

if __name__ == "__main__":
    main()
