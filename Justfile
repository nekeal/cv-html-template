new company_name:
    mkdir -p $(date +%Y)/{{company_name}}
    cp src/cv/context.py $(date +%Y)/{{company_name}}

export PYTHONPATH := ".:$PYTHONPATH"
render company_name:
    uv run python src/cv/render.py $(date +%Y).{{company_name}}.context
    google-chrome --headless --disable-gpu --run-all-compositor-stages-before-draw --virtual-time-budget=1000 --no-pdf-header-footer --print-to-pdf-no-header --print-to-pdf=$(date +%Y)/{{company_name}}/SURNAME_NAME_CV_{{company_name}}.pdf index.html

commit company_name:
    git add $(date +%Y)/{{company_name}}
    git commit -m "Apply to {{company_name}}"

html:
    uv run python src/cv/render.py

pdf: html
    google-chrome --headless --disable-gpu --run-all-compositor-stages-before-draw --virtual-time-budget=1000 --no-pdf-header-footer --print-to-pdf-no-header --print-to-pdf=index.pdf --print-to-pdf-paper-size=A4 index.html


autoformat:
    uv run ruff format src
    uv run ruff check --fix src