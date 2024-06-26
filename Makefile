install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run python3 -m pytest --cov-report xml --cov=gendiff_test
