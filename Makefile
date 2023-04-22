SHELL := /bin/bash


.PHONY: test/code
test/code:
	poetry run mypy --strict ./src

.PHONY: test
test: test/code
	poetry run python -m pytest ./test
