#!/usr/bin/env python3
"""
Script to remove hyperlinks from Markdown files for PDF generation.
Converts [text](url) to just text.
"""

import re
import sys
from pathlib import Path

def remove_hyperlinks(content):
    """
    Remove all markdown hyperlinks, keeping only the text.
    [text](url) -> text
    """
    
    # Pattern to match [text](url) and replace with just text
    # This will keep the link text but remove the URL
    link_pattern = r'\[([^\]]+)\]\([^\)]+\)'
    
    # Replace links with just the text
    modified_content = re.sub(link_pattern, r'\1', content)
    
    return modified_content

def process_file(file_path):
    """Process a single markdown file."""
    print(f"Processing {file_path.name}...")
    
    # Read the file
    content = file_path.read_text(encoding='utf-8')
    
    # Count links before
    links_before = len(re.findall(r'\[([^\]]+)\]\([^\)]+\)', content))
    
    # Remove hyperlinks
    modified_content = remove_hyperlinks(content)
    
    # Write back
    file_path.write_text(modified_content, encoding='utf-8')
    
    print(f"✓ {file_path.name} processed - removed {links_before} hyperlinks")

def main():
    # Process all material_semana*.md files
    docs_dir = Path(__file__).parent.parent / 'docs'
    
    files = sorted(docs_dir.glob('material_semana*.md'))
    
    if not files:
        print("No material_semana*.md files found")
        return 1
    
    print(f"Found {len(files)} files to process\n")
    
    total_removed = 0
    for file_path in files:
        # Count links before processing
        content = file_path.read_text(encoding='utf-8')
        links_count = len(re.findall(r'\[([^\]]+)\]\([^\)]+\)', content))
        total_removed += links_count
        
        process_file(file_path)
    
    print(f"\n✅ All files processed successfully!")
    print(f"Total hyperlinks removed: {total_removed}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
