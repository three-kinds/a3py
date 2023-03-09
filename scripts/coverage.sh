#!/usr/bin/env bash

PACKAGE_PATH="$(dirname "$0")/.."
cd $PACKAGE_PATH
export PYTHONPATH=$PYTHONPATH:$PACKAGE_PATH

coverage erase
# nosetests -w tests --with-coverage --cover-inclusive --cover-package=a3py
coverage run --source=a3py -m unittest discover
coverage html --title="a3py coverage report"
python -m webbrowser ./htmlcov/index.html
