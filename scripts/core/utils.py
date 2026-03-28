#!/usr/bin/env python3

def minify_json_payload(data):
    """Recursively strip nulls and standard Salesforce Audit metadata fields to conserve generative AI contextual limits universally."""
    audit_fields = {'attributes', 'CreatedDate', 'CreatedById', 'LastModifiedDate', 'LastModifiedById', 'SystemModstamp', 'IsDeleted'}
    
    if isinstance(data, dict):
        return {k: minify_json_payload(v) for k, v in data.items() if v is not None and k not in audit_fields}
    elif isinstance(data, list):
        return [minify_json_payload(v) for v in data if v is not None]
    else:
        return data
