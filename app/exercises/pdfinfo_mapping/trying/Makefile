#!/usr/bin/env python3

SHELL := /bin/bash

top_srcdir := $(shell cd ../../.. ; pwd)

all: \
  000015.pdf.pdfinfo-isodates.txt.mapped_as_json.json

.PHONY: \
  check-format \
  check-mypy \
  format

000015.pdf.pdfinfo-isodates.txt.mapped_as_json.json: \
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
	# Confirm unmapped-concepts file is not empty.  (Will be empty after input totally mapped.)
	test -s \
	  000015.pdf.pdfinfo-isodates.txt.mapped_as_json.unmapped.txt
	mv _$@ $@

check: \
  check-format \
  check-mypy

check-format: \
  $(top_srcdir)/.venv.done.log
	source $(top_srcdir)/venv/bin/activate \
	  && black \
	    --check \
	    .

check-mypy: \
  $(top_srcdir)/.venv.done.log
	source $(top_srcdir)/venv/bin/activate \
	  && mypy \
	    --strict \
	    .

format: \
  $(top_srcdir)/.venv.done.log
	source $(top_srcdir)/venv/bin/activate \
	  && black \
	    .
