SHELL = /bin/bash

build: lint install

install:
	docker build --target build . -t patch-python-build && \
	docker run --rm -v $(PWD)/build:/build patch-python-lint .

lint:
	docker build --target lint . -t patch-python-lint && \
	docker run --rm -v $(PWD):/data patch-python-lint .

test:
	docker build --target test . -t patch-python-test && \
	docker run --rm \
		-e SANDBOX_API_KEY=${SANDBOX_API_KEY} \
		patch-python-test

.PHONY: build lint test
