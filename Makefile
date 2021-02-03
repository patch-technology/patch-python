SHELL = /bin/bash

build:
	pip install -r requirements.txt \
	python setup.py install

lint:
	pre-commit

test:
	pip install -r test-requirements.txt && \
	python -m unittest discover test/

publish:
	python3 -m pip install --user --upgrade twine && \
	python3 -m twine upload -r pypi dist/* --config-file .pypirc

.PHONY: build test lint publish
