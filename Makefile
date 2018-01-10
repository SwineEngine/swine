build:
	python setup.py sdist

build_wheel:
	python setup.py bdist_wheel

install: clean build
	pip3 install dist/*

clean:
	rm -rf dist/

upload: clean build build_wheel
	twine upload dist/*