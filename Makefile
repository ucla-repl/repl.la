PANDOC_OPTIONS := -f markdown \
                  -t html -s \
                  -V maxwidth=650px \
                  -V mainfont=sans-serif

all: index.html

index.html: index.md
	pandoc $< $(PANDOC_OPTIONS) -o $@

.PHONY: all
