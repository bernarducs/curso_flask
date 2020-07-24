clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	pip install -e .[dev] --upgrade --no-cache
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf *.egg-info

install:
	pip install -e .['dev']

test:
	pytest tests/ -v --cov=delivery