#!/usr/bin/env python3
import subprocess
import json
import logging
from typing import List, Dict, Any

# Standardize Enterprise Logging Level
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] CPQ_AGENCY: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class SFClient:
    """Universal Salesforce CLI Driver. Inherently prevents OS shell injection."""
    
    @staticmethod
    def execute_query(query: str) -> List[Dict[str, Any]]:
        """Executes a SOQL query safely using strict argument arrays (shell=False)."""
        logger.debug(f"Executing explicit SOQL payload.")
        
        # Mitigate Shell Injection: Pass distinct isolated list arguments
        cmd = ["sf", "data", "query", "-q", query, "-t", "--json"]
        
        try:
            # shell=False ensures the command and arguments are strictly compartmentalized, neutralizing `rm -rf` injections
            res = subprocess.run(cmd, shell=False, capture_output=True, text=True, check=True)
            out = res.stdout
            json_start = out.find('{')
            if json_start != -1:
                data = json.loads(out[json_start:])
                if data.get('status') == 0:
                    return data.get('result', {}).get('records', [])
        except subprocess.CalledProcessError as e:
            logger.error(f"SFDX Execution Payload Failed: {e.stderr}")
        except Exception as e:
            logger.error(f"Failed to cleanly parse SFDX JSON framework: {str(e)}")
        
        return []

    @staticmethod
    def execute_command(cmd_args: List[str]) -> bool:
        """Executes a generic SF command safely without arbitrary contextual shell boundaries."""
        try:
            subprocess.run(cmd_args, shell=False, check=True)
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Command execution framework aborted natively: {e}")
            return False
            
# Expose standardized logger for ecosystem inheritance
__all__ = ['SFClient', 'logger']
