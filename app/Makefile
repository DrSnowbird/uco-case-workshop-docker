#!/usr/bin/make -f

SHELL := /bin/bash

all: \
  .venv.done.log

.git_submodule_init.done.log: \
  .gitmodules
	git submodule update \
	  --init
	touch $@

.venv.done.log: \
  .git_submodule_init.done.log \
  requirements.txt
	rm -rf venv
	python3 -m venv venv
	source venv/bin/activate && pip install --upgrade pip setuptools wheel
	source venv/bin/activate && pip install --requirement requirements.txt
	touch $@

check: \
  .venv.done.log
	$(MAKE) \
	  --directory tests \
	  check
