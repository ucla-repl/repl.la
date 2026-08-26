PANDOC_OPTIONS := -f markdown \
                  -t html -s \
                  -V maxwidth=650px \
                  -V mainfont=palatino,serif \
                  --citeproc

PUBS_N := 10

all: index.html

index.html: index.md pubs.bib pubs.csl
	pandoc $< $(PANDOC_OPTIONS) -o $@

pubs.bib: papers/references.bib scripts/top_pubs.py
	python3 scripts/top_pubs.py $(PUBS_N) papers/references.bib pubs.bib

.PHONY: all
