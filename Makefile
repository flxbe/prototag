VERSION := 0.1.1

SOURCE_FILES := prototag/*.py test/*.py
SOURCE := dist/prototag-$(VERSION).tar.gz
WHEEL := dist/prototag-$(VERSION)-py2.py3-none-any.whl

all: build

clean:
		rm -rf ./build
		rm -rf ./dist

readme:
		restview --pypi-strict --long-description

test-upload: build
		twine upload --repository-url $(SOURCE) $(SOURCE).asc
		twine upload --repository-url $(WHEEL) $(WHEEL).asc

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

activate:
		@source ./env/bin/activate