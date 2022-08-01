#!/usr/bin/make -f

SHELL := /bin/bash

top_srcdir := $(shell cd .. ; pwd)

all:

.PHONY: \
  check-mypy \
  check-pytest

check: \
  check-mypy \
  check-pytest

check-mypy: \
  $(top_srcdir)/.venv.done.log
	source $(top_srcdir)/venv/bin/activate \
	  && mypy \
	    --strict \
	    $(top_srcdir)/exercises/pdfinfo_mapping/completed \
	    $(top_srcdir)/templates

check-pytest: \
  $(top_srcdir)/.venv.done.log
	source $(top_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG
