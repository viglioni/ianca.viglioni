#!/usr/bin/env python3
import re
from pathlib import Path

def fix_content_escapes(content):
    """Fix problematic escape sequences in content."""
    # Escape backslashes that aren't already escaped
    content = content.replace('\\', '\\\\')
    # But fix double-escaping of already escaped chars
    content = content.replace('\\\\`', '\\`')
    content = content.replace('\\\\${', '\\${')
    return content

def extract_and_fix_lesson(html_file, aula_num):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = f'<h3[^>]*><span class="section-number-3">[\d.]+</span>\\s+Aula\\s+{aula_num}</h3>(.*?)(?=<h3[^>]*><span class="section-number-3">|<h2[^>]*>|$)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        return fix_content_escapes(match.group(1).strip())
    return None

base_dir = Path(__file__).parent.parent
html_dir = base_dir / 'docs' / 'output' / 'html'
vue_dir = base_dir / 'src' / 'views' / 'UFMG' / 'classes'

# Fix Aula 26 and 30
for aula_num in [26, 30]:
    week = 1 if aula_num <= 29 else 2
    html_file = html_dir / f'material_semana{week}.html'
    
    fixed_content = extract_and_fix_lesson(html_file, aula_num)
    
    if fixed_content:
        # Find existing vue file for this lesson
        vue_files = list(vue_dir.glob(f'*-{aula_num}.vue'))
        
        if vue_files:
            vue_file = vue_files[0]
            content = vue_file.read_text(encoding='utf-8')
            
            # Replace lessonContent
            new_content = re.sub(
                r'const lessonContent = `.*?`;',
                f'const lessonContent = `{fixed_content}`;',
                content,
                flags=re.DOTALL
            )
            
            vue_file.write_text(new_content, encoding='utf-8')
            print(f"✓ Fixed {vue_file.name}")
        else:
            print(f"❌ No Vue file found for Aula {aula_num}")
    else:
        print(f"❌ Could not extract Aula {aula_num}")

print("\n✅ Escape errors fixed!")
