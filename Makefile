PROJECT_NAME = a3py

sync:
	uv sync

coverage: format check
	coverage erase
	coverage run --source=$(PROJECT_NAME) --branch -m unittest discover
	coverage html
	python -m webbrowser ./htmlcov/index.html

test:
	poe test-all

build: clean
	uv build

clean:
	rm -rf build dist .egg *.egg-info

upload:
	twine upload dist/* --verbose

format:
	ruff format

check:
	ruff check
	mypy
