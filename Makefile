build:
	python setup.py sdist

install: clean build
	pip install dist/*

clean:
	rm -rf dist/

upload:
	twine upload dist/*

test:
	python test_vali.py
