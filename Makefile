install:
	sudo apt install default-libmysqlclient-dev
	python3 --version
	python3 -m pip --version
	python3 -m venv venv
	venv/bin/pip3 install -r requirements.txt

run:
	venv/bin/python3 manage.py runserver

inspectdb:
	venv/bin/python3 manage.py inspectdb
