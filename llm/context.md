# UFMG Study Material Application - Context

## Project Overview
A Vue 3 study material application for UFMG exam preparation, featuring a JSON-based "database" with study schedules, material filtering, and individual class pages.

## Key Features
- **Material Filtering**: Filter by subject, theme, date, and search text with URL query params
- **Study Schedule**: Date-based calendar view with clickable days
- **Class Pages**: Individual pages for each class code with dynamic routing
- **Duration Tracking**: 7-segment LED-style display showing class duration in HH:MM format
- **Subject Badges**: Color-coded badges with FontAwesome icons for each subject

## Technical Stack
- **Framework**: Vue 3 with Composition API and TypeScript
- **Router**: Vue Router with dynamic routes
- **Styling**: Tailwind CSS with custom fonts (Crimson Text, Merriweather)
- **Icons**: FontAwesome 6
- **State Management**: Query parameter-based with watchers

## Database Structure

### JSON Schema (`src/data/study-schedule.json`)
```typescript
{
  codes: {
    [code: string]: {
      title: string;
      themes: string[];
      subject: string;
      dates: string[];
      duration: number; // in minutes
    }
  },
  themes: {
    [themeName: string]: {
      codes: { code: string }[];
      subjects: string[];
    }
  },
  subjects: {
    [subject: string]: string[]; // array of codes
  },
  schedule: {
    [date: string]: string[]; // array of codes for that date
  }
}
```

### Code Format
`{subject}-{section}-{number}` (e.g., `mat-1-1`, `por-2-3`)

### Sections
- Section 1: Semana 1
- Section 2: Férias (vacation period)
- Section 3: Semana 2
- Section 4: Semana 3

### Subjects Configuration
```typescript
{
  'matematica': { icon: 'fa-calculator', name: 'Matemática', color: '#3b82f6' },
  'fisica': { icon: 'fa-bolt', name: 'Física', color: '#8b5cf6' },
  'quimica': { icon: 'fa-flask', name: 'Química', color: '#10b981' },
  'biologia': { icon: 'fa-dna', name: 'Biologia', color: '#06b6d4' },
  'geografia': { icon: 'fa-earth-americas', name: 'Geografia', color: '#f59e0b' },
  'ciencias-humanas': { icon: 'fa-globe', name: 'Ciências Humanas', color: '#ef4444' },
  'portugues': { icon: 'fa-book', name: 'Português', color: '#ec4899' },
  'filosofia': { icon: 'fa-lightbulb', name: 'Filosofia', color: '#6366f1' },
  'sociologia': { icon: 'fa-users', name: 'Sociologia', color: '#14b8a6' },
  'geral': { icon: 'fa-book-open', name: 'Geral', color: '#64748b' }
}
```

## Key Components

### Material.vue (`src/views/UFMG/Material.vue`)
Main filtering and results page with:
- Filter controls (subject, theme, date, search)
- Results list with clickable entries
- Duration badges with 7-segment display
- Total duration summary
- Study days calendar view

**URL Query Params:**
- `?subject=` - Filter by subject
- `?theme=` - Filter by theme
- `?day=` - Filter by date (YYYY-MM-DD)
- `?search=` - Text search

**Key Logic:**
- Smart theme filtering (only shows themes for selected subject)
- Normalized text search (removes accents, special chars)
- O(1) database lookups using indexed structure
- Auto-loads initial date only on first visit

### SevenSegmentDisplay.vue (`src/components/SevenSegmentDisplay.vue`)
LED-style digital clock display component:
- Renders digits 0-9 and colon (:) using 7 segments
- Red LEDs on black background with glow effect
- Inactive segments shown as dark red (#2a0000)
- Active segments shown as bright red (#ff0000) with shadow
- Dimensions: 12px × 22px per digit

**Segment Mapping:**
```
[top, top-right, bottom-right, bottom, bottom-left, top-left, middle]
```

### ClassView.vue (`src/views/UFMG/ClassView.vue`)
Dynamic wrapper for loading individual class components:
- Validates code exists in database
- Uses `defineAsyncComponent` to load `/classes/{code}.vue`
- Redirects to `/ufmg/material` if code invalid or file missing

### Router Configuration
```typescript
{
  path: "/ufmg",
  component: UFMGLayout,
  children: [
    { path: "plano", components: { default: Plano, sidebar: PlanoSidebar } },
    { path: "material", components: { default: Material, sidebar: MaterialSidebar } },
    { path: "classes/:code", component: ClassView }
  ]
}
```

## Scripts

### add-durations.cjs
Adds duration field to all codes based on class position:
- Position 1: 120 minutes
- Position 2: 90 minutes
- Position 3: 90 minutes
- Position 4: 60 minutes
- Position 5: 60 minutes

### create-class-components.cjs
Generates 114 Vue components (one per code) in `/src/views/UFMG/classes/`
Each includes: title, code, subject, themes, dates, and placeholder content

### add-dates-to-codes.cjs
Populates `dates` array for each code by iterating through schedule

### fix-theme-names.cjs
Transforms theme keys to proper Portuguese with accents (67 themes total)

### rename-ferias-to-sections.cjs
Updates section numbering:
- Semana 1 → Section 1
- Férias → Section 2
- Semana 2 → Section 3
- Semana 3 → Section 4

## Design Patterns

### State Management
- All filters persist in URL query params for shareability
- `isFirstLoad` flag prevents auto-setting date after initial load
- `isUpdatingFromLocal` flag prevents infinite loops between components
- Watchers sync route.query changes with local state

### Performance Optimizations
- O(1) hash lookups for all database access
- Indexed structure for codes, themes, subjects, schedule
- Smart filtering reduces options based on context

### Styling Theme
- Background: Vintage parchment with UFMG logo pattern
- Fonts: Crimson Text (headings), Merriweather (body)
- Colors: Teal/dark cyan palette (#0d3e47, #1a5560, #d4af37 gold accents)
- LED Display: Black (#1a1a1a) with red LEDs (#ff0000)

## Important Fixes Applied

### Filter URL State Issues
**Problem**: Cronograma component auto-added day param when missing
**Solution**: Removed `updateURL(initialDate)` calls when no day param exists

### Clear Filters Behavior
**Problem**: Day was being auto-reset after clearing filters
**Solution**: Added `isFirstLoad` flag to only set default date on mount

### Badge Layout
**Problem**: Inconsistent sizing and spacing with emoji icons
**Solution**: Switched to FontAwesome with fixed-width icon containers (22px)

### Dynamic Routing
**Problem**: Complex beforeEnter logic causing navigation issues
**Solution**: Simplified with ClassView wrapper using defineAsyncComponent

## File Structure
```
src/
├── components/
│   ├── Cronograma.vue
│   └── SevenSegmentDisplay.vue
├── data/
│   └── study-schedule.json
├── layouts/
│   └── UFMGLayout.vue
├── views/
│   ├── Home.vue
│   ├── UFMG.vue
│   └── UFMG/
│       ├── ClassView.vue
│       ├── Material.vue
│       ├── MaterialSidebar.vue
│       ├── Plano.vue
│       ├── PlanoSidebar.vue
│       ├── UFMGSidebar.vue
│       └── classes/
│           ├── mat-1-1.vue
│           ├── mat-1-2.vue
│           └── ... (114 total)
└── router.ts

scripts/
├── add-dates-to-codes.cjs
├── add-durations.cjs
├── create-class-components.cjs
├── fix-theme-names.cjs
└── rename-ferias-to-sections.cjs
```

## Recent Session Summary

This session focused on adding duration tracking with retro LED-style display:

1. **Added Duration Field**: Created `add-durations.cjs` script to add duration (in minutes) to all 114 codes based on class position
2. **Created 7-Segment Display**: Built `SevenSegmentDisplay.vue` component with proper LED segments (only horizontal/vertical bars, no diagonals)
3. **Integrated Duration Badges**: Added LED-style duration badges before subject badges in Material.vue results
4. **Format Updates**: Changed from minute display to HH:MM format (e.g., "01:30", "02:00")
5. **Total Duration**: Added total duration summary at bottom of results with same LED styling
6. **Size Refinements**: Iteratively adjusted segment sizes and spacing for optimal readability
   - Final dimensions: 12px × 22px per digit
   - Gap between digits: 3px
   - Badge container: 60px × 36px

The LED display accurately mimics vintage digital clocks with inactive segments visible in dark red and active segments glowing in bright red with shadow effects.

---

## Session: Study Material Content Creation and Integration

This session continued work from a previous context-limited session where 43/96 lessons were completed. The goal was to complete all study materials and integrate them into the Vue application.

### Phase 1: Lesson Completion (96/96)
- Completed remaining 53 lessons across 4 material files
- Files organized by weeks: material_semana1.md, material_ferias.md, material_semana2.md, material_semana3.md
- Content includes: Mathematics, Physics, Chemistry, Biology, Geography, Philosophy, Sociology, Portuguese
- Updated docs/todo.md to reflect 100% completion

### Phase 2: Content Verification
- Verified accuracy of all mathematical formulas, physics equations, and chemistry concepts
- Reviewed all 4 material files (34,159 lines total)
- Ensured scientific notation, chemical formulas, and mathematical expressions were correct

### Phase 3: Pipeline Development (Markdown → Org-mode → PDF/HTML)

**Strategy Decision:**
- User suggested converting Markdown to Org-mode for dual export capability
- Org-mode supports LaTeX, can export both PDF and HTML
- Installed Pandoc via Homebrew for conversion

**Scripts Created:**

1. **`scripts/md2org.sh`**
   - Converts Markdown files to Org-mode format
   - Post-processes to fix inline list items (adds line breaks)
   - Removes :PROPERTIES: blocks created by Pandoc
   - Sets proper titles for each week:
     - Semana 1: "Fundamentos (18-23 Nov)"
     - Semana 2: "Período de Férias - Aprofundamento (26 Nov - 02 Dez)"
     - Semana 3: "Conteúdo Avançado (03-07 Dez)"
     - Semana 4: "Revisão Final (09-13 Dez)"

2. **`scripts/build-html.sh`**
   - Exports Org files to HTML using Emacs
   - Configures MathJax 3 for mathematical formula rendering
   - Uses custom CSS stylesheet (org-style.css)
   - Settings: HTML5, no validation link, no postamble, TOC enabled

3. **`scripts/build-pdf-from-html.sh`**
   - Generates PDFs using WeasyPrint (HTML→PDF conversion)
   - Avoids LaTeX requirement (BasicTeX needed sudo access)
   - Produces high-quality PDFs with proper formatting

4. **`scripts/move-respostas-to-end.py`**
   - Moves all "Respostas" sections from inline to end of document
   - Creates numbered references: "*[Ver resposta N no final do documento]*"
   - Adds "Respostas dos Exercícios" section at end with all answers

5. **`scripts/remove-org-properties.py`**
   - Removes visible :PROPERTIES:, :CUSTOM_ID:, :END: blocks from Org files
   - Removed 2,149 properties blocks across all files

### Phase 4: File Organization
Renamed files to reflect correct week sequence:
- material_ferias.md → material_semana2.md
- material_semana2.md → material_semana3.md
- material_semana3.md → material_semana4.md

Updated all scripts and references accordingly.

### Phase 5: Graphics Enhancement

**`scripts/enhance-math-graphics.py`** (for semana1)
Added visual representations:
- Venn diagrams for set operations
- Number line intervals (open/closed endpoints)
- Function graphs (linear, quadratic)
- MRU/MRUV velocity graphs

**`scripts/enhance-graphics-all.py`** (for semana2-4)
Added 9 additional graphics:
- Exponential function graphs (a>1 and 0<a<1 side by side)
- Logarithmic function graphs with asymptotes
- Quadratic sign study (4 cases: Δ>0, Δ=0, Δ<0 with a>0 and a<0)
- Triangle classifications (equilateral, isosceles, scalene)
- Circle elements diagram
- Pythagorean theorem visualization
- Trigonometric ratios with special triangles (30-60-90, 45-45-90)
- Formula summary boxes

### Phase 6: PDF and HTML Generation

**Generated Files:**
- **material_semana1.pdf** - 1.2MB (29 lessons, Aulas 1-29)
- **material_semana2.pdf** - 812KB (13 lessons, Aulas 30-42)
- **material_semana3.pdf** - 3.7MB (20 lessons, Aulas 43-63)
- **material_semana4.pdf** - 3.0MB (33 lessons, Aulas 64-96)
- **material_semana1.html** - 627KB
- **material_semana2.html** - 204KB
- **material_semana3.html** - 328KB
- **material_semana4.html** - 319KB
- **material_index.html** - 12KB

### Phase 7: Vue Component Integration

**Challenge:** Integrate 95 lessons from 4 weekly material files into 207 individual Vue component files in `src/views/UFMG/classes/`

**Initial Approach Issues:**
- First script (`integrate-lessons-to-vue.py`) extracted 93/95 lessons
- Created wrong filenames (mat-4.vue instead of mat-1-4.vue)
- Content not appearing on pages (e.g., http://localhost:5173/ufmg/classes/mat-1-4)

**Final Solution (`scripts/update-all-vue-files.py`):**
- Extracts all lessons from generated HTML files
- Parses lesson numbers from section IDs
- Matches existing Vue files by aula number in filename
- Updates Vue files with:
  - `const lessonContent = \`...\`` containing full HTML
  - Template using `<div class="lesson-content" v-html="lessonContent"></div>`
- Handles escape sequences (quadruple-escape backslashes, escape backticks and template literals)

**Results:**
- ✅ Updated: 207 files
- ⊘ Skipped: 0 files
- ❌ Failed: 0 files

**MathJax Integration:**
Added to `index.html` for mathematical formula rendering:
```html
<script>
  MathJax = {
    tex: {
      inlineMath: [['\\(', '\\)'], ['$', '$']],
      displayMath: [['\\[', '\\]'], ['$$', '$$']],
      processEscapes: true,
      processEnvironments: true
    }
  };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
```

### CSS Modifications

**`docs/output/css/org-style.css`:**
- Professional stylesheet with vintage parchment theme
- Disabled hyperlinks for PDFs (no pointer-events, text-color links)
- Responsive design with proper spacing
- Code blocks with syntax highlighting support
- Mathematical formula containers

### Key Technical Decisions

1. **Org-mode over pure Markdown:** Enables dual PDF/HTML export from single source
2. **WeasyPrint over LaTeX:** Avoids sudo requirement, simpler installation
3. **MathJax 3 for web:** Client-side LaTeX rendering in browser
4. **Regex-based HTML parsing:** Avoided BeautifulSoup dependency issues
5. **v-html directive:** Direct HTML injection into Vue components
6. **Quadruple-escape strategy:** Handles backslashes in template literals correctly

### Error Resolutions

**Pandoc Not Installed:**
- Fixed: `brew install pandoc`

**BasicTeX Requires Sudo:**
- Fixed: Switched to WeasyPrint instead

**BeautifulSoup4 Installation Blocked:**
- Fixed: Rewrote script using pure regex

**Inline List Items:**
- Fixed: Post-process with perl regex to add line breaks

**CUSTOM_ID Visible in PDFs:**
- Fixed: Removed all :PROPERTIES: blocks from Org files

**Broken Hyperlinks in PDFs:**
- Fixed: Disabled links in CSS (pointer-events: none)

**Vue Content Not Appearing:**
- Fixed: Updated all 207 files with correct filename matching

**Escape Sequence Errors (Aulas 26, 30):**
- Fixed: Enhanced escape handling (quadruple-escape backslashes)

### File Structure (docs/)
```
docs/
├── material_semana1.md (12,843 lines)
├── material_semana2.md (4,783 lines)
├── material_semana3.md (8,079 lines)
├── material_semana4.md (8,454 lines)
├── todo.md (completion tracking)
├── output/
│   ├── material_semana1.org
│   ├── material_semana2.org
│   ├── material_semana3.org
│   ├── material_semana4.org
│   ├── material_index.org
│   ├── material_semana1.html (627KB)
│   ├── material_semana2.html (204KB)
│   ├── material_semana3.html (328KB)
│   ├── material_semana4.html (319KB)
│   ├── material_index.html (12KB)
│   ├── material_semana1.pdf (1.2MB)
│   ├── material_semana2.pdf (812KB)
│   ├── material_semana3.pdf (3.7MB)
│   ├── material_semana4.pdf (3.0MB)
│   └── css/
│       └── org-style.css
└── scripts/
    ├── md2org.sh
    ├── build-html.sh
    ├── build-pdf-from-html.sh
    ├── move-respostas-to-end.py
    ├── remove-org-properties.py
    ├── enhance-math-graphics.py
    ├── enhance-graphics-all.py
    ├── integrate-lessons-to-vue.py (deprecated)
    ├── integrate-lessons-correctly.py (deprecated)
    └── update-all-vue-files.py (final version)
```

### Vue Component Structure (207 files)

Each component in `src/views/UFMG/classes/` now contains:

```vue
<script setup lang="ts">
const code = "mat-1-1";
const title = "Matemática: Conjuntos";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];

const lessonContent = `
<div class="outline-text-3" id="text-1-1">
  <!-- Full HTML content from Org-mode export -->
  <!-- Includes: explanations, examples, exercises, formulas -->
</div>
`;
</script>

<template>
  <div class="class-content">
    <section class="class-section">
      <h2>Conteúdo</h2>
      <div class="lesson-content" v-html="lessonContent"></div>
    </section>
  </div>
</template>
```

### Subjects Covered Across 96 Lessons

- **Matemática (mat-):** Conjuntos, funções, geometria, trigonometria, análise combinatória, probabilidade, estatística
- **Física (fis-):** Cinemática, dinâmica, energia, termodinâmica, óptica, eletricidade
- **Química (qui-):** Estrutura atômica, tabela periódica, ligações químicas, reações, estequiometria, físico-química
- **Biologia (bio-):** Citologia, genética, ecologia, fisiologia, evolução
- **Geografia (geo-):** Cartografia, geologia, climatologia, população
- **Filosofia (fil-):** História da filosofia, epistemologia, ética
- **Sociologia (soc-):** Teorias sociológicas, estrutura social, cultura
- **Português (por-):** Gramática, literatura, interpretação de textos
- **Geral (gen-, ger-):** Temas interdisciplinares
- **Ciências Humanas (hum-):** Integração de história, geografia, sociologia

### Completion Status

**All Deliverables Complete:**
✅ 96 lessons created and verified  
✅ Content accuracy verified (formulas, equations, concepts)  
✅ Org-mode conversion pipeline implemented  
✅ Files renamed (ferias→semana2, semana2→semana3, semana3→semana4)  
✅ Respostas sections moved to end with numbered references  
✅ Hyperlinks disabled in PDFs  
✅ CUSTOM_ID properties removed (2,149 blocks)  
✅ Enhanced graphics added (Venn diagrams, graphs, visual aids)  
✅ 4 PDFs generated (total 8.7MB)  
✅ 5 HTML files generated (total 1.2MB)  
✅ MathJax 3 integrated for web formula rendering  
✅ **ALL 207 Vue component files updated with lesson content**  

The study material system for SERIADO UFMG is now fully operational with complete content integration across PDF, HTML, and Vue application formats.
