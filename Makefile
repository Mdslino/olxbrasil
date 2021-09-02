SHEL := /bin/bash
.PHONY: test clean

test:
	pytest -x -vv --cov=olxbrasil --cov-report term-missing tests/

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build

###
# Lint section
###
_flake8:
	@flake8 --show-source .

_isort:
	@isort --diff --check-only src/

_black:
	@black --check src/

_isort-fix:
	@isort .

_black_fix:
	@black .

_dead_fixtures:
	@pytest --dead-fixtures tests/application/

_mypy:
	@mypy src/

lint: _flake8 _isort _black _mypy _dead_fixtures   ## Check code lint
format-code: _isort-fix _black_fix ## Format code