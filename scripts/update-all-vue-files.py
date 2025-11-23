#!/usr/bin/env python3
import re
from pathlib import Path

def extract_lessons_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lessons = {}
    h3_pattern = r'<h3[^>]*><span class="section-number-3">[\d.]+</span>\s+Aula\s+(\d+)</h3>(.*?)(?=<h3[^>]*><span class="section-number-3">|<h2[^>]*>|$)'
    
    for match in re.finditer(h3_pattern, content, re.DOTALL):
        aula_num = int(match.group(1))
        lesson_html = match.group(2)
        
        subject_match = re.search(r'<li>([^:]+):\s*([^<]+)</li>', lesson_html)
        
        if subject_match:
            subject = subject_match.group(1).strip()
            topic = subject_match.group(2).strip()
        else:
            subject = "Geral"
            topic = f"Aula {aula_num}"
        
        lessons[aula_num] = {
            'number': aula_num,
            'subject': subject,
            'topic': topic,
            'content': lesson_html.strip(),
            'title': f"{subject}: {topic}"
        }
    
    return lessons

def update_vue_file(vue_file, lesson):
    """Update Vue file with lesson content."""
    try:
        content = vue_file.read_text(encoding='utf-8')
    except:
        print(f"   ⚠️  Could not read {vue_file.name}")
        return False
    
    # Clean lesson content - fix escapes
    lesson_html = lesson['content']
    # Escape backticks and template literals first
    lesson_html = lesson_html.replace('\\', '\\\\\\\\')  # Quadruple escape backslashes
    lesson_html = lesson_html.replace('`', '\\`')
    lesson_html = lesson_html.replace('${', '\\${')
    
    # Update title
    clean_title = lesson['title'].replace('"', '\\"').replace('\\\\', '\\')
    content = re.sub(r'const title = "[^"]*";', f'const title = "{clean_title}";', content)
    
    # Add or update lessonContent
    if 'lessonContent' not in content:
        script_addition = f'\nconst lessonContent = `{lesson_html}`;\n'
        content = re.sub(r'(const dates = \[.*?\];)', r'\1' + script_addition, content, flags=re.DOTALL)
    else:
        content = re.sub(
            r'const lessonContent = `.*?`;',
            f'const lessonContent = `{lesson_html}`;',
            content,
            flags=re.DOTALL
        )
    
    # Update template to use v-html
    if 'v-html="lessonContent"' not in content:
        content = re.sub(
            r'<p>Conteúdo da aula será adicionado aqui\.\.\.</p>',
            '<div class="lesson-content" v-html="lessonContent"></div>',
            content
        )
    
    try:
        vue_file.write_text(content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"   ❌ Error writing {vue_file.name}: {e}")
        return False

def main():
    base_dir = Path(__file__).parent.parent
    html_dir = base_dir / 'docs' / 'output' / 'html'
    vue_dir = base_dir / 'src' / 'views' / 'UFMG' / 'classes'
    
    # Extract all lessons indexed by aula number
    all_lessons = {}
    for week_num in range(1, 5):
        html_file = html_dir / f'material_semana{week_num}.html'
        if html_file.exists():
            print(f"📖 Extracting from {html_file.name}...")
            lessons = extract_lessons_from_html(html_file)
            all_lessons.update(lessons)
    
    print(f"\n📊 Total lessons available: {len(all_lessons)}")
    print(f"   Aulas: {min(all_lessons.keys())} to {max(all_lessons.keys())}")
    
    # Get all Vue files
    vue_files = sorted(vue_dir.glob('*.vue'))
    print(f"\n📁 Total Vue files: {len(vue_files)}")
    
    print(f"\n🔧 Updating ALL Vue files with matching content...")
    
    updated = 0
    skipped = 0
    failed = 0
    
    for vue_file in vue_files:
        # Try to extract aula number from filename
        # Patterns: mat-1.vue, fis-3-2.vue, qui-1-1.vue, etc.
        name = vue_file.stem
        
        # Try to find any number in the filename that could be an aula number
        # First, try to find explicit aula numbers (1-96)
        for aula_num in all_lessons.keys():
            # Check if this file could correspond to this aula
            # Simple heuristic: if filename contains the number
            if str(aula_num) in name.split('-'):
                lesson = all_lessons[aula_num]
                
                if update_vue_file(vue_file, lesson):
                    print(f"   ✓ {vue_file.name} ← Aula {aula_num}")
                    updated += 1
                else:
                    failed += 1
                break
        else:
            # No matching aula found
            skipped += 1
            print(f"   ⊘ {vue_file.name} (no matching aula)")
    
    print(f"\n" + "="*50)
    print(f"✅ Updated: {updated} files")
    print(f"⊘  Skipped: {skipped} files (no matching content)")
    print(f"❌ Failed:  {failed} files (errors)")
    print(f"="*50)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
