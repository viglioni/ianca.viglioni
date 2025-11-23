#!/bin/bash

# PDF Build Script for Org-mode materials
# Exports .org files to professional PDFs via LaTeX

set -e

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ORG_DIR="../docs/org"
OUTPUT_DIR="../docs/output/pdf"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  PDF Export Pipeline${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Check if emacs is installed
if ! command -v emacs &> /dev/null; then
    echo -e "${RED}Error: emacs is not installed${NC}"
    echo -e "Install with: ${YELLOW}brew install emacs${NC} (macOS)"
    exit 1
fi

# Check if pandoc is installed (backup method)
if ! command -v pandoc &> /dev/null; then
    echo -e "${YELLOW}Warning: pandoc not installed (recommended for fallback)${NC}"
    echo -e "Install with: ${YELLOW}brew install pandoc${NC}"
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Emacs Lisp configuration for export
EMACS_CONFIG=$(cat << 'EOF'
(require 'ox-latex)
(setq org-export-with-toc t)
(setq org-export-headline-levels 4)
(setq org-latex-listings 'listings)
(setq org-latex-packages-alist '(("" "listings") ("" "color")))
(setq org-latex-pdf-process
      '("pdflatex -shell-escape -interaction nonstopmode -output-directory %o %f"
        "pdflatex -shell-escape -interaction nonstopmode -output-directory %o %f"
        "pdflatex -shell-escape -interaction nonstopmode -output-directory %o %f"))
(setq org-latex-hyperref-template
      "\\hypersetup{\n pdfauthor={%a},\n pdftitle={%t},\n pdfkeywords={%k},\n pdfsubject={%d},\n pdflang={%L},\n colorlinks=true,\n linkcolor=blue,\n urlcolor=blue\n}\n")
EOF
)

# Function to export org to PDF
export_to_pdf() {
    local org_file=$1
    local basename=$(basename "$org_file" .org)
    
    echo -e "${YELLOW}Exporting:${NC} ${basename}.org → ${basename}.pdf"
    
    # Try emacs export first
    if emacs "$org_file" \
        --batch \
        --eval "$EMACS_CONFIG" \
        --funcall org-latex-export-to-pdf \
        2>/dev/null; then
        
        # Move PDF to output directory
        if [ -f "${org_file%.org}.pdf" ]; then
            mv "${org_file%.org}.pdf" "${OUTPUT_DIR}/${basename}.pdf"
            echo -e "${GREEN}✓${NC} PDF created successfully\n"
            return 0
        fi
    fi
    
    # Fallback to pandoc if emacs fails
    echo -e "${YELLOW}Emacs export failed, trying pandoc...${NC}"
    
    if command -v pandoc &> /dev/null; then
        pandoc "$org_file" \
            -f org \
            -t latex \
            --pdf-engine=xelatex \
            -V mainfont="DejaVu Serif" \
            -V monofont="DejaVu Sans Mono" \
            -V geometry:margin=2cm \
            -V colorlinks=true \
            --toc \
            --number-sections \
            -o "${OUTPUT_DIR}/${basename}.pdf"
        
        echo -e "${GREEN}✓${NC} PDF created with pandoc\n"
        return 0
    else
        echo -e "${RED}✗${NC} Failed to create PDF (no tools available)\n"
        return 1
    fi
}

# Export all org files
success_count=0
fail_count=0

for org_file in ${ORG_DIR}/material_*.org; do
    if [ -f "$org_file" ]; then
        if export_to_pdf "$org_file"; then
            ((success_count++))
        else
            ((fail_count++))
        fi
    fi
done

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  PDF Export Complete!${NC}"
echo -e "${GREEN}========================================${NC}\n"
echo -e "Successful: ${GREEN}${success_count}${NC}"
echo -e "Failed: ${RED}${fail_count}${NC}"
echo -e "\nPDFs saved to: ${BLUE}${OUTPUT_DIR}/${NC}\n"

# List generated PDFs
if [ $success_count -gt 0 ]; then
    echo -e "${BLUE}Generated PDFs:${NC}"
    ls -lh "${OUTPUT_DIR}"/*.pdf 2>/dev/null || true
fi
