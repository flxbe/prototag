VERSION := 0.1.0

SOURCE_FILES := prototag/*.py test/*.py
SOURCE := dist/prototag-$(VERSION).tar.gz
WHEEL := dist/prototag-$(VERSION)-py2.py3-none-any.whl

all: build

clean:
		rm -rf ./build
		rm -rf ./dist

test-upload: build
		twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload: build
		twine upload $(SOURCE) $(SOURCE).asc
		twine upload $(WHEEL) $(WHEEL).asc

build: $(SOURCE).asc $(WHEEL).asc

%.asc: %
		gpg --detach-sign -a $<

%.tar.gz: $(SOURCE_FILES)
		python setup.py sdist

%.whl: $(SOURCE_FILES)
		python setup.py bdist_wheel
