.PHONY: clean clean-build clean-pyc lint test setup help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

setup: ## install python project dependencies
	pip install .

setup-tests: ## install python project dependencies for tests
	pip install -r requirements.test.txt

setup-dev: ## install python project dependencies for development
	pip install -r requirements.dev.txt
	# not very elegant to use || to be sure to have a database created and updated
	# need IMP ideally get the db name from anyblok config file and check if database already exists
	anyblok_createdb -c app.dev.cfg || anyblok_updatedb -c app.dev.cfg
	anyblok_createdb -c app.test.cfg || anyblok_updatedb -c app.test.cfg

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

lint: ## check style with flake8
	flake8 .

test: ## run anyblok nose tests
	anyblok_nose -c app.test.cfg -- -v -s {{ cookiecutter.python_package }}
