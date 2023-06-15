SHELL = /bin/bash -c
VIRTUAL_ENV = $(shell poetry env info --path)
export BASH_ENV=$(VIRTUAL_ENV)/bin/activate

.PHONY: lint
lint: _black _mypy

.PHONY: complexity
test: lint complexity
	pytest --cov --mypy --cov-report term-missing --junitxml=reports/pytest.xml --cov-report xml:reports/coverage.xml

.PHONY: install
install: $(VIRTUAL_ENV)
	poetry install

.PHONY: clean
clean:
	[[ -d "$(VIRTUAL_ENV)" ]] && rm -rf "$(VIRTUAL_ENV)" || true
	[[ -d .mypy_cache ]] && rm -rf .mypy_cache || true
	[[ -d .pytest_cache ]] && rm -rf .pytest_cache || true
	[[ -d dist ]] && rm -rf dist || true
	[[ -d reports ]] && rm -rf reports || true
	[[ -d cfn_guard_test/cfn_guard_test.egg-info ]] && rm -rf cfn_guard_test/cfn_guard_test.egg-info || true
	[[ -f .coverage ]] && rm .coverage || true

.PHONY: run
run:
	cfn-guard-test --verbose --cfn-guard-path "/usr/local/bin/cfn-guard" --junit-path "reports/cfn-guard.xml"

.PHONY: patch
patch:
	semantic-release --patch version
	git add pyproject.toml cfn_guard_test/__init__.py
	git commit -m "chore: trigger new release"

.PHONY: minor
minor:
	semantic-release --minor version
	git add pyproject.toml cfn_guard_test/__init__.py
	git commit -m "chore: trigger new release"

.PHONY: complexity
complexity:
	$(info Maintenability index)
	radon mi --min A --max A --show --sort cfn_guard_test
	$(info Cyclomatic complexity index)
	xenon --max-absolute A --max-modules A --max-average A cfn_guard_test

.PHONY: _black _mypy

_black:
	$(info [*] Formatting python files...)
	black .

_mypy:
	$(info [*] Python static type checker...)
	mypy --junit-xml reports/typecheck.xml cfn_guard_test

$(VERBOSE).SILENT:
