#!/bin/bash
# HTML Build Script for Org-mode materials

set -e

ORG_DIR="../docs/org"
OUTPUT_DIR="../docs/output/html"
CSS_DIR="../docs/output/css"

mkdir -p "$OUTPUT_DIR"
mkdir -p "$CSS_DIR"

# Emacs Lisp configuration for HTML export
EMACS_CONFIG=$(cat << 'EOF'
(require 'ox-html)
(setq org-html-html5-fancy t
      org-html-doctype "html5"
      org-html-validation-link nil
      org-html-postamble nil
      org-html-head-include-default-style nil
      org-html-head-include-scripts t
      org-export-with-toc t
      org-html-mathjax-options
      '((path "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js")
        (scale "100")
        (align "center")
        (font "TeX")
        (linebreaks "false")
        (autonumber "AMS")
        (indent "0em")
        (multlinewidth "85%")
        (tagindent ".8em")
        (tagside "right"))
      org-html-mathjax-template
      "<script>
  MathJax = {
    tex: {
      inlineMath: [['\\\\(', '\\\\)']],
      displayMath: [['\\\\[', '\\\\]']],
      tags: 'ams',
      packages: {'[+]': ['ams']}
    },
    svg: {
      fontCache: 'global'
    }
  };
</script>
<script src='%PATH' async></script>")
EOF
)

# Function to export org to HTML
export_to_html() {
    local org_file=$1
    local basename=$(basename "$org_file" .org)
    
    echo "Exporting $basename to HTML..."
    
    # Try emacs export first
    if command -v emacs &> /dev/null; then
        if emacs "$org_file" \
            --batch \
            --eval "$EMACS_CONFIG" \
            --eval "(setq org-html-head \"<link rel='stylesheet' type='text/css' href='../css/org-style.css' />\")" \
            --funcall org-html-export-to-html 2>/dev/null; then
            
            mv "${org_file%.org}.html" "${OUTPUT_DIR}/${basename}.html"
            echo "✅ Successfully exported $basename using Emacs"
            return 0
        fi
    fi
    
    # Fallback to pandoc
    echo "⚠️  Emacs not available or export failed, using Pandoc fallback..."
    pandoc "$org_file" \
        -f org \
        -t html5 \
        --standalone \
        --mathjax \
        --toc \
        --toc-depth=3 \
        --number-sections \
        --css="../css/org-style.css" \
        --metadata title="$(grep '^#+TITLE:' "$org_file" | cut -d: -f2- | xargs)" \
        -o "${OUTPUT_DIR}/${basename}.html"
    
    echo "✅ Successfully exported $basename using Pandoc"
}

# Export all org files
echo "🚀 Starting HTML export for all Org-mode materials..."
echo ""

for org_file in ${ORG_DIR}/material_*.org; do
    if [ -f "$org_file" ]; then
        export_to_html "$org_file"
    fi
done

echo ""
echo "✅ HTML export complete!"
echo "📁 Output directory: $OUTPUT_DIR"
echo ""
echo "Next steps:"
echo "  1. Create CSS stylesheet: ${CSS_DIR}/org-style.css"
echo "  2. Test HTML files in browser"
echo "  3. Integrate into Vue application"
