#!/usr/bin/env python3
import argparse
import subprocess
import json
import os

def create_record(sobject, fields):
    # fields is a dict. Convert into space separated k=v for the sf command
    field_str = " ".join([f'"{k}={v}"' for k, v in fields.items()])
    cmd = f'sf data create record -s {sobject} -v "{field_str}" --json'
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        out = res.stdout
        json_start = out.find('{')
        if json_start != -1:
            data = json.loads(out[json_start:])
            if data.get('status') == 0:
                print(f"✅ Success: Created {sobject} with ID {data.get('result', {}).get('id')}")
            else:
                print(f"❌ Failed to create {sobject}: {data.get('message')}")
        else:
            print(f"❌ Failed to create {sobject}: {res.stderr}")
    except Exception as e:
        print(f"Execution Error creating {sobject}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Create CPQ declarative data records directly from JSON payloads seamlessly")
    parser.add_argument("--file", type=str, required=True, help="Path to JSON file containing records to create. Spec: [{'type': 'SObjectAPI', 'fields': {'Field': 'Value'}}]")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"File {args.file} not found.")
        return

    with open(args.file, 'r') as f:
        try:
            records = json.load(f)
            if not isinstance(records, list):
                print("JSON must contain a list of record objects.")
                return
            
            for rec in records:
                obj_type = rec.get("type")
                fields = rec.get("fields", {})
                if not obj_type or not fields:
                    print(f"Skipping invalid record format: {rec}")
                    continue
                create_record(obj_type, fields)
                
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")

if __name__ == "__main__":
    main()
