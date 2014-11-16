LATEXFILE = bool_func.tex
PYTHONFILE = gen-data.py
DATADIR = data
PDF = pdflatex
OPTS = --file-line-error
OPTIONGREP = -e ^Overfull -e Warning --color

export max_print_line=1000
export error_line=254
export half_error_line=238

all: python
	-@echo "LaTeX compilation. Beware, this may take a long time..."
	@$(PDF) $(OPTS) $(LATEXFILE) | grep $(OPTIONGREP)

python: $(DATADIR)/$(PYTHONFILE)
	-@echo "Generates data"
	@cd $(DATADIR) && ./$(PYTHONFILE)


clean:
	-@du -sh
	-@rm $(DATADIR)/*.dat
	-@rm *.aux
	-@rm *.out
	-@rm *.log
	-@du -sh
