#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import argparse
from datetime import datetime

def run_command(cmd, as_json=False):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if as_json:
            try:
                # sf CLI sometimes outputs text before the json if there are warnings
                # find the first '{' 
                out = result.stdout
                json_start = out.find('{')
                if json_start != -1:
                    return json.loads(out[json_start:])
                return {"status": "Error", "result": {"details": {"componentFailures": [{"problem": "CLI Output Parsing Error"}]}}}
            except json.JSONDecodeError:
                return {"status": "Error", "result": {"details": {"componentFailures": [{"problem": "JSON Decode Error"}]}}}
        return result.stdout
    except Exception as e:
        print(f"Error executing command {cmd}: {e}")
        return None

def get_modified_files():
    # Helper to get untracked and modified files via git
    status = run_command("git status --porcelain")
    files = []
    if status:
        for line in status.strip().split('\n'):
            if len(line) > 3:
                # ' M path', '?? path'
                file_path = line[3:].strip()
                if os.path.isfile(file_path):
                    files.append(file_path)
    return files

def prompt_selection(files):
    if not files:
        print("No modified or untracked files found to deploy.")
        return []
    
    print("\nModified/Untracked files:")
    for i, f in enumerate(files):
        print(f"[{i+1}] {f}")
    
    sel = input("\nEnter numbers of files to deploy (comma separated, e.g. 1,3) or 'all': ").strip()
    if sel.lower() == 'all':
        return files
    
    selected_files = []
    for s in sel.split(','):
        try:
            idx = int(s.strip()) - 1
            if 0 <= idx < len(files):
                selected_files.append(files[idx])
        except ValueError:
            pass
    return selected_files

def deploy_metadata(files):
    print(f"\nDeploying {len(files)} metadata components...")
    # sf project deploy start -d path1 -d path2 --json
    cmd = "sf project deploy start " + " ".join([f"-d \"{f}\"" for f in files]) + " --json"
    result = run_command(cmd, as_json=True)
    return result

def deploy_document(file_path):
    print(f"\nUploading document {file_path}...")
    title = os.path.basename(file_path).split('.')[0]
    cmd = f'sf data create record -s ContentVersion -v "Title=\'{title}\' PathOnClient=\'{file_path}\'" --json'
    result = run_command(cmd, as_json=True)
    return result

def generate_markdown_report(metadata_result, doc_results, mode):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = "docs/deployments"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"deployment_log_{timestamp}.md")
    
    lines = []
    lines.append(f"# CPQ Deployment Log - {timestamp}")
    lines.append(f"**Execution Mode:** {mode}")
    lines.append("")
    
    # Process metadata results
    if metadata_result:
        status = metadata_result.get('status', 'Unknown')
        lines.append(f"## Metadata Deployment (Status: {status})")
        if status == 0:
            lines.append("✅ **Success**")
        else:
            lines.append("❌ **Failed**")
        
        lines.append("")
        lines.append("| Component Name | Type | Status |")
        lines.append("|---|---|---|")
        
        details = metadata_result.get('result', {}).get('details', {}).get('componentSuccesses', [])
        for comp in details:
            if comp.get('componentType') != 'Package':
                name = comp.get('fullName', 'Unknown')
                ctype = comp.get('componentType', 'Unknown')
                cstatus = 'Changed' if comp.get('changed') else ('Created' if comp.get('created') else 'Unchanged')
                lines.append(f"| {name} | {ctype} | {cstatus} |")
                
        errors = metadata_result.get('result', {}).get('details', {}).get('componentFailures', [])
        if errors:
            lines.append("\n### Errors")
            for err in errors:
                lines.append(f"- **{err.get('fileName')}**: {err.get('problem')}")
    
    # Process document results
    if doc_results:
        lines.append("\n## Document Uploads")
        for f, res in doc_results.items():
            if res and res.get('status') == 0:
                cv_id = res.get('result', {}).get('id', 'Unknown')
                lines.append(f"- ✅ `{f}` -> ContentVersion ID: {cv_id}")
            else:
                lines.append(f"- ❌ `{f}` failed to upload.")
                
    with open(log_path, 'w') as f:
        f.write("\n".join(lines))
    print(f"\nDeployment documentation written to: {log_path}")

def main():
    parser = argparse.ArgumentParser(description="Automated CPQ Deployment Script")
    parser.add_argument('--manifest', type=str, help="Path to JSON manifest file for automated deployment")
    args = parser.parse_args()
    
    files_to_deploy = []
    mode = "Interactive"
    
    if args.manifest:
        mode = f"Config-Driven ({args.manifest})"
        try:
            with open(args.manifest, 'r') as f:
                data = json.load(f)
                files_to_deploy = data.get("files", [])
        except Exception as e:
            print(f"Error reading manifest: {e}")
            sys.exit(1)
    else:
        candidates = get_modified_files()
        files_to_deploy = prompt_selection(candidates)
        
    if not files_to_deploy:
        print("No files selected for deployment. Exiting.")
        sys.exit(0)
        
    metadata_files = []
    document_files = []
    
    # Simple split based on extension
    doc_extensions = ['.docx', '.pdf', '.rtf', '.txt']
    for f in files_to_deploy:
        ext = os.path.splitext(f)[1].lower()
        if ext in doc_extensions:
            document_files.append(f)
        else:
            metadata_files.append(f)
            
    meta_result = None
    doc_results = {}
    
    if metadata_files:
        meta_result = deploy_metadata(metadata_files)
        
    if document_files:
        for df in document_files:
            doc_results[df] = deploy_document(df)
            
    generate_markdown_report(meta_result, doc_results, mode)

if __name__ == "__main__":
    main()
