#!/bin/bash

# MD to Org Conversion Script for SERIADO UFMG Materials
# Converts all markdown study materials to org-mode format

set -e  # Exit on error

DOCS_DIR="../docs"
SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ORG_DIR="${DOCS_DIR}/org"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  MD → Org Conversion Pipeline${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Create org directory if it doesn't exist
mkdir -p "$ORG_DIR"

# Function to add org-mode headers
add_org_headers() {
    local org_file=$1
    local title=$2
    
    # Create header content
    cat > "${org_file}.tmp" << EOF
#+TITLE: ${title}
#+AUTHOR: Material de Estudo SERIADO UFMG
#+DATE: $(date +%Y-%m-%d)
#+OPTIONS: toc:2 num:t H:4 ^:nil
#+STARTUP: showeverything
#+LATEX_CLASS: article
#+LATEX_CLASS_OPTIONS: [11pt,a4paper]
#+LATEX_HEADER: \usepackage[utf8]{inputenc}
#+LATEX_HEADER: \usepackage[brazil]{babel}
#+LATEX_HEADER: \usepackage{amsmath,amssymb}
#+LATEX_HEADER: \usepackage{tikz}
#+LATEX_HEADER: \usepackage{graphicx}
#+LATEX_HEADER: \usepackage{xcolor}
#+LATEX_HEADER: \usepackage{geometry}
#+LATEX_HEADER: \geometry{margin=2cm}
#+LATEX_HEADER: \usepackage{fancyhdr}
#+LATEX_HEADER: \pagestyle{fancy}
#+LATEX_HEADER: \fancyhead[L]{SERIADO UFMG}
#+LATEX_HEADER: \fancyhead[R]{${title}}
#+HTML_HEAD: <meta charset="utf-8">
#+HTML_HEAD: <meta name="viewport" content="width=device-width, initial-scale=1.0">
#+HTML_HEAD: <link rel="stylesheet" type="text/css" href="../css/org-style.css"/>
#+HTML_HEAD: <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
#+HTML_MATHJAX: align: left indent: 5em tagside: right font: Neo-Euler

EOF
    
    # Append original content
    cat "$org_file" >> "${org_file}.tmp"
    mv "${org_file}.tmp" "$org_file"
}

# Convert each markdown file
for md_file in ${DOCS_DIR}/material_*.md; do
    if [ -f "$md_file" ]; then
        basename=$(basename "$md_file" .md)
        org_file="${ORG_DIR}/${basename}.org"
        
        echo -e "${YELLOW}Converting:${NC} $basename.md → ${basename}.org"
        
        # Convert using pandoc
        pandoc "$md_file" \
            -f markdown \
            -t org \
            --wrap=none \
            --standalone \
            -o "$org_file"
        
        # Post-process: Fix inline list items by adding line breaks
        # Replace " - " with newline + "- " to separate list items
        perl -i -pe 's/(?<=\S) - /\n- /g' "$org_file"
        
        # Post-process: Remove :PROPERTIES: blocks created by Pandoc
        # These appear as visible text in PDF exports
        perl -i -0pe 's/:PROPERTIES:\n(?::.*\n)*:END:\n//g' "$org_file"
        
        # Determine title based on filename
        case "$basename" in
            material_semana1)
                title="Semana 1 - Fundamentos (18-23 Nov)"
                ;;
            material_semana2)
                title="Semana 2 - Período de Férias - Aprofundamento (26 Nov - 02 Dez)"
                ;;
            material_semana3)
                title="Semana 3 - Conteúdo Avançado (03-07 Dez)"
                ;;
            material_semana4)
                title="Semana 4 - Revisão Final (09-13 Dez)"
                ;;
            *)
                title="Material de Estudo SERIADO UFMG"
                ;;
        esac
        
        # Add org headers
        add_org_headers "$org_file" "$title"
        
        echo -e "${GREEN}✓${NC} Converted successfully\n"
    fi
done

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Conversion Complete!${NC}"
echo -e "${GREEN}========================================${NC}\n"
echo -e "Org files created in: ${BLUE}${ORG_DIR}/${NC}\n"
echo -e "Next steps:"
echo -e "  1. Run ${BLUE}./build-pdf.sh${NC} to generate PDFs"
echo -e "  2. Run ${BLUE}./build-html.sh${NC} to generate HTML"
echo -e "  3. Check output in ${BLUE}../docs/output/${NC}\n"
