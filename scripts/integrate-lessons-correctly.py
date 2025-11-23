#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict

def extract_lessons_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lessons = []
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
        
        lessons.append({
            'number': aula_num,
            'subject': subject,
            'topic': topic,
            'content': lesson_html.strip(),
            'title': f"{subject}: {topic}"
        })
    
    return lessons

def subject_code_map(subject):
    mapping = {
        'Matemática': 'mat', 'Física': 'fis', 'Química': 'qui',
        'Geografia': 'geo', 'História': 'his', 'Biologia': 'bio',
        'Filosofia': 'fil', 'Sociologia': 'soc', 'Português': 'por'
    }
    return mapping.get(subject, 'gen')

def find_matching_vue_file(vue_dir, subject_code, aula_num):
    """Find existing Vue file that matches this lesson."""
    # Try patterns: subj-week-n.vue, subj-n.vue, subj-aula_num.vue
    patterns = [
        f"{subject_code}-*-*.vue",
        f"{subject_code}-*.vue"
    ]
    
    for pattern in patterns:
        matches = list(vue_dir.glob(pattern))
        for match in matches:
            # Check if this file needs content
            content = match.read_text(encoding='utf-8')
            if 'Conteúdo da aula será adicionado aqui' in content or 'lessonContent' not in content:
                return match
    
    return None

def update_vue_file(vue_file, lesson):
    """Update Vue file with lesson content."""
    content = vue_file.read_text(encoding='utf-8')
    
    # Clean lesson content
    lesson_html = lesson['content'].replace('`', '\\`').replace('${', '\\${')
    # Fix backslashes
    lesson_html = lesson_html.replace('\\', '\\\\')
    lesson_html = lesson_html.replace('\\\\`', '\\`')
    lesson_html = lesson_html.replace('\\\\${', '\\${')
    
    # Update metadata
    clean_title = lesson['title'].replace('"', '\\"')
    content = re.sub(r'const title = "[^"]*";', f'const title = "{clean_title}";', content)
    
    # Add lessonContent if not present
    if 'lessonContent' not in content:
        script_addition = f'\nconst lessonContent = `{lesson_html}`;\n'
        content = re.sub(r'(const dates = \[.*?\];)', r'\1' + script_addition, content, flags=re.DOTALL)
    else:
        # Replace existing lessonContent
        content = re.sub(
            r'const lessonContent = `.*?`;',
            f'const lessonContent = `{lesson_html}`;',
            content,
            flags=re.DOTALL
        )
    
    # Update template to use v-html if not already
    if 'v-html="lessonContent"' not in content:
        content = re.sub(
            r'<p>Conteúdo da aula será adicionado aqui\.\.\.</p>',
            '<div class="lesson-content" v-html="lessonContent"></div>',
            content
        )
    
    vue_file.write_text(content, encoding='utf-8')
    return True

def main():
    base_dir = Path(__file__).parent.parent
    html_dir = base_dir / 'docs' / 'output' / 'html'
    vue_dir = base_dir / 'src' / 'views' / 'UFMG' / 'classes'
    
    # Extract all lessons
    all_lessons = []
    for week_num in range(1, 5):
        html_file = html_dir / f'material_semana{week_num}.html'
        if html_file.exists():
            print(f"📖 Processing {html_file.name}...")
            lessons = extract_lessons_from_html(html_file)
            all_lessons.extend(lessons)
    
    print(f"\n📊 Total lessons: {len(all_lessons)}")
    
    # Group lessons by subject
    by_subject = defaultdict(list)
    for lesson in all_lessons:
        code = subject_code_map(lesson['subject'])
        by_subject[code].append(lesson)
    
    print(f"\n🔧 Updating existing Vue files...")
    
    updated = 0
    failed = []
    
    # For each subject, update files in order
    for subject_code, lessons in sorted(by_subject.items()):
        subject_lessons = sorted(lessons, key=lambda x: x['number'])
        print(f"\n{subject_code.upper()}: {len(subject_lessons)} lessons")
        
        for i, lesson in enumerate(subject_lessons, 1):
            # Find existing file pattern (e.g., mat-1-1, mat-1-2, etc.)
            possible_files = list(vue_dir.glob(f"{subject_code}-*-{i}.vue"))
            if not possible_files:
                possible_files = list(vue_dir.glob(f"{subject_code}-{i}.vue"))
            
            if possible_files:
                vue_file = possible_files[0]
                try:
                    update_vue_file(vue_file, lesson)
                    print(f"   ✓ Updated {vue_file.name} (Aula {lesson['number']})")
                    updated += 1
                except Exception as e:
                    print(f"   ❌ Failed {vue_file.name}: {e}")
                    failed.append(lesson['number'])
            else:
                print(f"   ⚠️  No file found for Aula {lesson['number']} ({subject_code}-{i})")
    
    print(f"\n✅ Updated: {updated} files")
    if failed:
        print(f"❌ Failed: {len(failed)} files - Aulas: {failed}")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
