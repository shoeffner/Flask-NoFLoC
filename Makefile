.PHONY: all test docs clean

VERSION=$(shell grep "__version__" flask_nofloc.py | sed "s/__version__ = '\(.*\)'/\\1/g")

all: test docs
publish: dist/Flask-NoFLoC-${VERSION}.tar.gz dist/Flask_NoFLoC-${VERSION}-py3-none-any.whl
	twine check $^
	gpg --detach-sign -a dist/Flask-NoFLoC-${VERSION}.tar.gz
	gpg --detach-sign -a dist/Flask_NoFLoC-${VERSION}-py3-none-any.whl
	twine upload $^ $(addsuffix .asc,$^)

testpublish: dist/Flask-NoFLoC-${VERSION}.tar.gz dist/Flask_NoFLoC-${VERSION}-py3-none-any.whl
	twine check $^
	gpg --detach-sign -a dist/Flask-NoFLoC-${VERSION}.tar.gz
	gpg --detach-sign -a dist/Flask_NoFLoC-${VERSION}-py3-none-any.whl
	twine upload --repository pypitest $^ $(addsuffix .asc,$^)

test: htmlcov/index.html
htmlcov/index.html: .coverage
	python3 -m coverage html

.coverage: flask_nofloc.py test_flask_nofloc.py setup.py
	python3 -m coverage run --omit='.venv/*' -m pytest

docs: docs/_build/html/index.html
docs/_build/html/index.html: docs/conf.py docs/*.rst docs/Makefile LICENSE README.rst flask_nofloc.py setup.py
	$(MAKE) html -C docs

dist/Flask-NoFLoC-${VERSION}.tar.gz: test
	python3 setup.py sdist

dist/Flask_NoFLoC-${VERSION}-py3-none-any.whl: test
	python3 setup.py bdist_wheel

clean:
	@-rm -rf htmlcov
	@-rm -rf docs/_build
	@-rm -rf build
	@-rm -rf dist
	@-rm -r .coverage
