#!/usr/bin/env python3
import re
import os

def mask_pii_and_prices(markdown_text):
    # Mask explicitly tracked PII or Account Names (Simulated regex)
    masked = re.sub(r'Account: ([A-Za-z0-9\s]+)', r'Account: [REDACTED_SECURE_CORP_ENTITY]', markdown_text)
    
    # Mask raw list prices out of CPQ rules to prevent LLM Scraping/Training
    masked = re.sub(r'ListPrice: \$[0-9,\.]+', r'ListPrice: $[REDACTED_FINANCIAL_VALUE]', masked)
    
    # Mask Email Addresses and Contact Names parsed in generated quotes
    masked = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', r'[REDACTED_EMAIL_ADDRESS]', masked)
    
    return masked

def execute_masking_pipeline(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r') as f:
        data = f.read()
        
    secure_data = mask_pii_and_prices(data)
    
    with open(filepath, 'w') as f:
        f.write(secure_data)
        
    print(f"🔒 Data InfoSec Masking Complete. Compliance applied to RAG Context: {filepath}.")

if __name__ == "__main__":
    # Test execution
    print("CPQ Masking Utility loaded successfully.")
