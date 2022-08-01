#!/usr/bin/env python3

SHELL := /bin/bash

top_srcdir := $(shell cd ../../.. ; pwd)

all: \
  000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.json \
  000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.ttl

000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.json: \
  $(top_srcdir)/.venv.done.log \
  000015.pdf.pdfinfo-isodates.txt \
  pdf_info_txt_to_case.py
	source $(top_srcdir)/venv/bin/activate \
	  && python3 pdf_info_txt_to_case.py \
	    _$@ \
	    000015.pdf.pdfinfo-isodates.txt
	source $(top_srcdir)/venv/bin/activate \
	  && case_validate \
	    _$@
	mv _$@ $@

000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.ttl: \
  $(top_srcdir)/.venv.done.log \
  000015.pdf.pdfinfo-isodates.txt \
  pdf_info_txt_to_case.py
	source $(top_srcdir)/venv/bin/activate \
	  && python3 pdf_info_txt_to_case.py \
	    --unmapped-txt 000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.unmapped.txt \
	    _$@ \
	    000015.pdf.pdfinfo-isodates.txt
	source $(top_srcdir)/venv/bin/activate \
	  && case_validate \
	    _$@
	# Confirm unmapped-concepts file is not empty.  (Will be empty after input totally mapped.)
	test -s \
	  000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.unmapped.txt
	mv _$@ $@

check: \
  $(top_srcdir)/.venv.done.log
	source $(top_srcdir)/venv/bin/activate \
	  && mypy \
	    --strict \
	    .
