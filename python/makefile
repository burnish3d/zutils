setup: requirements_dev.txt
	python3 -m pip install requirements_dev.txt 

clean:
	rm -rf build
	rm -rf dist
	rm -rf __pycache__

venv: venv/bin/activate 
	source venv/bin/activate

venv/bin/activate: requirements_dev.txt
	python3 -m venv venv
	./venv/bin/python3 -m pip install -r requirements_dev.txt

