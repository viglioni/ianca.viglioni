#!/usr/bin/env python3
"""
Script to extract inline answers and move them to a separate section at the end of the document.
"""

import re
import sys
from pathlib import Path

def extract_and_move_respostas(content):
    """
    Extract all **Respostas:** lines and move them to the end.
    Replace them with a reference number in the original location.
    """
    
    # Find all respostas with their context
    respostas = []
    answer_counter = 1
    
    # Pattern to find respostas lines
    resposta_pattern = r'\*\*Respostas?:\*\*[^\n]+'
    
    def replace_resposta(match):
        nonlocal answer_counter
        resposta_text = match.group(0)
        
        # Store the answer with its number and context
        # Try to find the exercise/aula number from nearby context
        respostas.append({
            'num': answer_counter,
            'text': resposta_text.replace('**Respostas:**', '').replace('**Resposta:**', '').strip()
        })
        
        # Replace with reference
        replacement = f'*[Ver resposta {answer_counter} no final do documento]*'
        answer_counter += 1
        return replacement
    
    # Replace all respostas and collect them
    modified_content = re.sub(resposta_pattern, replace_resposta, content)
    
    # If we found any respostas, add a section at the end
    if respostas:
        # Find where to insert (before the final summary/checklist if present)
        # Look for the last ## heading
        lines = modified_content.split('\n')
        
        # Find the position before the last summary section
        insert_pos = len(lines)
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].startswith('**O que você estudou'):
                insert_pos = i
                break
        
        # Build respostas section
        respostas_section = [
            '',
            '---',
            '',
            '# Respostas dos Exercícios',
            ''
        ]
        
        for resp in respostas:
            respostas_section.append(f"**{resp['num']}.** {resp['text']}")
            respostas_section.append('')
        
        # Insert the section
        lines = lines[:insert_pos] + respostas_section + lines[insert_pos:]
        modified_content = '\n'.join(lines)
    
    return modified_content

def process_file(file_path):
    """Process a single markdown file."""
    print(f"Processing {file_path.name}...")
    
    # Read the file
    content = file_path.read_text(encoding='utf-8')
    
    # Extract and move respostas
    modified_content = extract_and_move_respostas(content)
    
    # Write back
    file_path.write_text(modified_content, encoding='utf-8')
    
    print(f"✓ {file_path.name} processed successfully")

def main():
    # Process all material_semana*.md files
    docs_dir = Path(__file__).parent.parent / 'docs'
    
    files = sorted(docs_dir.glob('material_semana*.md'))
    
    if not files:
        print("No material_semana*.md files found")
        return 1
    
    print(f"Found {len(files)} files to process\n")
    
    for file_path in files:
        process_file(file_path)
    
    print(f"\n✅ All files processed successfully!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
