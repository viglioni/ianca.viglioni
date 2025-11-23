#!/bin/bash
# Master Build Script - Converts MD to Org and exports to PDF + HTML

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "🚀 SERIADO UFMG Materials - Complete Build Pipeline"
echo "===================================================="
echo ""

# Step 1: Convert MD to Org
echo "📝 Step 1/3: Converting Markdown to Org-mode..."
echo "------------------------------------------------"
cd "$SCRIPT_DIR"
./md2org.sh
echo ""

# Step 2: Build PDFs
echo "📄 Step 2/3: Building PDFs..."
echo "------------------------------------------------"
./build-pdf.sh
echo ""

# Step 3: Build HTML
echo "🌐 Step 3/3: Building HTML..."
echo "------------------------------------------------"
./build-html.sh
echo ""

echo "✅ BUILD COMPLETE!"
echo "=================="
echo ""
echo "📊 Summary:"
echo "  • Org files:  ../docs/org/"
echo "  • PDF files:  ../docs/output/pdf/"
echo "  • HTML files: ../docs/output/html/"
echo "  • CSS file:   ../docs/output/css/org-style.css"
echo ""
echo "Next steps:"
echo "  1. Review PDF outputs for LaTeX rendering quality"
echo "  2. Open HTML files in browser to check MathJax rendering"
echo "  3. Integrate HTML files into Vue application"
echo "  4. (Optional) Upgrade critical diagrams to TikZ/LaTeX"
echo ""
