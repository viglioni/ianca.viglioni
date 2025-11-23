#!/usr/bin/env python3
import re
from pathlib import Path

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

def create_vue_component(lesson, vue_template):
    subject_code = subject_code_map(lesson['subject'])
    vue_filename = f"{subject_code}-{lesson['number']}.vue"
    
    template = vue_template
    clean_title = lesson['title'].replace('"', '\\"')
    
    template = re.sub(r'const code = "[^"]*";', f'const code = "{subject_code}-{lesson["number"]}";', template)
    template = re.sub(r'const title = "[^"]*";', f'const title = "{clean_title}";', template)
    template = re.sub(r'const subject = "[^"]*";', f'const subject = "{lesson["subject"].lower()}";', template)
    
    content = lesson['content'].replace('`', '\\`').replace('${', '\\${')
    script_addition = f'\nconst lessonContent = `{content}`;\n'
    
    template = re.sub(r'(const dates = \[.*?\];)', r'\1' + script_addition, template, flags=re.DOTALL)
    
    content_section = '''      <section class="class-section">
        <h2>Conteúdo</h2>
        <div class="lesson-content" v-html="lessonContent"></div>
      </section>'''
    
    template = re.sub(r'<section class="class-section">\s*<h2>Conteúdo</h2>.*?</section>', content_section, template, flags=re.DOTALL)
    
    return vue_filename, template

def main():
    base_dir = Path(__file__).parent.parent
    html_dir = base_dir / 'docs' / 'output' / 'html'
    vue_dir = base_dir / 'src' / 'views' / 'UFMG' / 'classes'
    
    template_file = vue_dir / 'mat-1-1.vue'
    vue_template = template_file.read_text(encoding='utf-8')
    
    all_lessons = []
    for week_num in range(1, 5):
        html_file = html_dir / f'material_semana{week_num}.html'
        if html_file.exists():
            print(f"📖 Processing {html_file.name}...")
            lessons = extract_lessons_from_html(html_file)
            all_lessons.extend(lessons)
            print(f"   Found {len(lessons)} lessons")
    
    print(f"\n📊 Total: {len(all_lessons)} lessons\n🔧 Generating Vue components...")
    
    created, updated = 0, 0
    for lesson in all_lessons:
        try:
            vue_filename, vue_content = create_vue_component(lesson, vue_template)
            vue_path = vue_dir / vue_filename
            
            if vue_path.exists():
                updated += 1
            else:
                created += 1
            
            vue_path.write_text(vue_content, encoding='utf-8')
            print(f"   ✓ {vue_filename} (Aula {lesson['number']})")
        except Exception as e:
            print(f"   ❌ Aula {lesson['number']}: {e}")
    
    print(f"\n✅ Created: {created}, Updated: {updated}")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
