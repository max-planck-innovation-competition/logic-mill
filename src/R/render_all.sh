#!/bin/bash

# Script to render all R Markdown files to HTML
# 
# Usage:
#   bash render_all.sh              # Render all .Rmd files in current directory
#   bash render_all.sh /path/to/dir # Render all .Rmd files in specified directory

TARGET_DIR="${1:-.}"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}R Markdown Renderer${NC}"
echo "Target directory: $TARGET_DIR"
echo ""

rendered=0
skipped=0

# Check if rmarkdown is installed
Rscript --vanilla --quiet << 'EOF' 2>/dev/null
if (!requireNamespace("rmarkdown", quietly = TRUE)) {
  stop("rmarkdown")
}
EOF

if [ $? -ne 0 ]; then
  echo -e "${YELLOW}Installing rmarkdown...${NC}"
  Rscript --vanilla -e "install.packages('rmarkdown', repos='http://cran.r-project.org')" 2>&1 | head -1
  echo ""
fi

# Find and render all .Rmd files
for rmd_file in "$TARGET_DIR"/*.Rmd; do
    if [ -f "$rmd_file" ]; then
        filename=$(basename "$rmd_file")
        html_file="${rmd_file%.Rmd}.html"
        
        # Skip if HTML is up-to-date
        if [ -f "$html_file" ] && [ "$html_file" -nt "$rmd_file" ]; then
            echo -e "${YELLOW}⊘ Skipping: $filename${NC}"
            ((skipped++))
            continue
        fi
        
        echo -e "${BLUE}→ Rendering: $filename${NC}"
        Rscript --vanilla --quiet -e "rmarkdown::render('$rmd_file', quiet=TRUE)" 2>&1 | tail -1
        
        if [ -f "$html_file" ]; then
            echo -e "${GREEN}✓ Success${NC}"
            ((rendered++))
        fi
        echo ""
    fi
done

# Render README.md if it exists
readme_file="$TARGET_DIR/README.md"
if [ -f "$readme_file" ]; then
    readme_html="${readme_file%.md}.html"
    
    # Skip if HTML is up-to-date
    if [ -f "$readme_html" ] && [ "$readme_html" -nt "$readme_file" ]; then
        echo -e "${YELLOW}⊘ Skipping: README.md${NC}"
        ((skipped++))
    else
        echo -e "${BLUE}→ Rendering: README.md${NC}"
        Rscript --vanilla --quiet -e "rmarkdown::render('$readme_file', quiet=TRUE)" 2>&1 | tail -1
        
        if [ -f "$readme_html" ]; then
            echo -e "${GREEN}✓ Success${NC}"
            ((rendered++))
        fi
    fi
    echo ""
fi

echo -e "${BLUE}Complete: $rendered rendered, $skipped skipped${NC}"
