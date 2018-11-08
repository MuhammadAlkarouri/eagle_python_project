.PHONY: run install-tools install-deps clean format test

run:
	pipenv run python -m eagle_python_project

clean:
	pipenv --rm

format:
	pipenv run black .
	pipenv run isort -rc .

install-deps:
	pipenv --python 3.7
	pipenv install sanic
	pipenv install --dev aiohttp ipython pytest

install-tools: install-deps
	pipenv install --dev isort pre-commit 
	pipenv install --dev --pre black

test:
	pipenv run py.test
