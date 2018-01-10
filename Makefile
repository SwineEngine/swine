build:
	python3 setup,py sdist

build_wheel:
	python3 setup.py bdist_wheel

install: clean build
	pip3 install dist/*

clean:
	rm -rf dist/

upload:
	twine upload dist/*