#!/usr/bin/make -f

SHELL := /bin/bash

top_srcdir := $(shell cd ../.. ; pwd)

all: \
  document_nodes_and_authors.html \
  document_nodes_and_authors.md

document_nodes_and_authors.%: \
  document_nodes_and_authors.sparql \
  $(top_srcdir)/.venv.done.log \
  ../pdfinfo_mapping/completed/000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.json \
  ../pdfinfo_mapping/completed/000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && case_sparql_select \
	    _$@ \
	    document_nodes_and_authors.sparql \
	    ../pdfinfo_mapping/completed/000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.json \
	    ../pdfinfo_mapping/completed/000015.pdf.pdfinfo-isodates.txt.mapped_with_rdflib.ttl
	mv _$@ $@

# Included for provenance.
Q2928358.ttl:
	wget \
	  --header 'Accept: text/turtle' \
	  --output-document _$@ \
	  http://www.wikidata.org/entity/Q2928358
	mv _$@ $@
