# Detect OS
UNAME_S := $(shell uname -s)

server:
ifeq ($(UNAME_S), Linux)
	@sudo systemctl start postgresql.service
endif
	$(VENV)/python src/manage.py makemigrations;
	$(VENV)/python src/manage.py migrate;
	$(VENV)/python src/manage.py runserver;

migrate:
	$(VENV)/python manage.py makemigrations;
	$(VENV)/python manage.py migrate;

test:
	$(VENV)/coverage run --source='.' manage.py test;
	$(VENV)/coverage html

lint:
	$(VENV)/isort .;
	$(VENV)/black .;
	$(VENV)/flake8


