#!/usr/bin/env python3
"""
Script to remove :PROPERTIES: blocks from Org-mode files.
These are created by Pandoc but are visible in PDF exports.
"""

import re
import sys
from pathlib import Path

def remove_properties_blocks(content):
    """
    Remove all :PROPERTIES: ... :END: blocks from Org content.
    """
    
    # Pattern to match properties blocks including the lines they're on
    # :PROPERTIES:
    # :CUSTOM_ID: something
    # :END:
    properties_pattern = r':PROPERTIES:\n(?::.*\n)*:END:\n'
    
    # Remove all properties blocks
    modified_content = re.sub(properties_pattern, '', content)
    
    return modified_content

def process_file(file_path):
    """Process a single org file."""
    print(f"Processing {file_path.name}...")
    
    # Read the file
    content = file_path.read_text(encoding='utf-8')
    
    # Count properties blocks before
    blocks_before = len(re.findall(r':PROPERTIES:', content))
    
    # Remove properties blocks
    modified_content = remove_properties_blocks(content)
    
    # Write back
    file_path.write_text(modified_content, encoding='utf-8')
    
    blocks_after = len(re.findall(r':PROPERTIES:', modified_content))
    
    print(f"✓ {file_path.name} processed - removed {blocks_before - blocks_after} properties blocks")

def main():
    # Process all .org files in docs/org/
    org_dir = Path(__file__).parent.parent / 'docs' / 'org'
    
    files = sorted(org_dir.glob('material_*.org'))
    
    if not files:
        print("No material_*.org files found")
        return 1
    
    print(f"Found {len(files)} files to process\n")
    
    for file_path in files:
        process_file(file_path)
    
    print(f"\n✅ All files processed successfully!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
