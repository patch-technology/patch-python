SHELL = /bin/bash

build:
	pip install -r requirements.txt

test:
	pip install -r test-requirements.txt && \
	python -m unittest discover test/

.PHONY: build test
