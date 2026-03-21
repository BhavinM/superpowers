# CPQ Automated Deployment Script Design

## Goal
Create a Python script (`cpq_deploy.py`) that acts as a wrapper for the Salesforce CLI (`sf`). It will automate the deployment of CPQ metadata (Apex Callbacks, Layouts, Price Rules) and Document templates (for Conga Composer/Quote Generation), while providing a zero-friction developer experience by automatically logging all changes.

## Architecture

The script will be a standalone Python utility located at `scripts/deployment/cpq_deploy.py`. It requires Python 3+ and the Salesforce CLI (`sf` / `sfdx`). 

### Core Modes of Operation
To satisfy both developer-driven deployments and CI/CD pipelines, the tool supports two modes:

1. **Interactive Mode (Default)**
   - The script scans the local `force-app` directory (or runs `git diff`) to present a multi-select list of modified or untracked files.
   - The user selects the exact files to deploy using arrow keys and the spacebar (via `inquirer` or simple numbered CLI).
   - Generates a dynamic `package.xml` or passes the files to `sf project deploy start --source-dir ...`.

2. **Config-Driven Mode (Flag: `--manifest`)**
   - The user executes `python cpq_deploy.py --manifest deploy_manifest.json`.
   - The script bypasses the UI, reads the direct file paths from the JSON configuration, and executes the deployment.

### Features
- **Dynamic package.xml Generation:** Converts selected files into a standard Salesforce `package.xml` structure for deployment validity.
- **Document Upload Logic:** 
  - Deploying Conga Templates/Documents via metadata API lacks data context. The script identifies if a selected file is a binary document (e.g., `.docx`, `.pdf` inside a specific quotes/templates folder).
  - It triggers `sf data create record -s ContentVersion` or `Document` via the REST API rather than the Metadata API, linking the document to the correct CPQ Workspace if mapped.
- **Auto-Documentation (The "Deployment Log")**
  - Appends `--json` to all `sf project deploy start` commands.
  - Parses the JSON output to identify successful deployments, failures, and component types.
  - Generates a markdown file: `docs/deployments/deployment_log_YYYYMMDD_HHMMSS.md`.
  - Content includes: Start time, Execution Mode, Status, Table of Deployed Components, and Execution Time.

## Data Flow
1. User executes `python cpq_deploy.py`.
2. Script detects untracked/modified CPQ metadata.
3. User selects `[x] CustomPricingCallback.cls` and `[x] Master_Quote_Template.docx`.
4. Script splits execution:
   - Uses `sf project deploy` for `CustomPricingCallback.cls` using `--json`.
   - Uses `sf data create record` for `Master_Quote_Template.docx`.
5. Script aggregates all JSON responses.
6. Script outputs `docs/deployments/deployment_log_YYYYMMDD_HHMMSS.md`.

## Tech Stack
- **Python 3.x**
- **Libraries:** `subprocess` (shell exec), `json` (parsing sf cli), `os`/`sys` (pathing). Avoid heavy external dependencies to keep it portable, but allow `inquirer` for the UI if installed.
