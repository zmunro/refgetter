.PHONY: refgetter
refgetter:
	docker exec -it refgetter pipenv run refgetter --seq_id $(SEQID)

.PHONY: build-dev
build-dev:
	docker exec -it refgetter pipenv run pip install --editable .

.PHONY: black
black:
	docker exec -it refgetter pipenv run black .

.PHONY: lint
lint:
	docker exec -t refgetter bash -c "pipenv run pylint /refgetter/***"

.PHONY: test
test:
	docker exec -it refgetter pipenv run pytest

.PHONY: build-wheel
build-wheel:
	docker exec -it refgetter pipenv run python setup.py bdist_wheel

.PHONY: publish
publish:
	docker exec -it refgetter pipenv run python -m twine upload dist/*

.PHONY: bash
bash:
	docker exec -it refgetter pipenv run bash

.PHONY: python
python:
	docker exec -it refgetter pipenv run python