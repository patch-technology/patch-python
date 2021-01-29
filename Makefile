SHELL = /bin/bash

build:
	pip install -r requirements.txt \
	python setup.py install

lint:
	flake8 \


test:
	pip install -r test-requirements.txt && \
	python -m unittest discover test/

.PHONY: build test
