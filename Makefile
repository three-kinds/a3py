init:
	pip3 install -r requirements.txt

coverage:
	coverage erase
	coverage run --source=a3py -m unittest discover
	coverage html --title="coverage report"
	python3 -m webbrowser ./htmlcov/index.html

test: coverage

build:
	python -m build

clean:
	rm -rf build dist .egg *.egg-info

upload:
	twine upload dist/* --verbose

format:
	ruff format a3py tests

check:
	ruff check a3py tests
