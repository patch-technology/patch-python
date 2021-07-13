SHELL = /bin/bash

build:
	pip install -r requirements.txt && \
	python setup.py install

test:
	pip install -r test-requirements.txt && \
	pip install -r requirements.txt && \
	python -m unittest discover test/

.PHONY: build lint test
