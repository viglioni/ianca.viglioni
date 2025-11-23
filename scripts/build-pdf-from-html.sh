#!/bin/bash
# PDF Generation from HTML using WeasyPrint

set -e

HTML_DIR="../docs/output/html"
OUTPUT_DIR="../docs/output/pdf"
CSS_FILE="../docs/output/css/org-style.css"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  HTML → PDF Conversion (WeasyPrint)${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Convert each HTML file to PDF
for html_file in ${HTML_DIR}/material_*.html; do
    if [ -f "$html_file" ]; then
        basename=$(basename "$html_file" .html)
        pdf_file="${OUTPUT_DIR}/${basename}.pdf"
        
        echo -e "${YELLOW}Converting:${NC} ${basename}.html → ${basename}.pdf"
        
        # Use WeasyPrint to convert HTML to PDF
        weasyprint "$html_file" "$pdf_file" 2>/dev/null
        
        if [ $? -eq 0 ]; then
            file_size=$(ls -lh "$pdf_file" | awk '{print $5}')
            echo -e "${GREEN}✓${NC} PDF created successfully (${file_size})\n"
        else
            echo -e "${RED}✗${NC} Failed to create PDF\n"
        fi
    fi
done

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  PDF Generation Complete!${NC}"
echo -e "${GREEN}========================================${NC}\n"
echo -e "PDF files created in: ${BLUE}${OUTPUT_DIR}/${NC}\n"

# List generated PDFs
echo -e "${BLUE}Generated PDFs:${NC}"
ls -lh ${OUTPUT_DIR}/*.pdf 2>/dev/null | awk '{print "  • " $9 " (" $5 ")"}'
echo ""
