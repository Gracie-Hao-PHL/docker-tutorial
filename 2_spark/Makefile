git
.PHONY: bash clean _clean-test _clean-pyc _clean-build

bash: ## open bash in running container
	bash

kedro_new:
	kedro new --starter=pyspark

clean: _clean-build _clean-pyc _clean-test ## remove all build, test, coverage and Python artifacts

_clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr .empty/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

_clean-pyc: ## remove Python file artifacts
	rm -fr .spark-warehouse/
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

_clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache