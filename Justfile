export VERSION					:= if `git describe --tags 2>/dev/null || true` == "" { "v0.0.1" } else { `git describe --tags` }
export IMAGE						:= "johandry/librero"
export DOCKER_BUILDKIT	:= "1"

# Prints the available recipes
default:
	@just --list

# Perform unit tests
test:
	pytest --cov=app --cov-report=term-missing --cov-branch tests/*

# Initialize the virtual environment
init:
	python3 -m venv .venv
	source ./.venv/bin/activate
	pip install -r requirements.txt

# Runs pip freeze to save the requirements
pip-freeze:
	pip freeze > requirements.txt

install:
	pip install -e .

build:
	python3 setup.py sdist bdist_wheel
	python3 -m build
	tree dist/
	twine check dist/*

# Runs the Librero server, requires the server repository to be in the parent directory
run-backend:
	LIBRERO_LOG_LEVEL=DEBUG \
	LIBRERO_PORT=3100 \
	../librero/bin/librero

# Runs the Librero server as new, no database. Requires the server repository to be in the parent directory
run-backend-clean:
	rm -f ../librero/bin/librero.*
	just run-backend

# Runs a Jupyter container to import the package
run-jupyter:
	open http://localhost:8888?token=mytoken
	docker run -it --rm \
		-p 8888:8888 \
		-v ${PWD}/volume/jupyter:/home/jovyan/work \
		-e JUPYTER_TOKEN=mytoken \
		quay.io/jupyter/minimal-notebook
	

# Runs the Librero server and the Jupyter container to import the package
run-all: run-backend run-jupyter

# Cleans all the generated files
clean:
	rm -rf .venv .pytest_cache/ .coverage dist/ build/ *.egg-info/ volume/
	rm -f ../librero/bin/librero.*
	docker rmi -f quay.io/jupyter/minimal-notebook || true
	docker images 
